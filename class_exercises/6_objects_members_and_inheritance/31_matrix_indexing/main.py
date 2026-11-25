class Matrix:
    
    def __init__(self, array_or_tuple, value = 0):
        
        if isinstance(array_or_tuple, tuple):
            rows, cols = array_or_tuple
            self.__matrix = [[value for _ in range(cols)] for _ in range(rows)]
        
        else:
            self.__matrix = array_or_tuple
            
    def __getitem__(self, key):
        
        if isinstance(key, int):
            return self.__matrix[key]
        
        elif isinstance(key, tuple):
            row, col = key
            return self.__matrix[row][col]
    
    def __call__(self, row, col):

        return self.__matrix[row][col]
            
    def __setitem__(self, key, value):
        raise TypeError("Notation exactly as in the C language")
        
    def __str__(self):
        result = ''
        for vertical_index in range(len(self.__matrix)):
            result += '|'
            for horizontal_index in range(len(self.__matrix[0])):
                if self.__matrix[vertical_index][horizontal_index] < 0:
                    result += f"{self.__matrix[vertical_index][horizontal_index]}"
                else:
                    result += f" {self.__matrix[vertical_index][horizontal_index]}"
            result += " |\n"
            
        return result

def main():
    results = []
    results.append(Matrix([[1, 0, 2],
                           [-1, 3, 1]]))
    
    rows, cols = 2, 3
    
    results.append(Matrix((rows, cols), 1))
    results.append(Matrix((rows, cols), 0))
    
    for vertical_index in range(rows):
        for horizontal_index in range(cols):
            
            results[2][vertical_index][horizontal_index] = results[0][vertical_index, horizontal_index] + results[1](vertical_index, horizontal_index)
                 
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
