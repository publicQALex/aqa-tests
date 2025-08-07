import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Contacts_Brief(BasePage):
    PAGE_URL = Links.CONTACTS_BRIEF
    footer_class = (By.XPATH, "/html/body/main/footer")
    #self.driver.execute_script("arguments[0].scrollIntoView(true);", footer_class)

    @allure.step("Go to Contacts#Brief' page")
    def find_footer_elements_contacts_brief(self):
        self.wait.until(EC.visibility_of_element_located(self.footer_class))
        footer_missing_elements = []
        elements = {
            #На случай если вдруг на разных страницах разное содержание футера, можно было бы вынести в base_page.py
            "footer_class": "/html/body/main/footer",
            "footer_button_new_project": "/html/body/main/footer/div[1]/button",
            "footer_social_button_be": "/html/body/main/footer/div[1]/div[1]/a[1]",
            "footer_social_button_dp": "/html/body/main/footer/div[1]/div[1]/a[2]",
            "footer_social_button_tg": "/html/body/main/footer/div[1]/div[1]/a[3]",
            "footer_social_button_vk": "/html/body/main/footer/div[1]/div[1]/a[4]",
            "footer_logo": "/html/body/main/footer/div[1]/svg",
            "footer_contacts_email": "/html/body/main/footer/div[1]/div[3]/a[1]",
            "footer_contacts_phone_number": "/html/body/main/footer/div[1]/div[3]/a[2]",
            "footer_contacts_telegram_link": "/html/body/main/footer/div[1]/div[2]/a",
            "footer_pdf_presentation": "/html/body/main/footer/div[1]/div[4]/div/a[1]",
            "footer_pitch_presentation": "/html/body/main/footer/div[1]/div[4]/div/a[2]",
            "footer_privacy_policy": "/html/body/main/footer/div[2]/a"
        }
        for name, xpath in elements.items():
            try:
                setattr(self, name, self.driver.find_element(By.XPATH, xpath))
            except NoSuchElementException:
                footer_missing_elements.append(f"Элемент {name} отсутствует")
        if footer_missing_elements:
            return "\n".join(footer_missing_elements)
        return "Все элементы найдены"