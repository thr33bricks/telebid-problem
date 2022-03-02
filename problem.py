#n is goat count, k is max_travels
n,k = map(int, input().split())

#goats' weight is taken into consideration
goats = list(map(int, input().split()))
goats.sort(reverse=True)

#capacity
cap = goats[0]

while(True):
    newGoats = goats.copy()
    for i in range(k):
        currCap = cap
        for g in range(n):
            if(newGoats[g] <= currCap):
                currCap-=newGoats[g]
                newGoats[g] = 0
    if(all(p == 0 for p in newGoats)):
        break
    else:
        cap+=1

print(cap)
