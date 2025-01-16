import unittest
from unittest.mock import patch
from io import StringIO
from index import LoanSystem

class TestLoanSystem(unittest.TestCase):
    def setUp(self):
        self.loan_system = LoanSystem()

    def test_apply_loan(self):
        # Test applying for a loan
        with patch('builtins.input', side_effect=['John Doe', 'john@example.com', '1234567890', '1000', '1']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                self.loan_system.customer_flow()
                output = fake_output.getvalue().strip()
                self.assertIn("Loan application confirmed", output)

    def test_view_loan_status(self):
        # Test viewing loan status
        with patch('builtins.input', side_effect=['view', '001']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                self.loan_system.customer_flow()
                output = fake_output.getvalue().strip()
                self.assertIn("Loan ID: 001", output)
                self.assertIn("Status: Approved", output)
                self.assertIn("Amount: 1000", output)
                self.assertIn("Balance: 500", output)

    def test_close_account(self):
        # Test closing an account with zero balance
        with patch('builtins.input', side_effect=['close', '001']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                self.loan_system.customer_flow()
                output = fake_output.getvalue().strip()
                self.assertIn("Account ID 001", output)
                self.assertIn("John Doe", output)
                self.assertIn("successfully closed", output)

        # Test closing an account with non-zero balance
        with patch('builtins.input', side_effect=['close', '002']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                self.loan_system.customer_flow()
                output = fake_output.getvalue().strip()
                self.assertIn("Account cannot be closed", output)
                self.assertIn("Outstanding balance: 2000", output)

    def test_submit_documents(self):
        # Test submitting documents
        with patch('builtins.input', side_effect=['submit', 'document_name', 'document_type']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                self.loan_system.customer_flow()
                output = fake_output.getvalue().strip()
                self.assertIn("Document submitted", output)

    def test_resubmit_documents(self):
        # Test resubmitting documents
        with patch('builtins.input', side_effect=['resubmit', 'document_name', 'document_type']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                self.loan_system.customer_flow()
                output = fake_output.getvalue().strip()
                self.assertIn("Document resubmitted", output)

    def test_accept_loan_agreement(self):
        # Test accepting loan agreement
        with patch('builtins.input', side_effect=['accept', 'agreement_name', 'agreement_type']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                self.loan_system.customer_flow()
                output = fake_output.getvalue().strip()
                self.assertIn("Loan agreement accepted", output)

    def test_reapply_for_loan(self):
        # Test reapplying for a loan
        with patch('builtins.input', side_effect=['reapply', '2000', '2']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                self.loan_system.customer_flow()
                output = fake_output.getvalue().strip()
                self.assertIn("Loan application confirmed", output)

    def test_receive_loan(self):
        # Test receiving a loan
        with patch('builtins.input', side_effect=['receive', '001']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                self.loan_system.customer_flow()
                output = fake_output.getvalue().strip()
                self.assertIn("Loan ID 001 received", output)

    def test_pay_emi(self):
        # Test paying EMI
        with patch('builtins.input', side_effect=['payemi', '500']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                self.loan_system.customer_flow()
                output = fake_output.getvalue().strip()
                self.assertIn("EMI payment processed successfully", output)

if __name__ == '__main__':
    unittest.main()