from playwright.sync_api import Page, expect, BrowserContext, Dialog
import re


def test_task_one(page: Page):
    def accept_alert(alert: Dialog):
        alert.accept()
    page.on("dialog", accept_alert)
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.get_by_role("link", name="Click").click()
    result_text = page.locator("#result-text")
    expect(result_text).to_have_text("Ok")


def test_task_two(page: Page, context: BrowserContext):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")
    button_click = page.locator(".a-button")
    with context.expect_page() as new_page_event:
        button_click.click()
    new_page = new_page_event.value
    result = new_page.locator("#result-text")
    expect(result).to_have_text("I am a new page in a new tab")
    expect(button_click).to_be_enabled()


def test_task_three(page: Page):
    page.goto("https://demoqa.com/dynamic-properties")
    button = page.locator("#colorChange")
    expect(button).to_have_class(re.compile(r".text-danger"))
    button.click()
