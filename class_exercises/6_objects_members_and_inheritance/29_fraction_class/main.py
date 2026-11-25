class Fraction:
    __counter = 0
    
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.__counter += 1
    
    def __del__(self):
        Fraction.__counter -= 1
        
    def reduce(self):
        greatest_common_divisor = self.__greatest_common_divisor(self.numerator, self.denominator)
        self.numerator = self.numerator // greatest_common_divisor
        self.denominator = self.denominator // greatest_common_divisor
        
    @staticmethod
    def count():
        return Fraction.__counter
        
    @classmethod
    def fromdecimal(cls, decimal):
        index_from_behind = -1
        counter = 0
        string_decimal = str(decimal)
        
        while (index_from_behind >= -len(string_decimal) and string_decimal[index_from_behind] != '.'):
            counter += 1
            index_from_behind -= 1
            
        denominator = 10**counter
        numerator = round(decimal * denominator)
        
        result = cls(numerator, denominator)
        result.reduce()
        return result
        
        
    @staticmethod
    def __least_common_multiple(a, b):
        return (a * b) // Fraction.__greatest_common_divisor(a, b)
            
    @staticmethod
    def __greatest_common_divisor(a, b):
        while(b != 0):
            a, b = b, a % b
        return a
        
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
        
    def __add__(self, other):
        least_common_multiple = self.__least_common_multiple(self.denominator, other.denominator)
        result = Fraction((self.numerator * (least_common_multiple // self.denominator)) + (other.numerator * (least_common_multiple // other.denominator)), least_common_multiple)
        result.reduce()
        return result
    
    def __sub__(self, other):
        least_common_multiple = self.__least_common_multiple(self.denominator, other.denominator)
        result = Fraction((self.numerator * (least_common_multiple // self.denominator)) - (other.numerator * (least_common_multiple // other.denominator)), least_common_multiple)
        result.reduce()
        return result
    
    def __mul__(self, other):
        result = Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        result.reduce()
        return result
        
    def __truediv__(self, other):
        result = Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        result.reduce()
        return result
        
def main():
    u1 = Fraction(6,4)
    u2 = Fraction.fromdecimal(0.25)
    print(f"{u1} {u2}")
    print(u1 + u2)
    print(u1 - u2)
    print(u1 * u2)
    print(u1 / u2)
    print(u1.count())
    u1 = u2
    print(u1.count())
    
if __name__ == "__main__":
    main()
