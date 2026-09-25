import pytest
from pages.search_page import SearchPage
from utilities.read_data import read_config, read_csv_data
from utilities.custom_logger import get_logger

logger = get_logger("TestSearch")
test_data = read_csv_data("search_data.csv")

class TestSearch:

    @pytest.mark.parametrize("data", test_data)
    def test_search_functionality(self, driver, data):
        logger.info(f"Executing search test for query: {data['search_term']}")
        search_page = SearchPage(driver)

        search_page.open(read_config("common", "base_url"))
        search_page.search_product(data["search_term"])

        if data["expected_result"] == "success":
            results = search_page.get_search_results_titles()
            assert any(data["product_name"] in item for item in results), (
                f"Expected product {data['product_name']} not found in search results."
            )
            logger.info(f"Product '{data['product_name']}' found successfully.")
        else:
            assert search_page.has_no_product_message(), (
                "No-product message was not shown for non-existent item."
            )
            logger.info("Non-existent product handled cleanly.")