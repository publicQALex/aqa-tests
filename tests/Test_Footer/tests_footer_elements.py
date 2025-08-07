import allure
import pytest
import time
from base.base_test import BaseTest



@allure.feature("Footer elements")
class Test_Footer_Verify_Elements(BaseTest):

    @allure.title("Verify footer elements")
    @allure.severity("Major")
    #@allure.mark.smoke
    def test_find_footer_elements(self):

        self.projects.open()
        time.sleep(3)
        self.projects.find_footer_elements_projects()
        time.sleep(1)
        self.main_page.make_screenshot("Success projects")

        time.sleep(3)
        self.main_page.find_footer_elements_main_page()
        time.sleep(1)
        self.main_page.make_screenshot("Success main_page")

        self.job.open()
        time.sleep(3)
        self.job.find_footer_elements_job()
        time.sleep(1)
        self.main_page.make_screenshot("Success job")