# Selenium Python Automation Framework (PyTest + POM)

A modular, data-driven test automation framework developed in Python using Selenium WebDriver, PyTest, and the Page Object Model (POM) design pattern. This suite automates and validates user authentication and catalog search workflows on the TutorialsNinja e-commerce platform.

---

## Key Features

- **Page Object Model (POM):** Decouples test logic from UI locators and interactions for maintainability.
- **Data-Driven Testing (DDT):** Test suites read dynamic positive and negative datasets directly from external CSV files.
- **Centralized Configuration:** Environment base URLs, browser targets, and implicit wait thresholds are managed via `config.ini`.
- **Reusable Utility Layer:** Centralized helper modules handle CSV parsing, configuration extraction, and formatted execution logging.
- **Robust Synchronization:** Replaced fragile arbitrary pauses with custom Selenium explicit waits (`WebDriverWait` + Expected Conditions).
- **Automated Failure Capture:** PyTest hook captures full-page browser screenshots on test failure and embeds them into the execution dashboard.
- **Rich HTML Reporting:** Self-contained execution reports generated via `pytest-html`.

---

## Tech Stack & Libraries

- **Language:** Python 3.10+
- **Browser Engine:** Selenium WebDriver 4.x
- **Test Runner:** PyTest
- **Driver Management:** WebDriver Manager (automated binary resolution)
- **Reporting:** PyTest-HTML

---

## Framework Architecture

```text
├── config/
│   └── config.ini              # Centralized framework configuration
├── pages/
│   ├── __init__.py
│   ├── base_page.py            # Reusable wrapper around Selenium actions & waits
│   ├── login_page.py           # Locators and business actions for User Login
│   └── search_page.py          # Locators and business actions for Product Search
├── reports/
│   ├── report.html             # Self-contained HTML execution dashboard
│   └── screenshots/            # Automated failure screenshots
├── test_data/
│   ├── login_data.csv          # Positive and negative credentials
│   └── search_data.csv         # Valid and invalid catalog queries
├── tests/
│   ├── __init__.py
│   ├── conftest.py             # Fixtures (browser lifecycle) & PyTest reporting hooks
│   ├── test_login.py           # Data-driven test scenarios for authentication
│   └── test_search.py          # Data-driven test scenarios for product search
├── utilities/
│   ├── __init__.py
│   ├── custom_logger.py        # Centralized logging formatters
│   └── read_data.py            # Parsers for CSV files and config.ini
├── pytest.ini                  # PyTest runtime arguments and paths
├── requirements.txt            # Project dependencies
└── README.md
