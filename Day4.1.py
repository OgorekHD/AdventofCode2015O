import hashlib
Key = input("Input Key: ")
b = 0
while True:
    P_Key = Key + str(b)
    Code = hashlib.md5(P_Key.encode())
    H_code = Code.hexdigest()
    if H_code.startswith("00000"):
        print(Key + str(b))
        break
    b += 1
    P_Key = ""
