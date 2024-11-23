#Please note that this is an advanced version of the code.

n=int(input("Enter number of rows:"))
for i in range(1, n+1):
    print("#"*(n-i+1), end="")
    print("*"*(2*(i)), end="")
    print("#"*(n-i+1))
for i in range(n-1, 0, -1):
    print("#"*(n-i+1), end="")
    print("*"*(2*(i)), end="")
    print("#"*(n-i+1))    
