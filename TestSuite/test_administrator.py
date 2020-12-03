from administrator import Administrator

admin = Administrator()
#requirement 4.4.5 testing login to admin account
def test_admin_log_in():
    assert admin.admin_log_in() == True, "account not admin"
