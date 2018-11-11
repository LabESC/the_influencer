import os
from ecosystem_components.ecosystem import ecosystem
from ecosystem_components.project import project
from ecosystem_components.user import user
from assistants.csv_file import csv_file


ecosystem = ecosystem("npm")
diretorio = "C:\\Users\\faria\\Desktop\\results"

for file in os.listdir(diretorio):
    if file == "repo-index.csv":
        pass
    else:
        project_name = file.split("#")[1].replace(".csv","")
        print("project: " + project_name)
        print(file)

        csv_info_file = csv_file()
        csv_info_file.load_informations(os.path.join(diretorio, file))

        ecosystem_project = project(project_name)

        counter = 0
        print(csv_info_file.retrieve_quantity_of_users())
        users_names = csv_info_file.retrieve_user_information_name()
        closeness = csv_info_file.retrieve_user_information_ct()
        long_time = csv_info_file.retrieve_user_information_lt()
        status = csv_info_file.retrieve_user_information_st()
        status_project = csv_info_file.retrieve_user_information_stp()
        content_value = csv_info_file.retrieve_user_information_cv()
        source_learning = csv_info_file.retrieve_user_information_sl()
        participation_code = csv_info_file.retrieve_user_information_pcode()
        participation_comment = csv_info_file.retrieve_user_information_pcomm()
        while counter < csv_info_file.retrieve_quantity_of_users():
            print(users_names.pop())
            counter += 1

        print("Adding project " + project_name + " to ecosystem npm")
        ecosystem.add_project_to_ecosystem(ecosystem_project)


