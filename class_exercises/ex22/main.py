def to_upper(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result.upper()
    return wrapper

@to_upper
def numbers_in_words(writing):
    
    digits = {"0":"zero", "1":"one", "2":"two", "3":"three", 
          "4":"four", "5":"five", "6":"six","7":"seven",
          "8":"eight", "9":"nine"}

    converted_writing = ""

    for char in writing:
        if char in digits:
            converted_writing += (digits[char] + " ")
    
    return converted_writing
    
def drukuj(*args, sep=' ', end='\n'):
    
    writing = ''
    for argument in args:
        writing += str(argument) + sep
    return writing[:-len(sep)]
    
drukuj = to_upper(drukuj)
    
def main():
    print(numbers_in_words("1410"))
    print(drukuj("Ala", "ma", "kota", sep="-"))
    
if __name__ == "__main__":
    main()
