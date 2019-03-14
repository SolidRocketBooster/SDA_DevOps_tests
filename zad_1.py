#Napisz funkcje ktora z podanej listy poda najnizszy element


def minimum(int_liste):
    min = int_liste[1]
    for num in int_liste:
        try:
            if num < min:
                min = num
        except Exception as exp:
            min = str(exp)
    return min

