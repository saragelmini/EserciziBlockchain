import web3
from Crypto.Hash import keccak

def Prontohash(str:instring):
    k = keccak.new(digest_bits=256)
    k.update(stringa1.encode("utf8"))
return k.hexdigest()