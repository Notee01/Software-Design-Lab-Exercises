def reverseString(s):
    if len(s) == 0 or len(s) == 1:
        return s
    else:
        head = s[0]
        tail = s[1:]

        return reverseString(tail) + head
    

print()    
print(reverseString('pots&pans'))
print()
