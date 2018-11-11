

class ecosystem:
    def __init__(self, ecosystem_name):
        self.ecosystem_name = ecosystem_name
        self.projects = []
        self.total_ecosystem_influence = 0

    def add_project_to_ecosystem(self, project):
        if self.verify_project_already_in_ecosystem(project):
            print("Project " + project.project_name + " is already in ecosystem")
        else:
            print("Adding project " + project.project_name + " to ecosystem " + self.ecosystem_name)
            self.projects.append(project)
            self.total_ecosystem_influence = self.total_ecosystem_influence + project.total_project_influence

    def verify_project_already_in_ecosystem(self, project):
        if project in self.projects:
            return True
        return False

    def show_ecosystem_projects(self):
        for project in self.projects:
            print(project.project_name)