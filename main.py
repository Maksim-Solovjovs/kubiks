a = int (input("Ievadi pirma kuba šķautnes izmers:  "))
b = int (input("Ievadi otra kuba šķautnes izmers:  "))
a = a**3
b = b**3
if a >b:
  print ("lielakais kuba tilpums ir "+str(a))
elif b > a:
  print ("lielakais kuba tilpums ir "+str(b))
else:
  print ("lielakais kuba tilpums ir "+str(b))