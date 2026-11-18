def separate():
    print("------------")

def fibonacci_until(how_many):
    current = 1
    next_value = 1
    counter = 1
    
    while counter <= how_many:
        yield current
        next_value, current = next_value + current, next_value
        counter += 1
        
def fibonacci_inf():
    current = 1
    next_value = 1
    
    while True:
        yield current
        next_value, current = next_value + current, next_value
        
def main():
    
    for fibo in fibonacci_until(10):
        print(fibo)
    separate()
    
    fibo_gen = fibonacci_inf()
    
    counter = 1
    for fibo in fibo_gen:
        print(fibo)
        if counter == 10:
            break
        counter += 1
    separate()
    
    for fibo in fibo_gen:
        if (fibo % 3 == 0):
            print(fibo)
        if counter == 19:
            break
        counter += 1
    separate()
    
    for fibo in fibo_gen:
        if (fibo % 5 == 0):
            print(fibo)
        if counter == 28:
            break
        counter += 1
    separate()
        
if __name__ == "__main__":
    main()
