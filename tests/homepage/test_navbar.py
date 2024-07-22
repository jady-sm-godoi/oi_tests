import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logo_xpath = '/html/body/header/div[2]/div/div/div/a[1]/img'
logo_img = (
    'data/files/52/14/4B/27/FA44481004D804484B5BABA8/logoNova%20-%20header.svg'
)
nav_items_xpath = '/html/body/header/div[2]/div/div/div/ul'


# @pytest.mark.skip
def test_logo_exists(browser, home_url):
    browser.get(home_url)
    logo = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, logo_xpath))
    )
    assert logo is not None

    logo_src = logo.get_attribute('src')
    assert logo_src == f'{home_url}{logo_img}'

    logo.click()
    WebDriverWait(browser, 10).until(EC.url_to_be(home_url))
    assert browser.current_url == home_url


# @pytest.mark.skip
def test_items_exists(browser, home_url):
    browser.get(home_url)
    section = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, nav_items_xpath))
    )

    assert section is not None


#  test navbar  ###############################################################
nav_items = [
    (
        '/html/body/header/div[2]/div/div/div/ul/li[1]/a',
        'https://www.oi.com.br/grandes-empresas/conheca/',
    ),
    (
        '/html/body/header/div[2]/div/div/div/ul/li[3]/a',
        'https://www.oi.com.br/grandes-empresas/blog/',
    ),
    (
        '/html/body/header/div[2]/div/div/div/ul/li[4]/a',
        'https://www.oi.com.br/grandes-empresas/podcast/',
    ),
    (
        '/html/body/header/div[2]/div/div/div/ul/li[5]/a',
        'https://www.oi.com.br/grandes-empresas/fale-com-um-consultor/',
    ),
    (
        '/html/body/header/div[2]/div/div/div/a[2]',
        'https://portaloisolucoes.oi.com.br/login',
    ),
]

nav_items_ids = [
    'conheca',
    'blog',
    'podcast',
    'fale com um consultor',
    'portal oi solucoes',
]


# @pytest.mark.skip
@pytest.mark.parametrize(
    ('link_xpath', 'target_url'), nav_items, ids=nav_items_ids
)
def test_click_navbar_item__(browser, home_url, link_xpath, target_url):
    browser.get(home_url)
    item_link = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, link_xpath))
    )
    assert item_link is not None

    item_link.click()
    WebDriverWait(browser, 10).until(EC.url_to_be(target_url))
    assert browser.current_url == target_url


#  test navbar dropdown  ######################################################
nav_dropdown_items = [
    (
        '/html/body/header/div[2]/div/div/div/ul/li[2]/div/ul/li[1]/a',
        'https://www.oi.com.br/grandes-empresas/cloud/',
    ),
    (
        '/html/body/header/div[2]/div/div/div/ul/li[2]/div/ul/li[2]/a',
        'https://www.oi.com.br/grandes-empresas/big-data/',
    ),
    (
        '/html/body/header/div[2]/div/div/div/ul/li[2]/div/ul/li[3]/a',
        'https://www.oi.com.br/grandes-empresas/seguranca/',
    ),
    (
        '/html/body/header/div[2]/div/div/div/ul/li[2]/div/ul/li[4]/a',
        'https://www.oi.com.br/grandes-empresas/aplicacoes-digitais/',
    ),
    (
        '/html/body/header/div[2]/div/div/div/ul/li[2]/div/ul/li[5]/a',
        'https://www.oi.com.br/grandes-empresas/observabilidade/',
    ),
    (
        '/html/body/header/div[2]/div/div/div/ul/li[2]/div/ul/li[6]/a',
        'https://www.oi.com.br/grandes-empresas/conectividade/',
    ),
    (
        '/html/body/header/div[2]/div/div/div/ul/li[2]/div/ul/li[7]/a',
        'https://www.oi.com.br/grandes-empresas/uc-c/',
    ),
    (
        '/html/body/header/div[2]/div/div/div/ul/li[2]/div/ul/li[8]/a',
        'https://www.oi.com.br/grandes-empresas/fixa/',
    ),
    (
        '/html/body/header/div[2]/div/div/div/ul/li[2]/div/ul/li[9]/a',
        'https://www.oi.com.br/grandes-empresas/iot/',
    ),
]

nav_dropdown_items_ids = [
    'cloud',
    'big data',
    'seguranca',
    'aplicacoes digitais',
    'observabilidade',
    'conectividade',
    'uc-c',
    'fixa',
    'iot',
]


@pytest.mark.parametrize(
    ('link_xpath', 'target_url'),
    nav_dropdown_items,
    ids=nav_dropdown_items_ids,
)
def test_click_navbar_dropdown_item__(
    browser, home_url, link_xpath, target_url
):
    browser.get(home_url)
    dropdown_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((
            By.XPATH,
            '/html/body/header/div[2]/div/div/div/ul/li[2]/a',
        ))
    )
    assert dropdown_element is not None

    dropdown_hover = ActionChains(browser)
    dropdown_hover.move_to_element(dropdown_element).perform()
    dropdown_menu = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.menu-subitems'))
    )
    assert dropdown_menu is not None

    item_link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, link_xpath))
    )
    assert item_link is not None

    svg_tag = item_link.find_element(By.TAG_NAME, 'svg')
    assert svg_tag is not None

    item_link.click()

    WebDriverWait(browser, 10).until(EC.url_to_be(target_url))
    assert browser.current_url == target_url
