import sys

def pobierz_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Podaj poprawną liczbę całkowitą!")

def pobierz_liste_wag():
    while True:
        try:
            s = input("Podaj listę wag np. 1,2,3,4: ")
            # Usuń nawiasy i podziel po przecinkach
            parts = s.replace('[','').replace(']','').replace('(','').replace(')','').split(',')
            result = []
            for x in parts:
                x = x.strip()
                if x:
                    result.append(int(x))
            if result:
                return result
            else:
                print("Nie podano żadnych liczb!")
        except ValueError as e:
            print(f"Błąd: nie można przekonwertować na liczbę całkowitą. Spróbuj ponownie.")

def format_wynik_do_zapisu(wynik):
    """
    Formatuje wynik do zapisu - konwertuje wszystkie struktury do list
    aby były kompatybilne z inputem (eval)
    """
    if isinstance(wynik, list):
        result = []
        for item in wynik:
            if isinstance(item, dict):
                # Dla słowników z wynikami rownolegle_b_r - zwróć jako jest
                result.append(item)
            elif isinstance(item, (list, tuple)):
                # Dla list/tuple - konwertuj na listę
                result.append(list(item))
            else:
                # Dla pozostałych - zwróć jako jest
                result.append(item)
        return result
    elif isinstance(wynik, dict):
        return wynik
    else:
        return wynik

def zapisz_wynik_do_pliku(wynik, nazwa_operacji):
    """
    Pyta użytkownika czy chce zapisać wynik do pliku i zapisuje w bieżącym katalogu
    """
    odpowiedz = input("\nCzy chcesz zapisać wynik do pliku? (y/n): ").strip().lower()
    
    if odpowiedz == 'y':
        import os
        from datetime import datetime
        
        # Bieżący katalog
        current_dir = os.getcwd()
        
        # Nazwa pliku z timestamp'iem
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nazwa_pliku = f"wynik_{nazwa_operacji}_{timestamp}.txt"
        sciezka_pliku = os.path.join(current_dir, nazwa_pliku)
        
        # Formatuj wynik
        wynik_sformatowany = format_wynik_do_zapisu(wynik)
        
        try:
            with open(sciezka_pliku, 'w', encoding='utf-8') as f:
                # Napisz wynik w formacie kompatybilnym z inputem
                f.write(str(wynik_sformatowany))
            print(f"Wynik zapisany do: {sciezka_pliku}")
            return True
        except Exception as e:
            print(f"Błąd przy zapisie pliku: {e}")
            return False
    else:
        print("Wynik nie został zapisany.")
        return False

def pushing_down_sym_ro(G, lista_wag, k):
    """
    Dla ustalonego T_pqr i listy wag:
    1. Liczy symetryczną
    2. Dodaje ro_1 do każdej listy wag
    3. Liczy rownolegle_b_r dla wszystkich list wag po ro_1
    4. Dodaje ro_2 do każdej wagi wynikowej z rownolegle_b_r
    """
    print("\n=== PUSHING DOWN SYM RO ===")
    
    # Krok 1: Oblicz symetryczną
    print(f"\n--- Krok 1: Obliczam symetryczną (k={k}) ---")
    wynik_symetryczna = symetryczna(lista_wag, k)
    print(f"Wynik symetrycznej ({len(wynik_symetryczna)} elementów):")
    for idx, w in enumerate(wynik_symetryczna, 1):
        print(f"  {idx}. {w}")
    
    # Krok 2: Dodaj ro_1 do każdej listy wag
    print("\n--- Krok 2: Dodaję ro_1 do każdej listy wag ---")
    wynik_po_ro = []
    for idx, w in enumerate(wynik_symetryczna, 1):
        wagi_po_ro = ro_1(G, list(w) if isinstance(w, tuple) else w)
        print(f"  {idx}. {list(w) if isinstance(w, tuple) else w} -> {wagi_po_ro}")
        wynik_po_ro.append(wagi_po_ro)
    
    # Krok 3: Oblicz rownolegle_b_r dla wszystkich list wag po ro_1
    print("\n--- Krok 3: Obliczam rownolegle_b_r ---")
    wynik_rbr = rownolegle_b_r(G, wynik_po_ro)
    for idx, wpis in enumerate(wynik_rbr, 1):
        print(f"  {idx}. waga_oryg={list(wpis['waga_original'])}, waga_przem={list(wpis['waga_przemnozona'])}, "
              f"parz={wpis['suma_count_parzyste']}, nieparz={wpis['suma_count_nieparzyste']}, znak={wpis['znak']}")
    
    # Krok 4: Dodaj ro_2 do każdej wagi wynikowej (waga_przem)
    print("\n--- Krok 4: Dodaję ro_2 do każdej wagi wynikowej ---")
    wynik_po_ro2 = []
    for idx, wpis in enumerate(wynik_rbr, 1):
        w = list(wpis['waga_przemnozona'])
        wagi_po_ro2 = ro_2(G, w)
        print(f"  {idx}. {w} -> {wagi_po_ro2}")
        wynik_po_ro2.append(wagi_po_ro2)

    print("\n--- Wynik końcowy (wszystkie wagi nieujemne) ---")
    for idx, w in enumerate(wynik_po_ro2, 1):
        if w and all(x >= 0 for x in w):
            print(f"  {idx}. {w}")
    
    print("\n=== KONIEC ===")
    return wynik_po_ro2

def pushing_down_zewn_ro(G, lista_wag, k):
    """
    Dla ustalonego T_pqr i listy wag:
    1. Liczy zewnętrzną
    2. Dodaje ro_1 do każdej listy wag
    3. Liczy rownolegle_b_r dla wszystkich list wag po ro_1
    4. Dodaje ro_2 do każdej wagi wynikowej z rownolegle_b_r
    """
    print("\n=== PUSHING DOWN ZEWN RO ===")
    
    # Krok 1: Oblicz zewnętrzną
    print(f"\n--- Krok 1: Obliczam zewnętrzną (k={k}) ---")
    wynik_zewnetrzna = zewnetrzna(lista_wag, k)
    print(f"Wynik zewnętrznej ({len(wynik_zewnetrzna)} elementów):")
    for idx, w in enumerate(wynik_zewnetrzna, 1):
        print(f"  {idx}. {w}")
    
    # Krok 2: Dodaj ro_1 do każdej listy wag
    print("\n--- Krok 2: Dodaję ro_1 do każdej listy wag ---")
    wynik_po_ro = []
    for idx, w in enumerate(wynik_zewnetrzna, 1):
        wagi_po_ro = ro_1(G, list(w) if isinstance(w, tuple) else w)
        print(f"  {idx}. {list(w) if isinstance(w, tuple) else w} -> {wagi_po_ro}")
        wynik_po_ro.append(wagi_po_ro)
    
    # Krok 3: Oblicz rownolegle_b_r dla wszystkich list wag po ro_1
    print("\n--- Krok 3: Obliczam rownolegle_b_r ---")
    wynik_rbr = rownolegle_b_r(G, wynik_po_ro)
    for idx, wpis in enumerate(wynik_rbr, 1):
        print(f"  {idx}. waga_oryg={list(wpis['waga_original'])}, waga_przem={list(wpis['waga_przemnozona'])}, "
              f"parz={wpis['suma_count_parzyste']}, nieparz={wpis['suma_count_nieparzyste']}, znak={wpis['znak']}")
    
    # Krok 4: Dodaj ro_2 do każdej wagi wynikowej (waga_przem)
    print("\n--- Krok 4: Dodaję ro_2 do każdej wagi wynikowej ---")
    wynik_po_ro2 = []
    for idx, wpis in enumerate(wynik_rbr, 1):
        w = list(wpis['waga_przemnozona'])
        wagi_po_ro2 = ro_2(G, w)
        print(f"  {idx}. {w} -> {wagi_po_ro2}")
        wynik_po_ro2.append(wagi_po_ro2)

    print("\n--- Wynik końcowy (wszystkie wagi nieujemne) ---")
    for idx, w in enumerate(wynik_po_ro2, 1):
        if w and all(x >= 0 for x in w):
            print(f"  {idx}. {w}")
    
    print("\n=== KONIEC ===")
    return wynik_po_ro2

