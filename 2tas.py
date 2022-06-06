with open('func.txt') as file:
    start = file.read()
funk = start
funk = funk.replace(' ', '')
list = funk.split('\n')

c = 0

spisok = []
perem = []
per = ''
skob = list[0].find('(')  # аргументы которые передаются в функцию смотрим здесь
skob2 = list[0].find(')')
for i in list[0][skob + 1:skob2]:
    per += i

perem = per.split(',')

for i in list:
    if '+' not in i and '-' not in i and '/' not in i and '*' not in i and '%' not in i and '.' not in i:
        if '=' in i:
            a = i.find('=')
            if '[' in i:
                spisok.append(i[0:a])

            else:
                perem.append(i[0:a])

s = 1
p = 1

for i in spisok:
    start = start.replace(i, 'R' + str(s))
    s += 1

for i in perem:
    start = start.replace(i, 'a' + str(p))
    p += 1

with open('answer.txt', 'w') as file:
    file.write(start)