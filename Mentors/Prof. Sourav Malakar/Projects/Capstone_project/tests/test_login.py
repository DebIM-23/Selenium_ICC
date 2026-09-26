import pytest
from pages.login_page import LoginPage
from utilities.read_data import read_config, read_csv_data
from utilities.custom_logger import get_logger

logger = get_logger("TestLogin")
test_data = read_csv_data("login_data.csv")

class TestLogin:

    @pytest.mark.parametrize("data", test_data)
    def test_user_login(self, driver, data):
        logger.info(f"Executing login test with expected result: {data['expected_result']}")
        login_page = LoginPage(driver)
        
        login_page.open(read_config("common", "base_url"))
        login_page.navigate_to_login()
        login_page.login(data["email"], data["password"])

        if data["expected_result"] == "success":
            assert login_page.is_login_successful(), "Login failed for valid credentials."
            logger.info("Valid user successfully logged in.")
        else:
            warning = login_page.get_warning_message()
            assert "Warning: No match for E-Mail Address and/or Password." in warning
            logger.info("Expected warning message displayed for invalid credentials.")