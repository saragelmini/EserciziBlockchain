import web3
from Crypto.Hash import keccak
print ("import corretto")
print ("---------------------------------------")

#test su prima stringa
stringa1 = "Hello, World!"
print(stringa1)

k1 = keccak.new(digest_bits=256)
k1.update(stringa1.encode("utf8"))
print ("Il suo hash è: ",k1.hexdigest())
print ("---------------------------------------")


#test su seconda stringa: stringa1 senza virgola 
stringa2 = "Hello World!"
print(stringa2)

k2 = keccak.new(digest_bits=256)
k2.update(stringa2.encode("utf8"))
print ("Il suo hash è: ",k2.hexdigest())
print ("---------------------------------------")


#test su terza stringa: stringa1 con due spazi

stringa3 = "Hello,  World!"
print(stringa3)

k3 = keccak.new(digest_bits=256)
k3.update(stringa3.encode("utf8"))
print ("Il suo hash è: ",k3.hexdigest())
print ("---------------------------------------")

if (k1 == k2 or k1 == k3 or k3 == k1):
    print ("Hashing failed")
else :
    print ("Hashing successful - all the stings are different")