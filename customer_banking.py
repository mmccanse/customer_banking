# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("What is your savings balance?"))
    interest_rate = float(input("What is your interest rate?"))
    savings_maturity = int(input("How many months are you calculating savings interest for?"))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, interest_rate, savings_maturity)
    

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Savings interest earned: ${savings_interest_earned:,.2f}")
    print(f"Savings updated balance: ${updated_savings_balance:,.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    CD_balance = float(input("What is your CD balance?"))
    CD_interest = float(input("What is your CD interest rate?"))
    CD_maturity = int(input("How many months are you calculating CD interest for?"))
    
    

    # Call the create_cd_account function and pass the variables from the user.
    updated_CD_balance, CD_interest_earned = create_cd_account(CD_balance, CD_interest, CD_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"CD interest earned: ${CD_interest_earned:,.2f}")
    print(f"CD updated balance: ${updated_CD_balance:,.2f}")
        
    
if __name__ == "__main__":
    # Call the main function.
    main()



