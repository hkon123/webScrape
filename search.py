

q = str(raw_input("What do you want to search for?(capitalize first letter) "))



f = open('test.txt', 'r')
entries = []
for i in f:
    if len(i)>4:
        if i[0]!=' ':
            b = i
            b = b[:-1]
            entries.append(b)
f.close()

containes = []

for i in entries:
    if (q in i) == True:
        containes.append(i)


print(containes)
#print(entries)
