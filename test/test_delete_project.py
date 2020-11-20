from model.project import Project
import random


def test_delete_project(app):
    app.session.login("administrator", "root")
    if len(app.project.get_projects_list()) == 0:
        app.project.create_project(Project(name="project-name-" + str(random.randrange(50)),
                                           status=random.choice(["development", "release"]),
                                           view_status=random.choice(["private", "public"]),
                                           description="project-description-" + str(random.randrange(50))))
    old_projects_list = app.soap.get_projects_list("administrator", "root")
    project = random.choice(old_projects_list)
    app.project.delete_project(project)
    new_projects_list = app.soap.get_projects_list("administrator", "root")
    old_projects_list.remove(project)
    assert old_projects_list == new_projects_list
