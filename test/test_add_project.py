from model.project import Project
import random


def test_create_project(app):
    project = Project(name="project-name-" + str(random.randrange(50)),
                      status=random.choice(["development", "release"]),
                      view_status=random.choice(["private", "public"]),
                      description="project-description-" + str(random.randrange(50)))
    app.session.login("administrator", "root")
    old_projects_list = app.project.get_projects_lst()
    app.project.create_project(project)
    new_projects_list = app.project.get_projects_lst()
    old_projects_list.append(project)
    assert sorted(old_projects_list, key=Project.id_or_max) == sorted(new_projects_list, key=Project.id_or_max)