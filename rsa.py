def mmi(a,m):
    for i in range(100):
        if(((a*i)%m)==1):
            break
    return i
def gcd(m,n):
    ans = []
    for i in range(1,m):
        if (m%i==0) and (n%i==0):
            ans.append(i)
    return ans[len(ans)-1]
print("Enter 2 big prime numbers: ")
p=int(input())
q=int(input())
n=p*q
phi_n = (p-1)*(q-1)
es=[]
for i in range(2,phi_n):
    if(gcd(phi_n, i)==1):
        es.append(i)
e1 = es[0]
d = mmi(e1,phi_n)
public_key = [e1, n]
private_key = [d, n]
plain_text = int(input("Enter the plain text:"))
cipher_text = (plain_text**e1)%n
print("Public key: ", public_key)
print("Private key: ", private_key)
print("Cipher text: ", cipher_text)
encrypted_text = ((cipher_text)**d)%n
print("Decrypted text: ", encrypted_text)
