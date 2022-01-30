import csv
from .filters import main as filters

students = open("knust_students.csv", newline='')
knust_students = list(csv.reader(students))

filters.filter_knust_female_students(knust_students)
filters.filter_knust_male_students(knust_students)
filters.filter_knust_students_age_above_22(knust_students)
filters.filter_knust_students_age_below_22(knust_students)