def pushing_down_sym(G, lista_wag, k):
    """
    Dla ustalonego T_pqr i listy wag:
    1. Liczy symetryczną
    2. Liczy rownolegle_b_r dla wszystkich list wag
    """
    print("\n=== PUSHING DOWN SYM ===")
    
    # Krok 1: Oblicz symetryczną
    print(f"\n--- Krok 1: Obliczam symetryczną (k={k}) ---")
    wynik_symetryczna = symetryczna(lista_wag, k)
    print(f"Wynik symetrycznej ({len(wynik_symetryczna)} elementów):")
    for idx, w in enumerate(wynik_symetryczna, 1):
        print(f"  {idx}. {w}")
    
    # Krok 2: Oblicz rownolegle_b_r dla wszystkich list wag
    print("\n--- Krok 2: Obliczam rownolegle_b_r ---")
    wynik_rbr = rownolegle_b_r(G, wynik_symetryczna)
    for idx, wpis in enumerate(wynik_rbr, 1):
        print(f"  {idx}. waga_oryg={list(wpis['waga_original'])}, waga_przem={list(wpis['waga_przemnozona'])}, "
              f"parz={wpis['suma_count_parzyste']}, nieparz={wpis['suma_count_nieparzyste']}, znak={wpis['znak']}")
    
    print("\n--- Wynik końcowy (wszystkie wagi nieujemne) ---")
    for idx, wpis in enumerate(wynik_rbr, 1):
        w = list(wpis['waga_original'])
        wp = list(wpis['waga_przemnozona'])
        if w and all(x >= 0 for x in w):
            print(f"  {idx}. waga_oryg={w}, waga_przem={wp}")
    
    print("\n=== KONIEC ===")
    return wynik_rbr

def pushing_down_zewn(G, lista_wag, k):
    """
    Dla ustalonego T_pqr i listy wag:
    1. Liczy zewnętrzną
    2. Liczy rownolegle_b_r dla wszystkich list wag
    """
    print("\n=== PUSHING DOWN ZEWN ===")
    
    # Krok 1: Oblicz zewnętrzną
    print(f"\n--- Krok 1: Obliczam zewnętrzną (k={k}) ---")
    wynik_zewnetrzna = zewnetrzna(lista_wag, k)
    print(f"Wynik zewnętrznej ({len(wynik_zewnetrzna)} elementów):")
    for idx, w in enumerate(wynik_zewnetrzna, 1):
        print(f"  {idx}. {w}")
    
    # Krok 2: Oblicz rownolegle_b_r dla wszystkich list wag
    print("\n--- Krok 2: Obliczam rownolegle_b_r ---")
    wynik_rbr = rownolegle_b_r(G, wynik_zewnetrzna)
    for idx, wpis in enumerate(wynik_rbr, 1):
        print(f"  {idx}. waga_oryg={list(wpis['waga_original'])}, waga_przem={list(wpis['waga_przemnozona'])}, "
              f"parz={wpis['suma_count_parzyste']}, nieparz={wpis['suma_count_nieparzyste']}, znak={wpis['znak']}")
    
    print("\n--- Wynik końcowy (wszystkie wagi nieujemne) ---")
    for idx, wpis in enumerate(wynik_rbr, 1):
        w = list(wpis['waga_original'])
        wp = list(wpis['waga_przemnozona'])
        if w and all(x >= 0 for x in w):
            print(f"  {idx}. waga_oryg={w}, waga_przem={wp}")
    
    print("\n=== KONIEC ===")
    return wynik_rbr

def pushing_down_sym_ro_twist(G, lista_wag, k, lista):
    """
    Dla ustalonego T_pqr i listy wag:
    1. Liczy symetryczną
    2. Dodaje twist (lista) do każdego wyniku symetrycznej
    3. Dodaje ro_1 do każdej listy wag po twiście
    4. Liczy rownolegle_b_r dla wszystkich list wag po ro_1
    5. Odejmuje ro (ro_2) od każdej wagi wynikowej z rownolegle_b_r (waga_przem)
    """
    print("\n=== PUSHING DOWN SYM RO TWIST ===")

    # Krok 1: Oblicz symetryczną
    print(f"\n--- Krok 1: Obliczam symetryczną (k={k}) ---")
    wynik_symetryczna = symetryczna(lista_wag, k)
    print(f"Wynik symetrycznej ({len(wynik_symetryczna)} elementów):")
    for idx, w in enumerate(wynik_symetryczna, 1):
        print(f"  {idx}. {w}")

    # Krok 2: Dodaj twist do każdego wyniku symetrycznej
    print(f"\n--- Krok 2: Dodaję twist={lista} do każdego wyniku symetrycznej ---")
    wynik_po_twiście = []
    for idx, w in enumerate(wynik_symetryczna, 1):
        w_list = list(w) if isinstance(w, tuple) else w
        w_twist = [x + y for x, y in zip(w_list, lista)]
        print(f"  {idx}. {w_list} + {lista} = {w_twist}")
        wynik_po_twiście.append(w_twist)

    # Krok 3: Dodaj ro_1 do każdej listy wag po twiście
    print("\n--- Krok 3: Dodaję ro_1 do każdej listy wag po twiście ---")
    wynik_po_ro = []
    for idx, w in enumerate(wynik_po_twiście, 1):
        wagi_po_ro = ro_1(G, w)
        print(f"  {idx}. {w} -> {wagi_po_ro}")
        wynik_po_ro.append(wagi_po_ro)

    # Krok 4: Oblicz rownolegle_b_r dla wszystkich list wag po ro_1
    print("\n--- Krok 4: Obliczam rownolegle_b_r ---")
    wynik_rbr = rownolegle_b_r(G, wynik_po_ro)
    for idx, wpis in enumerate(wynik_rbr, 1):
        print(f"  {idx}. waga_oryg={list(wpis['waga_original'])}, waga_przem={list(wpis['waga_przemnozona'])}, "
              f"parz={wpis['suma_count_parzyste']}, nieparz={wpis['suma_count_nieparzyste']}, znak={wpis['znak']}")

    # Krok 5: Odejmij ro (ro_2) od każdej wagi wynikowej (waga_przem)
    print("\n--- Krok 5: Odejmuję ro (ro_2) od każdej wagi wynikowej ---")
    wynik_koncowy = []
    for idx, wpis in enumerate(wynik_rbr, 1):
        w = list(wpis['waga_przemnozona'])
        wagi_po_ro2 = ro_2(G, w)
        print(f"  {idx}. {w} -> {wagi_po_ro2}")
        wynik_koncowy.append(wagi_po_ro2)

    print("\n--- Wynik końcowy (wszystkie wagi nieujemne) ---")
    for idx, w in enumerate(wynik_koncowy, 1):
        if w and all(x >= 0 for x in w):
            print(f"  {idx}. {w}")

    print("\n=== KONIEC ===")
    return wynik_koncowy


