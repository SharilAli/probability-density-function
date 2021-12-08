import math

def get_mean():
    '''Request and validate for Mean value input'''
    print("Mean value can be any value between minus infinity and plus infinity")
    print("Press ENTER key for a Mean default value of 0")
    
    while True:
        mean = input("Enter a Mean value: ")
        if mean == "":
            # Default input of Mean if user press ENTER without providing any value
            mean = 0
            print(f"You have entered a default Mean value: {mean}")
            return mean
        
        else:
            try:
                # Validate if input is numeric
                mean = float(mean)
                print(f"You have entered a Mean value: {mean}")
                return mean
            
            except ValueError: print("Invalid input. Enter a numeric Mean value")

                
def get_variance():
    '''Request and validate for Variance value input'''
    print("Variance value can be any value between more than zero and infinity")
    print("Press ENTER key for a Mean default value of 1")
    
    while True:
        variance = input("Enter a Variance value: ")
        # Default input of Variance if user press Enter without providing any value
        if variance == "":
            variance = 1
            print(f"You have entered a default Variance value: {variance}")
            return variance
        
        else:
            try: 
                # Validate if input is numeric
                variance = float(variance)
                if variance > 0:
                    print(f"You have entered a Variance value: {variance}")
                    return variance
                else: print(f"Variance value must be more than 0, try again")
            
            except ValueError: print("Invalid input. Enter a numeric Variance value")

def get_x():
    '''Request and validate for X value input'''
    print("Value of X can be any value between minus infinity and plus infinity")
    while True:
        x = input("Enter a X value: ")
        try:
            x = float(x)
            print(f"You have entered a X value: {x}")
            return x
        except ValueError: print("Invalid input. Enter a numeric X value")

def probability_density(mean, variance, x):
    '''Return the probability density function value of a normal distribution \n
    Where Mean can be any value between minus infinity and plus infinity, \n
    Variance value can be any value between more than zero and infinity, \n
    and Value of X can be any value between minus infinity and plus infinity
    '''
    # Based on formula 
    pd = (1 / math.sqrt(2 * math.pi * variance)) * math.exp(- (x - mean ) ** 2 / (2 * variance))
    return pd

def cumulative_distribution(mean, variance, x):
    '''Return the cumulative distrbution value of a normal distribution'''
    k = x
    mean = mean
    variance = variance
    
    range_increment = 0.00001
    starting_value = -100 - range_increment
    
    # Calculate number of iteration and make it into a range
    starting_range  = round(starting_value / range_increment) 
    ending_range = round(k / range_increment) 
    
    cumulative_value = 0.0
    
    for _ in range(starting_range, ending_range):
        starting_value += range_increment
        x = starting_value
        cumulative_value += probability_density(mean, variance, x)
    
    return cumulative_value*range_increment
    
def main():
    mean = get_mean()
    variance = get_variance()
    x = get_x()
    
    pd = round(probability_density(mean, variance, x), 4)
    cd = round(cumulative_distribution(mean, variance, x), 4)
    print(f"With the mean of {mean}, variance of {variance} and x value of {x}")
    print(f"The calculated probability density is: {pd} (rounded up to 4 significant figure)")
    print(f"The calculated cumulative distribution is: {cd} (rounded up to 4 significant figure)")
    return pd,cd
    

if __name__ == '__main__':
    main()
    
