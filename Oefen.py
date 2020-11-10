def main():
    gff = "TAIR10_GFF3_genes_kort.gff"
    data = lees_gff(gff)
    print(data)
    exon_teller(data)
    exon_teller_2(data)

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
        # print(regel.split("\t")[0])
        # print(regel.split("\t")[2])
        data.append(regel.split("\t")[0])
        data.append(regel.split("\t")[2])


    return data

def exon_teller(data):
    chr_1 = 0
    for i in range (len(data)):
        if data[i] == "Chr1":
            # print(data[i+1])
            if data[i+1] == "exon":
                # print(data[i+1])
                chr_1 += 1
    print("Chr_1: ", chr_1)

def exon_teller_2(data):
    chr_2 = 0
    for i in range (len(data)):
        if data[i] == "Chr2" and data[i+1] == "exon":
            chr_2 += 1
    print("Chr_2: ", chr_2)


main()