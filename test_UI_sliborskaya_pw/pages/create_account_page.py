from test_UI_sliborskaya_pw.pages.base_page import BasePage
from playwright.sync_api import expect

firstname_loc = "#firstname"
last_name_loc = "#lastname"
email_input_loc = "#email_address"
psw_input_loc = "#password"
psw_confirmation_input_loc = "#password-confirmation"
create_an_account_button_loc = 'button.action.submit.primary'
email_address_error_loc = "#email_address-error"
psw_error_loc = "#password-error"
last_name_error_loc = "#lastname-error"


class CreateAccount(BasePage):
    page_url = "/customer/account/create/"


    def fill_create_form(self, firstname, lastname, email, psw, psw_confirmation):
        firstname_input = self.find(firstname_loc)
        last_name_input = self.find(last_name_loc)
        email_input = self.find(email_input_loc)
        psw_input = self.find(psw_input_loc)
        psw_confirmation_input = self.find(psw_confirmation_input_loc)
        create_an_account_button = self.find(create_an_account_button_loc)
        firstname_input.fill(firstname)
        last_name_input.fill(lastname)
        email_input.fill(email)
        psw_input.fill(psw)
        psw_confirmation_input.fill(psw_confirmation)
        create_an_account_button.click()


    def check_email_address_error_is_displayed(self):
        email_error = self.find(email_address_error_loc)
        expect(email_error).to_be_visible()


    def check_password_format_error_is_displayed(self):
        psw_error = self.find(psw_error_loc)
        expect(psw_error).to_be_visible()


    def check_lastname_is_required(self):
        last_name_error = self.find(last_name_error_loc)
        expect(last_name_error).to_be_visible()
