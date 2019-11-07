import numpy as np
key="GYBNQKURP"
alpha="abcdefghijklmnopqrstuvwxyz"
key = [ord(i)-65 for i in key]
key = np.array(key).reshape(3,3)
p="act"
p=list(p)
p = [ord(i)-97 for i in p]
pm = np.array(p).reshape(3,1)
enc_prod = np.dot(key, pm)
enc_prod%=26
entext = []
for i in range(3):
    entext.append(chr(enc_prod[i,0]+97))
print("Encrypted text is: ", "".join(entext))
det = np.linalg.det(key)
inv = np.linalg.inv(key)
inv*=det
inv*=25
inv%=26
dec_prod = np.dot(inv, enc_prod)
dec_prod%=26
dec=[]
for i in range(3):
    dec.append(int(round(dec_prod[i,0])%26))
dtext=[]
for i in dec:
    dtext.append(chr(i+97))
print("Decrypted test: ","".join(dtext))