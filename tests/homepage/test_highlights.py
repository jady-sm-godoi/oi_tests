import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# @pytest.mark.skip
def test_highlights_exists(browser, home_url):
    browser.get(home_url)
    section = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR,
            'section.solucoes-digitais',
        ))
    )

    assert section is not None


#  test click items  ########################################################
items = [
    (
        '//*[@id="home"]/section[3]/div/div/div[2]/div[1]',
        'https://www.oi.com.br/grandes-empresas/cloud/',
        'data/files/A4/E0/DD/89/D5FCD8105313FCD84B5BABA8/cloud.svg',
    ),
    (
        '//*[@id="home"]/section[3]/div/div/div[2]/div[2]',
        'https://www.oi.com.br/grandes-empresas/seguranca/',
        'data/files/AC/E0/93/99/D5FCD8105313FCD84B5BABA8/seguranca.svg',
    ),
    (
        '//*[@id="home"]/section[3]/div/div/div[2]/div[3]',
        'https://www.oi.com.br/grandes-empresas/observabilidade/',
        'data/files/21/E0/E8/08/54F4F81014E8BCE8EA6BABA8/observabilidade.svg',
    ),
]

ids = ['cloud', 'seguranca', 'observabilidade']


# @pytest.mark.skip
@pytest.mark.parametrize(
    ('btn_xpath', 'target_url', 'expected_src'), items, ids=ids
)
def test_click_item__(browser, home_url, btn_xpath, target_url, expected_src):
    browser.get(home_url)
    highlight_item = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, btn_xpath))
    )
    assert highlight_item is not None

    img_tag = highlight_item.find_element(By.TAG_NAME, 'img')
    img_src = img_tag.get_attribute('src')

    assert img_src == f'{home_url}{expected_src}'

    a_tag = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            highlight_item.find_element(By.TAG_NAME, 'a')
        )
    )
    browser.execute_script('arguments[0].scrollIntoView();', a_tag)
    a_tag.click()

    WebDriverWait(browser, 10).until(EC.url_to_be(target_url))
    assert browser.current_url == target_url