def pushing_down_zewn_ro_twist(G, lista_wag, k, lista):
    """
    Dla ustalonego T_pqr i listy wag:
    1. Liczy zewnętrzną
    2. Dodaje twist (lista) do każdego wyniku zewnętrznej
    3. Dodaje ro_1 do każdej listy wag po twiście
    4. Liczy rownolegle_b_r dla wszystkich list wag po ro_1
    5. Odejmuje ro (ro_2) od każdej wagi wynikowej z rownolegle_b_r (waga_przem)
    """
    print("\n=== PUSHING DOWN ZEWN RO TWIST ===")

    # Krok 1: Oblicz zewnętrzną
    print(f"\n--- Krok 1: Obliczam zewnętrzną (k={k}) ---")
    wynik_zewnetrzna = zewnetrzna(lista_wag, k)
    print(f"Wynik zewnętrznej ({len(wynik_zewnetrzna)} elementów):")
    for idx, w in enumerate(wynik_zewnetrzna, 1):
        print(f"  {idx}. {w}")

    # Krok 2: Dodaj twist do każdego wyniku zewnętrznej
    print(f"\n--- Krok 2: Dodaję twist={lista} do każdego wyniku zewnętrznej ---")
    wynik_po_twiście = []
    for idx, w in enumerate(wynik_zewnetrzna, 1):
        w_list = list(w) if isinstance(w, tuple) else w
        w_twist = [x + y for x, y in zip(w_list, lista)]
        print(f"  {idx}. {w_list} + {lista} = {w_twist}")
        wynik_po_twiście.append(w_twist)

    # Krok 3: Dodaj ro_1 do każdej listy wag po twiście
    print("\n--- Krok 3: Dodaję ro_1 do każdej listy wag po twiście ---")
    wynik_po_ro = []
    for idx, w in enumerate(wynik_po_twiście, 1):
        wagi_po_ro = ro_1(G, w)
        print(f"  {idx}. {w} -> {wagi_po_ro}")
        wynik_po_ro.append(wagi_po_ro)

    # Krok 4: Oblicz rownolegle_b_r dla wszystkich list wag po ro_1
    print("\n--- Krok 4: Obliczam rownolegle_b_r ---")
    wynik_rbr = rownolegle_b_r(G, wynik_po_ro)
    for idx, wpis in enumerate(wynik_rbr, 1):
        print(f"  {idx}. waga_oryg={list(wpis['waga_original'])}, waga_przem={list(wpis['waga_przemnozona'])}, "
              f"parz={wpis['suma_count_parzyste']}, nieparz={wpis['suma_count_nieparzyste']}, znak={wpis['znak']}")

    # Krok 5: Odejmij ro (ro_2) od każdej wagi wynikowej (waga_przem)
    print("\n--- Krok 5: Odejmuję ro (ro_2) od każdej wagi wynikowej ---")
    wynik_koncowy = []
    for idx, wpis in enumerate(wynik_rbr, 1):
        w = list(wpis['waga_przemnozona'])
        wagi_po_ro2 = ro_2(G, w)
        print(f"  {idx}. {w} -> {wagi_po_ro2}")
        wynik_koncowy.append(wagi_po_ro2)

    print("\n--- Wynik końcowy (wszystkie wagi nieujemne) ---")
    for idx, w in enumerate(wynik_koncowy, 1):
        if w and all(x >= 0 for x in w):
            print(f"  {idx}. {w}")

    print("\n=== KONIEC ===")
    return wynik_koncowy


