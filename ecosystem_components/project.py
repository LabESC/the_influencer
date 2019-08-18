

class project:

    def __init__(self, project_name):
        self.project_name = project_name
        self.users = []
        self.total_project_influence = 0.0

    def add_user_to_project(self, user):
        print("Adding user " + user.user_name + " to project " + self.project_name)
        self.users.append(user)
        self.total_project_influence = round(self.total_project_influence,5) + round(user.project_influence_level,5)

    def project_influence_calculation(self):
        influence_level = 0
        for user in self.users:
            influence_level = influence_level + user.project_influence_level

        self.total_project_influence = influence_level

    def project_influence_standarization(self):
        for user in self.users:
            if self.total_project_influence == 0.0:
                user.project_influence_level = 0.0
            else:
                user.project_influence_level = round((user.project_influence_level / self.total_project_influence) * 100.0,5)

        self.total_project_influence = 100.0
