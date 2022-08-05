def isPrime(num):
    p=True

    for i in range(2,num):
        if num%i==0:
            p=False
            break
    return p

num=int(input("Enter a number: "))
print("primes upto ",num,": ")
for i in range(2,num+1):
    if isPrime(i):
        print(i)