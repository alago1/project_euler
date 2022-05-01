nums = []

with open('data') as file:
    nums = list(int(i) for i in file.read().split(","))

alph = 'abcdefghijklmnopqrstuvwxyz'
keys = set()
for i in alph:
    for j in alph:
        for k in alph:
            keys.add(f"{i}{j}{k}")

potential_keys = set()
answer = ""
for key in keys:
    out = ["" for i in range(len(nums))]

    for i in range(len(nums)):
        out[i] = chr(ord(key[i%3])^nums[i])
    
    o = "".join(out)
    if "the" in o and "and" in o:
        # print(f"{key}: {o}")
        potential_keys.add(key)

    if key == "exp":
        answer = o

print(answer)

s = 0
for i in answer:
    s += ord(i)
print(s)