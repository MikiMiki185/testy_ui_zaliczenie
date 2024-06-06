from pages.home_page import HomePage
from fixtures.testarena.login import browser
from fixtures.chrome import chrome_browser
from pages.projects import Project


def test_add_new_project(browser):
    home_page = HomePage(browser)
    home_page.click_admin_panel()

    project_page = Project(browser)
    project_page.add_project()
    project_page.add_name_of_project()
    project_page.save_new_project()

    project_page.click_in_button_project()
    project_page.search_added_project()

    assert project_page.random_project_name == project_page.return_name_of_project()