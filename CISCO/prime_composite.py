def Prime(arr):
  flag = 0
  for i in arr:
    if i<=2: print(True)
    elif i>2:
      if i%2==0 :
         flag = 1
         print(False)
      for j in range(3,int(i**0.5)+1,2):
        if(i%j==0): 
          print(False)
          flag = 1
          break
      if(flag!=1):
        print(True)
      flag = 0

Prime([1,2,3,4,5,6,7,8,9,11,13])
