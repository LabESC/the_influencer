

class project:

    def __init__(self, project_name):
        self.project_name = project_name
        self.users = []
        self.total_project_influence = 0

    def add_user_to_project(self, user):
        print("Adding user " + user.user_name + " to project " + self.project_name)
        self.users.append(user)
        self.total_project_influence = self.total_project_influence + user.project_influence_level

