

class user:

    def __init__(self, name, project_name, closeness, long_time, status, status_project, content_value, source_learning,
                 participation_code, participation_comments):
        self.ecosystem_influence_level = 0
        self.project_influence_level = 0
        self.user_name = name
        self.user_project = project_name
        self.user_cl_influence_metric = closeness
        self.user_lt_influence_metric = long_time
        self.user_st_influence_metric = status
        self.user_stp_influence_metric = status_project
        self.user_cv_influence_metric = content_value
        self.user_sl_influence_metric = source_learning
        self.user_pcode_influence_metric = participation_code
        self.user_pcomm_influence_metric = participation_comments



    def define_ecosystem_influence_level(self, ecosystem_influence_level):
        self.ecosystem_influence_level = ecosystem_influence_level

    def define_project_influence_level(self, project_influence_level):
        self.project_influence_level = project_influence_level

    def define_user_cl_influence_metric(self, user_cl_influence_metric):
        self.user_cl_influence_metric = user_cl_influence_metric

    def define_user_lt_influence_metric(self, user_lt_influence_metric):
        self.user_lt_influence_metric = user_lt_influence_metric

    def define_user_st_influence_metric(self, user_st_influence_metric):
        self.user_st_influence_metric = user_st_influence_metric

    def define_user_stp_influence_metric(self, user_stp_influence_metric):
        self.user_stp_influence_metric = user_stp_influence_metric

    def define_user_cv_influence_metric(self, user_cv_influence_metric):
        self.user_cv_influence_metric = user_cv_influence_metric

    def define_user_sl_influence_metric(self, user_sl_influence_metric):
        self.user_sl_influence_metric = user_sl_influence_metric

    def define_user_pcode_influence_metric(self, user_pcode_influence_metric):
        self.user_pcode_influence_metric = user_pcode_influence_metric

    def define_user_pcomm_influence_metric(self, user_pcomm_influence_metric):
        self.user_pcomm_influence_metric = user_pcomm_influence_metric

    def define_user_name(self, user_name):
        self.user_name = user_name

    def define_user_project(self, user_project):
        self.user_project = user_project

    def update_ecosystem_influence_level(self):
        self.ecosystem_influence_level = self.ecosystem_influence_level + self.project_influence_level

