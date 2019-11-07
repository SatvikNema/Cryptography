def mmi(a,m):
    for i in range(1,100):
        if (a*i)%m==1:
            break
    return i
m=input("Enter the plain text: ")
m=m.lower()
alpha = 9
beta = 2
key_vals=[alpha, beta]
m=list(m)
#Encryption
enc_text=[]
for i in m:
    y=(alpha*(ord(i)-97) + beta)%26
    enc_char = chr(y+97)
    enc_text.append(enc_char)
print("The encrypted text is: ",''.join(enc_text))
dec_text=[]
for i in enc_text:
    alpha_inv = mmi(alpha, 26)
    x = ((alpha_inv)*(ord(i)-97-beta))%26
    dec_char = chr(x+97)
    dec_text.append(dec_char)
print("The decrypted text is: ", ''.join(dec_text))
    
