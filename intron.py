with open("refFlat.txt", "r") as infile:
    outfile = open("intron.txt", "w")
    
    for a_line in infile:
        line = a_line.split("\t")
        exonNum = int(line[8]) - 1
        posStart, posEnd = line[9].split(","), line[10].split(",")

        for i in range(exonNum):
            intronSize = int(posStart[i+1]) - int(posEnd[i])
            outfile.write("{0}\n".format(intronSize))

    outfile.close()
    infile.close()
