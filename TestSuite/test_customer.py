from customer import Customer

customer = Customer()

# Requirement 4.1.1ai testing that the password entered in registration is in the valid format
def test_verify_password_format():
    password = ""
    assert customer.verify_password_format(password) == True, "password is not in the correct format "

# requirement 4.1.1aii testing that the email entered on the registration page is in valid format
def test_verify_email_format():
    email = ""
    assert customer.verify_email_format(email) == True, "the email is not in correct format"

# requirement 4.2.2a testing that the customer account is registered
def test_verify_account():
    email = ""
    password = ""
    assert customer.verify_account(email, password) == True, "this account is not registered"

# requirement 4.3.4 testing if account info is retrieved from the db
def test_get_account_info():
    email = ""
    password = ""
    assert customer.get_account_info(email, password) == True, "this account is not in the db"

# requirement 4.3.4a testing if the account info gets updated in db
def test_update_account_info():
    assert customer.update_account_info() == True, "this info was not updated"

# requirement 4.3.3 testing to see if all the customer orders are retrieved from db
def test_get_all_orders():
    customerId= ""
    assert customer.get_all_orders(customerId) == True, "customer has no orders"
