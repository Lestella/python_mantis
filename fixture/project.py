from model.project import Project
from selenium.webdriver.support.ui import Select



class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("manage_proj_page.php")):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_option_value(self, field_name, option):
        wd = self.app.wd
        if option is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(option)

    def fill_project_form(self, project):
        self.change_field_value("name", project.name)
        self.change_option_value("status", project.status)
        self.change_option_value("view_state", project.viewstatus)
        self.change_field_value("description", project.description)

    def get_projects_lst(self):
        wd = self.app.wd
        self.open_project_page()
        proj_table = wd.find_elements_by_tag_name("table")[2]
        proj_rows = proj_table.find_elements_by_tag_name("tr")[2:]
        get_proj_lst = []
        for element in proj_rows:
            cells = element.find_elements_by_tag_name("td")
            id_ = cells[0].find_element_by_tag_name("a").get_attribute("href").replace("http://localhost/mantis/manage_proj_edit_page.php?project_id=", "")
            name = cells[0].find_element_by_tag_name("a").text
            status = cells[1].text
            view_status = cells[3].text
            description = cells[4].text
            get_proj_lst.append(Project(id=id_, name=name, status=status, view_status=view_status, description=description))
        return get_proj_lst

    def create_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath("//input[@type='submit' and @value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def delete_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_css_selector("a[href='manage_proj_edit_page.php?project_id=%s" % project.id).click()
        wd.find_element_by_xpath("//input[@type='submit' and @value='Delete Project']").click()
        if wd.current_url.endswith("/manage_proj_delete.php"):
            wd.find_element_by_xpath("//input[@type='submit' and @value='Delete Project']").click()
        self.back_to_the_main_page()

    def back_to_the_main_page(self):
        wd = self.app.wd
        wd.get("http://localhost/mantis/my_view_page.php")