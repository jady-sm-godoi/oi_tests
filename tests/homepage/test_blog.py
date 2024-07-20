import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from slugify import slugify


# @pytest.mark.skip
def test_blog_exists(browser, home_url):
    browser.get(home_url)
    section = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "section.blog",
            )
        )
    )

    assert section is not None


#  test click items  ##########################################################
items = [
    ('//*[@id="home"]/section[4]/div/div/div[2]',),
    ('//*[@id="home"]/section[4]/div/div/div[3]',),
    ('//*[@id="home"]/section[4]/div/div/div[4]',),
]

ids = ["post 1", "post 2", "post 3"]


# @pytest.mark.skip
@pytest.mark.parametrize(("btn_xpath",), items, ids=ids)
def test_click_item__(browser, home_url, btn_xpath):
    browser.get(home_url)
    blog_item = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, btn_xpath))
    )
    assert blog_item is not None

    img_tag = blog_item.find_element(By.TAG_NAME, "img")
    img_src = img_tag.get_attribute("src")

    assert img_src is not None

    a_tag = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(blog_item.find_element(By.TAG_NAME, "a"))
    )
    browser.execute_script("arguments[0].scrollIntoView();", a_tag)
    future_title = a_tag.get_attribute("href").split("/")[-3]

    a_tag.click()

    current_title = slugify(browser.title)
    assert future_title in current_title
