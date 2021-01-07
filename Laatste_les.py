
dlijst = [["hoi", "hallo", "HAllo"],[3, 5, 5], ["hoe is het",
                                                    "hoe gaat het",
                                                    "Enne"]]
print(dlijst[1])
print(int(dlijst[1][0]) + int(dlijst[1][1]) + dlijst[1][2])


# totaal = 0
# for cijfer in dlijst[1]:
#     totaal += cijfer
# print(totaal)

totale_letters = 0
for letter in dlijst:
    # print(letter)
    for i in letter:
        try:
            # print(len(i))
            totale_letters += (len(i))
        except TypeError:
            pass
print(totale_letters)


def lees_gff():
    gff = "TAIR10_GFF3_genes_kort.gff"
    """
    Een functie die het hele GFF3 file leest en alle
    info van de genen returnd in vorm van een lijst.
    :param gff: is TAIR10_GFF3_genes.gff
    :return: Een lijst met de data van de genen
    """
    bestand = open(gff)
    data = []
    for regel in bestand:
        regel = regel.strip()
        data.append(regel.split("\t"))
    # print(data)
    return data

def tellen(data):
    plus_tellen = 0
    for plus in data:
        # print(plus)
        for i in plus:
            # print(i)
            if i == "+": # als die door gaat altijd string met +
                plus_tellen += 1 # kan je niet optellen want is een
                # string is dat nodig? of wat wil je weten
    print(plus_tellen)

def main():
    data = lees_gff()
    tellen(data)

main()