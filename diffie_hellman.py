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
p=int(input("Enter a big prime number p: "))
Zp = [i for i in range(p)]
g=generator(Zp)
print("The generator of Zp: ", g[0])
a = int(input("Alice selects a random number 'a' (a<p), where 'a' is Alice's private key: "))
x=(g[0]**a)%p
print("Alice's sends bob: ", x)
b = int(input("Bob's private key 'b': "))
y=(g[0]**b)%p
print("Bob sends Alice: ", y)
shared_key = (x**b)%p
print("After key exchange, both have the key: ", shared_key)


