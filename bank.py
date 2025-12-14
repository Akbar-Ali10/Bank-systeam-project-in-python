import random
class Bank:
    bank_name ="Apna Bank"
    def __init__(self, branch_name, branch_deposit=0):
        self.branch_name = branch_name
        self.branch_deposit = branch_deposit
        self.branch_accounts = []
    def open_account(self, cnic, account_title, initial_deposit=0):
        account = {
            'cnic': cnic,
            'title': account_title,
            'balance': initial_deposit,
            'account_number': random.randint(1000, 9999),
            'pin': random.randint(1000, 9999),
            
        }
        # self.branch_deposit = self.branch_deposit + initial_deposit
        self.branch_accounts.append(account)
        return account
        
    def close_account(self, account_number,pin):
        for account in self.branch_accounts:
            if account['account_number'] == account_number:
                if account['pin'] == pin:
                    self.branch_deposit = self.branch_deposit - account['balance']
                    self.branch_accounts.remove(account)
                    return account
                else:
                    return "Wrong Pin"
            else:
                return "Account Not Found"  
             
    def show_balance(self,account_number, pin):
        for acc in self.branch_accounts:
            if acc['account_number'] == account_number:
                if acc['pin'] == pin:
                    return acc['balance'], None
                else:
                    return None, "Invalid PIN"
        return None, "Account Not Found" 
            
    def deposit_amt(self,account_number, amount):
        for acc in self.branch_accounts:
            if acc['account_number'] == account_number:
                acc['balance'] += amount
                return acc['balance'], None
        return None, "Account Not Found"   
    def withdraw_amt(self,account_number, pin, amount):
        for acc in self.branch_accounts:
            if acc['account_number'] == account_number:
                if acc['pin'] != pin:
                    return None, "Invalid PIN"

                if amount > acc['balance']:
                    return None, "Insufficient Balance"

                acc['balance'] -= amount
                return acc['balance'], None
        
            return None, "Account Not Found"
            
    def transfer_amt(self,account_number, pin, amount, beneficiary_acc):
        for acc in self.branch_accounts:
            if acc['account_number'] == account_number:

                if acc['pin'] != pin:
                    return None, "Invalid PIN"

                if acc['balance'] < amount:
                    return None, "Insufficient Balance"

                # beneficiary check
                for bacc in self.branch_accounts:
                    if bacc['account_number'] == beneficiary_acc:
                        acc['balance'] -= amount
                        bacc['balance'] += amount
                        return acc['balance'], None

            return None, "Beneficiary Account Not Found"

        return None, "Account Not Found"
    def show_all_accounts(self):
        return self.branch_accounts