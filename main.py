import json,urllib.request as u
V=0,100,320,330,500,900,0
P='KKKKLMMGLJIKKKKOLLMPMMOQUUUUKKKKGIIJIKKKIKLLJKLLKKLLILLLIKLKGIIJ'
ND=-33,-31,-18,-14,14,18,31,33
KD=-17,-15,15,17,-16,-1,1,16
OF=(ND,KD[:4],KD[4:],KD,KD)
D={7:1,0:2,119:4,112:8}
B=[0]*128
KS=[116,4]
S=[];N=[0];TT={}
AB=Exception
def E():
 s=0
 for q,p in enumerate(B):
  if q&136 or not p:continue
  t=abs(p);r=q>>4;f=min(q&7,7-(q&7))
  s+=(V[t]+(ord(P[(t>1)*32+(7-r if p>0 else r)*4+f])-75)*5)*(p//abs(p))
 return s
def AT(s,c):
 for d in(-15*c,-17*c):
  q=s+d
  if not q&136 and B[q]==c:return 1
 for d in ND:
  q=s+d
  if not q&136 and B[q]==2*c:return 1
 for d in KD:
  q=s+d
  while not q&136:
   p=B[q]
   if p:
    if p==5*c or p==(4*c if d in KD[4:]else 3*c)or(q==s+d and p==6*c):return 1
    break
   q+=d
 return 0
def G(w,cp):
 m=[]
 for s,p in enumerate(B):
  if s&136 or p*w<=0:continue
  t=abs(p)
  if t==1:
   d=16*w;pr=(s>>4)==(7+5*w)//2
   for e in(d-1,d,d+1):
    q=s+e
    if q&136:continue
    if e==d:
     if B[q]==0 and(not cp or pr):
      m.append(s*128+q|81920*pr)
      if(s>>4)==(7-5*w)//2 and B[s+2*d]==0:m.append(s*128+s+2*d)
    elif(B[q]and B[q]*w<0)or q==EP:
     m.append(s*128+q|81920*pr)
  else:
   for d in OF[t-2]:
    q=s+d
    while not q&136:
     if B[q]==0:
      if not cp:m.append(s*128+q)
     else:
      if B[q]*w<0:m.append(s*128+q)
      break
     if t in(2,6):break
     q+=d
 if not cp:
  for r,b,k in((1,4,1),(2,4,-1),(4,116,1),(8,116,-1)):
   if CR&r and not B[b+k]and not B[b+2*k]and(k>0 or not B[b-3])and all(not AT(b+j*k,-w)for j in(0,1,2)):m.append(b*128+b+2*k)
 return m
def MK(m):
 global CR,EP
 f=m>>7&127;t=m&127;pr=m>>14;pc=B[f];cp=B[t];S.append((m,cp,CR,EP));w=pc//abs(pc)
 B[t]=pr*w if pr else pc;B[f]=0
 if pc==w and t==EP and cp==0:B[t-16*w]=0
 if abs(pc)==6:
  if abs(t-f)==2:
   a=f+3 if t>f else f-4;b=f+1 if t>f else f-1;B[b]=B[a];B[a]=0
  KS[(w+1)//2]=t;CR&=~(3 if w>0 else 12)
 for q in f,t:CR&=~D.get(q,0)
 EP=f+16*w if abs(pc)==1 and abs(t-f)==32 else -1
def UM():
 global CR,EP
 m,cp,cr,ep=S.pop();f=m>>7&127;t=m&127;pr=m>>14;pc=B[t];w=pc//abs(pc)
 if abs(pc)==6:
  if abs(t-f)==2:
   a=f+3 if t>f else f-4;b=f+1 if t>f else f-1;B[a]=B[b];B[b]=0
  KS[(w+1)//2]=f
 B[f]=w if pr else pc;B[t]=cp
 if abs(pc)==1 and t==ep and cp==0:B[t-16*w]=-w
 CR=cr;EP=ep
def SC(m):
 c=B[m&127];s=0
 if c:s=10*V[abs(c)]-V[abs(B[m>>7&127])]//10
 if m>>14:s+=9000
 return s
def SR(w,d,al,be,pl):
 N[0]+=1
 if N[0]>5e4:raise AB
 k=(tuple(B),CR,EP,w)
 if d<=0:
  s=E()*w
  if s>=be:return be
  if s>al:al=s
  if d<=-6:return al
 ck=AT(KS[(w+1)//2],-w);ms=[]
 for m in G(w,0 if d>0 else not ck):
  MK(m)
  if not AT(KS[(w+1)//2],-w):ms.append(m)
  UM()
 if not ms:return -9999+pl if ck else(0 if d>0 else al)
 t=TT.get(k);ms.sort(key=lambda m:(m!=t,-SC(m)))
 bs=-1e5;bt=ms[0]
 for m in ms:
  MK(m)
  try:s=-SR(-w,d-1,-be,-al,pl+1)
  except AB:UM();raise
  UM()
  if s>bs:bs=s;bt=m
  if s>al:al=s
  if al>=be:break
 TT[k]=bt;len(TT)>2e4 and TT.pop(next(iter(TT)));return al if d<=0 else bs
def MC(x):
 f,t=[ord(x[i])-97+16*int(x[i+1])-16 for i in(0,2)];p=0
 if len(x)>4:p='nbrq'.index(x[4])+2
 return f*128+t|p<<14
def UC(m):
 f=m>>7&127;t=m&127;p=m>>14
 return f"{chr(97+f%8)}{f//16+1}{chr(97+t%8)}{t//16+1}{'nbrq'[p-2] if p else ''}"
def ST(mv):
 global CR,EP
 a=[4,2,3,5,6,3,2,4];B[:]=a+[0]*8+[1]*8+[0]*72+[-1]*8+[0]*8+[-x for x in a]+[0]*8;CR=15;EP=-1;KS[:]=[116,4]
 for x in mv:MK(MC(x))
 return 1-len(mv)%2*2
def BM(w,lg):
 ms=[MC(x) for x in lg];bm=ms[0];N[0]=0
 for d in range(2,6):
  try:
   ms.sort(key=lambda m:(m!=bm,-SC(m)));bs=-1e5;cur=bm
   for m in ms:
    MK(m)
    try:s=-SR(-w,d-1,-1e5,1e5,1)
    except AB:UM();raise
    UM()
    if s>bs:bs=s;cur=m
   bm=cur
  except AB:break
 return UC(bm)
U=__import__('os').environ['MAKEFUN_ENV_URL']
PO=lambda a,o:json.load(u.urlopen(U+a,json.dumps(o).encode()))
g=PO('/game',{})
while g['status'][0]!='d':
 if g['status'][0]=='y':
  w=ST(g['moves']);lg=g['legal_moves'];mv=BM(w,lg)
  g=PO('/move',{'game':g['game'],'move':mv})
 else:g=PO('/game',{})
