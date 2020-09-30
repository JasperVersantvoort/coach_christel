
def main():
    gff = "TAIR10_GFF3_genes_kort.gff"
    data = lees_gff(gff)
    print(data[0][1])

def lees_gff(gff):
    """
    Een functie die het hele GFF3 file leest en alle
    info van de genen returnd in vorm van een lijst.
    :param gff: is TAIR10_GFF3_genes.gff
    :return: Een lijst met de data van de genen
    """
    # Afvangen fout bestand
    if gff[-3:] != "gff":
        gff = input("Bestand is geen GFF3 bestand. Geef goed bestand")
        # Roept functie opnieuw aan
        # Om opnieuw het bestand te controleren
        lees_gff(gff)
    bestand = open(gff)
    data = []
    for regel in bestand:
        regel = regel.strip()
        data.append(regel.split("\t"))

    return data

main()
