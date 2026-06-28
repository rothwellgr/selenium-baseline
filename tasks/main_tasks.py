from selenium.webdriver.support.ui import WebDriverWait

def _highlight(element):
    element.parent.execute_script(
        "arguments[0].style.outline = '3px solid red'", element
    )

class MainTasks:
    def __init__(self, driver):
        self.driver = driver

    def click_action(self, locator):
        print(f"  -> click {locator}", flush=True)
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(lambda _ : self.driver.find_element(*locator))
        _highlight(element)
        element.click()

    def assert_text_exists(self, locator, text):
        print(f"  -> assert text '{text}' at {locator}", flush=True)
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(lambda _ : self.driver.find_element(*locator))
        _highlight(element)
        return wait.until(lambda _ : element.text == text)