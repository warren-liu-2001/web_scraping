def find_first_alnum(string):
    i = 0
    while i < len(string):
        if string[i].isnumeric():
            return i
        i += 1
    return -1

def find_data_end(string):
    alnum = find_first_alnum(string)
    j = alnum
    while j < len(string):
        if string[j] == ' ':
            return j
        j += 1
    return -1


def clean_data_array(liste):
    nu_liste = []
    for i in range(len(liste)):
        datum = liste[i]
        datum_start = find_first_alnum(datum)
        datum_end = find_data_end(datum)
        filtered_data = datum[datum_start:datum_end]
        nu_liste.append(filtered_data)

    return nu_liste
