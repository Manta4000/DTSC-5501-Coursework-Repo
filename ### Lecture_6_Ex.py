###9.8.2026

def compare(a,b,c):
    if a+b==c:
        print("True")
        return True, a+b==c
    else:
        print("False")
        return False, a+b!=c

compare(10, 20, 30)
compare(11, 20, 30)

print(0.1+0.2) ## Spits out 0.30000000000000004, which is not equal to 0.3, so 
                ## any comparison will return False
                ##the floating points of 0.1 and 0.2 are not exact in system memory

# so if we compare 0.1+0.2 to 0.3 it should return false

compare(0.1, 0.2, 0.3)

