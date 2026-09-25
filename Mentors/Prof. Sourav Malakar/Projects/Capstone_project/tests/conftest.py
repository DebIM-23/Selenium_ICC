import os
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utilities.read_data import read_config

@pytest.fixture(scope="function")
def driver(request):
    browser_type = read_config("common", "browser").lower()
    
    if browser_type == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
    else:
        raise ValueError(f"Browser {browser_type} is not supported.")

    driver.implicitly_wait(int(read_config("common", "implicit_wait")))
    request.cls.driver = driver if request.cls else None

    yield driver
    driver.quit()
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            reports_dir = os.path.join(os.getcwd(), "reports", "screenshots")
            os.makedirs(reports_dir, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join(reports_dir, file_name)
            driver.save_screenshot(file_path)

            if pytest_html:
                html = (
                    f'<div><img src="screenshots/{file_name}" alt="failure_screenshot" '
                    f'style="width:320px;height:240px;" onclick="window.open(this.src)" align="right"/></div>'
                )
                extras.append(pytest_html.extras.html(html))
        report.extras = extras
