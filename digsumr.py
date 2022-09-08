l = []

def sum_dig(b):
    if(b==0):
        return l
    dig = b%10
    l.append(dig)
    sum_dig(b//10)

n = int(input("Enter a number: "))
sum_dig(n)
print(sum(l))