def reverse(s): 
    res=''
    for i in range(len(s)-1,-1,-1):
        res += s[i]
    return res

def reverse2(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0] 

        