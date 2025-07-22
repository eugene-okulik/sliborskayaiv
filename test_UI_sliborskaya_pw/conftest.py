import pytest
from playwright.sync_api import BrowserContext

from test_UI_sliborskaya_pw.pages.create_account_page import CreateAccount
from test_UI_sliborskaya_pw.pages.products_page import ProductPage
from test_UI_sliborskaya_pw.pages.sale_page import SalePage


@pytest.fixture()
def create_account_page(page):
    return CreateAccount(page)


@pytest.fixture()
def sale_page(page):
    return SalePage(page)


@pytest.fixture()
def product_page(page):
    return ProductPage(page)


@pytest.fixture()
def page(context: BrowserContext):
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page
