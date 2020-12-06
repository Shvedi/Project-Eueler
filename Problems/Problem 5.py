def divided_by_all(a,b):
    not_found = False
    counter = 19*19
    while True:
        for x in range(1,21):
            if not counter%x==0:
                break
        else:
            return counter
        counter+=1
    
print(divided_by_all(1,20))
