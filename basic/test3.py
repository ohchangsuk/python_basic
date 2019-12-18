results= list()
for a in range(3,8):
    if a == 5:
        continue
    for b in range(1,10):
       results=[a*b]
print(results, len(results))