import allure
import time
from base.base_test import BaseTest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


@allure.feature("Footer elements")
class Test_Footer_Verify_Elements(BaseTest):

    @allure.title("Verify footer elements")
    @allure.severity("Major")
    #@allure.mark.smoke 

    def test_find_footer_elements(self):
        
        self.projects.open()
        time.sleep(4)   #Конечно было бы лучше заменить фикс.паузы на явные ожидания, например:   Но я столкнулся с некоторыми трудностями и не сделал.
                        #WebDriverWait(self.driver, 10).until(
                                        #EC.visibility_of_element_located((By.XPATH, "//footer"))
        self.projects.find_footer_elements_projects()
        time.sleep(1)
        self.projects.make_screenshot("Success projects")

        self.main_page.open()
        time.sleep(4)
        self.main_page.find_footer_elements_main_page()
        time.sleep(1)
        self.main_page.make_screenshot("Success main_page")

        self.job.open()
        time.sleep(4)
        self.job.find_footer_elements_job()
        time.sleep(1)
        self.job.make_screenshot("Success job")

        self.fields.open()
        time.sleep(4)
        self.fields.find_footer_elements_fields()
        time.sleep(1)
        self.fields.make_screenshot("Success fields")

        self.contacts.open()
        time.sleep(4)
        self.contacts.find_footer_elements_contacts()
        time.sleep(1)
        self.contacts.make_screenshot("Success contacts")

        self.contacts_brief.open()
        time.sleep(4)
        self.contacts_brief.find_footer_elements_contacts_brief()
        time.sleep(1)
        self.contacts_brief.make_screenshot("Success contacts_brief")

        self.company.open()
        time.sleep(4)
        self.company.find_footer_elements_company()
        time.sleep(1)
        self.company.make_screenshot("Success company")

        self.blog.open()
        time.sleep(4)
        self.blog.find_footer_elements_blog()
        time.sleep(1)
        self.blog.make_screenshot("Success blog")