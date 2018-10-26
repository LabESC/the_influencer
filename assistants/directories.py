import os
import shutil


def verify_directory_existence(directory_path):
    return os.path.isdir(directory_path)

def create_directory_structure(directory_path):
    gexf_directory = os.path.join(directory_path, "ecosystem_gexf")
    os.mkdir(gexf_directory)
    projects_gexf_directory = os.path.join(gexf_directory, "projects_gexfs")
    os.mkdir(projects_gexf_directory)

def remove_directory_structure(directory_path):
    gexf_directory = os.path.join(directory_path, "ecosystem_gexf")
    shutil.rmtree(gexf_directory)
