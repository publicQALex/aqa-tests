import allure
import pytest
from base.base_page import Footer
from base.base_test import BaseTest



@allure.feature("Footer elements")
class Test_Footer_Verify_Elements(BaseTest):

    @allure.title("Verify footer elements")
    @allure.severity("Major")
    @pytest.mark.smoke

    