from models.data.facultydb import faculty_signup_tbl
from models.data.faculty import Signup


class FacultySignupRepository:
    def add_item(self, item: Signup):
        try:
            faculty_signup_tbl[item.sign_id] = item
        except Exception:
            return False
        return True

    def remove_item(self, sign_id: int):
        try:
            del faculty_signup_tbl[sign_id]
        except Exception:
            return False
        return True

    def get_item(self, sign_id: int):
        try:
            account = faculty_signup_tbl[sign_id]
        except Exception:
            return None
        return account
