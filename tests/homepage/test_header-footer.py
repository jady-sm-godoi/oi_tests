import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#  test header  ###############################################################

header_items_xpath = '/html/body/header/div[1]/div/div/div/ul'


@pytest.mark.skip
def test_header_exists(browser, home_url):
    browser.get(home_url)
    section = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, header_items_xpath))
    )

    assert section is not None


header_items = [
    (
        '/html/body/header/div[1]/div/div/div/ul/ul[2]/li[1]/a',
        'https://www.oi.com.br/',
    ),
    (
        '/html/body/header/div[1]/div/div/div/ul/ul[2]/li[2]/a',
        'https://www.oi.com.br/empresas/',
    ),
    (
        '/html/body/header/div[1]/div/div/div/ul/ul[2]/li[3]/a',
        'https://ri.oi.com.br/',
    ),
]

header_items_ids = [
    'voce',
    'pequenas empresas',
    'investidores',
]


@pytest.mark.skip
@pytest.mark.parametrize(
    ('link_xpath', 'target_url'), header_items, ids=header_items_ids
)
def test_click_header_item(browser, home_url, link_xpath, target_url):
    browser.get(home_url)
    item_link = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, link_xpath))
    )
    assert item_link is not None

    item_link.click()
    WebDriverWait(browser, 10).until(EC.url_to_be(target_url))
    assert browser.current_url == target_url


#  test footer  ######################################################

footer_items_xpath = '/html/body/footer'
logo_xpath = '/html/body/footer/div/div/a/img'
logo_img = (
    'data/files/52/14/4B/27/FA44481004D804484B5BABA8/logoNova%20-%20header.svg'
)


@pytest.mark.skip
def test_items_exists(browser, home_url):
    browser.get(home_url)
    section = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, footer_items_xpath))
    )

    assert section is not None


@pytest.mark.skip
def test_logo_exists(browser, home_url):
    browser.get(home_url)
    logo = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, logo_xpath))
    )
    assert logo is not None

    logo_src = logo.get_attribute('src')
    assert logo_src == f'{home_url}{logo_img}'

    browser.execute_script('arguments[0].scrollIntoView();', logo)
    logo.click()
    WebDriverWait(browser, 10).until(EC.url_to_be(home_url))
    assert browser.current_url == home_url


footer_items = [
    (
        '/html/body/footer/div/div/div/ul/li[1]/a',
        'https://br.linkedin.com/company/oisolucoes',
    ),
    (
        '/html/body/footer/div/div/div/ul/li[2]/a',
        'https://www.oi.com.br/grandes-empresas/conheca/',
    ),
    (
        '/html/body/footer/div/div/div/ul/li[3]/a',
        'https://www.oi.com.br/grandes-empresas/blog/',
    ),
    (
        '/html/body/footer/div/div/div/ul/li[4]/a',
        'https://www.oi.com.br/grandes-empresas/podcast/',
    ),
    (
        '/html/body/footer/div/div/div/ul/li[5]/a',
        'https://www.oi.com.br/portal-de-privacidade/',
    ),
]

footer_items_ids = [
    'linkedin',
    'conheca',
    'blog',
    'podcast',
    'privacidade',
]


@pytest.mark.parametrize(
    ('link_xpath', 'target_url'),
    footer_items,
    ids=footer_items_ids,
)
def test_click_footer_item__(browser, home_url, link_xpath, target_url):
    browser.get(home_url)
    item_link = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, link_xpath))
    )
    assert item_link is not None

    browser.execute_script('arguments[0].scrollIntoView();', item_link)
    item_link.click()

    if target_url == 'https://www.linkedin.com/company/oisolucoes/mycompany/':
        try:
            close_button = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    '//button[@aria-label="Dismiss"]',
                ))
            )
            close_button.click()
        except TimeoutError:
            pass

    WebDriverWait(browser, 10).until(EC.url_to_be(target_url))
    assert browser.current_url == target_url
