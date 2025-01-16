import sys

class LoanSystem:
    def _init_(self):
        self.user_type = None
        self.customer_id = None
        self.admin_id = None
        self.agent_id = None

    def register(self):
        print("Registering user...")
        # Registration logic here
        self.user_type = input("Enter user type (customer/admin/agent): ").lower() #change this to make the system automaticall detect user type
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
            elif action == "close":
                print("Closing account...")
                # Close account logic
            elif action == "submit":
                print("Submitting documents...")
                # Submit documents logic
            elif action == "resubmit":
                print("Resubmitting documents...")
                # Resubmit documents logic
            elif action == "accept":
                print("Accepting loan agreement...")
                # Accept loan agreement logic
            elif action == "reapply":
                print("Reapplying for loan...")
                # Reapply for loan logic
            elif action == "receive":
                print("Receiving loan...")
                # Receive loan logic
            elif action == "payemi":
                print("Paying EMI...")
                # Pay EMI logic
            else:
                print("Invalid action")
                break

    def admin_flow(self):
        while True:
            action = input("Choose action (setloan/receive/loanrecovery): ").lower()
            if action == "setloan":
                print("Setting loan type...")
                # Set loan type logic
            elif action == "receive":
                print("Receiving payment...")
                # Receive payment logic
            elif action == "loanrecovery":
                print("Initiating loan recovery...")
                # Loan recovery logic
            else:
                print("Invalid action")
                break

    def agent_flow(self):
        while True:
            action = input("Choose action (createloan/getreport): ").lower()
            if action == "createloan":
                print("Creating loan account...")
                # Create loan account logic
            elif action == "getreport":
                print("Getting report...")
                # Get report logic
            else:
                print("Invalid action")
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

if _name_ == "_main_":
    loan_system = LoanSystem()
    loan_system.run()