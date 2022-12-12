import random
def eod_fn(n):
 '''this function will check
 whether the number is even or odd'''
 if n%2==0:
     print(n,'is an even number.')
 else:
    print(n,'is an odd number.')
def pon_fn(n):
 '''this function will check whether
 the number is positive or negative'''
 if n==0:
    print('0 is neither positive nor negative number.')
 elif n>0:
     print(n,'is a positive number.')
 else:
     print(n,'is a negative number.')
def poc_fn(n):

    if n>1:
        for i in range(2, n):
            if (n % i) == 0:
                print(n, "is a COMPOSITE number.")
                break
            else:
                print(n, "is a PRIME number.")
    else:
        print(n, "is a neither prime NOR composite number.")
x = int(input('Enter starting number range: '))
y = int(input('Enter ending number range: '))
r = random.randint(x,y)
print("Range is (%d,%d) and randomly picked number is %d"%(x,y,r))
print('Then the properties followed by this number are:')
pon_fn(r)
eod_fn(r)
poc_fn(r)