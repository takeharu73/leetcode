text = "nlaebolko"

s = list(text)
dic = {"b":0,"a":0,"l":0,"o":0,"n":0}

for l in s:
    if l in dic:
        dic[l]+=1

# print(dic)
res = list(dic.values())
# print(res)
res[2]/=2
res[3]/=2
print(min(res))