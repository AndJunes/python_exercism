"Convert a number into its corresponding raindrop sounds."
def convert(number):
    """ divisible by 3, add "Pling", is divisible by 5, add "Plang", is divisible by 7, add "Plong" to the result. is not divisible by 3, 5, or 7, the result should be the number as a string. """
    result = ""
    if (number % 3 == 0):
        result += 'Pling'
        
    if (number % 5 == 0):
        result +='Plang'
        
    if (number % 7 == 0):
        result += 'Plong'
       
    return result or str(number)