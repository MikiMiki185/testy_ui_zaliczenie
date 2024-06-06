import string
import random
from selenium.webdriver.common.by import By


class Project:

    button_add_project = (By.CSS_SELECTOR, '.button_link[href="http://demo.testarena.pl/administration/add_project"]')
    name_project = (By.ID, 'name')
    description = (By.ID, 'description')
    prefix = (By.ID, 'prefix')
    save_button = (By.ID, 'save')
    project_button = (By.CSS_SELECTOR, '.item2')

    def __init__(self, browser):
        self.browser = browser

    def add_project(self):
        return self.browser.find_element(*self.button_add_project).click()

    def generate_random_string(length=10):
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string

    random_project_name = generate_random_string()
    random_prefix = generate_random_string(3)
    random_description = generate_random_string()

    def add_name_of_project(self):
        self.browser.find_element(*self.name_project).send_keys(self.random_project_name)
        self.browser.find_element(*self.prefix).send_keys(self.random_prefix)
        self.browser.find_element(*self.description).send_keys(self.random_description)
        return self

    def click_add_project(self):
        return self.browser.find_element(*self.button_add_project).click()

    def save_new_project(self):
        self.browser.find_element(*self.save_button).click()

    def click_in_button_project(self):
        return self.browser.find_element(*self.project_button).click()

    search_filed = (By.ID, 'search')
    search_button = (By.ID, 'j_searchButton')
    added_project = (By.CSS_SELECTOR, 'tr>td>a')

    def search_added_project(self):
        self.browser.find_element(*self.search_filed).send_keys(self.random_project_name)
        self.browser.find_element(*self.search_button).click()

    def return_name_of_project(self):
        return self.browser.find_element(*self.added_project).text
