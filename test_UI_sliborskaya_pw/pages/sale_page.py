from test_UI_sliborskaya_pw.pages.base_page import BasePage
from playwright.sync_api import expect



page_header_loc = 'h1'
side_bar_loc = '.sidebar-main'
promo_block_loc = 'a.block-promo.sale-main'


class SalePage(BasePage):
    page_url = "/sale.html"


    def check_page_header(self, text):
        page_header = self.find(page_header_loc)
        expect(page_header).to_have_text(text)


    def check_side_bar_menu(self):
        page_side_bar = self.find(side_bar_loc)
        expect(page_side_bar).to_be_visible()


    def click_on_promo_women(self):
        self.find(promo_block_loc).click()


    def check_women_sale_page_url(self):
        expect(self.page).to_have_url("https://magento.softwaretestingboard.com/promotions/women-sale.html")
