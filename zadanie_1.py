# ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
# przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi


def zad_1(code_1, code_2):
    c_1 = int(code_1.replace('-', ''))
    c_2 = int(code_2.replace('-', ''))
    code_list = [f"{str(i)[:2]}-{str(i)[2:]}" for i in range(c_1+1, c_2)]
    return code_list


print(zad_1('79-900', '80-155'))