def menu(grafy_cache, wagi_cache):
    while True:
        print("\n=== MENU GŁÓWNE ===")
        print("--- Ustawienia danych ---")
        print("1. Ustal graf T_pqr")
        print("2. Ustal listę wag (format: [[1,2],[3,4]] - wszystkie na raz)")
        print("\n--- Operacje ---")
        print("3. symetryczna")
        print("4. zewnetrzna")
        print("5. rownolegle")
        print("6. rownolegle_mod")
        print("7. positive")
        print("8. pushing down symetryczna twist")
        print("9. pushing down zewnetrzna twist")
        print("10. extremal")
        print("11. pushing down symetryczna ro")
        print("12. pushing down zewnnętrzna ro")
        print("13. pushing down symetryczna")
        print("14. pushing down zewnętrzna")
        print("15. pushing down symetryczna ro twist")
        print("16. pushing down zewnętrzna ro twist")
        print("\n17. Wyjdź")
        
        wybor = input("\nWybierz opcję: ").strip()
        
        if wybor == '1':
            p = pobierz_int("Podaj p: ")
            q = pobierz_int("Podaj q: ")
            r = pobierz_int("Podaj r: ")
            grafy_cache['T_pqr'] = T_pqr(p, q, r)
            print(f"Graf T_pqr ustawiony ({grafy_cache['T_pqr'].number_of_nodes()} wierzchołków).")
            
        elif wybor == '2':
            # Deklaruj wszystkie wagi jednocześnie
            print("\n=== DEKLARACJA LISTY WAG ===")
            print("Wszystkie wagi deklaruj teraz jednocześnie w jednym wejściu!")
            print("\nFormat:")
            print("  Dla jednej listy wag:  [[1,2,3,4]]")
            print("  Dla wielu list wag:    [[1,2],[3,4],[5,6]]")
            print("\nPrzykład:")
            print("  Wpisz: [[1,2],[3,4]]")
            print("  To będzie zinterpretowane jako dwie listy: [1,2] i [3,4]")
            print("\nLista zapisana w pliku tekstowym będzie miała dokładnie taki format,")
            print("więc możesz ją bezpośrednio wkleić tutaj w następnym uruchomieniu!")
            input_wagi = input("\nPodaj listy wag: ").strip()
            try:
                lista_wag = eval(input_wagi)
                # Sprawdź czy to jest lista list
                if not isinstance(lista_wag, list):
                    lista_wag = [lista_wag]
                # Konwersja do list liczb całkowitych
                lista_wag_czyszczna = []
                for row in lista_wag:
                    if isinstance(row, (list, tuple)):
                        lista_wag_czyszczna.append([int(x) for x in row])
                    else:
                        lista_wag_czyszczna.append([int(row)])
                wagi_cache['wagi'] = lista_wag_czyszczna
                print(f"Zapisano wagi: {lista_wag_czyszczna}")
            except Exception as e:
                print(f"Błąd przy parsowaniu wag: {e}")
        
        elif wybor in ['3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']:
            # Sprawdź czy graf jest ustawiony
            if 'T_pqr' not in grafy_cache:
                print("Najpierw ustaw graf T_pqr (opcja 1)!")
                continue
            
            G = grafy_cache['T_pqr']
            
            # Wykonaj wybraną operację
            if wybor in ['3', '4']:  # symetryczna lub zewnetrzna
                if 'wagi' in wagi_cache:
                    A = wagi_cache['wagi']
                else:
                    A = eval(input("Podaj listę list (A) np [[1,2],[3,4]]: "))
                
                # Konwersja do int
                A_clean = []
                for row in A:
                    if isinstance(row, (list, tuple)):
                        A_clean.append([int(x) for x in row])
                    else:
                        A_clean.append(row)
                A = A_clean
                
                k = pobierz_int("Podaj wartość k: ")
                wynik = symetryczna(A, k) if wybor == '3' else zewnetrzna(A, k)
                print("\nWynik:")
                for idx, w in enumerate(wynik, 1):
                    print(f"{idx}. {w}")
                wagi_cache['ostatni_wynik'] = wynik
                # Pytanie o zapis wyniku
                nazwa_op = "symetryczna" if wybor == '3' else "zewnetrzna"
                zapisz_wynik_do_pliku(wynik, nazwa_op)
                
            elif wybor in ['5', '6']:  # rownolegle lub rownolegle_mod
                if 'wagi' in wagi_cache:
                    lista_wag = wagi_cache['wagi']
                else:
                    lista_wag = eval(input("Podaj listę list wag np [[1,2],[3,4]]: "))
                
                if wybor == '5':
                    wynik = rownolegle4(G, lista_wag)
                else:
                    wynik = rownolegle_mod(G, lista_wag)
                print("\nWynik:")
                print(wynik)
                # Wyciągnij odpowiednią wagę w zależności od typu wyniku
                wynik_do_zapisu = []
                for wpis in wynik:
                    if 'waga_przemnozona' in wpis:
                        # Dla rownolegle4
                        wynik_do_zapisu.append(list(wpis['waga_przemnozona']))
                    elif 'waga' in wpis:
                        # Dla rownolegle_mod
                        wynik_do_zapisu.append(wpis['waga'])
                
                wagi_cache['ostatni_wynik'] = wynik
                # Pytanie o zapis wyniku
                nazwa_op = "rownolegle" if wybor == '5' else "rownolegle_mod"
                zapisz_wynik_do_pliku(wynik_do_zapisu, nazwa_op)
                
            elif wybor == '7':  # positive
                if 'wagi' in wagi_cache and isinstance(wagi_cache['wagi'], list) and len(wagi_cache['wagi']) > 0:
                    wagi = wagi_cache['wagi'][0] if isinstance(wagi_cache['wagi'][0], list) else wagi_cache['wagi']
                else:
                    wagi = eval(input("Podaj listę wag np [1,2,3,4]: "))
                wynik, count = positive(G, wagi)
                print(f"\nWynik: {wynik}, liczba iteracji: {count}")
                wagi_cache['ostatni_wynik'] = wynik
                # Pytanie o zapis wyniku
                zapisz_wynik_do_pliku(wynik, "positive")
                
            elif wybor == '8':  # pushing_down
                if 'wagi' in wagi_cache:
                    wagi = wagi_cache['wagi']
                else:
                    wagi = eval(input("Podaj listę wag np [[1,2],[3,4]]: "))
                k = int(input("Podaj wartość k do potęgi symetrycznej: "))
                lista = eval(input("Podaj listę twist np [1,2,3,4]: "))
                wynik = pushing_down(G, wagi, k, lista)
                print("\nWynik:")
                print(wynik)
                wagi_cache['ostatni_wynik'] = wynik
                # Pytanie o zapis wyniku
                zapisz_wynik_do_pliku(wynik, "pushing_down_sym_twist")
                
            elif wybor == '9':  # pushinkg_down_zewnetrzna
                if 'wagi' in wagi_cache:
                    wagi = wagi_cache['wagi']
                else:
                    wagi = eval(input("Podaj listę wag np [[1,2],[3,4]]: "))
                k = int(input("Podaj wartość k do potęgi zewnentrznej: "))
                lista = eval(input("Podaj listę twist np [1,2,3,4]: "))
                wynik = pushinkg_down_zewnetrzna(G, wagi, k, lista)
                print("\nWynik:")
                print(wynik)
                wagi_cache['ostatni_wynik'] = wynik
                # Pytanie o zapis wyniku
                zapisz_wynik_do_pliku(wynik, "pushing_down_zewn_twist")
                
            elif wybor == '10':  # extremal
                if 'wagi' in wagi_cache and isinstance(wagi_cache['wagi'], list) and len(wagi_cache['wagi']) > 0:
                    wagi = wagi_cache['wagi'][0] if isinstance(wagi_cache['wagi'][0], list) else wagi_cache['wagi']
                else:
                    wagi = eval(input("Podaj listę wag np [1,2,3,4]: "))
                exception = pobierz_int("Podaj indeks wyjątku: ")
                wynik = extremal(G, wagi, exception)
                wagi_cache['ostatni_wynik'] = wynik
                # Pytanie o zapis wyniku
                zapisz_wynik_do_pliku(wynik, "extremal")
                
            elif wybor == '11':  # pushing_down_sym_ro
                if 'wagi' in wagi_cache:
                    lista_wag = wagi_cache['wagi']
                else:
                    lista_wag = eval(input("Podaj listę wag np [[1,2],[3,4]]: "))
                k = int(input("Podaj wartość k do potęgi symetrycznej: "))
                wynik = pushing_down_sym_ro(G, lista_wag, k)
                # Filtruj tylko wagi nieujemne do zapisania
                wynik_do_zapisu = [w for w in wynik if w and all(x >= 0 for x in w)]
                wagi_cache['ostatni_wynik'] = wynik
                # Pytanie o zapis wyniku
                zapisz_wynik_do_pliku(wynik_do_zapisu, "pushing_down_sym_ro")
                
            elif wybor == '12':  # pushing_down_zewn_ro
                if 'wagi' in wagi_cache:
                    lista_wag = wagi_cache['wagi']
                else:
                    lista_wag = eval(input("Podaj listę wag np [[1,2],[3,4]]: "))
                k = int(input("Podaj wartość k do potęgi zewnętrznej: "))
                wynik = pushing_down_zewn_ro(G, lista_wag, k)
                # Filtruj tylko wagi nieujemne do zapisania
                wynik_do_zapisu = [w for w in wynik if w and all(x >= 0 for x in w)]
                wagi_cache['ostatni_wynik'] = wynik
                # Pytanie o zapis wyniku
                zapisz_wynik_do_pliku(wynik_do_zapisu, "pushing_down_zewn_ro")

            elif wybor == '13':  # pushing_down_sym
                if 'wagi' in wagi_cache:
                    lista_wag = wagi_cache['wagi']
                else:
                    lista_wag = eval(input("Podaj listę wag np [[1,2],[3,4]]: "))
                k = int(input("Podaj wartość k do potęgi symetrycznej: "))
                wynik = pushing_down_sym(G, lista_wag, k)
                # Dla pushing_down_sym wynik to lista dicts, zapisz tylko waga_przem z każdego wpisu
                wynik_do_zapisu = [list(wpis['waga_przemnozona']) for wpis in wynik]
                wagi_cache['ostatni_wynik'] = wynik
                # Pytanie o zapis wyniku
                zapisz_wynik_do_pliku(wynik_do_zapisu, "pushing_down_sym")

            elif wybor == '14':  # pushing_down_zewn
                if 'wagi' in wagi_cache:
                    lista_wag = wagi_cache['wagi']
                else:
                    lista_wag = eval(input("Podaj listę wag np [[1,2],[3,4]]: "))
                k = int(input("Podaj wartość k do potęgi zewnętrznej: "))
                wynik = pushing_down_zewn(G, lista_wag, k)
                # Dla pushing_down_zewn wynik to lista dicts, zapisz tylko waga_przem z każdego wpisu
                wynik_do_zapisu = [list(wpis['waga_przemnozona']) for wpis in wynik]
                wagi_cache['ostatni_wynik'] = wynik
                # Pytanie o zapis wyniku
                zapisz_wynik_do_pliku(wynik_do_zapisu, "pushing_down_zewn")

            elif wybor == '15':  # pushing_down_sym_ro_twist
                if 'wagi' in wagi_cache:
                    lista_wag = wagi_cache['wagi']
                else:
                    lista_wag = eval(input("Podaj listę wag np [[1,2],[3,4]]: "))
                k = int(input("Podaj wartość k do potęgi symetrycznej: "))
                lista = eval(input("Podaj listę twist np [1,2,3,4]: "))
                wynik = pushing_down_sym_ro_twist(G, lista_wag, k, lista)
                # Filtruj tylko wagi nieujemne do zapisania
                wynik_do_zapisu = [w for w in wynik if w and all(x >= 0 for x in w)]
                wagi_cache['ostatni_wynik'] = wynik
                # Pytanie o zapis wyniku
                zapisz_wynik_do_pliku(wynik_do_zapisu, "pushing_down_sym_ro_twist")

            elif wybor == '16':  # pushing_down_zewn_ro_twist
                if 'wagi' in wagi_cache:
                    lista_wag = wagi_cache['wagi']
                else:
                    lista_wag = eval(input("Podaj listę wag np [[1,2],[3,4]]: "))
                k = int(input("Podaj wartość k do potęgi zewnętrznej: "))
                lista = eval(input("Podaj listę twist np [1,2,3,4]: "))
                wynik = pushing_down_zewn_ro_twist(G, lista_wag, k, lista)
                # Filtruj tylko wagi nieujemne do zapisania
                wynik_do_zapisu = [w for w in wynik if w and all(x >= 0 for x in w)]
                wagi_cache['ostatni_wynik'] = wynik
                # Pytanie o zapis wyniku
                zapisz_wynik_do_pliku(wynik_do_zapisu, "pushing_down_zewn_ro_twist")

        elif wybor == '17':
            print("Do widzenia!")
            break
        else:
            print("Niepoprawny wybór!")
