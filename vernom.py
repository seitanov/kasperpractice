gamma = input()
alf = "qwertyuiopasdfghjklzxcvbnm_{}1234567890"
txt = input()

keys = len(txt)//len(gamma)
if len(txt)%len(gamma) != 0:
    keys += 1

gammaAll = gamma * keys

ans = ''

for i in range(len(txt)):
    ans += alf[(alf.find(gammaAll[i])+alf.find(txt[i])+2)%len(alf)]

print(ans)
