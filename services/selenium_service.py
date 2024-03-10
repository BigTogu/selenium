from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def launch_browser():
    try:
        print("Lanzando el navegador...")
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=chrome_options)
        return driver
    except Exception as e:
        print("Error al lanzar el navegador:", str(e))
        raise e

def close_browser(driver):
    try:
        driver.quit()
    except Exception as e:
        print("Error al cerrar el navegador:", str(e))

def get_price_from_url(product_url, deny_btn_selector, price_selector, name_price_selector):
    try:
        driver = launch_browser()
        driver.get(product_url)

        content = driver.page_source
        print(content, "--------content")

        try:
            time.sleep(3)
            deny_btn = driver.find_element_by_css_selector(deny_btn_selector)
            deny_btn.click()
            content = driver.page_source
        except Exception as e:
            print("Error al hacer click en el botón de cookies:", str(e))

        time.sleep(3)
        price_element = driver.find_element_by_css_selector(price_selector)
        price = price_element.text

        close_browser(driver)

        return price
    except Exception as e:
        print("Error al obtener el precio del producto:", str(e))
        return None

