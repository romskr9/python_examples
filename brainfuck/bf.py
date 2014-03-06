from sys import*;a=b=0;d=[];e=list(file(argv[1]).read())
def m(f,g,h,i=0):
 global b
 while e[b]!=g or i>1:
  if e[b]==g:i-=1
  if e[b]==h:i+=1
  b+=f
while b<len(e):
 c=e[b];b+=1
 if a>=len(d):d.append(0)  
 if c=='.':stdout.write(chr(d[a]))
 elif c==',':d[a]=ord(stdin.read(1))
 elif c=='>':a+=1
 elif c=='<':a-=1
 elif c=='+':d[a]+=1
 elif c=='-':d[a]-=1
 elif c=='['and d[a]==0:m(1,']','[')
 elif c==']'and d[a]!=0:m(-1,'[',']')