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
    # As long as validateFloat() returns None, the while loop will never end and the user will be continuously prompted for a float value
    # Once a float value is entered, while loop ends and program continues
    while (loanAmount := validateFloat(input("\tTotal Loan Amount: "))) == None:
        pass

    # Get interest rate from user, validate it as a number, then convert to float
    while (interestRate := validateFloat(input("\tInterest Rate: "))) == None:
        pass
    
    # Get loan term in years from the user
    while (loanTerm := validateFloat(input("\tLoan Term (in years): "))) == None:
        pass

    print("\nCalculating weekly payments... ...\n")

    # Perform calculations
    weeklyInterest = interestRate / 5200
    weeklyPayment = (weeklyInterest / (1 - (1 + weeklyInterest) ** (-52 * loanTerm))) * loanAmount

    # Output calculations, formatted
    print("""Interest Rate: {0:.1f}%
    Loan Term: {1:.1f} years
    Total Loan Amount: ${3:.2f}
    Weekly Payment: ${2:.2f}""".format(interestRate, loanTerm, weeklyPayment, loanAmount))

# Validates whether inputQuery is a valid number by trying to convert to a float
# Returns the converted float if successfull and None if fails
def validateFloat(inputQuery):
    try:
        return float(inputQuery)
    except:
        errorString = "Please enter a valid number"
        print("-" * len(errorString))
        print(errorString)
        print("-" * len(errorString))
        return None

if __name__ == "__main__":
    main()