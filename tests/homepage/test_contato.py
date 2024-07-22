# import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# from slugify import slugify


# @pytest.mark.skip
def test_contato_exists(browser, home_url):
    browser.get(home_url)
    section = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR,
            'section.contato',
        ))
    )

    assert section is not None


#  test click buttom  ######################################################


def test_click_btnToForm(browser, home_url):
    browser.get(home_url)
    btnToBlog = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((
            By.XPATH,
            '//*[@id="home"]/section[5]/div/div/div[2]/a',
        ))
    )
    browser.execute_script('arguments[0].scrollIntoView();', btnToBlog)
    btnToBlog.click()
    target_url = (
        'https://www.oi.com.br/grandes-empresas/fale-com-um-consultor/'
    )
    WebDriverWait(browser, 10).until(EC.url_to_be(target_url))
    assert browser.current_url == target_url
