# Pseudocode.
# Function euclidean_algorithm (number1, number2)
#   if number2 = 0 Then
#       return number1
#   else
#       return euclidean_algorithm (number2, number1 mod number2)


# Application with encapsulation.
class EuclideanAlgorithm:  # Create class.
    def gcd_keyboard_input(self):  # The method of the class which takes input via keyboard input.
        try:
            number1 = int(input("Enter the 1st positive integer:"))
            number2 = int(input("Enter the 2nd positive integer:"))
            if number1 < 0 or number2 < 0:  # Check for valid input (both numbers should be non-negative).
                raise ValueError("Both numbers should be non-negative integers.")
            if number1 == 0 and number2 == 0: # Check for valid input (if both numbers are zero, GCD is undefinable.)
                raise ValueError("Both numbers are 0. GCD undefinable.")
            return f"Greatest common divisor of given two non-negative integers is {self.gcd(number1, number2)}"
        except ValueError as error:  # Print error message when invalid input given.
            print("Invalid input:", error)

    def gcd(self, num1, num2):  # Recursive function as the class method.
        if num2 == 0:  # Base case. If number2 = 0, number1 is GCD.
            return num1
        else:
            return self.gcd(num2, num1 % num2)  # Recursive case. Call the function with number2 and the remainder of number1 divided by number2.


test = EuclideanAlgorithm()
print(test.gcd_keyboard_input())

# Q6. Extended pseudocode
# ax+by=GCD(a,b)
# This pseudocode extends the Euclidean Algorithm by returning not only the GCD of two numbers a and b, but also the coefficients x and y. These coefficients can be used to express the GCD as a linear combination of a and b.
# function ExtendedEuclideanAlgorithm(a, b)
#     if b == 0 then
#         return (a, 1, 0)  // Base case: GCD(a, 0) = a, x = 1, y = 0
#     else
#         (gcd, x1, y1) = ExtendedEuclideanAlgorithm(b, a mod b)  // Recursive call
#         x = y1
#         y = x1 - (a div b) * y1
#         return (gcd, x, y)

# Q5. GIT repository link: https://github.com/Oyunbold05/FC723-Assignment-3.-P437033
# By using git commands such as commit and push. I have effectively tracked the changes I have made through the process. For example, by committing new changes regularly, I can restore my code in case where the new change does not work.
# 'Commit changes', 'View Commit History' and 'View Differences Between Commits' are all useful for me by allowing me to see the changes and differences between my changes.