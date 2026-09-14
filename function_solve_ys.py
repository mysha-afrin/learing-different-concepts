#WAF to print the length of a list (list is the parameter)
cities = ['Dhaka', 'Chittagong', 'Khulna', 'Rajshahi', 'Barisal', 'Sylhet', 'Pabna']

def print_length(cities):
    print(len(cities))
    return len(cities)

print_length(cities)







#WAF to print the elements of a list in a single line (list is the parameter)
def print_elements(cities):
    for city in cities:
        print(city, end=' ')
    print()
print_elements(cities)



#WAF  to find the factorial of a number (number is the parameter)
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        
        fact *= i
        print(fact)
    
factorial(6)