from orders import Orders

order = Orders()

# requirement 4.3.4b testing to retrieve an individual order information
def test_get_one_order():
    orderId= ""
    assert order.get_order(orderId) == True, " Unable to retrieve order"
