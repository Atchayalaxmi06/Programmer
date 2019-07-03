sta=input()
sta=sta.split()
sr=int(sta[0])
en=int(sta[1])
for i in range(sr+1,en):
  if(i%2==0):
    print(i,end=' ')
