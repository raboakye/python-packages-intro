import csv


def filter_knust_female_students(students, save_to_file="knust_female_students.csv"):
    knust_female_students_file = open(save_to_file, 'w')
    csv_writer = csv.writer(knust_female_students_file)
    female_students = list(filter(lambda student: student[2] == 'Female', students))

    csv_writer.writerows(female_students)

    knust_female_students_file.close()


def filter_knust_male_students(students, save_to_file = 'knust_male_students.csv'):
    knust_male_students_file = open(save_to_file, 'w')
    csv_writer = csv.writer(knust_male_students_file)
    male_students = list(filter(lambda student: student[2] == 'Male', students))

    csv_writer.writerows(male_students)
    knust_male_students_file.close()


def filter_knust_students_age_above_22(students, save_to_file = 'knust_students_age_above_22.csv'):
    students_age_above_22_file = open(save_to_file, 'w')
    csv_writer = csv.writer(students_age_above_22_file)
    students_above_22 = list(filter(lambda student: student[3] > '22', students))

    csv_writer.writerows(students_above_22)
    students_age_above_22_file.close()


def filter_knust_students_age_below_22(students, save_to_file='knust_students_age_below_22.csv'):
    students_age_below_22_file = open(save_to_file, 'w')
    csv_writer = csv.writer(students_age_below_22_file)
    students_below_22 = list(filter(lambda student: student[3] > '22', students))

    csv_writer.writerows(students_below_22)
    students_age_below_22_file.close()