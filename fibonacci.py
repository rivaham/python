def fibonacci(n):
        if(n==0):
            return n
        elif(n==1):
            return n
        else:
            return (fibonacci(n-1) + fibonacci(n-2))

def printFibonacci(n):
    for i in range(n):
        if(i==0): 
            first = i
            print(i, end = " ")
        elif(i==1):
            second=i
            print(i, end = " ")
        else:
            result = first + second
            print(result, end = " ")
            first = second
            second = result
    print()

n=int(input("Enter N: "))
print(n,"th fibonnaci is", fibonacci(n-1))
printFibonacci(n)