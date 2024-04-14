# Pseudocode.
# Function euclidean_algorithm (number1, number2)
#   if number2 = 0 Then
#       return number1
#   else
#       return euclidean_algorithm (number2, number1 mod number2)


# Application.
def euclidean_algorithm(num1, num2):  # Recursive function that implements the Euclidean Algorithm to find GSD of given two positive integers.
    if num2 == 0:  # Base case. If number2 = 0, number1 is GSD.
        return num1
    else:
        return euclidean_algorithm(num2, num1 % num2)  # Recursive case. Call the function with number2 and the remainder of number1 divided by number2.


print(euclidean_algorithm(192, 270))  # Test. Expected output is 6.