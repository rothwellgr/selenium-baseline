import pytest
from pages.main_page import MainPage
from pages.about_page import AboutPage
from pages.about_dropdown_menu import AboutDropdownMenu
from tasks.main_tasks import MainTasks

main_page = MainPage()
about_page = AboutPage()
about_dropdown_menu = AboutDropdownMenu()

class TestAboutPage:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.task = MainTasks(driver)

    def test_page_title(self):
        self.driver.get("https://selenium.dev")
        assert "Selenium" in self.driver.title

    def test_about_page_renders(self):
        self.driver.get("https://selenium.dev")
        self.task.click_action(main_page.about_menu)
        self.task.click_action(about_dropdown_menu.about_selenium)
        result = self.task.assert_text_exists(about_page.about_selenium, "About Selenium")
        assert result