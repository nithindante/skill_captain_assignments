arr = [3,7,1,55,12]
length = len(arr)
x,y,key = 0,0,0
for x in range(length):
    y = x
    while(y>0 and arr[y]<arr[y-1]):       
          key = arr[y-1]
          arr[y-1] =arr[y]
          arr[y] = key
          y =y-1
print(arr)