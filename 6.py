yl=input()
if((yl%400==0) or ((yl%4=0) and (yl%100!=0))):
  print("yes")
else:
  print("no")
