import pytest
from pages.blog import Blog
from pages.company import Company
from pages.contacts_brief import Contacts_Brief
from pages.contacts import Contacts
from pages.fields import Fields
from pages.job import Job
from pages.main_page import Main_Page
from pages.projects import Projects



class BaseTest:
#аннотация типов:
    blog: Blog
    company: Company
    contacts_brief: Contacts_Brief
    contacts: Contacts
    fields: Fields
    job: Job
    main_page: Main_Page
    projects: Projects


    #Мультистраничный доступ
    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.main_page = Main_Page(driver)
        request.cls.blog = Blog(driver)
        request.cls.company = Company(driver)
        request.cls.contacts_brief = Contacts_Brief(driver)
        request.cls.fields = Fields(driver)
        request.cls.job = Job(driver)
        request.cls.projects = Projects(driver)
        request.cls.contacts = Contacts(driver)

