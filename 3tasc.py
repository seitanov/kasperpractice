file = input('Message: ')
with open(file, 'rb') as file:
  asd = file.read(2).decode('utf-8')
print(asd)
if asd == "MZ":
  print('executable, OS Windows' )
else:
  print('non-executable')