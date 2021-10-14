import web3
from Crypto.Hash import keccak
from ProntoFunz import Prontohash
import sys
print ("import corretto")
print ("---------------------------------------")

#test su prima stringa
stringa1 = "Hello, World!"
print(stringa1)
k1 = Prontohash(stringa1)
print ("Il suo hash è: ",k1)
print ("---------------------------------------")


#test su seconda stringa: stringa1 senza virgola 
stringa2 = "Hello World!"
print(stringa2)
k2 = Prontohash(stringa2)
print ("Il suo hash è: ",k2)
print ("---------------------------------------")


#test su terza stringa: stringa1 con due spazi

stringa3 = "Hello,  World!"
print(stringa3)
k3 = Prontohash(stringa3)
print ("Il suo hash è: ",k3)
print ("---------------------------------------")

if (k1 == k2 or k1 == k3 or k3 == k1):
    print ("Hashing failed")
else :
    print ("Hashing successful")

#ricerca del nonce ad hoc 

print ("---------------------------------------")
print ('Verifica hash che iniziano per zero')
#uno zero iniziale
i=0
while i>= 0:
    if Prontohash(stringa1+str(i))[0]== '0' and Prontohash(stringa1+str(i))[1]!= '0':
        print ("Valore nonce: ",i)
        print (Prontohash(stringa1+str(i)))
        break
    i =i+1
#due zeri iniziali
print ("---------------------------------------")
i=0
while i>= 0:
    if Prontohash(stringa1+str(i))[0]== '0' and Prontohash(stringa1+str(i))[1]== '0' and Prontohash(stringa1+str(i))[2]!= '0':
        print ("Valore nonce: ",i)
        print (Prontohash(stringa1+str(i)))
        break
    i =i+1
#tre zeri iniziali
print ("---------------------------------------")
i=0
while i>= 0:
    if Prontohash(stringa1+str(i))[0]== '0' and Prontohash(stringa1+str(i))[1]== '0' and Prontohash(stringa1+str(i))[2]=='0' and Prontohash(stringa1+str(i))[3]!= '0':
        print ("Valore nonce",i)
        print (Prontohash(stringa1+str(i)))
        break
    i =i+1

print ("---------------------------------------")


#conta di tutti i nonce per cui ho inizio con 0, 00 o 000 in intervallo i tra 0 e 3*10^7
#inizializzo il contatore per gli zeri
z1=1
z2=1
z3=1

for i in range (0,30000000):
   
    if Prontohash(stringa1+str(i))[0]== '0' and Prontohash(stringa1+str(i))[1]!= '0':
        z1 = z1 + 1
    elif Prontohash(stringa1+str(i))[0]== '0' and Prontohash(stringa1+str(i))[1] == '0' and Prontohash(stringa1+str(i))[2]!= '0':
        z2 = z2 + 1
    elif Prontohash(stringa1+str(i))[0]== '0' and Prontohash(stringa1+str(i))[1]== '0' and Prontohash(stringa1+str(i))[2]== '0' and Prontohash(stringa1+str(i))[3]!= '0':
        z3 = z3 + 1
    

print ('# di nonce per hash che inizia per 0: ',z1-1)
print ('# di nonce per hash che inizia per 00: ',z2-1)
print ('# di nonce per hash che inizia per 000: ',z3-1)

