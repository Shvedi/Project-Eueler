def check_if_palindrome(num):
    s = str(num)
    x=0
    while x < len(s)-1:
        if not s[x] == s[len(s)-1 - x]:
            return False
        x+=1
    return True

def find_palindrome(digits):
    highest = (10**digits)
    pal_list = [0]
    for x in range(highest):
        for y in range(highest):
            if check_if_palindrome(highest*(highest-y)):

                pal_list.append(highest*(highest-y))
                
        highest-=1
    return max(pal_list)


print(find_palindrome(3))
