def left_shift(s):
    s=list(s)
    temp=[]
    for i in range(len(s)-1):
        temp.append(s[i+1])
    temp.append(s[0])
    s=temp
    return s

def xor(a,b):
    a=list(a)
    b=list(b)
    res_xor=[]
    for i in range(len(a)):
        if(a[i]==b[i]):
            res_xor.append(0)
        else:
            res_xor.append(1)
    return res_xor

def keys_gen(inkey):
    inkey=list(inkey)
    permute10_num = [2,4,1,6,3,9,0,8,7,5]
    p10=[]
    for i in range(10):
        p10.append(inkey[permute10_num[i]])
    p10_f5 = p10[:5]
    p10_l5 = p10[5:10]
    p10_f5 = left_shift(p10_f5)
    p10_l5 = left_shift(p10_l5)
    p10 = p10_f5+p10_l5
    permute8_num = [5,2,6,3,7,4,9,8]
    p8_key1=[]
    for i in range(8):
        p8_key1.append(p10[permute8_num[i]])
    key1 = p8_key1
    for i in range(2):
        p10_f5 = left_shift(p10_f5)
        p10_l5 = left_shift(p10_l5)
    p10 = p10_f5+p10_l5
    p8_key2=[]
    for i in range(8):
        p8_key2.append(p10[permute8_num[i]])
    key2 = p8_key2
    print("The keys generated are: ", )
    return(key1, key2)

def encryption(plain_text, inkey):
    plain_text = list(plain_text) 
    ip1=[]
    t=0
    ip1_num = [1,5,2,0,3,7,4,6]
    ipinv_num = [3,0,2,4,6,1,7,5]
    s0 = [[1,0,3,2], [3,2,1,0], [0,2,1,3], [3,1,3,2]]
    s1 = [[0,1,2,3], [2,0,1,3], [3,0,1,0], [2,1,0,3]]                   
    for i in range(8):
        ip1.append(plain_text[ip1_num[i]])
    while t<2:
        ip1_f4 = ip1[:4]
        ip1_l4 = ip1[4:8]
        ip1_l4 = [str(i) for i in ip1_l4]
        #ip1 = ip1_f4+ip1_l4
        exp_permute_num = [3,0,1,2,1,2,3,0]
        exp=[]
        for i in range(8):
            exp.append(ip1_l4[exp_permute_num[i]])
        #print(exp)
        exp = [str(i) for i in exp]
        exp = list(exp)
        key = keys_gen(inkey)[t]
        #print(key)
        #print(exp)
        res_xor1 = xor(exp, key)
        #print(res_xor1)
        res_xor1_f4 = res_xor1[:4]
        res_xor1_l4 = res_xor1[4:9]
        row1 = int((str(res_xor1_f4[0])+str(res_xor1_f4[3])),2)
        col1 = int((str(res_xor1_f4[1])+str(res_xor1_f4[2])),2)
        op1 = '{0:b}'.format(s0[row1][col1])
        row1 = int((str(res_xor1_l4[0])+str(res_xor1_l4[3])),2)
        col1 = int((str(res_xor1_l4[1])+str(res_xor1_l4[2])),2)
        op2 = '{0:b}'.format(s1[row1][col1])
        if op1=='0' or op1=='1':
            op1 = '0'+op1
        if op2=='0' or op2=='1':
            op2 = '0'+op2
        op_total = op1+op2
        #print(op_total)
        op_total = list(op_total)
        p4_num = [1,3,2,0]
        p4=[]
        for i in range(4):
            p4.append(op_total[p4_num[i]])
        right_side = xor(p4, ip1_f4)
        #print(right_side)
        sw = ip1_l4+right_side
        if t==1:
            sw = right_side+ip1_l4
        #print(sw)
        ip1 = sw
        t+=1
    #print(ip1)
    ipinv = []
    for i in range(8):
        ipinv.append(ip1[ipinv_num[i]])
    #print(ipinv)
    return ipinv

key_input = '1011001100'
plain_text = '10110100'
print("The key value given(10 bit) is: ", key_input)
print("The plain text to be encrypted is: ", plain_text)
enc = encryption(plain_text, key_input)
enc = [str(i) for i in enc]
enc = ''.join(enc)
print("The encrypted text is: ", enc)
