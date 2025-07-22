from test_UI_sliborskaya_pw.pages.base_page import BasePage
from playwright.sync_api import expect


selected_item_loc = '//li[contains(@class, "product-item")]//a[@class="product-item-link"]'
add_to_compare_loc = '//a[@class="action tocompare"]'
product_link_loc = "//ol[@id='compare-items']//a[contains(@class, 'product-item-link')]"


class ProductPage(BasePage):
    page_url = "/collections/eco-friendly.html"

    def add_to_compare(self):
        selected_item = self.find(selected_item_loc).first
        selected_item_name = self.find(selected_item_loc).first.text_content()
        selected_item.hover()
        self.find(add_to_compare_loc).first.click()
        compare_item = self.find(product_link_loc)
        expect(compare_item).to_have_text(selected_item_name)

    def remove_all_from_compare(self):
        clear_all_button = self.find("#compare-clear-all")
        clear_all_button.click()
        modal_ok_button = self.find("button.action-primary.action-accept")
        modal_ok_button.click()

    def check_alert_text(self, expected_message):
        alert = self.find("//div[@role='alert']//div[contains(text(), 'cleared the comparison')]")
        alert_text = alert.text_content()
        assert alert_text == expected_message

    def hover_over_product(self):
        selected_item = self.find(selected_item_loc).first
        selected_item.hover()

    def check_add_to_card_actions_is_displayed(self):
        self.hover_over_product()
        add_to_cart_btn = self.find('//button[@type="submit"]').first
        expect(add_to_cart_btn).to_be_visible()

    def check_add_to_wishlist_actions_is_displayed(self):
        self.hover_over_product()
        add_to_wishlist = self.find('//a[@class="action towishlist"]').first
        expect(add_to_wishlist).to_be_visible()

    def check_add_to_compare_actions_is_displayed(self):
        self.hover_over_product()
        add_to_compare = self.find('//a[@class="action tocompare"]').first
        expect(add_to_compare).to_be_visible()
