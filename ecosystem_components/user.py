

class user:

    def __init__(self):
        self.ecosystem_influence_level = 0
        self.project_influence_level = 0
        self.user_cl_influence_metric = 0
        self.user_lt_influence_metric = 0
        self.user_st_influence_metric = 0
        self.user_stp_influence_metric = 0
        self.user_cv_influence_metric = 0
        self.user_sl_influence_metric = 0
        self.user_pcode_influence_metric = 0
        self.user_pcomm_influence_metric = 0
        self.user_name = ""
        self.user_project = ""

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

