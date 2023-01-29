from hw8_views import get_type_user, get_type_action, get_subject, get_student, get_score, view_journal
from hw8_models import read_file, get_data_file, update_journal
from hw8_logger import logger

# Выполнение программы
def process_func():
    students = read_file('hw8_students.txt')
    dict_students = get_data_file(students, ':', '\n')
    subjects = read_file('hw8_subjects.txt')
    dict_subjects = get_data_file(subjects, ':', '\n')
    type_user = get_type_user()
    if type_user == 1:
        work = 1
        while work == 1:
            type_action = get_type_action()
            journal = read_file('hw8_journal.txt')
            if type_action == 1:
                print(dict_students)
                student = get_student(type_user)
                print(dict_subjects)
                subject = get_subject()
                score = get_score()
                update_journal(student, subject, score, journal)
                logger([student, subject, score], 'hw8_log.csv', 'update_journal')
            elif type_action == 2:
                view_journal('hw8_journal.txt', type_user, dict_students, dict_subjects)
            elif type_action == 3:
                work = 0
    elif type_user == 2:
        id_student = get_student(type_user)
        view_journal('hw8_journal.txt', type_user, dict_students, dict_subjects, id_student)
