nn=input()
nn=nn.split()
st=int(nn[0])
en=int(nn[1])
for num in range(st,en+1):
  su=0
  temp=num
  while temp>0:
    di=temp%10
    su=su+di**3
    temp//=10
  if(su==num):
    print(num,end=' ')
