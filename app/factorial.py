def factorial(n):   
    count = n
    if n == 0:
        return n
    else:
        for i in range(1,count+1):
            print("i is ",i)
            print(n)
        return n

def reverse_factorial(n):
    count = n
    if n ==0:
       return n
    else:
        while n > 1:
            for i in range(i,(count+1)):
                print("i is ",i)
                n /= i
                if n ==1:
                    return i 
    return none

