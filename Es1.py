import web3
from Crypto.Hash import keccak
from ProntoFunz import Prontohash
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
    print ("Hashing successful - all the stings are different")