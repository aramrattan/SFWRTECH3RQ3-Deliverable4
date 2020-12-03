class Customer:

    # makes sure that password entered has correct values
    def verify_password_format(self, password):
        return None

    # makes sure the email address is in the correct format
    def verify_email_format(self, email):
        return None

    # gets customer account information
    def get_account_info(self, email, password):
        return None

    # will retrieve the account info from the db and return error if none
    def verify_account(self, email, password):
        return None

    # this is for modifying the customer's  account info
    def update_account_info(self):
        return None

    #will get customer's previous orders
    def get_all_orders(self, cxId):
        return None
