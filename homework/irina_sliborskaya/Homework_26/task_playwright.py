from playwright.sync_api import Page, expect


def test_task_one(page: Page):
    page.goto('https://the-internet.herokuapp.com')
    page.get_by_role('link', name='Form Authentication').click()
    page.get_by_role('textbox', name='username').fill('test')
    page.get_by_role('textbox', name='password').fill('password')
    page.get_by_role('button').click()


def test_task_two(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.get_by_placeholder('First Name').fill('Test')
    page.get_by_placeholder('Last Name').fill('Testovich')
    page.get_by_placeholder('name@example.com').fill('test@test.coooom')
    page.locator('label[for="gender-radio-2"]').click()
    page.get_by_placeholder('Mobile Number').fill('1234567890')
    page.locator('input[id="dateOfBirthInput"]').click()
    page.locator('//div[@role="option" and text()="10"]').click()
    subject_field = page.locator('.subjects-auto-complete__value-container input')
    subject_field.press_sequentially("English")
    subject_field.press('Enter')
    page.locator('label[for="hobbies-checkbox-2"]').click()
    page.get_by_placeholder('Current Address').fill('Some address in UK')
    state_selector = page.locator('//div[contains(text(), "Select State")]')
    state_selector.click()
    page.locator("//div[text()='Haryana']").click()
    city_selector = page.locator('//div[contains(text(), "Select City")]')
    city_selector.click()
    page.locator("//div[text()='Karnal']").click()
    page.get_by_text('Submit').click()

