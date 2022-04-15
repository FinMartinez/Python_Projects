#Pascal's Triangle
#@author Fin Martinez
#@version 1.0
#@since 4/12/2022

#Imports
from Fin_Martinez_PascalTriangle import make_Triangle, get_Choices

#Project1 is the driver program used to ask the user to:
#   1. enter the size of the triangle
#   2. enter the position and row to display an integer result

#Print instructions
print("Welcome, please follow the following prompts.")
#assign input to variable num_input
num_input = input("Please enter a whole number: ")
row_num = int(num_input)

#assign input to variable row_input
row_input = input("Please enter the value of the desired row: ")
n = int(row_input)

#assign input to variable position_input
position_input = input("Please enter the desired position: ")
k = int(position_input)

#Print message
print("Thank you, here are your results: ")

#Function calls
make_Triangle(row_num)
get_Choices(n,k)

#end