import itertools as it
import numpy as np
import networkx as nx
import copy
from collections import defaultdict, Counter

import networkx as nx

def T_pqr(p, q, r):
    """
    Tworzy graf typu T(p,q,r):
    - jeden węzeł centralny (0)
    - trzy ramiona o długościach p-1, q-1, r-1
    """
    if p < 1 or q < 1 or r < 1:
        raise ValueError("p, q, r muszą być >= 1")

    G = nx.Graph()
    G.add_node(0, weight=0)

    current = 1

    def add_arm(length):
        nonlocal current
        prev = 0
        for _ in range(length):
            G.add_node(current, weight=0)
            G.add_edge(prev, current)
            prev = current
            current += 1

    add_arm(p - 1)
    add_arm(q - 1)
    add_arm(r - 1)

    return G
def symetryczna(A, k):
    max_len = max(len(sublist) for sublist in A)
    wyniki = []

    for kombinacja in it.combinations_with_replacement(range(len(A)), k):
        summed_sublist = []

        for j in range(max_len):
            sublist_sum = sum(
                A[i][j] if j < len(A[i]) else 0
                for i in kombinacja
            )
            summed_sublist.append(sublist_sum)

        wyniki.append(summed_sublist)

    return wyniki



def zewnetrzna(A, k):
    max_len = max(len(sublist) for sublist in A)
    wyniki = []

    for kombinacja in it.combinations(range(len(A)), k):
        summed_sublist = []
        for j in range(max_len):
            sublist_sum = sum(
                A[i][j] if j < len(A[i]) else 0
                for i in kombinacja
            )
            summed_sublist.append(sublist_sum)

        wyniki.append(summed_sublist)

    return wyniki
#liczy zewenętrznąale numeruje poszczególne linijki outputu. Dla testów
# czy liczy odpowiednio
def zewnetrzna_num(A, k):
    
    max_len = max(len(sublist) for sublist in A)
    zewn = []
    
    for kombinacja in it.combinations(range(len(A)), k):
        summed_sublist = []
        for j in range(max_len):
            sublist_sum = sum(A[i][j] if j < len(A[i]) else 0 for i in kombinacja)
            summed_sublist.append(sublist_sum)
        zewn.append(summed_sublist)
    for idx, wynik in enumerate(zewn, 1):
        print(f"{idx} : {wynik}")


def nadawanie_wag(G, wagi_lista):
    wagi = []
    n = G.number_of_nodes()
    if len(wagi_lista) < n:
        raise ValueError(f"Za krótka waga: podano {len(wagi_lista)}, oczekiwano {n}.")
    if len(wagi_lista) > n:
        raise ValueError(f"Za długa waga: podano {len(wagi_lista)}, oczekiwano {n}.")
    for idx, (node, weight) in enumerate(zip(G.nodes, wagi_lista)):
        G.nodes[node]['weight'] = weight
    for _, w in G.nodes(data='weight'):
        wagi.append(w)
    return wagi
def odbicie(G, node, wagi):
    #jeśli chcesz sprawdzić, czy odbicie działa oraz chcesz mieć wypisane wagi, komenda poniżej to umożliwia:
    #print(nadawanie_wag(G, wagi_lista))
    
    wagi = [] 

    neighbors = list(G.neighbors(node))

    nowa_waga1 = - G.nodes[node]['weight']
    G.nodes[node]['weight'] = nowa_waga1

    for neighbor in neighbors:
        nowa_waga = G.nodes[neighbor]['weight'] -  G.nodes[node]['weight']
        G.nodes[neighbor]['weight'] = nowa_waga
    for _, w in G.nodes(data='weight'):
        wagi.append(w)
    return wagi
def ro_1(G, wagi):
    # Najpierw nadaj wagi do grafu
    nadawanie_wag(G, wagi)
    # Zwiększ każdą wagę o 1
    nowe_wagi = []
    for node in G.nodes():
        G.nodes[node]['weight'] += 1
        nowe_wagi.append(G.nodes[node]['weight'])
    return nowe_wagi

def ro_2(G, wagi):
    # Najpierw nadaj wagi do grafu
    nadawanie_wag(G, wagi)
    # Zmniejsz każdą wagę o 1
    nowe_wagi = []
    for node in G.nodes():
        G.nodes[node]['weight'] -= 1
        nowe_wagi.append(G.nodes[node]['weight'])
    return nowe_wagi

#podział na plusy i minusy

### aby zwiększyć limit na councie popraw liczbę w linijce:
### while not pozytywne(wagi_kopia) and count < 10000000: (13 linijka, nie licząc pustych)

