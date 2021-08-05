import numpy as np

#大文字A～Zのみ対応

p = int(input("p="))
q = int(input("q="))
e = int(input("e="))

m = p * q
L = np.lcm(p-1,q-1)

#-----暗号化-----

plain=(input("平文をを入力してください(大文字A～Zのみ対応）\n"))


plainlst=list(plain)
word_count=len(plainlst)
count = word_count
asciilst = []
n = 26
g = 64
P = 0


for s in plain:    #文字列をn進数に変換
    word_count -= 1
    ord_num = ord(s) - g #Aを基準に
    P = P + ord_num * (n ** word_count)
        
print(P)

i = 1
C = P

while i < e:
    C = C * P % m
    i += 1


#C = P ** e % m
print("暗号文は")
print(C)
tmp = C
#-----文字に変換-----
rlist = []
q = 1
i = -1

while(q != 0):
    q = C // n
    r = C % n
    rlist.append(r)

    C = q
    i += 1

rlist.reverse()
print(rlist)
plain = []
 
for s in rlist:
    ord_num = chr(s+g)  
    plain.append(ord_num)
    
plain = ''.join(plain)
print(plain)
#-------------------



#------------復号化--------------

# 商と余りと割られる数の保存先
qlist =[]
rlist =[]
wlist =[]

s = e
t = L

r = s #とりあえず余りとしてaをおく
i = 0 #式の番号


#ユークリッドの互除法----------
while(r != 0 ):
    q = s // t
    r = s % t
    # 商と余りを式の番号ごとに保存
    qlist.append(q)
    rlist.append(r)
    wlist.append(s)

    s = t
    t = r
    i += 1
#-------------------------


#一次不定方程式------------
i = i - 2

q = qlist[i]
r = rlist[i]
bq = qlist[i-1] #前の式の商
br = rlist[i-1] #前の式の余り
w = wlist[i] #割られる数
bw = wlist[i-1] #前の式の割られる数

k = r #値の保存
v = q = -q
j = 1

while(i > 0):
    q = qlist[i]
    r = rlist[i]
    bq = qlist[i-1]
    br = rlist[i-1]
    w = wlist[i]
    bw = wlist[i-1]
    
    bq = -bq #移項
    
    h = v #値の入れ替え
    v = j + bq * v
    k = q #値の入れ替え
    j = h #値の入れ替え
    
    i = i-1
#-------------------------


print()
print("d ≡",j,"(mod",L,")" )
print()

#P = C ** int(j) % m

i = 1
P = C = tmp
while(i < j):
    P = P * C % m
    i += 1


#-----文字に変換-----
print("平文は")
print (P)


rlist = []
q = 1
i = -1

while(q != 0):
    q = P // n
    r = P % n
    rlist.append(r)

    P = q
    i += 1

rlist.reverse()
print(rlist)
plain = []
 
for s in rlist:
    ord_num = chr(s+g)  
    plain.append(ord_num)
    
plain = ''.join(plain)
print(plain)
#-------------------