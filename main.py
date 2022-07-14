import numpy as np
import matplotlib.pyplot as plt


def plik(nazwa):
    x = open(nazwa, "r")
    f = x.readlines()
    del f[0]
    k = ""
    for i in range(0, len(f)):
        k += f[i].rstrip("\n")
    return k


def macierz(s1, s2):
    k1 = plik(s1)
    k2 = plik(s2)
    x = len(k1)
    y = len(k2)
    matrix = np.zeros((x, y))
    matrix = matrix.astype(int)
    for i in range(len(k1)):
        for j in range(len(k2)):
            if k1[i] == k2[j]:
                matrix[i][j] = 1
    return matrix


def filtrowanie(s1, s2, okno, prog):
    if okno < prog:
        raise ValueError("Okno nie może być mniejsze od progu")
    k1 = plik(s1)
    k2 = plik(s2)
    x = len(k1)
    y = len(k2)
    matrix = np.zeros((x, y))
    matrix = matrix.astype(int)
    for i in range(len(k1)):
        for j in range(len(k2)):
            if k1[i] == k2[j]:
                matrix[i][j] = 1
                o3 = -len(k1)
            for g in range(len(k1 + k2) - 1):
                o3 = o3 + 1
                q = matrix.diagonal(o3)
            if o3 < 0:
                for t in range(len(q)):
                    v = q[t:t + okno]
                    if sum(v) >= prog:
                        matrix[t][t]
                    else:
                        matrix[abs(o3) + t][t] = 0
            elif o3 >= 0:
                for t in range(len(q)):
                    v = q[t:t + okno]
                    if sum(v) >= prog:
                        matrix[t][t]
                    else:
                        matrix[t][abs(o3) + t] = 0
    return matrix

def wykres(macierz, nazwa):
    plt.imshow(macierz)
    plt.title("Wykres")
    plt.xlabel("Sekwencja 1")
    plt.ylabel("Sekwencja 2")
    plt.savefig(nazwa)
    plt.show()

# Examples (Macierz_kropkowa is my file path):
# print(macierz("Macierz_kropkowa\Albu_chicken.fasta", "Macierz_kropkowa\Albu_human.fasta.txt"))
# print(filtrowanie('Macierz_kropkowa\Albu_chicken.fasta', 'Macierz_kropkowa\Albu_human.fasta.txt', 3, 3))

# print(wykres(macierz('Macierz_kropkowa\Albu_chicken.fasta', 'Macierz_kropkowa\Albu_human.fasta.txt'), 'Wykres macierzy albuminy ludzkiej i kurczaka'))
# print(wykres(filtrowanie('Macierz_kropkowa\Albu_chicken.fasta', 'Macierz_kropkowa\Albu_human.fasta.txt', 3, 2),
#         'Wykres przefiltrowanej macierzy albuminy ludzkiej i kurczaka'))


# print(wykres(macierz('Macierz_kropkowa\Q8BLY7.fasta.txt','Macierz_kropkowa\Q86YV9_hooman.fasta'), 'Wykres porównawczy powiazanej ze sobą pary sekdwencji'))
# print(wykres(filtrowanie('Macierz_kropkowa\Q8BLY7.fasta.txt','Macierz_kropkowa\Q86YV9_hooman.fasta',3,2), 'Wykres porównawczy powiazanej ze sobą pary sekdwencji'))
# print(wykres(macierz('Macierz_kropkowa\Albu_chicken.fasta','Macierz_kropkowa\Q86YV9_hooman.fasta'), 'Wykres porównawczy nie powiazanej ze sobą pary sekdwencji'))
# print(wykres(filtrowanie('Macierz_kropkowa\Albu_chicken.fasta','Macierz_kropkowa\Q86YV9_hooman.fasta',3,2), 'Wykres porównawczy nie powiazanej ze sobą pary sekdwencji'))
#
# print(wykres(macierz('Macierz_kropkowa\macierzWyjsciowa.txt','Macierz_kropkowa\macierzWyjsciowa.txt'), 'Macierz wyjściowa'))
# print(wykres(macierz('Macierz_kropkowa\macierzWyjsciowa.txt','Macierz_kropkowa\substytucja.txt'), 'Macierz po substytucji'))
# print(wykres(macierz('Macierz_kropkowa\macierzWyjsciowa.txt','Macierz_kropkowa\delecja.txt'), 'Macierz po delecji'))
# print(wykres(macierz('Macierz_kropkowa\macierzWyjsciowa.txt','Macierz_kropkowa\insercja.txt'), 'Macierz po insercji'))
# print(wykres(macierz('Macierz_kropkowa\macierzWyjsciowa.txt','Macierz_kropkowa\duplikacja.txt'), 'Macierz po duplikacji'))
# print(wykres(macierz('Macierz_kropkowa\macierzWyjsciowa.txt','Macierz_kropkowa\inwersja.txt'), 'Macierz po inwersji'))
