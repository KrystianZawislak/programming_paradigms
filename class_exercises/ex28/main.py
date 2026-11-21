def my_range(*args):
    if len(args) == 3:
        start = args[0]
        end = args[1]
        jump = args[2]
    
    if len(args) == 2:
        start = args[0]
        end = args[1]
        jump = 1.0
    
    if len(args) == 1:
        start = 0.0
        end = args[0]
        jump = 1.0
    
    if len(args) > 3 or len(args) < 1 or jump == 0.0:
        return
        
    if jump < 0:
        while (start > end):
            yield start
            start += jump
    
    if jump > 0:
        while (start < end):
            yield start
            start += jump

def main():
    for range_element in my_range(1.1, 2.2, 0.5):
        print(range_element)
    print("--------------------")
    
    for range_element in my_range(1.1, 2.1, 0.5):
        print(range_element)
    print("--------------------")
    
    for range_element in my_range(1.1, 2.2):
        print(range_element)
    print("--------------------")
    
    for range_element in my_range(2.2):
        print(range_element)
    print("--------------------")
    
    for range_element in my_range(2.2, 0.1, -0.5):
        print(range_element)
    print("--------------------")
    
if __name__ == "__main__":
    main()
