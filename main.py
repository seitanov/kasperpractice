Alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alf = 'abcdefghijklmnopqrstuvwxyz'
with open ('text.txt') as file:
    text = file.read()
ans = ''
lstpos = 0
print(type(text))
#def rasb(text):

start = text
text = text.split("?")
cord = []


cord.append(lstpos)
lent = 0
for i, jai in enumerate(text):
    if jai.rfind("!") >= 0 or jai.rfind(".") >= 0:

        if i == 0:
            lstpos = jai.rfind(".") + jai.rfind("!") + 3
            cord.append(lstpos)

        else:
            lstpos = lent + jai.rfind(".") + jai.rfind("!") + 3
            cord.append(lstpos)
    lent += len(jai)+1

a = []
print(len(cord))
for i in range(1, len(cord)):
    a.append(start[cord[i-1]:cord[i]])

for txt in a:

    for i in range(27):
        ans = ''
        for g in txt:
            if g in Alf:
                ans+=Alf[(Alf.find(g)+i)%26]
            if g in alf :
                ans+=alf[(alf.find(g)+i)%26]
            if g not in alf and g not in Alf:
                ans += g

        print(ans)
        print(i)

    print('--------------------NEXT KEY-----------------------')
