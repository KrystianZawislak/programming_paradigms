import math

def quadratic_function(number):
    return number**2

def derivative(function, critical_point, increase=0.0001):
    approximate_derivative = (function(critical_point + increase) - function(critical_point)) / increase
    return approximate_derivative 

def main():
    sin = math.sin
    print(derivative(sin, 1))
    print(derivative(sin, 0))
    print(derivative(quadratic_function, 1, 0.00001))

if __name__ == "__main__":
    main()
