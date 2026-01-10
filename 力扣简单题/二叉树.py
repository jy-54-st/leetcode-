def dfs(n,m,u):
  ans=1
  if (u-1)*m+2>n:
    return ans
  elif u*m+1<=n:
    for c in range((u-1)*m+2,u*m+2):
      ans +=dfs(n,m,c)
    return ans
  else:
    return n-u*m+m
t=int(input())
for _ in range(t):
  n,m,k=map(int,input().split( ))
  print(dfs(n,m,k))
