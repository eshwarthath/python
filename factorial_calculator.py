def factorial(n):
    if n < 0:
        return "Error"
    
    if n == 0:
        return 1
    
    final_answer = 1
    for i in range(1, n + 1):
        final_answer *= i   
    return final_answer


n = int(input())

print(factorial(n))


























