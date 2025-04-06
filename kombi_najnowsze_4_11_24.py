{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "dd904401-2729-4f67-935b-c6f50b2d0425",
   "metadata": {},
   "outputs": [],
   "source": [
    "import itertools as it\n",
    "import numpy as np\n",
    "import networkx as nx\n",
    "import matplotlib.pyplot as plt\n",
    "import copy\n",
    "from collections import defaultdict\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "35f7c0fb",
   "metadata": {},
   "outputs": [],
   "source": [
    "def T_pqr(p,q,r):\n",
    "    G = nx.Graph()\n",
    "    if p> 1 and q>1 and r >1:\n",
    "        for i in range(p+q+r-2):\n",
    "            G.add_node(i, waga=i)\n",
    "        for i in range (0, p-1):\n",
    "            G.add_edge(i,i+1)\n",
    "        for i in range (p,p+q-2):\n",
    "            G.add_edge(i,i+1)\n",
    "            G.add_edge(0,p)\n",
    "        for i in range(p+q-1,p+q+r-3):\n",
    "            G.add_edge(i,i+1)\n",
    "            G.add_edge(0,p+q-1)\n",
    "    if p == 1 or q ==1 or r == 1:\n",
    "        for i in range(p+q+r-2):\n",
    "            G.add_node(i, waga=i)\n",
    "        for i in range (0, p+q+r-3):\n",
    "            G.add_edge(i,i+1)\n",
    "    if p == 2:\n",
    "        for i in range(0,p+q+r-2):\n",
    "            G.add_node(i, waga=i)\n",
    "        for i in range (0, 1):\n",
    "            G.add_edge(i,i+1)\n",
    "        for i in range (2,q):\n",
    "            G.add_edge(i,i+1)\n",
    "            G.add_edge(0,2)\n",
    "        for i in range(q+1,q+r-1):\n",
    "            G.add_edge(i,i+1)\n",
    "            G.add_edge(0,q+1)\n",
    "    if q ==2 :\n",
    "        for i in range(0,p+q+r-2):\n",
    "            G.add_node(i, waga=i)\n",
    "        for i in range (0, p-1):\n",
    "            G.add_edge(i,i+1)\n",
    "            G.add_edge(0,p)\n",
    "        for i in range(p+2,p+q+r-3):\n",
    "            G.add_edge(i,i+1)\n",
    "            G.add_edge(0,p+2)\n",
    "    if r == 2:\n",
    "        for i in range(0,p+q+r-2):\n",
    "            G.add_node(i, waga=i)\n",
    "        for i in range (0, p-1):\n",
    "            G.add_edge(i,i+1)\n",
    "        for i in range (p,p+q-2):\n",
    "            G.add_edge(i,i+1)\n",
    "            G.add_edge(0,p)\n",
    "        G.add_edge(0,p+q-1)\n",
    "    return G"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "3d010801-5de1-42a2-890d-b44d843f190d",
   "metadata": {},
   "outputs": [],
   "source": [
    "def symetryczna(A, k):\n",
    "    \n",
    "    max_len = max(len(sublist) for sublist in A)\n",
    "    zewn = []\n",
    "    \n",
    "    for kombinacja in it.combinations_with_replacement(range(len(A)), k):\n",
    "        summed_sublist = []\n",
    "        for j in range(max_len):\n",
    "            sublist_sum = sum(A[i][j] if j < len(A[i]) else 0 for i in kombinacja)\n",
    "            summed_sublist.append(sublist_sum)\n",
    "        zewn.append(summed_sublist)\n",
    "    return zewn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1c0fda85-fbbf-4a88-821a-d3b4b806c13f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def symetryczna(A, k):\n",
    "    \n",
    "    max_len = max(len(sublist) for sublist in A)\n",
    "    zewn = []\n",
    "    \n",
    "    for kombinacja in it.combinations_with_replacement(range(len(A)), k):\n",
    "        summed_sublist = []\n",
    "        for j in range(max_len):\n",
    "            sublist_sum = sum(A[i][j] if j < len(A[i]) else 0 for i in kombinacja)\n",
    "            summed_sublist.append(sublist_sum)\n",
    "        zewn.append(summed_sublist)\n",
    "    return zewn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "080fdd2d",
   "metadata": {},
   "outputs": [],
   "source": [
    "def zewnetrzna(A, k):\n",
    "    \n",
    "    max_len = max(len(sublist) for sublist in A)\n",
    "    zewn = []\n",
    "    \n",
    "    for kombinacja in it.combinations(range(len(A)), k):\n",
    "        summed_sublist = []\n",
    "        for j in range(max_len):\n",
    "            sublist_sum = sum(A[i][j] if j < len(A[i]) else 0 for i in kombinacja)\n",
    "            summed_sublist.append(sublist_sum)\n",
    "        zewn.append(summed_sublist)\n",
    "    return zewn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "66977750-cca3-4b45-af8b-3bc8ad8bf343",
   "metadata": {},
   "outputs": [],
   "source": [
    "#liczy zewenętrznąale numeruje poszczególne linijki outputu. Dla testów\n",
    "# czy liczy odpowiednio\n",
    "def zewnetrzna_num(A, k):\n",
    "    \n",
    "    max_len = max(len(sublist) for sublist in A)\n",
    "    zewn = []\n",
    "    \n",
    "    for kombinacja in it.combinations(range(len(A)), k):\n",
    "        summed_sublist = []\n",
    "        for j in range(max_len):\n",
    "            sublist_sum = sum(A[i][j] if j < len(A[i]) else 0 for i in kombinacja)\n",
    "            summed_sublist.append(sublist_sum)\n",
    "        zewn.append(summed_sublist)\n",
    "    for idx, wynik in enumerate(zewn, 1):\n",
    "        print(f\"{idx} : {wynik}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "62f36f6d-30d6-4b2c-b9b0-bf0b8205d586",
   "metadata": {},
   "outputs": [],
   "source": [
    "D3= T_pqr(2,2,1)\n",
    "D5= T_pqr(3,2,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "b2e30f54-deeb-4759-ac0b-a267ab833d3b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "nx.draw(D5, with_labels=True, node_size=500, node_color='lightblue', font_weight='bold')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "928692de-e60c-4e2f-bf8b-0e65f7ec169f",
   "metadata": {},
   "outputs": [],
   "source": [
    "waga = [[0,0,0,0,1],[1,0,0,0,-1],[-1,1,0,1,0],[0,1,0,-1,0],\n",
    "            [0,-1,1,1,0],[1,-1,1,-1,0],[0,0,-1,1,0],\n",
    "            [-1,0,1,0,1],[1,0,-1,-1,0],[0,0,0,-1,0],[-1,0,0,1,0],[1,-1,0,0,-1],\n",
    "           [0,-1,0,0,1],[0,1,-1,0,-1],[0,0,1,0,-1], [-1,1,-1,0,1]]\n",
    "wagas = tuple(symetryczna(waga,2))\n",
    "\n",
    "wagaaa = list(zewnetrzna(waga, 2))\n",
    "wagaz = zewnetrzna(waga,2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e2dc790d-6f6a-4fa7-a5d7-37d316539bdf",
   "metadata": {
    "tags": []
   },
   "source": [
    "# Tak było w grafach -> zastosowanie operacji ro dla pojedynczej wagi dopóki są ujemne wierzchołki"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "42ad2a7d-61e5-45b9-a12a-0176dba42ef1",
   "metadata": {},
   "outputs": [],
   "source": [
    "def nadawanie_wag(G, wagi_lista):\n",
    "    wagi = []\n",
    "    for idx, (node, weight) in enumerate(zip(G.nodes, wagi_lista)):\n",
    "        G.nodes[node]['weight'] = weight\n",
    "    for _, w in G.nodes(data='weight'):\n",
    "        wagi.append(w)\n",
    "    return wagi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "56d00082-6e4f-43db-9e9e-f4c8411c9092",
   "metadata": {},
   "outputs": [],
   "source": [
    "def odbicie(G, node, wagi):\n",
    "    #jeśli chcesz sprawdzić, czy odbicie działa oraz chcesz mieć wypisane wagi, komenda poniżej to umożliwia:\n",
    "    #print(nadawanie_wag(G, wagi_lista))\n",
    "    \n",
    "    wagi = [] \n",
    "\n",
    "    neighbors = list(G.neighbors(node))\n",
    "\n",
    "    nowa_waga1 = - G.nodes[node]['weight']\n",
    "    G.nodes[node]['weight'] = nowa_waga1\n",
    "\n",
    "    for neighbor in neighbors:\n",
    "        nowa_waga = G.nodes[neighbor]['weight'] -  G.nodes[node]['weight']\n",
    "        G.nodes[neighbor]['weight'] = nowa_waga\n",
    "    for _, w in G.nodes(data='weight'):\n",
    "        wagi.append(w)\n",
    "    return wagi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "07a01f42-87d2-4efb-8186-0808b65ce822",
   "metadata": {},
   "outputs": [],
   "source": [
    "def ro_1(G, wagi):    \n",
    "    wagi = []\n",
    "    for node in G.nodes():\n",
    "        G.nodes[node]['weight'] += 1\n",
    "        wagi.append( G.nodes[node]['weight'])\n",
    "    return wagi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "7ffeba11-5c6b-4000-97d9-bf018da14927",
   "metadata": {},
   "outputs": [],
   "source": [
    "def ro_2(G, wagi):    \n",
    "    wagi = []\n",
    "    for node in G.nodes():\n",
    "        G.nodes[node]['weight'] -= 1\n",
    "        wagi.append( G.nodes[node]['weight'])\n",
    "    return wagi"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "80d9499f-ef31-48c8-8ff1-a9879b4fd4c5",
   "metadata": {},
   "source": [
    "# operacje ro i sumy countów list modulo 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "ad55c975-7d56-45fc-abcd-8a7f12ba9c6b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def rownolegle_mod(G, lista_wag):\n",
    "    def pozytywne(wagi):\n",
    "        return all(weight >= 0 for weight in wagi)\n",
    "\n",
    "    count = 0\n",
    "    wyniki_dla_wszystkich_list = []\n",
    "\n",
    "    for wagi in lista_wag:\n",
    "        wagi_kopia = wagi.copy()\n",
    "        nadawanie_wag(G, wagi_kopia)\n",
    "        if pozytywne(wagi_kopia):\n",
    "            wyniki_dla_wszystkich_list.append((wagi_kopia, count))\n",
    "            continue\n",
    "\n",
    "        poczatkowy_stan = tuple(wagi_kopia)\n",
    "\n",
    "        while not pozytywne(wagi_kopia) and count < 10000:\n",
    "            sorted_nodes = sorted(G.nodes(data=True), key=lambda x: x[1][\"weight\"], reverse=True)\n",
    "            nodes_ujemne = [\n",
    "                node for node, data in sorted_nodes\n",
    "                if isinstance(data.get('weight'), (int, float)) and data['weight'] < 0\n",
    "            ]\n",
    "\n",
    "            for node in nodes_ujemne:\n",
    "                wynik = ro_1(G, wagi_kopia)\n",
    "                wynik2 = odbicie(G, node, wynik)\n",
    "                wynik3 = ro_2(G, wynik2)\n",
    "                \n",
    "                wagi_kopia = wynik3.copy()\n",
    "                count += 1\n",
    "\n",
    "                if pozytywne(wagi_kopia):\n",
    "                    wyniki_dla_wszystkich_list.append((wagi_kopia, count))\n",
    "                    break\n",
    "\n",
    "                if tuple(wagi_kopia) == poczatkowy_stan:\n",
    "                    wyniki_dla_wszystkich_list.append(([], count))\n",
    "                    break\n",
    "\n",
    "            else:\n",
    "                continue\n",
    "            break\n",
    "\n",
    "    waga_do_count = {}\n",
    "\n",
    "    for waga, count in wyniki_dla_wszystkich_list:\n",
    "        waga_tuple = tuple(waga)\n",
    "        if waga_tuple in waga_do_count:\n",
    "            waga_do_count[waga_tuple] += count\n",
    "        else:\n",
    "            waga_do_count[waga_tuple] = count\n",
    "\n",
    "    wynik = [(suma_count , list(waga)) for waga, suma_count in waga_do_count.items()]\n",
    "    \n",
    "    return wynik\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "33b6047f-ba2b-46d9-b29e-260bcb7d8ac1",
   "metadata": {},
   "outputs": [],
   "source": [
    "def rownolegle_mod(G, lista_wag):\n",
    "    def pozytywne(wagi):\n",
    "        return all(weight >= 0 for weight in wagi)\n",
    "\n",
    "    count = 0\n",
    "    wyniki_dla_wszystkich_list = []\n",
    "\n",
    "    for wagi in lista_wag:\n",
    "        wagi_kopia = wagi.copy()\n",
    "        nadawanie_wag(G, wagi_kopia)\n",
    "        if pozytywne(wagi_kopia):\n",
    "            wyniki_dla_wszystkich_list.append((wagi_kopia, count))\n",
    "            continue\n",
    "\n",
    "        poczatkowy_stan = tuple(wagi_kopia)\n",
    "\n",
    "        while not pozytywne(wagi_kopia) and count < 10000:\n",
    "            sorted_nodes = sorted(G.nodes(data=True), key=lambda x: x[1][\"weight\"], reverse=True)\n",
    "            nodes_ujemne = [\n",
    "                node for node, data in sorted_nodes\n",
    "                if isinstance(data.get('weight'), (int, float)) and data['weight'] < 0\n",
    "            ]\n",
    "\n",
    "            for node in nodes_ujemne:\n",
    "                wynik = ro_1(G, wagi_kopia)\n",
    "                wynik2 = odbicie(G, node, wynik)\n",
    "                wynik3 = ro_2(G, wynik2)\n",
    "                \n",
    "                wagi_kopia = wynik3.copy()\n",
    "                count += 1\n",
    "\n",
    "                if pozytywne(wagi_kopia):\n",
    "                    wyniki_dla_wszystkich_list.append((wagi_kopia, count))\n",
    "                    break\n",
    "\n",
    "                if tuple(wagi_kopia) == poczatkowy_stan:\n",
    "                    wyniki_dla_wszystkich_list.append(([], count))\n",
    "                    break\n",
    "\n",
    "            else:\n",
    "                continue\n",
    "            break\n",
    "\n",
    "\n",
    "    for waga, count in wyniki_dla_wszystkich_list:\n",
    "        waga_do_count = defaultdict(int)\n",
    "\n",
    "        for waga, count in wyniki_dla_wszystkich_list:\n",
    "            waga_tuple = tuple(waga)\n",
    "            waga_do_count[waga_tuple] += count\n",
    "\n",
    "        wynik = [(suma_count, list(waga)) for waga, suma_count in waga_do_count.items()]\n",
    "        return wynik\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "665f12dc-c880-43fa-b58e-81a190480dd0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(3, [1, 0, 0, 0, 0])]"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rownolegle_mod(D5, ([2,0,0,0,-2],[2,0,0,0,-2]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "e43fae26-205c-485d-b122-80cb631c460d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(0, [0, 0, 0, 0, 1]), (120, [])]"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rownolegle_mod(D5, waga)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "99f8f4ea-31c5-4668-b5ee-a69bc774ff5a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(0, [0, 0, 0, 0, 2]),\n",
       " (14, [1, 0, 0, 0, 0]),\n",
       " (338, []),\n",
       " (20057, [0, 0, 1, 0, 0])]"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rownolegle_mod(D5, wagas)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "e902b7bf-6824-47e3-8cd7-f4bed3ebb222",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(0, [1, 0, 0, 0, 0]), (473, []), (10113, [0, 0, 1, 0, 0])]"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rownolegle_mod(D5, wagaz)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "08c43ced-6d3a-477d-bb0a-cf2ba60d962d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
