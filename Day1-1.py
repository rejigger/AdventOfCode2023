file1 = open('Day1input.txt', 'r')
Lines = file1.readlines()
total = []


for i in range(len(Lines)):
    lineScan = []
    for character in Lines[i]:
        if character.isnumeric():
            lineScan.append(character)
            
    lineTotal = lineScan[0] + lineScan[len(lineScan)-1]
    total.append(int(lineTotal))
    print(lineTotal)
answer=sum(total)
print(answer)
