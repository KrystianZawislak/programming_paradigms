def separate():
    print("------------")

class Fibo_Iter:
    
    def __init__(self, how_many = None, counter = 1, current = 1, next_value = 1):
        
        self.how_many = how_many
        self.current = current
        self.counter = counter
        self.next_value = next_value

        if (self.how_many == None):
            self.how_many = float("inf")
            
    def __iter__(self):
        return self
        
    def __next__(self):
        actual = self.current
        if (self.counter <= self.how_many):
            self.next_value, self.current = self.next_value + self.current, self.next_value
            self.counter += 1
            return actual
        else:
            raise StopIteration

def main():
    
    for fibo in Fibo_Iter(10):
        print(fibo)
    separate()
    
    fibo_gen = Fibo_Iter()
    
    for _ in range(10):
        print(next(fibo_gen))
    separate()

    for _ in range(10):
        fibo = next(fibo_gen)
        if fibo % 3 == 0:
            print(fibo)
    separate()

    for _ in range(10):
        fibo = next(fibo_gen)
        if fibo % 5 == 0:
            print(fibo)
    separate()
    
if __name__ == "__main__":
    main()
