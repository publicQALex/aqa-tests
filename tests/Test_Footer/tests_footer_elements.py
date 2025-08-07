import allure
import pytest
from base.base_test import BaseTest



@allure.feature("Footer elements")
class Test_Footer_Verify_Elements(BaseTest):

    @allure.title("Verify footer elements")
    @allure.severity("Major")
    @pytest.mark.smoke

    def test_find_footer_elements(self):
        self.main_page.open()
        self.main_page.find_footer_elements_main_page()