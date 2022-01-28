import rsa
import json
import base64

with open("public.txt",'rb') as f:
    publicKey = rsa.PublicKey.load_pkcs1(f.read())

data = json.load(open("data.json"))


try:
    verify = rsa.verify(data['msg'].encode(),base64.b64decode(data['signature'].encode()),publicKey)
    print("verified")

except Exception:
    print("something is wrong..")
    print("verification failed")

