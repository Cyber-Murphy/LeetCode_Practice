
def max_shoe(n,shoes):
    hashmap={}
    for size,side in shoes:
        if size not in hashmap:
            hashmap[size]={'L':0,'R':0}
        hashmap[size][side]+=1
    
    pairs=0
    for count in hashmap.values():
        pairs+=min(count['L'],count['R'])
    
    return pairs









shoes=[]
n=int(input())
for i in range(n):
    line=input().split()
    size=int(line[0])
    side=line[1]
    shoes.append((size,side))
    
print(max_shoe(n,shoes))
    