def rownolegle_mod(G, lista_wag):
    def pozytywne(wagi):
        return all(weight >= 0 for weight in wagi)

    wyniki_dla_wszystkich_list = []

    for wagi in lista_wag:
        # Ensure wagi is a list before copying
        if isinstance(wagi, (int, float)):
            wagi_kopia = [wagi]
        else:
            wagi_kopia = wagi.copy()
        nadawanie_wag(G, wagi_kopia)

        count = 0
        if pozytywne(wagi_kopia):
            wyniki_dla_wszystkich_list.append((tuple(wagi_kopia), count))
            continue

        poczatkowy_stan = tuple(wagi_kopia)

        while not pozytywne(wagi_kopia) and count < 10000:
            sorted_nodes = sorted(G.nodes(data=True), key=lambda x: x[1]["weight"],
                reverse=True)
            nodes_ujemne = [node for node, data in sorted_nodes
                if isinstance(data.get('weight'), (int, float)) and data['weight'] < 0]

            for node in nodes_ujemne:
                wynik = ro_1(G, wagi_kopia)
                wynik2 = odbicie(G, node, wynik)
                wynik3 = ro_2(G, wynik2)

                wagi_kopia = wynik3.copy()
                count += 1

                if pozytywne(wagi_kopia):
                    wyniki_dla_wszystkich_list.append((tuple(wagi_kopia), count))
                    break

                if tuple(wagi_kopia) == poczatkowy_stan:
                    wyniki_dla_wszystkich_list.append(([], count))
                    break
            else:
                continue
            break

    wystapienia_wag = Counter(waga for waga, _ in wyniki_dla_wszystkich_list if waga)

    waga_do_count = defaultdict(lambda: {'nieparzyste': 0, 'parzyste': 0})
    
    for waga, count in wyniki_dla_wszystkich_list:
        if waga:
            if wystapienia_wag[waga] == 1 and count == 0:
                waga_do_count[waga]['parzyste'] = 1
                waga_do_count[waga]['nieparzyste'] = '0'

            else:
                if count % 2 == 0:
                    waga_do_count[waga]['parzyste'] += 1
                else:
                    waga_do_count[waga]['nieparzyste'] += 1

    wynik = [
        {'suma_count_nieparzyste': counts['nieparzyste'], 'suma_count_parzyste':counts['parzyste'], 'waga': list(waga)}
        for waga, counts in waga_do_count.items()
    ]

    return wynik

#podział na plusy i minusy

### aby zwiększyć limit na councie popraw liczbę w linijce:
### while not pozytywne(wagi_kopia) and count < 10000000: (13 linijka, nie licząc pustych)

### ta procedura redukuje wagi, które mają tyle samo plusów co minusów
def rownolegle(G, lista_wag):
    def pozytywne(wagi):
        return all(weight >= 0 for weight in wagi)

    wyniki_dla_wszystkich_list = []

    for wagi in lista_wag:
        wagi_kopia = wagi.copy()
        nadawanie_wag(G, wagi_kopia)

        count = 0
        if pozytywne(wagi_kopia):
            wyniki_dla_wszystkich_list.append((tuple(wagi_kopia), count))
            continue

        poczatkowy_stan = tuple(wagi_kopia)

        while not pozytywne(wagi_kopia) and count < 10000:
            sorted_nodes = sorted(G.nodes(data=True), key=lambda x: x[1]["weight"],
                reverse=True)
            nodes_ujemne = [node for node, data in sorted_nodes
                if isinstance(data.get('weight'), (int, float)) and data['weight'] < 0]

            for node in nodes_ujemne:
                wynik = ro_1(G, wagi_kopia)
                wynik2 = odbicie(G, node, wynik)
                wynik3 = ro_2(G, wynik2)

                wagi_kopia = wynik3.copy()
                count += 1

                if pozytywne(wagi_kopia):
                    wyniki_dla_wszystkich_list.append((tuple(wagi_kopia), count))
                    break

                if tuple(wagi_kopia) == poczatkowy_stan:
                    wyniki_dla_wszystkich_list.append(([], count))
                    break
            else:
                continue
            break

    wystapienia_wag = Counter(waga for waga, _ in wyniki_dla_wszystkich_list if waga)

    waga_do_count = defaultdict(lambda: {'nieparzyste': 0, 'parzyste': 0})
    
    for waga, count in wyniki_dla_wszystkich_list:
        if waga:
            if wystapienia_wag.get(waga, 0) == 1 and count == 0:
                waga_do_count[waga]['parzyste'] = 1
                waga_do_count[waga]['nieparzyste'] = 0
            else:
                if count % 2 == 0:
                    waga_do_count[waga]['parzyste'] += 1
                else:
                    waga_do_count[waga]['nieparzyste'] += 1
    wynik = [
        {'suma_count_nieparzyste': counts['nieparzyste'], 
         'suma_count_parzyste': counts['parzyste'], 
         'waga': waga}
        for waga, counts in waga_do_count.items()
        if counts['parzyste'] != counts['nieparzyste']

    ]
    return wynik

def rownolegle1(G, lista_wag):
    def pozytywne(wagi):
        return all(weight >= 0 for weight in wagi)

    wyniki_dla_wszystkich_list = []

    for wagi in lista_wag:
        wagi_kopia = wagi.copy()
        nadawanie_wag(G, wagi_kopia)

        count = 0
        if pozytywne(wagi_kopia):
            wyniki_dla_wszystkich_list.append((tuple(wagi_kopia), count))
            continue

        poczatkowy_stan = tuple(wagi_kopia)

        while not pozytywne(wagi_kopia) and count < 10000:
            sorted_nodes = sorted(
                G.nodes(data=True),
                key=lambda x: x[1].get("weight", 0),
                reverse=True
            )

            nodes_ujemne = [
                node for node, data in sorted_nodes
                if isinstance(data.get('weight'), (int, float)) and data['weight'] < 0
            ]

            for node in nodes_ujemne:
                wynik = ro_1(G, wagi_kopia)
                wynik2 = odbicie(G, node, wynik)
                wynik3 = ro_2(G, wynik2)

                wagi_kopia = wynik3.copy()
                count += 1

                if pozytywne(wagi_kopia):
                    wyniki_dla_wszystkich_list.append((tuple(wagi_kopia), count))
                    break

                if tuple(wagi_kopia) == poczatkowy_stan:
                    wyniki_dla_wszystkich_list.append(([], count))
                    break
            else:
                continue
            break

    # Liczenie wystąpień wag
    wystapienia_wag = Counter(waga for waga, _ in wyniki_dla_wszystkich_list if waga)

    waga_do_count = defaultdict(lambda: {'nieparzyste': 0, 'parzyste': 0})
    
    for waga, count in wyniki_dla_wszystkich_list:
        if waga:
            if wystapienia_wag.get(waga, 0) == 1 and count == 0:
                waga_do_count[waga]['parzyste'] = 1
                waga_do_count[waga]['nieparzyste'] = 0
            else:
                if count % 2 == 0:
                    waga_do_count[waga]['parzyste'] += 1
                else:
                    waga_do_count[waga]['nieparzyste'] += 1

    # Tworzenie wyniku
    wynik = []
    for waga, counts in waga_do_count.items():
        if counts['parzyste'] != counts['nieparzyste']:
            suma_count = counts['parzyste'] + counts['nieparzyste']
            wynik.append({
                'waga': waga,
                'suma_count_parzyste': counts['parzyste'],
                'suma_count_nieparzyste': counts['nieparzyste'],
                'suma_count': suma_count
            })

    return wynik


