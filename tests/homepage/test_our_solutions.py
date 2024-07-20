import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url = 'https://www.oi.com.br/grandes-empresas/'


items = [
    (
        '//*[@id="home"]/section[2]/div/div/div[2]/div/div/div/div[1]/a',
        'https://www.oi.com.br/grandes-empresas/cloud/',
        'data/files/A4/E0/DD/89/D5FCD8105313FCD84B5BABA8/cloud.svg',
    ),
    (
        '//*[@id="home"]/section[2]/div/div/div[2]/div/div/div/div[2]/a',
        'https://www.oi.com.br/grandes-empresas/seguranca/',
        'data/files/AC/E0/93/99/D5FCD8105313FCD84B5BABA8/seguranca.svg',
    ),
    (
        '//*[@id="home"]/section[2]/div/div/div[2]/div/div/div/div[3]/a',
        'https://www.oi.com.br/grandes-empresas/observabilidade/',
        'data/files/21/E0/E8/08/54F4F81014E8BCE8EA6BABA8/observabilidade.svg',
    ),
    (
        '//*[@id="home"]/section[2]/div/div/div[2]/div/div/div/div[4]/a',
        'https://www.oi.com.br/grandes-empresas/uc-c/',
        'data/files/A0/F0/66/99/D5FCD8105313FCD84B5BABA8/uc-and-c.svg',
    ),
    (
        '//*[@id="home"]/section[2]/div/div/div[2]/div/div/div/div[5]/a',
        'https://www.oi.com.br/grandes-empresas/iot/',
        'data/files/AA/E0/22/99/D5FCD8105313FCD84B5BABA8/iot.svg',
    ),
    (
        '//*[@id="home"]/section[2]/div/div/div[2]/div/div/div/div[6]/a',
        'https://www.oi.com.br/grandes-empresas/big-data/',
        'data/files/A2/E0/6C/89/D5FCD8105313FCD84B5BABA8/big-data.svg',
    ),
    (
        '//*[@id="home"]/section[2]/div/div/div[2]/div/div/div/div[7]/a',
        'https://www.oi.com.br/grandes-empresas/aplicacoes-digitais/',
        'data/files/B0/E0/1E/79/D5FCD8105313FCD84B5BABA8/aplicacoes-digitais.svg',
    ),
    (
        '//*[@id="home"]/section[2]/div/div/div[2]/div/div/div/div[8]/a',
        'https://www.oi.com.br/grandes-empresas/conectividade/',
        'data/files/A6/E0/4F/89/D5FCD8105313FCD84B5BABA8/conectividade.svg',
    ),
    (
        '//*[@id="home"]/section[2]/div/div/div[2]/div/div/div/div[9]/a',
        'https://www.oi.com.br/grandes-empresas/fixa/',
        'data/files/A8/E0/D0/99/D5FCD8105313FCD84B5BABA8/fixa.svg',
    ),
]

ids = [
    'cloud',
    'seguranca',
    'observabilidade',
    'uc-c',
    'iot',
    'big data',
    'aplicacoes digitais',
    'conectividade',
    'fixa',
]


# @pytest.mark.skip
def test_our_solutions_exists(browser):
    browser.get(url)
    section = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR,
            'section.nossas-solucoes',
        ))
    )

    assert section is not None


# @pytest.mark.skip
@pytest.mark.parametrize(
    ('btn_xpath', 'target_url', 'expected_src'), items, ids=ids
)
def test_click_item__(browser, btn_xpath, target_url, expected_src):
    browser.get(url)
    carosel_item = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, btn_xpath))
    )
    assert carosel_item is not None

    img_tag = carosel_item.find_element(By.TAG_NAME, 'img')
    img_src = img_tag.get_attribute('src')

    assert img_src == f'{url}{expected_src}'

    carosel_item.click()

    WebDriverWait(browser, 10).until(EC.url_to_be(target_url))
    assert browser.current_url == target_url
