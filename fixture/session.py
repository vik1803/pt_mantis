# -*- coding: utf-8 -*-
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name('username').click()
        wd.find_element_by_name('username').clear()
        wd.find_element_by_name('username').send_keys(username)
        wd.find_element_by_name('password').click()
        wd.find_element_by_name('password').clear()
        wd.find_element_by_name('password').send_keys(password)
        wd.find_element_by_css_selector('input[type="submit"]').click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text('Logout').click()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text('Logout')) > 0

    def is_logged_in_as(self, username):
        # wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("td.login-info-left span").text

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def add_project(self, name, description):
        wd = self.app.wd
        self.app.open_projects_page()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        wd.find_element_by_name('name').send_keys(name)
        wd.find_element_by_name('description').send_keys(description)
        wd.find_element_by_css_selector("input[value = 'Add Project']").click()

    def find_project_by_name(self, name):
        wd = self.app.wd
        self.app.open_projects_page()
        return wd.find_elements_by_link_text(name)

    def delete_project_by_name(self, name):
        wd = self.app.wd
        self.find_project_by_name(name)[0].click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()


