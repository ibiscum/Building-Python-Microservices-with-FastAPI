from typing import Dict, Any

from fastapi.encoders import jsonable_encoder
from models.data.students import Student
from models.data.studentsdb import students_tbl
# from collections import namedtuple


class StudentRepository:
    def insert_student(self, student: Student) -> bool:
        try:
            students_tbl[student.stud_id] = student
        except Exception as e:
            print(e)
            return False
        return True

    def update_student(self, stud_id: int, details: Dict[str, Any]) -> bool:
        try:
            profile = students_tbl[stud_id]
            profile_enc = jsonable_encoder(profile)
            profile_dict = dict(profile_enc)
            profile_dict.update(details)
            students_tbl[stud_id] = Student(**profile_dict)
        except Exception as e:
            print(e)
            return False
        return True

    def delete_student(self, user_id: int) -> bool:
        try:
            del students_tbl[user_id]
        except Exception as e:
            print(e)
            return False
        return True

    def get_all_students(self):
        return students_tbl
