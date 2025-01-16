class customer:
    def apply_loan():
        print("Welcome: \nLoan Application Form")
        print ("-------------------------------------------------------")

        #getting user details
        customer_name = input("Enter your name: ")
        customer_email = input("Enter your email: ")
        customer_phone = input("Enter your phone number: ") 

        #getting loan details
        loan_amount = float(input("Enter the loan amount: "))
        duration_choice = int(input ("select loan duration: \n1. 2 Weeks \n2. 1 Month \n"))

        if duration_choice==1:
            duration = "2 Weeks"
            interest_rate = 0.20
        elif duration_choice == 2:
            duration = "1 Month"
            interest_rate = 0.35
        else:
            print("Invalid choice. Exiting Application")
            return 

        #calculating interest & total payable
        interest_amount = loan_amount * interest_rate
        total_repayment_amount = loan_amount + interest_amount
        
        #displaying loan details
        print("\nLoan Details:")
        print ("-------------------------------------------------------")
        print(f"Customer Name: {customer_name}")
        print(f"Loan amount: K{loan_amount:.2f}")
        print(f"Duration: {duration}")
        print(f"Interest rate: {interest_rate*100}%")
        print(f"Interest Amount: K{interest_amount:.2f}")
        print(f"Total Repayment Amount: K{total_repayment_amount:.2f}")

        #customer application confirmation
        confirmation_application = input("\nConfirm Loan application? (Yes/No): ")
        if confirmation_application.lower() == "yes":
            print("Loan application confirmed. You will receive an email with further instructions.")
        else:
            print("Loan application cancelled.")
    apply_loan()

    def view_loan():
        
