def rem(l,word):
    n = []
    for item in l:
        if not (item == word):
            n.append(item)
    return n
            
l = ["harry","sayeed", "ranan", "an"]

print(rem(l,"an"))
