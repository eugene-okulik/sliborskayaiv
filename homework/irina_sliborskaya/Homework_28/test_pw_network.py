import re
from playwright.sync_api import Page, Route
import json


def test_title(page: Page):
    def change_res(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'яблокофон 16 про'
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )
    page.route(re.compile('/shop/api/digital-mat'), change_res)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator('.rf-hcard-content-title').nth(0).click()
    title_loc = page.locator('[data-autom="DigitalMat-overlay-header-0-0"]')
    title = title_loc.text_content()
    assert title == 'яблокофон 16 про'
