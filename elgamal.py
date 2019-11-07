def generator(zp):
    x=0
    gens = []
    zp = list(zp)
    for i in range(2,len(zp)):
        res=[]
        for j in range(100):
            x=(i**j)%(len(zp))
            if x not in res:
                res.append(x)
        if len(res)==(len(zp)-1):
           final = res
           gens.append(i)
    return gens
p = 17
zp = [i for i in range(p)]
a = int(input("A's private key: "))
g=generator(zp)[2]
g=6
x = (g**a)%p
public_key = [p,g,x]
print("Public key: ",public_key)
k=10
gamma = (g**k)%p
m = int(input("The message which B wants to send to A: "))
delta = (m*(x**k))%p
cipher_text = [gamma, delta]
print("Cipher text: ",cipher_text)
decr_text = ((gamma**(p-1-a))*delta)%p
print("A decrypts the text and got: ", decr_text)


                
