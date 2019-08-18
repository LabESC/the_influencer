

class ecosystem:
    def __init__(self, ecosystem_name):
        self.ecosystem_name = ecosystem_name
        self.projects = []
        self.total_ecosystem_influence = 0.0
        self.total_ecosystem_influence_after_standarization = 0.0

    def add_project_to_ecosystem(self, project):
        if self.verify_project_already_in_ecosystem(project):
            print("Project " + project.project_name + " is already in ecosystem")
        else:
            print("Adding project " + project.project_name + " to ecosystem " + self.ecosystem_name)
            self.projects.append(project)
            self.total_ecosystem_influence = self.total_ecosystem_influence + project.total_project_influence
            self.total_ecosystem_influence_after_standarization = self.total_ecosystem_influence

    def verify_project_already_in_ecosystem(self, project):
        if project in self.projects:
            return True
        return False

    def show_ecosystem_projects(self):
        for project in self.projects:
            print(project.project_name)

    def ecosystem_influence_standarization(self):
        for project in self.projects:
            if self.total_ecosystem_influence == 0.0:
                project.total_project_influence = 0.0
            else:
                project.total_project_influence = round((project.total_project_influence / self.total_ecosystem_influence) * 100.0, 5)
            print(project.project_name + ": " + str(project.total_project_influence))

            for user in project.users:
                if self.total_ecosystem_influence == 0.0:
                    user.ecosystem_influence_level = 0.0
                else:
                    user.ecosystem_influence_level = round((user.ecosystem_influence_level / self.total_ecosystem_influence) * 100.0, 5)

        self.total_ecosystem_influence = 100.0
