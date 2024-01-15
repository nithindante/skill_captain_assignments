a = []
try:
  length = int(input("enter the length of the array:"))
  for k in range(0,length):
    element = int(input("enter the element:"))
    a.append(element)
except:
  print("enter a valid number")
else:
  for i in range(length):
    for j in range(length-i-1):
      if a[j] > a[j+1]:
        a[j], a[j+1] = a[j+1], a[j]
  print(a)     
