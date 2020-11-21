import random
import sys
import time

def lxor(l1,l2):
    res = list()
    for i in range(len(l1)):
        res.append(l1[i] ^ l2[i])
    return res

#On va travailler avec des listes pour les XOR
# La clé etant genéré aleatoirement on a besoin de trouver son seed
ct = str(time.time()).encode('ASCII')
random.seed(ct)
ct = [x for x in ct]

ciphere_flag = [x for x in open("flag.enc", "rb").read()]
ciphere_flag = [x for x in ciphere_flag]

key = [random.randrange(256) for _ in ciphere_flag]
cipher_ct = ciphere_flag[56:]
plain_ct = lxor(cipher_ct, [0x99]*len(ct))

#Avec le plain_ct on peut en deduire la clé
ct = ''.join([chr(x) for x in plain_ct])
random.seed(ct)

#Avec la clé on retrieve le flag
key = [random.randrange(256) for _ in ciphere_flag]
plaintext = lxor(key, ciphere_flag)
flag = ''.join([chr(x) for x in plaintext])

print(f'cipher_ct : {cipher_ct}')
print(f'key : {key}')
print(f'flag : {flag}')
