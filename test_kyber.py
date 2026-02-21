import os
import time
import random

class KyberSimulator:
    PK_SIZE = 800
    SK_SIZE = 1632
    CT_SIZE = 768

    def generate_keypair(self):
        pk = os.urandom(self.PK_SIZE)
        sk = os.urandom(self.SK_SIZE)
        return pk, sk

    def encrypt(self, pk):
        time.sleep(random.uniform(0.005, 0.015))  # simulate crypto delay
        ct = os.urandom(self.CT_SIZE)
        ss = os.urandom(32)
        return ct, ss

    def decrypt(self, ct, sk):
        return os.urandom(32)


# Test
kyber = KyberSimulator()

pk, sk = kyber.generate_keypair()
ct, ss1 = kyber.encrypt(pk)
ss2 = kyber.decrypt(ct, sk)

print("PK:", len(pk))
print("SK:", len(sk))
print("CT:", len(ct))
print("Simulation OK")