def rownolegle2(G, lista_wag):
    def pozytywne(wagi):
        return all(weight >= 0 for weight in wagi)

    wyniki_dla_wszystkich_list = []

    for wagi in lista_wag:
        wagi_kopia = wagi.copy()
        nadawanie_wag(G, wagi_kopia)

        count = 0
        if pozytywne(wagi_kopia):
            wyniki_dla_wszystkich_list.append((tuple(wagi_kopia), count))
            continue

        poczatkowy_stan = tuple(wagi_kopia)

        while not pozytywne(wagi_kopia) and count < 10000:
            sorted_nodes = sorted(
                G.nodes(data=True),
                key=lambda x: x[1].get("weight", 0),
                reverse=True
            )

            nodes_ujemne = [
                node for node, data in sorted_nodes
                if isinstance(data.get('weight'), (int, float)) and data['weight'] < 0
            ]

            for node in nodes_ujemne:
                wynik = ro_1(G, wagi_kopia)
                wynik2 = odbicie(G, node, wynik)
                wynik3 = ro_2(G, wynik2)

                wagi_kopia = wynik3.copy()
                count += 1

                if pozytywne(wagi_kopia):
                    wyniki_dla_wszystkich_list.append((tuple(wagi_kopia), count))
                    break

                if tuple(wagi_kopia) == poczatkowy_stan:
                    wyniki_dla_wszystkich_list.append(([], count))
                    break
            else:
                continue
            break

    # Liczenie wystąpień wag
    wystapienia_wag = Counter(waga for waga, _ in wyniki_dla_wszystkich_list if waga)

    waga_do_count = defaultdict(lambda: {'nieparzyste': 0, 'parzyste': 0})
    
    for waga, count in wyniki_dla_wszystkich_list:
        if waga:
            if wystapienia_wag.get(waga, 0) == 1 and count == 0:
                waga_do_count[waga]['parzyste'] = 1
                waga_do_count[waga]['nieparzyste'] = 0
            else:
                if count % 2 == 0:
                    waga_do_count[waga]['parzyste'] += 1
                else:
                    waga_do_count[waga]['nieparzyste'] += 1

    # Tworzenie wyniku z dodanym współczynnikiem przed wagą
    wynik = []
    for waga, counts in waga_do_count.items():
        if counts['parzyste'] != counts['nieparzyste']:
            suma_count = counts['parzyste'] + counts['nieparzyste']
            waga_przemnozona = tuple(np.array(waga) * suma_count)
            wynik.append({
                'waga': waga_przemnozona,
                'suma_count_parzyste': counts['parzyste'],
                'suma_count_nieparzyste': counts['nieparzyste'],
                'suma_count': suma_count
            })

    return wynik


def rownolegle3(G, lista_wag):
    def pozytywne(wagi):
        return all(weight >= 0 for weight in wagi)

    wyniki_dla_wszystkich_list = []

    for wagi in lista_wag:
        wagi_kopia = wagi.copy()
        nadawanie_wag(G, wagi_kopia)

        count = 0
        if pozytywne(wagi_kopia):
            wyniki_dla_wszystkich_list.append((tuple(wagi_kopia), count))
            continue

        poczatkowy_stan = tuple(wagi_kopia)

        while not pozytywne(wagi_kopia) and count < 10000:
            sorted_nodes = sorted(
                G.nodes(data=True),
                key=lambda x: x[1].get("weight", 0),
                reverse=True
            )

            nodes_ujemne = [
                node for node, data in sorted_nodes
                if isinstance(data.get('weight'), (int, float)) and data['weight'] < 0
            ]

            for node in nodes_ujemne:
                wynik = ro_1(G, wagi_kopia)
                wynik2 = odbicie(G, node, wynik)
                wynik3 = ro_2(G, wynik2)

                wagi_kopia = wynik3.copy()
                count += 1

                if pozytywne(wagi_kopia):
                    wyniki_dla_wszystkich_list.append((tuple(wagi_kopia), count))
                    break

                if tuple(wagi_kopia) == poczatkowy_stan:
                    wyniki_dla_wszystkich_list.append(([], count))
                    break
            else:
                continue
            break

    # Liczenie wystąpień wag (tylko tych nie-pustych)
    wystapienia_wag = Counter(waga for waga, _ in wyniki_dla_wszystkich_list if waga)

    waga_do_count = defaultdict(lambda: {'nieparzyste': 0, 'parzyste': 0})

    for waga, count in wyniki_dla_wszystkich_list:
        if waga:
            # jeżeli waga wystąpiła tylko raz i count==0, traktujemy to jako parzyste=1 (jak w twojej logice)
            if wystapienia_wag.get(waga, 0) == 1 and count == 0:
                waga_do_count[waga]['parzyste'] = 1
                waga_do_count[waga]['nieparzyste'] = 0
            else:
                if count % 2 == 0:
                    waga_do_count[waga]['parzyste'] += 1
                else:
                    waga_do_count[waga]['nieparzyste'] += 1

    # Tworzenie końcowego wyniku
    wynik = []
    for waga, counts in waga_do_count.items():
        if counts['parzyste'] != counts['nieparzyste']:
            suma_count = counts['parzyste'] + counts['nieparzyste']
            # waga_przemnozona jako zwykła krotka intów (bez np.int64)
            waga_przemnozona = tuple(int(v * suma_count) for v in waga)
            wynik.append({
                'waga_original': tuple(int(v) for v in waga),
                'waga_przemnozona': waga_przemnozona,
                'suma_count_parzyste': counts['parzyste'],
                'suma_count_nieparzyste': counts['nieparzyste'],
                'suma_count': suma_count
            })

    return wynik

def rownolegle4(G, lista_wag):
    def pozytywne(wagi):
        return all(weight >= 0 for weight in wagi)

    wyniki_dla_wszystkich_list = []

    # Jeśli lista_wag to lista liczb (np. [1,2,3,4]), zamień na listę list
    if lista_wag and all(isinstance(x, (int, float)) for x in lista_wag):
        lista_wag = [lista_wag]

    for wagi in lista_wag:
        # Jeśli wagi są krotką, zamień na listę
        if isinstance(wagi, tuple):
            wagi_kopia = list(wagi)
        else:
            wagi_kopia = wagi.copy()
        nadawanie_wag(G, wagi_kopia)

        count = 0
        if pozytywne(wagi_kopia):
            wyniki_dla_wszystkich_list.append((tuple(wagi_kopia), count))
            continue

        poczatkowy_stan = tuple(wagi_kopia)

        while not pozytywne(wagi_kopia) and count < 10000:
            sorted_nodes = sorted(
                G.nodes(data=True),
                key=lambda x: x[1].get("weight", 0),
                reverse=True
            )

            nodes_ujemne = [
                node for node, data in sorted_nodes
                if isinstance(data.get('weight'), (int, float)) and data['weight'] < 0
            ]

            for node in nodes_ujemne:
                wynik = ro_1(G, wagi_kopia)
                wynik2 = odbicie(G, node, wynik)
                wynik3 = ro_2(G, wynik2)

                wagi_kopia = wynik3.copy()
                count += 1

                if pozytywne(wagi_kopia):
                    wyniki_dla_wszystkich_list.append((tuple(wagi_kopia), count))
                    break

                if tuple(wagi_kopia) == poczatkowy_stan:
                    wyniki_dla_wszystkich_list.append(([], count))
                    break
            else:
                continue
            break

    # Liczenie wystąpień wag (tylko tych nie-pustych)
    wystapienia_wag = Counter(waga for waga, _ in wyniki_dla_wszystkich_list if waga)

    waga_do_count = defaultdict(lambda: {'nieparzyste': 0, 'parzyste': 0})

    for waga, count in wyniki_dla_wszystkich_list:
        if waga:
            if wystapienia_wag.get(waga, 0) == 1 and count == 0:
                waga_do_count[waga]['parzyste'] = 1
                waga_do_count[waga]['nieparzyste'] = 0
            else:
                if count % 2 == 0:
                    waga_do_count[waga]['parzyste'] += 1
                else:
                    waga_do_count[waga]['nieparzyste'] += 1

    # Tworzenie końcowego wyniku
    wynik = []
    for waga, counts in waga_do_count.items():
        parz = counts['parzyste']
        nieparz = counts['nieparzyste']
        if parz != nieparz:
            suma_count = parz - nieparz
            # ustal znak: dodatni jeśli więcej parzystych, ujemny jeśli więcej nieparzystych
            znak = 1 if parz > nieparz else -1
            waga_przemnozona = tuple(int(v  * znak) for v in waga)
            wynik.append({
                'waga_original': tuple(int(v) for v in waga),
                'waga_przemnozona': waga_przemnozona,
                'suma_count_parzyste': parz,
                'suma_count_nieparzyste': nieparz,
                'suma_count': suma_count,
                'znak': znak
            })

    return wynik

