#WAF  to find the factorial of a number (number is the parameter)
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        
        fact *= i
        print(fact)
    
factorial(6)



def calculating_currency(amount, rate):
    converted_amount = amount * rate
    print(converted_amount)
    return converted_amount
calculating_currency(100, 0.85)  # Example: Convert 100 units of currency at a rate of 0.85


def number(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
    return
number(5)
number(10)
