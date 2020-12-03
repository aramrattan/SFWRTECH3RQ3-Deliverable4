from menu_item import MenuItem

menuItem = MenuItem()
adminID = ""
# requirement 4.4.6a testing if a new menu item is added to the db
def test_add_menu_item():
    assert menuItem.add_menu_item(adminID) == True, "item not added to the db"

# requirement 4.4.6b testing if a menu item is updated in db when changed by admin
def test_update_menu_item():
    assert menuItem.update_menu_item(adminID) == True, "item was not updated"

# requirement 4.4.6c testing if admin can delete an item
def test_delete_menu_item():
    assert menuItem.delete_menu_item(adminID) == True, "item was not deleted"

# requirement 4.4.6d testing if item is edited to be sold out
def test_sold_out():
    assert menuItem.sold_out() == True, "item is not marked as sold out"
