import os
import django
from datetime import date



# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
# Run and print your queries

from main_app.models import Student
from django.db.models import Value
from django.db.models.functions import Concat, Substr, StrIndex

def add_students():
    Student.objects.create(
        student_id= 'FC5204',
        first_name = 'John',
        last_name = 'Doe',
        birth_date= '1995-05-15',
        email= 'john.doe@university.com'
    )

    student_1 = Student(
        student_id= 'FE0054',
        first_name= 'Jane',
        last_name= 'Smith',
        email= 'jane.smith@university.com'
    )
    student_1.save()

    student_2 = Student()
    student_2.student_id = 'FH2014'
    student_2.first_name = 'Alice'
    student_2.last_name = 'Johnson'
    student_2.birth_date = '1998-02-10'
    student_2.email = 'alice.johnson@university.com'
    student_2.save()

    student_4 = Student.objects.create(
        student_id= 'FH2015',
        first_name= 'Bob',
        last_name= 'Wilson',
        birth_date= '1996-11-25',
        email= 'bob.wilson@university.com'
    )


def get_students_info():
    return '\n'.join(f"Student №{s.student_id}: {s.first_name} {s.last_name}; Email: {s.email}" for s in Student.objects.all())

def update_students_emails():
    # all_students = Student.objects.all()
    # for s in all_students:
    #     s.email = s.email.replace(s.email.split('@')[1], 'uni-students.com')
    #     s.save()
    Student.objects.update(
        email= Concat(
            Substr('email', 1, StrIndex('email', Value('@'))),
            Value('uni-students.com')
        )
    )

def truncate_students():
    Student.objects.all().delete()


