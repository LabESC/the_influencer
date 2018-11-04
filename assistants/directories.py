import os
import shutil


def verify_directory_existence(directory_path):
    return os.path.isdir(directory_path)

def verify_file_existence(file_path):
    return os.path.isfile(file_path)

def create_directory_structure(directory_path):
    gexf_directory = os.path.join(directory_path, "ecosystem_gexf")
    os.mkdir(gexf_directory)
    projects_gexf_directory = os.path.join(gexf_directory, "projects_gexfs")
    os.mkdir(projects_gexf_directory)

def remove_directory_structure(directory_path):
    shutil.rmtree(directory_path)

def verify_csv_files_existence_in_path(directory_path):
    for file in os.listdir(directory_path):
        if file.endswith(".csv"):
            return True
    return False

def get_gexf_directory_files_to_vector(directory_path):
    vector = []
    for file in os.listdir(directory_path):
        if file.endswith(".gexf"):
            vector.append(file)
    return vector
