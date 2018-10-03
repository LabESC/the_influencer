import os.path

class directories:

    def verify_directory_existence(self, directory_path):
        return os.path.isdir(directory_path)

    def create_directory_structure(self, directory_path):
        gexf_directory = os.path.join(directory_path, "gexf")
        os.mkdir(gexf_directory)
        ecosystem_gexf_directory = os.path.join(gexf_directory, "ecosystem_gexf")
        os.mkdir(ecosystem_gexf_directory)
        projects_gexf_directory = os.path.join(gexf_directory, "projects_gexfs")
        os.mkdir(projects_gexf_directory)

    def remove_directory_structure(self, directory_path):
        gexf_directory = os.path.join(directory_path, "gext")
        os.rmdir(gexf_directory)
