a = input()
s = a.split('|')
chisla = []
for i in s:
    chisla.append(int(i))

alf = ''.join([chr(i) for i in range(ord('a'), ord('z')+1)])
ans = ''
for i in chisla:
    ans+=alf[i-1]

print(ans)