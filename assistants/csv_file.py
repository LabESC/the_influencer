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
        self.quantity_users = 0

    def load_informations(self, csv_file_path):
        with open(csv_file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ';')
            line_count = 0
            for row in csv_reader:
                self.users_information_name.append(row[0])
                if row[1] == "OWNER":
                    self.users_information_ct.append(row[2])
                    self.users_information_lt.append(row[3])
                    self.users_information_st.append(row[4])
                    self.users_information_stp.append(row[5])
                    self.users_information_cv.append(row[6])
                    self.users_information_sl.append(row[7])
                    self.users_information_pcode.append(row[8])
                    self.users_information_pcomm.append(row[9])
                else:
                    self.users_information_ct.append("0")
                    self.users_information_lt.append(row[2])
                    self.users_information_st.append(row[3])
                    self.users_information_stp.append(row[4])
                    self.users_information_cv.append(row[5])
                    self.users_information_sl.append(row[6])
                    self.users_information_pcode.append(row[7])
                    self.users_information_pcomm.append(row[8])
                line_count += 1
            self.quantity_users = line_count

    def retrieve_ecosystem_name(self):
        return self.ecosystem_name

    def retrieve_project_name(self):
        return self.project_name

    def retrieve_user_information_name(self):
        return self.users_information_name

    def retrieve_user_information_ct(self):
        return self.users_information_ct

    def retrieve_user_information_lt(self):
        return self.users_information_lt

    def retrieve_user_information_st(self):
        return self.users_information_st

    def retrieve_user_information_stp(self):
        return self.users_information_stp

    def retrieve_user_information_cv(self):
        return self.users_information_cv

    def retrieve_user_information_sl(self):
        return self.users_information_sl

    def retrieve_user_information_pcode(self):
        return self.users_information_pcode

    def retrieve_user_information_pcomm(self):
        return self.users_information_pcomm

    def retrieve_quantity_of_users(self):
        return self.quantity_users

