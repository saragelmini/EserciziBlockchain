import web3
from Crypto.Hash import keccak

def Prontohash(instring=str()):
    """
    Funzione che prende in input una stringa e restituisce il suo hash
    """
    k = keccak.new(digest_bits=256)
    k.update(instring.encode("utf8"))
    return k.hexdigest()