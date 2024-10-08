data = input()
tmp = data[0]
ans1 = 1
ans2 = 0
for i in data[1:]:
    if i!=tmp:
        if i ==data[0]:
            ans1+=1
        else: ans2+=1
        tmp = i

print(min(ans1,ans2))
    
