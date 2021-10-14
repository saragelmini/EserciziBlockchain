#Merkel Tree
#8 foglie

import web3
from Crypto.Hash import keccak
from ProntoFunz import Prontohash
import sys

foglie_hash = list()
for i in range (0,8):
    foglie_hash.append(Prontohash('Foglia'+str(i)))

print ('hash foglie creati')
print ('lunghezza primo vettore: ', len(foglie_hash))
#accorpo le coppie di hash -> da 8 a 4
lev1_hash = list()
for i in range (0,8,2):
    lev1_hash.append(Prontohash(foglie_hash[i]+foglie_hash[i+1]))

print ("lev 1 andato a buon fine")
print('lunghezza nuovo vettore :',len(lev1_hash))

#accorpo le coppie di hash -> da 8 a 4
lev2_hash = list()
for i in range (0,4,2):
    lev2_hash.append(Prontohash(foglie_hash[i]+foglie_hash[i+1]))

print ("lev 2 andato a buon fine")
print('lunghezza nuovo vettore :',len(lev2_hash))

#merkel root
lev3_hash = Prontohash(lev2_hash[0]+lev2_hash[1])
print ("lev 3 andato a buon fine")
print('Merkel root :',lev3_hash)