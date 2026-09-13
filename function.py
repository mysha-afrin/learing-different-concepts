def calculate_sum (a,b):
    sum = a + b
    print( sum)
    return sum

calculate_sum(5, 10)


# def is used to define a function in Python. In this case, the function is named `calculate_sum` and it takes two parameters, `a` and `b`. Inside the function, it calculates the sum of `a` and `b`, prints the result, and then returns the sum. The function is then called with the arguments 5 and 10, which will output 15.
#line 6 is the way of calling the functition and defining the values of a and b.



#there is some build in functions in python like print(), input(), len() etc. which are used to perform specific tasks. For example, the print() function is used to display output to the console, while the input() function is used to take user input. The len() function is used to get the length of a string or list. These built-in functions are readily available in Python and can be used without any additional imports or definitions.


cities = ["Dhaka", "Chittagong", "Khulna", "Rajshahi", "Sylhet"]

def print_cities(cities):
    for city in cities:
        print(city)

print_cities(cities)
       
def print_cities_1(cities):
    for city in cities:
        print(len(city))


print_cities_1(cities)