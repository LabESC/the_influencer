import os
from ecosystem_components.ecosystem import ecosystem
from ecosystem_components.project import project
from ecosystem_components.user import user
from assistants.csv_file import csv_file
from assistants.gexf_file import gexf_file
import calculators.influencer_calculator as calculator


ecosystem = ecosystem("npm")
diretorio = "C:\\Users\\faria\\Desktop\\results"

ecosystem_gexf = gexf_file()

for file in os.listdir(diretorio):
    if file == "repo-index.csv":
        pass
    else:
        project_gexf = gexf_file()
        project_name = file.split("#")[1].replace(".csv","")
        #print("project: " + project_name)
        #print(file)

        csv_info_file = csv_file()
        csv_info_file.load_informations(os.path.join(diretorio, file))

        current_project = project(project_name)
        ecosystem_project = project(project_name)

        counter = 0

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
            project_user = user(users_names.pop(), project_name, closeness.pop(), long_time.pop(), status.pop(),
                                status_project.pop(), content_value.pop(), source_learning.pop(),
                                participation_code.pop(), participation_comment.pop())

            project_user.define_project_influence_level(calculator.user_influence_level_calculation_complete(project_user, uses_closeness=False, uses_content_value=False, uses_long_time=False, uses_participation_code=False, uses_participation_comment=False, uses_project_status=False, uses_source=False, uses_status=True))
            project_user.define_ecosystem_influence_level(calculator.user_influence_level_calculation_complete(project_user, uses_closeness=False, uses_content_value=False, uses_long_time=False, uses_participation_code=False, uses_participation_comment=False, uses_project_status=False, uses_source=False, uses_status=True))

            current_project.add_user_to_project(project_user)
            ecosystem_project.add_user_to_project(project_user)

            counter += 1

        current_project.project_influence_calculation()
        ecosystem_project.project_influence_calculation()

        ecosystem.add_project_to_ecosystem(ecosystem_project)

        current_project.project_influence_standarization()

        project_gexf.create_project_gexf(current_project)

        project_gexf.write_file(os.path.join("C:\\Users\\faria\\Desktop\\gexf_sample_status", current_project.project_name))


ecosystem.ecosystem_influence_standarization()

ecosystem_gexf.create_ecosystem_gexf(ecosystem)

ecosystem_gexf.write_file(os.path.join("C:\\Users\\faria\\Desktop\\gexf_sample_status", ecosystem.ecosystem_name))

