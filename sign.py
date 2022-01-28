import rsa
import json
import base64

with open("private.txt",'rb') as f:
    privateKey = rsa.PrivateKey.load_pkcs1(f.read())



string = input("Type a message: ").encode()

hash = rsa.compute_hash(string,"SHA-256")

signature = rsa.sign_hash(hash,privateKey,'SHA-256')
signature_encoded = base64.b64encode(signature)

data = {
    "msg":string.decode(),
    "signature":signature_encoded.decode()
}

json.dump(data,open("data.json","w"),indent=4)
print("message:",string.decode())
print("Digital Signature:",signature_encoded.decode())
print("To verify message run 'python verify.py'")