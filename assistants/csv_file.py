import csv


class csv_file:

    def __init__(self):
        self.ecosystem_name = ""
        self.project_name = ""
        self.users_information_name = []
        self.users_information_ct = []
        self.users_information_lt = []
        self.users_information_st = []
        self.users_information_stp = []
        self.users_information_cv = []
        self.users_information_sl = []
        self.users_information_pcode = []
        self.users_information_pcomm = []

    def load_informations(self, csv_file_path):
        self.ecosystem_name = csv_file_path.split("/")[-2]
        self.project_name = csv_file_path.split("/")[-1]
        with open(csv_file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimeter = ',')
            line_count = 0
            for row in csv_reader:
                self.users_information_name.append(row[0])
                self.users_information_ct.append(row[1])
                self.users_information_lt.append(row[2])
                self.users_information_st.append(row[3])
                self.users_information_stp.append(row[4])
                self.users_information_cv.append(row[5])
                self.users_information_sl.append(row[6])
                self.users_information_pcode.append(row[7])
                self.users_information_pcomm.append(row[8])
                line_count += 1

    def retrieve_ecosystem_name(self):
        return self.ecosystem_name

    def retrieve_project_name(self):
        return self.project_name

    def retrieve_user_information_name(self):
        return self.users_information_name.pop(0)

    def retrieve_user_information_ct(self):
        return self.users_information_ct.pop(0)

    def retrieve_user_information_lt(self):
        return self.users_information_lt.pop(0)

    def retrieve_user_information_st(self):
        return self.users_information_st.pop(0)

    def retrieve_user_information_stp(self):
        return self.users_information_stp.pop(0)

    def retrieve_user_information_cv(self):
        return self.users_information_cv.pop(0)

    def retrieve_user_information_sl(self):
        return self.users_information_sl.pop(0)

    def retrieve_user_information_pcode(self):
        return self.users_information_pcode.pop(0)

    def retrieve_user_information_pcomm(self):
        return self.users_information_pcomm.pop(0)

