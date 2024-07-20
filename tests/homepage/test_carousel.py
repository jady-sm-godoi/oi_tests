import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url = 'https://www.oi.com.br/grandes-empresas/'


items = [
    (
        'slick-slide-control04',
        '//*[@id="slick-slide04"]/div/div/div/div[3]/a',
        'https://portaloisolucoes.oi.com.br/login',
    ),
    (
        'slick-slide-control05',
        '//*[@id="slick-slide05"]/div/div/div/div[3]/a',
        'https://www.oi.com.br/grandes-empresas/blog/',
    ),
    (
        'slick-slide-control06',
        '//*[@id="slick-slide06"]/div/div/div/div[3]/a',
        'https://www.oi.com.br/grandes-empresas/cloud/',
    ),
]

ids = ['atendimento', 'solucoes em pauta', 'cloud hub']


# @pytest.mark.skip
def test_carousel_exists(browser):
    browser.get(url)
    section = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'section.banner'))
    )

    assert section is not None


# @pytest.mark.skip
@pytest.mark.parametrize(
    ('item_id', 'btn_xpath', 'target_url'), items, ids=ids
)
def test_click_item__(browser, item_id, btn_xpath, target_url):
    browser.get(url)
    carosel_item = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, item_id))
    )
    assert carosel_item is not None

    carosel_item.click()
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, btn_xpath))
    )
    assert button is not None

    button.click()
    WebDriverWait(browser, 10).until(EC.url_to_be(target_url))
    assert browser.current_url == target_url
