import numpy as np
def hill():  #Code for HILL CIPHER
    alpha="abcdefghijklmnopqrstuvwxyz"
    key="GYBNQKURP"
    key=list((ord(i)%65) for i in key)
    key=np.array(key).reshape(3,3)
    
    s=input("Enter the Plaintext: ") #ACT
    s=list((ord(i)%97) for i in s)
    s=np.array(s).reshape(3,1)
    prod=np.dot(key,s)
    prod=prod%26
    t=''
    for i in range(3):
        x=(s[i,0])
        t=t+alpha[x]
    print('PLain Text is ',t)
    
    #print(prod)
    t=''
    for i in range(3):
        x=prod[i,0]
        t=t+alpha[x]
    print('Encrypted Text :',t)
    
    det=np.linalg.det(key)
    print(det)
    
    if(det==0):
        print('Not possible to decrypt')
    elif det<0:
        det=det+25
    
    k=1
    i=1
    while(k==1):
        x=det*i
        i=i+1
        if x%26==1:
            k=0
            
    def modinv(det):
        for i in range(26):
            if (det*i)%26==1:
                return i
            
    inv=np.linalg.inv(key)
    inv=inv*det
    det=modinv(det)
    print("determinant is: ",det)
    for i in range(3):
        for j in range(3):
            inv[i,j]=inv[i,j]%26
    inv=inv*det
    
    for i in range(3):
        for j in range(3):
            inv[i,j]=inv[i,j]%26
    print("Inverse is: ",inv)
            
    #print(inv)
    decrypted=np.dot(inv,prod)
    #print(decrypted)
    for i in range(3):
        for j in range(1):
            decrypted[i,j]=round(decrypted[i,j])%26
    t=''        
    for i in range(3):
        x=int(decrypted[i,0])
        t=t+alpha[x]
    print('Decrypted text is : ',t)
hill()

