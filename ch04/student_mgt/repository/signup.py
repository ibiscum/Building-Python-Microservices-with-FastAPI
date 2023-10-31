from student_mgt.models.data.studentsdb import stud_signup_tbl
from student_mgt.models.data.students import Signup


class StudentSignupRepository:
    def insert_item(self, item: Signup):
        try:
            stud_signup_tbl[item.sign_id] = item
        except Exception:
            return False
        return True

    def delete_item(self, sign_id: int):
        try:
            del stud_signup_tbl[sign_id]
        except Exception:
            return False
        return True

    def get_item(self, sign_id: int):
        try:
            account = stud_signup_tbl[sign_id]
        except Exception:
            return None
        return account
