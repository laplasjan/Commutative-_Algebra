{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0e5d0ae8-5ce5-4e01-aab4-f6d12129455a",
   "metadata": {},
   "outputs": [],
   "source": [
    "### Proszę zrunować ten notatnik a na dole jest komander, który automatycznie\n",
    "# wykona procedury"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9d8f2277-d6c7-4921-871c-91d4ca825083",
   "metadata": {},
   "outputs": [],
   "source": [
    "import networkx as nx\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bb281324-758f-4044-b975-a8a00424ab1b",
   "metadata": {
    "tags": []
   },
   "source": [
    "### T_pqr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8330a73e-cfaa-473e-a66e-24d5809956e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Tworzenie grafu pzrez funkcję\n",
    "def T_pqr(p,q,r):\n",
    "    G = nx.Graph()\n",
    "    if p> 2 and q>2 and r >2:\n",
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
   "cell_type": "markdown",
   "id": "5f22c16a-332e-4459-9fec-ce1aee5fa615",
   "metadata": {
    "tags": []
   },
   "source": [
    "### T_pqr DLA UST. p,q,r o skończonych reprezentacjach"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a370a417-6026-480b-b4e9-01e907a6d780",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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diTEgLq6Ou3ateuEs5s7duyQ2+1uOLZr166NPijUvn171twEvoFCCSCmBAIBzZo1S3/+85/16quvauzYsWZHQhzw+/3av39/o9tXVlRUNBybmZnZ6G5C3bt3V3Iyt0kg8VAoAcSMQCCgW265Rb/4xS/0/PPP65prrjE7EhJEVVVVo9tXfvnll/L7D68mkJycfNyl9KPFMy8vT+npLDuF+EShBBAz7rvvPt1zzz166qmnNG/ePLPjAJIO38/75ZdfNjq76XK5Go7t3Llzo7ObHTp04FI6YhaFEkBM+NWvfqUFCxbogQce0J133ml2HCAogUBAZWVljS7wfuDAgYZjMzIyGt1NqGfPnlxKjwI82Nc4CiWAqPfcc89p+vTpuu222/TII48wi4O44XQ6G92+cvfu3fL5fJIki8Winj17NroMUkZGhsmfJL65PF7tsLu0swlLj+VmpykvgZYeo1ACiGqvvfaaJkyYoFmzZul3v/sdZRIJw+v1Hncp/djiWV1d3XBsx44dG53d7Ny5M39umonNEYJHoQQQtdauXavRo0fryiuv1AsvvMBC1MARgUBA5eXljS7wvn///oZj09LSvlY2j/26Z8+eatWqlYmfJHqV1dTpvVK76ti+NSgUSgBR6Z133lFBQYEGDx6s119/XSkpKWZHAmJGTU1No9tX7tq1Sx6PR5KUlJSkHj16nHB2s1evXsrMzDT5k5hj+6EabTngCPt5+3XMVK+28fmkP4USQNTZsmWLBg4cqH79+mn16tXsWgKEkc/n0549exqd3XQ4/lek2rdv3+he6V26dFFSUvxdxm2pMnlUvJZKCiWAqPLFF18oPz9fp556qt56662EnSEBzBAIBFRZWdnoEkj79u1rODY1NfVra2weWzpzcnLUunXsXd4tq6nT23srW3ycS7u3i7vL3xRKAFHjyy+/VP/+/WW1WrVp0yadcsopZkcCcIza2tqvXUo/doZz586dqq+vlyQZhqFTTz210QeF2rZta/InOZ7H59faneVhuWfyZFItSSrI7RBXD+pQKAFEhbKyMg0YMEAej0fFxcXq1q2b2ZEANIHP59O+fftOeBl9x44dOnToUMOxbdu2bXSv9G7duplyKf2D/Xbtrqpt0pPcocjJaqPzO2dHaLSWR6EEYDq73a5BgwbpwIEDKikpUV5entmRAITZoUOHGl0Cae/e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JDiPx6NJkybpH//4h9asWaPzzz/f7EgAgBhDoQQSmN/v1/Tp01VUVKQ333yz4WEcAACagkIJJKhAIKD58+frpZde0ssvv6zhw4ebHQkAEKMolECCuuuuu/Sb3/xGzzzzjCZMmGB2HABADEsyOwCAyHv00Uf14IMP6uc//7lmzpxpdhwAQIxjYXMgwfzhD3/QDTfcoLvvvls//elPzY4DAIgDFEoggbz00kuaOnWqbrrpJj3xxBMyDMPsSACAOEChBBLEihUrNH78eE2dOlXPPvuskpK44wUAEB4USiABbNy4USNGjNCIESP0t7/9TcnJPI8HAAgfCiUQ5/79739ryJAhuuSSS7R8+XK1bt3a7EgAgDhDoQTi2KeffqoBAwaod+/eWrdundLT082OBACIQxRKIE7t2LFD/fv3V4cOHbRx40a1bdvW7EgAgDhFoQTi0FdffaX8/HxZLBYVFxerU6dOZkcCAMQx7swH4szBgwdVUFAgj8ejDRs2UCYBAC2OQgnEEYfDoeHDh6u8vFzFxcXq0aOH2ZEAAAmAQgnEidraWl1++eXatm2bNmzYoN69e5sdCQCQICiUQBzweDyaOHGi/vWvf2ndunU677zzzI4EAEggFEogxvl8Pk2bNk1r1qzR8uXLdemll5odCQCQYCiUQAwLBAK66aab9Morr+hvf/ubCgsLzY4EAEhAFEoghi1evFi/+93v9Oyzz+rKK680Ow4AIEElmR0AQPM8/PDDeuSRR/TLX/5S06dPNzsOACCBUSiBGPTb3/5Wixcv1k9+8hMtWLDA7DgAgATHTjlAjPnrX/+qa6+9VgsWLNDjjz8uwzDMjgQASHAUSiCGLF++XOPHj9d1112nZ555RklJXGQAAJiPQgnEiLfeeksjR47U6NGj9fLLLys5mWfqAADRgUIJxIB//vOfGjp0qPr3769ly5apdevWZkcCAKABhRKIcp988okGDBigs846S2vWrFF6errZkQAA+BoKJRDFtm/frv79+6tz587asGGDsrOzzY4EAMBxKJRAlNq3b5/69++vVq1aqbi4WB07djQ7EgAAJ8QjokAUqqioUEFBgfx+v2w2G2USABDVeEwUiDJVVVUaPny4Dh48qOLiYp166qlmRwIA4FtRKIEo4nK5NGbMGG3fvl2bNm3SGWecYXYkAABOikIJRIn6+npdddVVev/9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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "D5 = T_pqr(2,2,3)\n",
    "labels = {n: D5.nodes[n] for n in D5.nodes}\n",
    "nx.draw(D5, with_labels=True, node_size=500, node_color='lightblue', font_weight='bold')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cff09b9e-be73-42fe-a71d-921850c6d9fe",
   "metadata": {
    "tags": []
   },
   "source": [
    "### WAGI WIERZCHOŁKÓW z listy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "aba30c3d-e3b8-4a43-862a-8b76e1b6511a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def nadawanie_wag(G, wagi_lista):\n",
    "    wagi = []\n",
    "    for idx, weight in enumerate(wagi_lista):\n",
    "        G.add_node(idx, weight=weight) \n",
    "    for _, w in G.nodes(data='weight'):\n",
    "        wagi.append(w)\n",
    "    return wagi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "497294c7-8468-4648-bf24-55e5367c8275",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[-1, -2, -3, 0, None]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nadawanie_wag(D5, [-1,-2,-3,0])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "16b21acf-fd7a-4814-acb3-87970941b6bf",
   "metadata": {},
   "source": [
    "### Odbicie do listy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d712d72a-8e8c-47e4-82a8-334948fa1dcf",
   "metadata": {},
   "outputs": [],
   "source": [
    "def odbicie(G, node):\n",
    "    #jeśli chcesz sprawdzić, czy odbicie działa oraz chcesz mieć wypisane wagi, komenda poniżej to umożliwia:\n",
    "    #print(nadawanie_wag(G, wagi_lista))\n",
    "    \n",
    "    wagi = [] \n",
    "    \n",
    "    neighbors = list(G.neighbors(node))\n",
    "    \n",
    "    nowa_waga1 = - G.nodes[node]['weight']\n",
    "    G.nodes[node]['weight'] = nowa_waga1\n",
    "    \n",
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
   "execution_count": 7,
   "id": "cde593bc-3ba6-4884-98bf-e5e6be241239",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, -3, -4, -1, None]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "odbicie(D5,0)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "31fc5121-9384-4257-b6f8-c20d88a62dd2",
   "metadata": {},
   "source": [
    "### ro"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c7edae33-fbbd-480e-b161-4678c075ef7e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def ro_1(G):    \n",
    "    weights = []\n",
    "    for node in G.nodes():\n",
    "        G.nodes[node]['weight'] -= 1\n",
    "        weights.append( G.nodes[node]['weight'])\n",
    "    return weights"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "6771f2bb-4d37-494e-ba59-1ca721f62cbf",
   "metadata": {},
   "outputs": [],
   "source": [
    "def ro_2(G):    \n",
    "    weights = []\n",
    "    for node in G.nodes():\n",
    "        G.nodes[node]['weight'] += 1\n",
    "        weights.append( G.nodes[node]['weight'])\n",
    "    return weights"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9ae0a7f9-1217-4bc0-9ae4-188c48fdd02f",
   "metadata": {},
   "source": [
    "# omijania miejsc"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "62328bc9-e69b-463e-908a-961798a87614",
   "metadata": {
    "tags": []
   },
   "source": [
    "### Eliminacja minusów"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "1ce02990-871d-4299-af33-fc64b292521e",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# aby zwiększyć liczbę iteracji do k iteracji, zrób to proszę w miejscu:    \n",
    "# while count < k:\n",
    "\n",
    "#ten program odbija w wierzchołkach ujemnych po kolei bez sortu na nich\n",
    "\n",
    "def zmiana_na_dodatnie_obl(G, wagi_lista):\n",
    "    def pozytywne(G):\n",
    "        for node, data in G.nodes(data=True):\n",
    "            if data['weight'] is not None and data['weight'] < 0:\n",
    "                return False\n",
    "        return True\n",
    "    count = 0\n",
    "    nodes_z_odbiciem = []\n",
    "    wagi = []\n",
    "    \n",
    "    nadawanie_wag(G, wagi_lista)\n",
    "    while count < 10000:\n",
    "        nodes_ujemne = [node for node, data in G.nodes(data=True) if isinstance(data.get('weight'), (int, float)) and data['weight'] < 0]\n",
    "\n",
    "        for node in nodes_ujemne:\n",
    "            odbicie(G, node)\n",
    "            nodes_z_odbiciem.append(node)\n",
    "        count += 1\n",
    "\n",
    "        if pozytywne(G):\n",
    "            break\n",
    "            \n",
    "    for _, w in G.nodes(data='weight'):\n",
    "        wagi.append(w) \n",
    "    print(f\"Wierzchołki w kolejności wywoływania:  {nodes_z_odbiciem}, wagi na końcu: {wagi}, count= {count}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "dddae678-ff44-4449-b91f-641bbf0c5f88",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wierzchołki w kolejności wywoływania:  [0, 1, 2, 3, 0, 4, 1, 2, 3, 0, 4, 1, 2, 3, 0], wagi na końcu: [1, 0, 0, 0, 0], count= 7\n"
     ]
    }
   ],
   "source": [
    "wagi_lista = [-1,0,0,0,0]\n",
    "G = T_pqr(2,2,3)\n",
    "zmiana_na_dodatnie_obl(G,wagi_lista)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "f1f1ad09-6c30-48f0-92bd-6793c71b5d75",
   "metadata": {},
   "outputs": [],
   "source": [
    "# aby zwiększyć liczbę iteracji do k iteracji, zrób to proszę w miejscu:    \n",
    "# while count < k:\n",
    "\n",
    "#ten program odbija zawsze w najmniejszym wierzchołku\n",
    "\n",
    "def zmiana_na_dodatnie(G, wagi_lista):\n",
    "    def pozytywne(G):\n",
    "        for node, data in G.nodes(data=True):\n",
    "            if data['weight'] is not None and data['weight'] < 0:\n",
    "                return False\n",
    "        return True\n",
    "    count = 0\n",
    "    nodes_z_odbiciem = []\n",
    "    wagi = []\n",
    "    \n",
    "    nadawanie_wag(G, wagi_lista)\n",
    "    while count < 10000:\n",
    "        sorted_nodes = sorted(G.nodes(data=True), key=lambda x: x[1][\"weight\"], reverse=True)\n",
    "        nodes_ujemne = [node for node, data in sorted_nodes if isinstance(data['weight'], (int, float)) and data['weight'] < 0]\n",
    "\n",
    "        for node in nodes_ujemne:\n",
    "            odbicie(G, node)\n",
    "            nodes_z_odbiciem.append(node)\n",
    "        count += 1\n",
    "\n",
    "        if pozytywne(G):\n",
    "            break\n",
    "            \n",
    "    for _, w in G.nodes(data='weight'):\n",
    "        wagi.append(w) \n",
    "    print(f\"Wierzchołki w kolejności wywoływania:  {nodes_z_odbiciem}, wagi na końcu: {wagi}, count= {count}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "129ef9ea-f177-4223-b7ad-14e632082593",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wierzchołki w kolejności wywoływania:  [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 0], wagi na końcu: [1, 0, 0, 0, 0], count= 7\n"
     ]
    }
   ],
   "source": [
    "wagi_lista = [-1,0,0,0,0]\n",
    "G = T_pqr(2,2,3)\n",
    "zmiana_na_dodatnie(G,wagi_lista)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "27facdc3-da8d-4741-abdc-9a572935a1e7",
   "metadata": {
    "tags": []
   },
   "source": [
    "### Eliminacja plusów"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "eec7ab6d-f060-42b5-ad35-940496e5b1af",
   "metadata": {},
   "outputs": [],
   "source": [
    "# aby zwiększyć liczbę iteracji do k iteracji, zrób to proszę w miejscu:    \n",
    "# while count < k:\n",
    "\n",
    "#ten program odbija w wierzchołkach ujemnych po kolei bez sortu na nich\n",
    "def zmiana_na_ujemne_obl(G, wagi_lista):\n",
    "    def ujemne(G):\n",
    "        for node, w in G.nodes(data='weight'):\n",
    "            if w is not None and w > 0:\n",
    "                return False\n",
    "        return True\n",
    "    nodes_z_odbiciem = []\n",
    "    wagi = []\n",
    "    count= 0\n",
    "    \n",
    "    nadawanie_wag(G, wagi_lista)\n",
    "    \n",
    "    while count < 10000: \n",
    "        nodes_dodatnie = [node for node, data in G.nodes(data = True) if isinstance(data.get('weight'), (int, float)) and data['weight'] > 0]\n",
    "        for node in nodes_dodatnie:\n",
    "            odbicie(G, node)\n",
    "            nodes_z_odbiciem.append(node)\n",
    "        count+=1\n",
    "        \n",
    "        if ujemne(G):\n",
    "            break\n",
    "            \n",
    "    for _, w in G.nodes(data='weight'):\n",
    "        wagi.append(w) \n",
    "    print(f\"Wierzchołki w kolejności wywoływania:  {nodes_z_odbiciem}, wagi na końcu: {wagi}, count = {count}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b7308f0e-0eae-478a-bfeb-1f36814bfe50",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wierzchołki w kolejności wywoływania:  [0, 1, 2, 4, 0, 3, 0, 1, 2, 4, 0, 3, 0, 1, 2, 4, 0, 1, 2], wagi na końcu: [-1, -1, -1, 0, -1], count = 7\n"
     ]
    }
   ],
   "source": [
    "wagi_lista = [1,1,1,0,1]\n",
    "G = T_pqr(2,2,3)\n",
    "zmiana_na_ujemne_obl(G,wagi_lista)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "9e8ee09f-06d2-4825-b84e-196456818d56",
   "metadata": {},
   "outputs": [],
   "source": [
    "# aby zwiększyć liczbę iteracji do k iteracji, zrób to proszę w miejscu:    \n",
    "# while count < k:\n",
    "\n",
    "#ten program odbija zawsze w największym wierzchołku\n",
    "\n",
    "def zmiana_na_ujemne(G, wagi_lista):\n",
    "    def ujemne(G):\n",
    "        for node, w in G.nodes(data='weight'):\n",
    "            if w is not None and w > 0:\n",
    "                return False\n",
    "        return True\n",
    "    nodes_z_odbiciem = []\n",
    "    wagi = []\n",
    "    count= 0\n",
    "    \n",
    "    nadawanie_wag(G, wagi_lista)\n",
    "    \n",
    "    while count < 10000: \n",
    "        sorted_nodes = sorted(G.nodes(data=True), key=lambda x: x[1][\"weight\"], reverse=False)\n",
    "        nodes_dodatnie = [node for node, data in sorted_nodes if isinstance(data['weight'], (int, float)) and data['weight'] > 0]\n",
    "        for node in nodes_dodatnie:\n",
    "            odbicie(G, node)\n",
    "            nodes_z_odbiciem.append(node)\n",
    "        count+=1\n",
    "        \n",
    "        if ujemne(G):\n",
    "            break\n",
    "            \n",
    "    for _, w in G.nodes(data='weight'):\n",
    "        wagi.append(w) \n",
    "    print(f\"Wierzchołki w kolejności wywoływania:  {nodes_z_odbiciem}, wagi na końcu: {wagi}, count = {count}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "dc59a94c-e8be-45a7-ba27-2e71d67cf0aa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wierzchołki w kolejności wywoływania:  [0, 1, 2, 4, 3, 0, 4, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2], wagi na końcu: [-1, -1, -1, 0, -1], count = 7\n"
     ]
    }
   ],
   "source": [
    "wagi_lista = [1,1,1,0,1]\n",
    "G = T_pqr(2,2,3)\n",
    "zmiana_na_ujemne(G,wagi_lista)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "855dca71-d1a2-4cf1-bcf9-9d2aab2bacd4",
   "metadata": {
    "tags": []
   },
   "source": [
    "### Omijanie miejsc plusów"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "f45a9a8a-0105-47f0-9970-790f17a98cb5",
   "metadata": {},
   "outputs": [],
   "source": [
    "def omijanie_dodatnich(G, wagi_lista, *args, count=0):\n",
    "    nodes_z_odbiciem = []\n",
    "    wagi = []\n",
    "    Y = set(args)\n",
    "    nadawanie_wag(G, wagi_lista)\n",
    "\n",
    "    while count <= 1000:\n",
    "        sorted_nodes = sorted(G.nodes(data=True), key=lambda x: x[1].get(\"weight\", float(\"inf\")), reverse=False)\n",
    "        nodes_dodatnie = [node for node, data in sorted_nodes if data.get(\"weight\", 0) < 0 and node not in Y]\n",
    "\n",
    "        if not nodes_dodatnie:\n",
    "            break\n",
    "        for node in nodes_dodatnie:\n",
    "            odbicie(G, node)\n",
    "            nodes_z_odbiciem.append(node)\n",
    "            count += 1\n",
    "\n",
    "        if count > 1000:\n",
    "            print(\"Maximum number of iterations reached. Exiting loop.\")\n",
    "            break\n",
    "\n",
    "    for _, w in G.nodes(data='weight'):\n",
    "        wagi.append(w)\n",
    "\n",
    "    print(f\"Wierzchołki w kolejności wywoływania:  {nodes_z_odbiciem}, wagi na końcu: {wagi}, count:  {count}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "49e036c3-76ea-47cf-9a84-f79c381d5af7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wierzchołki w kolejności wywoływania:  [0, 4, 3, 0, 4], wagi na końcu: [1, -1, -2, 0, 1], count:  5\n"
     ]
    }
   ],
   "source": [
    "wagi_lista = [-1,1,0,0,-1]\n",
    "G = T_pqr(2,2,3)\n",
    "omijanie_dodatnich(G, wagi_lista,1,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "67cd46b7",
   "metadata": {},
   "outputs": [],
   "source": [
    "def omijanie_ujemnych(G, wagi_lista, *args, count=0):\n",
    "    nodes_z_odbiciem = []\n",
    "    wagi = []\n",
    "    Y = set(args)\n",
    "    nadawanie_wag(G, wagi_lista)\n",
    "\n",
    "    while count <= 1000:\n",
    "        sorted_nodes = sorted(G.nodes(data=True), key=lambda x: x[1].get(\"weight\", float(\"inf\")), reverse=False)\n",
    "        nodes_ujemne = [node for node, data in sorted_nodes if data.get(\"weight\", 0) < 0 and node not in Y]\n",
    "        \n",
    "        if not nodes_ujemne:\n",
    "            break \n",
    "        \n",
    "        for node in nodes_ujemne:\n",
    "            odbicie(G, node)\n",
    "            nodes_z_odbiciem.append(node)\n",
    "            count += 1\n",
    "\n",
    "            if count > 1000:\n",
    "                print(\"Maximum number of iterations reached. Exiting loop.\")\n",
    "                break\n",
    "    \n",
    "    for _, w in G.nodes(data='weight'):\n",
    "        wagi.append(w)\n",
    "\n",
    "    print(f\"Wierzchołki w kolejności wywoływania: {nodes_z_odbiciem}, wagi na końcu: {wagi}, count: {count}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "678e060c-7e1d-4a13-a08c-81a1d4ac368d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wierzchołki w kolejności wywoływania: [0, 4, 3, 2, 0, 4, 2, 3], wagi na końcu: [0, -2, 1, 1, 0], count: 8\n"
     ]
    }
   ],
   "source": [
    "wagi_lista = [-1,1,0,0,-1]\n",
    "G = T_pqr(2,2,3)\n",
    "omijanie_ujemnych(G, wagi_lista,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1925c0ab-03cc-45c3-b024-ad72c7b75733",
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
