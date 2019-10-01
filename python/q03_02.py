for i in range(1,100+1):
  flag=0
  for j in range(1,100+1):
      if i%j==0:
          flag ^= 1
  if flag:
      print i
