def test_add_to_compare(product_page):
    product_page.open_page()
    product_page.add_to_compare()


def test_remove_all_from_compare(product_page):
    product_page.open_page()
    product_page.add_to_compare()
    product_page.remove_all_from_compare()
    expected_message = "You cleared the comparison list."
    product_page.check_alert_text(expected_message)


def test_product_actions_are_displayed(product_page):
    product_page.open_page()
    product_page.check_add_to_card_actions_is_displayed()
    product_page.check_add_to_wishlist_actions_is_displayed()
    product_page.check_add_to_compare_actions_is_displayed()
