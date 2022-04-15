#Pascal's Triangle
#@author Fin Martinez
#@version 1.2
#@since 4/12/2022

import math

#PascalTriangle is the file containing the functions to generate
#          a Pascal Triangle from the input passed from Project1.
#This file performs the following functions:
#   1. Generate a Pascal from the provided number of rows
#   2. Returns a calculated integer value from the choices provided
#      from Project1

#Generate a Triangle
def make_Triangle(rows): #Function takes rows variable from driver
    curr_row = [1]       #Starts curr_row list at 1
    y = [0]              #y list is the list that keeps track of which row the loop is on
    row_list = []        #row_list stores new versions of curr_row into a list
    #loop to generate pascal triangle via printing lists
    for x in range(rows):
        print(curr_row)
        row_list.append(curr_row)
        #new version of curr_row established by using zip() function
        curr_row = [left+right for left,right in zip(curr_row+y, y+curr_row)]
    return row_list

#Produce integer result from lists
def get_Choices(n,k):
    #combo_choices calculated with C(n,k) = n!/((n-k)!*k!)
    combo_choices = (math.factorial(int(n)))/((math.factorial(int(n - k))) * (math.factorial(int(k))))
    print("The result from the position and row is: ", combo_choices)

#end
