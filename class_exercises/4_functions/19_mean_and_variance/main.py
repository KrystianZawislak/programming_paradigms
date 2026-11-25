def mean_and_variance(numbers):
    
    numerical_coefficient_of_mean = 1/len(numbers)
    mean = 0
    for number in numbers:
        mean += number
    mean *= numerical_coefficient_of_mean
    
    numerical_coefficient_of_variance = 1/(len(numbers)-1)
    variance = 0
    for number in numbers:
        variance += (number - mean)**2
    variance *= numerical_coefficient_of_variance
    
    return mean, variance
    
def main():
    
    mean, variance = mean_and_variance([3,3,3,3])
    print(f"The mean is: {mean}")
    print(f"The variance is: {variance}")
    
    mean, variance = mean_and_variance([5,6,7,8,9])
    print(f"The mean is: {mean}")
    print(f"The variance is: {variance}")

if __name__ == "__main__":
    main()
