from selenium.webdriver.common.by import By

class AboutPage:
    def __init__(self):
        self.about_selenium = (By.TAG_NAME, "h1")