def decode(text:str,kod:str)->str:
    nr=''
    pos=0
    kod1=kod
    for i in range(len(text)):
        if len(text)!=len(kod1):
            kod1+=kod[pos]
            pos+=+1
            if pos ==(len(kod)-1):
                pos=0
        a=ord(text[i])
        k=ord(kod1[i])
        a=(((a-97)+k)%26)+97
        b=chr(a)
        nr+=b
    return nr
print(decode('Ahoj svet','kvet'))
