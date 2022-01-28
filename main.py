from os import putenv
import rsa
# from hashlib import  sha256
import base64
import json

(pub,priv) = rsa.newkeys(512)


def generateKeys():
    with open("private.txt","wb") as f:
        f.write(priv.save_pkcs1())
    with open("public.txt","wb") as f:
        f.write(pub.save_pkcs1())
    print("private and public key saved to files")
    print("-----------")
    print("Now sign your message with private key by running 'python sign.py'")
    print("-----------")

generateKeys()


# message = "this is a test message".encode()

# hash = rsa.compute_hash(message=message,method_name="SHA-256")

# signature = rsa.sign_hash(hash_value=hash,priv_key=priv,hash_method='SHA-256')
# # signature = rsa.find_signature_hash(signature,pub)
# print(signature)