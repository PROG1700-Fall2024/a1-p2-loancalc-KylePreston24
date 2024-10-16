#Program 2 – Weekly Loan Calculator
#Develop a short term loan calculator program as a console application 
"""
Student Name: Kyle Preston
Program: Program 2 – Weekly Loan Calculator

"""
import math 
def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #Variables 

    loanAmount = float(0)
    interestRate = float(0)
    numberOfYears = float(0)


    # Input 
    
    # This code is for entering the amount for the loan  via input

    loanAmount = input("Enter the amount of loan: ")


    # this code is for entering % amount for interest rate via input
    
    interestRate = input("Enter the inetest rate (%): ")

    #this code is a input for putting in amount of years

    numberOfYears = input("Enter the number of years: ")



    #Calcutions 

    #weekly interest calculation  (interestRate / 5200)

    weeklyInterest = float(interestRate) / 5200

    weeklyPayment = (weeklyInterest / (1-math.pow((1+weeklyInterest),-52 * float(numberOfYears)))) * float(loanAmount)

   


    print("Your weekly payment will be: ${0:.2f}".format(weeklyPayment))



    # YOUR CODE ENDS HERE

main()