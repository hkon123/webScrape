from lxml import html
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')



schools = []
for i in range(27):
    page = requests.get('http://www.modules.napier.ac.uk/Home.aspx?ID=1&Letter='+chr(65+i))
    tree = html.fromstring(page.content)

    schools.append(tree.xpath('//a[@title]/text()'))

schools1 = schools

print(len(schools1))
file = open("test.txt", 'w')
for j in range(len(schools1)):
    for i in schools1[j]:
        file.write(i + '\n')
file.close()

f = open('test.txt', 'r')
fixedSchools = []
for i in f:
    if len(i)>4:
        if i[0]!=' ':
            b = i
            b = b[:-1]
            fixedSchools.append(b)
f.close()

file = open("test.txt", 'w')

for i in fixedSchools:
    file.write(i + '\n')
file.close()


#print 'Schools ', schools1
#print(fixedSchools)
