from suds.client import Client
from suds import WebFault
from fixture.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.base_url + "api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self, username, password):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        client.service.mc_projects_get_user_accessible(username, password)
        try:
            projects_data = client.service.mc_projects_get_user_accessible(username, password)
            projects_list = []
            for itm in projects_data:
                project = Project(id=itm.id, name=itm.name, status=itm.status.name, view_status=itm.view_state.name,
                                  description=itm.description)
                projects_list.append(project)
            return projects_list
        except WebFault:
            return False
