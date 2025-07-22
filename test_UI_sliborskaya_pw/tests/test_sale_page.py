def test_check_page_header(sale_page):
    sale_page.open_page()
    sale_page.check_page_header('Sale')


def test_sidebar_is_displayed(sale_page):
    sale_page.open_page()
    sale_page.check_side_bar_menu()


def test_promo_block_is_clickable(sale_page):
    sale_page.open_page()
    sale_page.click_on_promo_women()
    sale_page.check_women_sale_page_url()
