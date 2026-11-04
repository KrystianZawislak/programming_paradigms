import sys

def drukuj(*args, sep=' ', end='\n'):
    
    writing = ''
    for argument in args:
        writing += str(argument) + sep
    sys.stdout.write(writing[:-len(sep)] + end)
    

def main():
    
    drukuj(192,168,0,1, sep=":")
    temperature = 36.6
    drukuj( "The temperature is", temperature , "degrees" )

    for _ in range(10):
        drukuj( "*", end="" )


if __name__ == "__main__":
    main()
