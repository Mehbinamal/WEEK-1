def fibonacci_series(n):
    a, b = 0, 1 
    print(a, b, end=" ")  
    for i in range(n - 2):  
        next_term = a + b
        print(next_term, end=" ")
        a, b = b, next_term  

n = int(input("Enter the number of terms: "))
print("Fibonacci series:")
fibonacci_series(n)