def rownolegle_b_r(G, lista_wag):
    def pozytywne(wagi):
        return all(weight >= 0 for weight in wagi)

    wyniki_dla_wszystkich_list = []

    # Jeśli lista_wag to lista liczb (np. [1,2,3,4]), zamień na listę list
    if lista_wag and all(isinstance(x, (int, float)) for x in lista_wag):
        lista_wag = [lista_wag]

    for wagi in lista_wag:
        # Jeśli wagi są krotką, zamień na listę
        if isinstance(wagi, tuple):
            wagi_kopia = list(wagi)
        else:
            wagi_kopia = wagi.copy()
        nadawanie_wag(G, wagi_kopia)

        count = 0
        if pozytywne(wagi_kopia):
            wyniki_dla_wszystkich_list.append((tuple(wagi_kopia), count))
            continue

        poczatkowy_stan = tuple(wagi_kopia)
        while not pozytywne(wagi_kopia) and count < 10000:
            sorted_nodes = sorted(
                G.nodes(data=True),
                key=lambda x: x[1].get("weight", 0),
                reverse=True
            )

            nodes_ujemne = [
                node for node, data in sorted_nodes
                if isinstance(data.get('weight'), (int, float)) and data['weight'] < 0
            ]

            for node in nodes_ujemne:
                wynik = odbicie(G, node, wagi_kopia)

                wagi_kopia = wynik.copy()
                count += 1

                if pozytywne(wagi_kopia):
                    wyniki_dla_wszystkich_list.append((tuple(wagi_kopia), count))
                    break

                if tuple(wagi_kopia) == poczatkowy_stan:
                    wyniki_dla_wszystkich_list.append(([], count))
                    break
            else:
                continue
            break

    # Liczenie wystąpień wag (tylko tych nie-pustych)
    wystapienia_wag = Counter(waga for waga, _ in wyniki_dla_wszystkich_list if waga)

    waga_do_count = defaultdict(lambda: {'nieparzyste': 0, 'parzyste': 0})

    for waga, count in wyniki_dla_wszystkich_list:
        if waga:
            if wystapienia_wag.get(waga, 0) == 1 and count == 0:
                waga_do_count[waga]['parzyste'] = 1
                waga_do_count[waga]['nieparzyste'] = 0
            else:
                if count % 2 == 0:
                    waga_do_count[waga]['parzyste'] += 1
                else:
                    waga_do_count[waga]['nieparzyste'] += 1

    # Tworzenie końcowego wyniku
    wynik = []
    for waga, counts in waga_do_count.items():
        parz = counts['parzyste']
        nieparz = counts['nieparzyste']
        if parz != nieparz:
            suma_count = parz - nieparz
            # ustal znak: dodatni jeśli więcej parzystych, ujemny jeśli więcej nieparzystych
            znak = 1 if parz > nieparz else -1
            waga_przemnozona = tuple(int(v * znak) for v in waga)
            wynik.append({
                'waga_original': tuple(int(v) for v in waga),
                'waga_przemnozona': waga_przemnozona,
                'suma_count_parzyste': parz,
                'suma_count_nieparzyste': nieparz,
                'suma_count': suma_count,
                'znak': znak
            })

    return wynik

def positive(G, wagi_lista):
    def pozytywne(G):
        for node, data in G.nodes(data=True):
            if data['weight'] is not None and data['weight'] <= 0:
                return False
        return True

    count = 0
    nodes_z_odbiciem = []
    wagi = []
    nadawanie_wag(G, wagi_lista)
    if pozytywne(G):
        return wagi_lista, count
    max_iter = 1000000
    iter_num = 0
    while True:
        iter_num += 1
        if iter_num > max_iter:
            break
        sorted_nodes = sorted(G.nodes(data=True), key=lambda x: x[1]["weight"], reverse=True)
        nodes_ujemne = [
            node for node, dat2a in sorted_nodes
            if isinstance(dat2a.get('weight'), (int, float)) and dat2a['weight'] < 0 and dat2a['weight'] != 0]
        if not nodes_ujemne:
            break
        for node in nodes_ujemne:
            odbicie(G, node, wagi_lista)
            nodes_z_odbiciem.append(node)
            count += 1
        if pozytywne(G):
            break
    for _, w in G.nodes(data='weight'):
        wagi.append(w)
    return(wagi, count)

def pushing_down(G, wagi_lista, k, lista):
    # Jeśli wagi_lista to lista liczb (np. [1,2,3,4]), zamień na listę list
    if wagi_lista and all(isinstance(x, (int, float)) for x in wagi_lista):
        wagi_lista = [wagi_lista]
    zewn = list(symetryczna(wagi_lista, k))
    modified_zewn = []

    for waga in zewn:
        modified_zewn.append([x + y for x, y in zip(waga, lista)])

    return modified_zewn

def pushinkg_down_zewnetrzna(G, wagi_lista, k, lista):
    # Jeśli wagi_lista to lista liczb (np. [1,2,3,4]), zamień na listę list
    if wagi_lista and all(isinstance(x, (int, float)) for x in wagi_lista):
        wagi_lista = [wagi_lista]
    zewn = list(zewnetrzna(wagi_lista, k))
    modified_zewn = []

    for waga in zewn:
        modified_zewn.append([x + y for x, y in zip(waga, lista)])

    return modified_zewn


def extremal(G, wagi_lista, exception, max_level=10):
    def action(node, wagi):
        # Upewnij się, że nwagi jest listą, nie krotką
        nwagi = list(wagi)
        w = nwagi[node]
        nwagi[node] = -w
        for neighbor in G.neighbors(node):
            nwagi[neighbor] += w
        return nwagi

    def isDistinguished(exception, wagi):

        return all(w >= 0 or idx == exception for idx, w in enumerate(wagi))

    level = 0
    orbit = [wagi_lista]
    poprzedni = [wagi_lista]
    N1 = 0 
    dalej = True

    while dalej and level < max_level:
        level += 1
        aktualne = []

        for wagi in poprzedni:
            for node in G.nodes():
                nwagi = action(node, wagi)
                if nwagi not in orbit:
                    orbit.append(nwagi)
                    aktualne.append(nwagi)
                    if isDistinguished(exception, nwagi):
                        N1 += 1
                        print(f"{N1} - Level {level}: {nwagi}")

        dalej = len(aktualne) > 0
        poprzedni = aktualne

    print(f"Liczba rozróżnionych przypadków: {N1}")
    #return orbit


if __name__ == "__main__":
    grafy_cache = {}
    wagi_cache = {}
    menu(grafy_cache, wagi_cache)