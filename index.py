import sys

class LoanSystem:
    """
    A class that represents a Loan Management System.

    Attributes:
    - user_type: The type of user (customer/admin/agent)
    - customer_id: The ID of the customer
    - admin_id: The ID of the admin
    - agent_id: The ID of the agent

    Methods:
    - register(): Registers a user in the system
    - login(): Logs in a user
    - customer_flow(): Handles the flow of actions for the customer in the loan management system
    """

    def __init__(self):
        self.user_type = None
        self.customer_id = None
        self.admin_id = None
        self.agent_id = None

    def register(self):
        """
        Registers a user in the loan management system.

        The user is prompted to enter their user type (customer/admin/agent) and their corresponding ID.

        Returns:
        None
        """
        print("Registering user...")
        # Registration logic here
        self.user_type = input("Enter user type (customer/admin/agent): ").lower() #change this to make the system automatically detect user type
        
        if self.user_type == "customer":
            self.customer_id = input("Enter customer ID: ")
        elif self.user_type == "admin":
            self.admin_id = input("Enter admin ID: ")
        elif self.user_type == "agent":
            self.agent_id = input("Enter agent ID: ")
        else:
            print("Invalid user type")
            sys.exit()

    def login(self):
        """
        Logs in a user in the loan management system.

        The user is prompted to enter their user type (customer/admin/agent) and their corresponding ID.

        Returns:
        None
        """
        print("Logging in...")
        # Login logic here
        if self.user_type == "customer":
            customer_id = input("Enter customer ID: ")
            if customer_id != self.customer_id:
                print("Invalid ID")
                sys.exit()
        elif self.user_type == "admin":
            admin_id = input("Enter admin ID: ")
            if admin_id != self.admin_id:
                print("Invalid ID")
                sys.exit()
        elif self.user_type == "agent":
            agent_id = input("Enter agent ID: ")
            if agent_id != self.agent_id:
                print("Invalid ID")
                sys.exit()

    def customer_flow(self):
        """
        Handles the flow of actions for the customer in the loan management system.

        The customer can choose from the following actions:
        - apply: Apply for a loan
        - view: View loan status
        - close: Close account
        - submit: Submit documents
        - resubmit: Resubmit documents
        - accept: Accept loan agreement
        - reapply: Reapply for a loan

        Returns:
        None
        """
        while True:
            action = input("Choose action (apply/view/close/submit/resubmit/accept/reapply/receive/payemi): ").lower()
            if action == "apply":
                print("Applying for loan...")
                # Apply loan logic
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
                
            elif action == "view":
                print("Viewing loan status...")
                # View loan status logic
                
        
                # Example: Retrieve loan status
                loan_id = input("Enter Loan ID to view status: ")

                # to be replaced with data from the DB
                loan_data = {
                    "001": {"status": "Approved", "amount": 1000, "balance": 500},
                    "002": {"status": "Pending", "amount": 2000, "balance": 2000},
                    "003": {"status": "Rejected", "amount": 1500, "balance": 0}
                }

                # to be replaced with data from the DB
                if loan_id in loan_data:
                    print(f"Loan ID: {loan_id}")
                    print(f"Status: {loan_data[loan_id]['status']}")
                    print(f"Amount: {loan_data[loan_id]['amount']}")
                    print(f"Balance: {loan_data[loan_id]['balance']}")
                else:
                    print("Loan ID not found.")

            elif action == "close":
                print("Closing account...")
                # Close account logic
                print("Closing an account...")

                # Example: Prompt user for the account ID or username
                account_id = input("Enter Account ID to close: ")

                # Mock data for example purposes
                accounts_data = {
                    "001": {"name": "John Doe", "loan_status": "Approved", "balance": 500},
                    "002": {"name": "Jane Smith", "loan_status": "Pending", "balance": 2000},
                    "003": {"name": "Alex Brown", "loan_status": "Rejected", "balance": 0}
                }

                # Check if the account exists
                if account_id in accounts_data:
                    account = accounts_data[account_id]

                    # Ensure the account balance is cleared before closing
                    if account["balance"] > 0:
                        print(f"Account cannot be closed. Outstanding balance: {account['balance']}")
                    else:
                        # Perform account closure
                        del accounts_data[account_id]
                        print(f"Account ID {account_id} ({account['name']}) has been successfully closed.")
                else:
                    print("Account ID not found.")

            elif action == "submit":
                print("Submitting documents...")
                # Submit documents logic
                # Example: Prompt user for document details
                document_name = input("Enter document name: ")
                document_type = input("Enter document type: ")

                # Example: Save document details to the database
                # Replace with your own database logic
                document_data = {
                    "name": document_name,
                    "type": document_type,
                    "status": "Submitted"
                }
                # Save document details to the database
                # Replace with your own database logic
                # document_id = save_document_to_database(document_data)
                # print(f"Document submitted. Document ID: {document_id}")

                print("Document submitted.")
                
            elif action == "resubmit":
                print("Resubmitting documents...")
                # Resubmit documents logic
                # Example: Prompt user for document details
                document_name = input("Enter document name: ")
                document_type = input("Enter document type: ")

                # Example: Save document details to the database
                # Replace with your own database logic
                document_data = {
                    "name": document_name,
                    "type": document_type,
                    "status": "Resubmitted"
                }
                # Save document details to the database
                # Replace with your own database logic
                # document_id = save_document_to_database(document_data)
                # print(f"Document resubmitted. Document ID: {document_id}")

                print("Document resubmitted.")
                
            elif action == "accept":
                print("Accepting loan agreement...")
                # Accept loan agreement logic
                # Example: Prompt user for loan agreement details
                agreement_name = input("Enter loan agreement name: ")
                agreement_type = input("Enter loan agreement type: ")

                # Example: Save loan agreement details to the database
                # Replace with your own database logic
                agreement_data = {
                    "name": agreement_name,
                    "type": agreement_type,
                    "status": "Accepted"
                }
                # Save loan agreement details to the database
                # Replace with your own database logic
                # agreement_id = save_agreement_to_database(agreement_data)
                # print(f"Loan agreement accepted. Agreement ID: {agreement_id}")

                print("Loan agreement accepted.")
                # agreement_id = save_agreement_to_database(agreement_data)
                # print(f"Loan agreement accepted. Agreement ID: {agreement_id}")

                print("Loan agreement accepted.")
                
            elif action == "reapply":
                print("Reapplying for loan...")
                # Reapply for loan logic
                # Example: Prompt user for loan details
                loan_amount = float(input("Enter the loan amount: "))
                duration_choice = int(input("Select loan duration: \n1. 2 Weeks \n2. 1 Month \n"))

                if duration_choice == 1:
                    duration = "2 Weeks"
                    interest_rate = 0.20
                elif duration_choice == 2:
                    duration = "1 Month"
                    interest_rate = 0.35
                else:
                    print("Invalid choice. Exiting Application")
                    return

                # Calculate interest & total payable
                interest_amount = loan_amount * interest_rate
                total_repayment_amount = loan_amount + interest_amount

                # Display loan details
                print("\nLoan Details:")
                print("-------------------------------------------------------")
                print(f"Loan amount: K{loan_amount:.2f}")
                print(f"Duration: {duration}")
                print(f"Interest rate: {interest_rate * 100}%")
                print(f"Interest Amount: K{interest_amount:.2f}")
                print(f"Total Repayment Amount: K{total_repayment_amount:.2f}")

                # Customer application confirmation
                confirmation_application = input("\nConfirm Loan application? (Yes/No): ")
                if confirmation_application.lower() == "yes":
                    print("Loan application confirmed. You will receive an email with further instructions.")
                else:
                    print("Loan application cancelled.")
                    print("Loan application confirmed. You will receive an email with further instructions.")
                else:
                    print("Loan application cancelled.")
                
            elif action == "receive":
                print("Receiving loan...")
                # Receive loan logic
                # Example: Prompt user for loan details
                loan_id = input("Enter Loan ID to receive: ")

                # Example: Update loan status in the database
                # Replace with your own database logic
                # update_loan_status(loan_id, "Received")
                # print(f"Loan ID {loan_id} received.")

                print(f"Loan ID {loan_id} received.")
                
            elif action == "payemi":
                print("Paying EMI...")
                # Pay EMI logic
                # Example: Prompt user for EMI details
                emi_amount = float(input("Enter the EMI amount: "))

                # Example: Process EMI payment
                # Replace with your own payment processing logic
                # process_emi_payment(emi_amount)
                # print("EMI payment processed successfully.")

                print("EMI payment processed successfully.")
            else:
                print("Invalid action")
                break

    def admin_flow(self):
        """
        Performs the administrative flow of the loan management system.
        This method allows the user to choose different actions such as setting loan types,
        receiving payments, and initiating loan recovery.

        Returns:
            None
        """
        while True:
            action = input("Choose action (setloan/receive/loanrecovery): ").lower()
            
            if action == "setloan":
                print("Setting loan type...")
                # Example logic for setting loan types
                loan_name = input("Enter loan type name: ")
                interest_rate = float(input("Enter interest rate (as a percentage): "))
                max_amount = float(input("Enter maximum loan amount: "))
                
                # Mock data to represent existing loan types
                loan_types = {"Personal Loan": {"interest_rate": 10.0, "max_amount": 5000}}
                
                # Add or update the loan type
                loan_types[loan_name] = {"interest_rate": interest_rate, "max_amount": max_amount}
                print(f"Loan type '{loan_name}' has been set with an interest rate of {interest_rate}% and max amount {max_amount}.")

            elif action == "receive":
                print("Receiving payment...")
                # Example logic for receiving payments
                account_id = input("Enter Account ID: ")
                payment_amount = float(input("Enter payment amount: "))
                
                # Mock data to represent account loans
                loans_data = {"001": {"balance": 1000}, "002": {"balance": 2000}}
                
                if account_id in loans_data:
                    loans_data[account_id]["balance"] -= payment_amount
                    print(f"Payment of {payment_amount} received. Remaining balance: {loans_data[account_id]['balance']}")
                else:
                    print("Account ID not found.")

            elif action == "loanrecovery":
                print("Initiating loan recovery...")
                # Example logic for loan recovery
                overdue_accounts = {
                    "001": {"name": "John Doe", "overdue_amount": 500},
                    "003": {"name": "Jane Smith", "overdue_amount": 1500}
                }
                
                if overdue_accounts:
                    print("Overdue accounts:")
                    for account_id, details in overdue_accounts.items():
                        print(f"Account ID: {account_id}, Name: {details['name']}, Overdue Amount: {details['overdue_amount']}")
                else:
                    print("No overdue accounts.")

            else:
                print("Invalid action. Exiting admin flow.")
                break

    def agent_flow(self):
        while True:
            action = input("Choose action (createloan/getreport): ").lower()

            if action == "createloan":
                print("Creating loan account...")
                # Create loan account logic
                account_id = input("Enter Account ID: ")
                customer_name = input("Enter Customer Name: ")
                loan_amount = float(input("Enter Loan Amount: "))
                interest_rate = float(input("Enter Interest Rate (as a percentage): "))
                duration = int(input("Enter Loan Duration (in months): "))

                # Mock data for storing loan accounts
                loan_accounts = {
                    # Example format: "001": {"name": "John Doe", "amount": 1000, "interest_rate": 10, "duration": 12}
                }

                if account_id not in loan_accounts:
                    loan_accounts[account_id] = {
                        "name": customer_name,
                        "amount": loan_amount,
                        "interest_rate": interest_rate,
                        "duration": duration
                    }
                    print(f"Loan account for {customer_name} created successfully!")
                else:
                    print("Account ID already exists. Loan creation failed.")

            elif action == "getreport":
                print("Getting report...")
                # Generate report logic
                # Mock data for loan accounts
                loan_accounts = {
                    "001": {"name": "John Doe", "amount": 1000, "interest_rate": 10, "duration": 12},
                    "002": {"name": "Jane Smith", "amount": 2000, "interest_rate": 8, "duration": 24},
                }

                if not loan_accounts:
                    print("No loan accounts found.")
                else:
                    print("Loan Accounts Report:")
                    for account_id, details in loan_accounts.items():
                        print(f"Account ID: {account_id}")
                        print(f"Customer Name: {details['name']}")
                        print(f"Loan Amount: {details['amount']}")
                        print(f"Interest Rate: {details['interest_rate']}%")
                        print(f"Duration: {details['duration']} months")
                        print("-" * 30)

            else:
                print("Invalid action. Exiting agent flow.")
                break

    def run(self):
        self.register()
        self.login()
        if self.user_type == "customer":
            self.customer_flow()
        elif self.user_type == "admin":
            self.admin_flow()
        elif self.user_type == "agent":
            self.agent_flow()

if __name__ == "_main_":
    loan_system = LoanSystem()
    loan_system.run()