# Pseudocode.
# Function euclidean_algorithm (number1, number2)
#   if number2 = 0 Then
#       return number1
#   else
#       return euclidean_algorithm (number2, number1 mod number2)


# Application with encapsulation.
class EuclideanAlgorithm():  # Create class.
    def euclidean_algorithm(self, num1, num2): # Recursive function as the class method.
        if num2 == 0:  # Base case. If number2 = 0, number1 is GSD.
            return num1
        else:
            return self.euclidean_algorithm(num2, num1 % num2)  # Recursive case. Call the function with number2 and the remainder of number1 divided by number2.


GSD = EuclideanAlgorithm()
print(GSD.euclidean_algorithm(192, 270))  # Test. Expected output is 6.