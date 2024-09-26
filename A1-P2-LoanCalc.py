"""
Student Name: Dan Shaw w0190983
Program Name: Weekly Loan Calculator
Program Description:  Develop a short term loan calculator program as a console application 
"""

def main():
    greeting = "WEEKLY LOAN CALCULATOR"
    # Output program title and greeting
    print(greeting)
    print("-" * len(greeting))
    print("Please enter the following information to calculate your weekly payments:")
    
    # Get loan amount from user, validate it as a number, then convert to float
    loanAmount = input("\tLoan Amount: ")
    while validateFloat(loanAmount) == 0:
        loanAmount = input("\tLoan Amount: ")
    loanAmount = float(loanAmount)

    # Get interest rate from user, validate it as a number, then convert to float
    interestRate = input("\tInterest Rate: ")
    while validateFloat(interestRate) == 0:
        interestRate = input("\tInterest Rate: ")
    interestRate = float(interestRate)
    
    # Get loan term in years from the user
    loanTerm = input("\tLoan Term (in years): ")
    while validateFloat(loanTerm) == 0:
        loanTerm = input("\tLoan Term (in years): ")
    loanTerm = float(loanTerm)

    print("\nCalculating weekly payments... ...\n")

    # Perform calculations
    weeklyInterest = interestRate / 5200
    weeklyPayment = (weeklyInterest / (1 - (1 + weeklyInterest) ** (-52 * loanTerm))) * loanAmount

    # Output calculations, formatted
    print("""With an interest rate of {0:.1f}% and a term of {1:.1f} years,
        you will have a weekly payment of: ${2:.2f}""".format(interestRate, loanTerm, weeklyPayment))

# Validates whether inputQuery is a valid number by trying to convert to a float
def validateFloat(inputQuery):
    try:
        float(inputQuery)
        return 1
    except:
        errorString = "Please enter a valid number"
        print("-" * len(errorString))
        print(errorString)
        print("-" * len(errorString))
        return 0

if __name__ == "__main__":
    main()