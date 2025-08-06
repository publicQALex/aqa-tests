import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class Company(BasePage):
    PAGE_URL = Links.COMPANY

    @allure.step("Go to 'Company' page")
    def find_footer(self):
        footer_class = self.driver.find_element(By.XPATH, "/html/body/main/footer")
        footer_button_new_project = self.driver.find_element(By.XPATH, "/html/body/main/footer/div[1]/button")
        footer_social_button_be = self.driver.find_element(By.XPATH, "/html/body/main/footer/div[1]/div[1]/a[1]")
        footer_social_button_dp = self.driver.find_element(By.XPATH, "/html/body/main/footer/div[1]/div[1]/a[2]")
        footer_social_button_tg = self.driver.find_element(By.XPATH, "/html/body/main/footer/div[1]/div[1]/a[3]")
        footer_social_button_vk = self.driver.find_element(By.XPATH, "/html/body/main/footer/div[1]/div[1]/a[4]")
        footer_logo = self.driver.find_element(By.XPATH, "/html/body/main/footer/div[1]/svg")
        footer_contacts_email = self.driver.find_element(By.XPATH, "/html/body/main/footer/div[1]/div[3]/a[1]")
        footer_contacts_phone_number = self.driver.find_element(By.XPATH, "/html/body/main/footer/div[1]/div[3]/a[2]")
        footer_contacts_telegram_link = self.driver.find_element(By.XPATH, "/html/body/main/footer/div[1]/div[2]/a")
        footer_pdf_presentation = self.driver.find_element(By.XPATH, "/html/body/main/footer/div[1]/div[4]/div/a[1]")
        footer_pitch_presentation = self.driver.find_element(By.XPATH, "/html/body/main/footer/div[1]/div[4]/div/a[2]")
        footer_privacy_policy = self.driver.find_element(By.XPATH, "/html/body/main/footer/div[2]/a")