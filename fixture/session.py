class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, user, pwd):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(user)
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(pwd)
        wd.find_element_by_css_selector('input[type="submit"]').click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user")

    def is_logged_in_as(self, username):
        return self.get_logged_user() == username

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("td.login-info-left span").text

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, user, pwd):
        if self.is_logged_in():
            if self.is_logged_in_as(user):
                return
            else:
                self.logout()
        self.login(user, pwd)