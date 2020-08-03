import datetime

project_name = datetime.datetime.now().strftime("%f")


def test_add_project(app):
    project_description = 'Description of the' + project_name
    app.session.login('administrator', 'root')
    app.session.add_project(project_name, project_description)
    assert len(app.session.find_project_by_name(project_name)) == 1
    app.session.logout()


def test_delete_project(app):
    app.session.login('administrator', 'root')
    app.session.delete_project_by_name(project_name)
    assert len(app.session.find_project_by_name(project_name)) == 0
    app.session.logout()
