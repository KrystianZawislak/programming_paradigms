import math

def polynomial(x):
    return x**3-(2*(x**2))+4*x-1

def finding_zeros_using_the_bisection_method(function, x1, x2, eps):
    while x2 - x1 > eps:
        midpoint = (x1 + x2) / 2
        if function(midpoint) == 0:
            return midpoint
        elif function(x1) * function (midpoint) < 0:
            x2 = midpoint
        elif function(midpoint) * function(x2) < 0:
            x1 = midpoint
        
    return midpoint
    
def main():
    
    sin = math.sin
    print(finding_zeros_using_the_bisection_method(sin, -1.5, 1, 0.001))
    print(finding_zeros_using_the_bisection_method(polynomial, -10, 10, 0.001))

if __name__ == "__main__":
    main()
