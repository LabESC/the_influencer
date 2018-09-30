

class ecosystem:

    def __init__(self):
        self.projects = []
        self.total_ecosystem_influence = 0

    def add_project_to_ecosystem(self, project):
        self.projects.append(project)
        self.total_ecosystem_influence = self.total_ecosystem_influence + project.total_project_influence