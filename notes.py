import random
import pandas
# nums = [1, 2, 3, 4, 5]
# new_list = [round(item ** 2, 2) for item in nums]
# print(new_list)
#
# name = 'joshua'
# new_list = [letter for letter in name]
# print(new_list)
#
# numbers = [n for n in range(1, 20)]
# even_nums = [i for i in numbers if i % 2 != 0]
# print(even_nums)

# names = ['Alex', 'Beth', 'Carolina', 'Dave', 'Eleanor', 'Freddie']
# student_scores = {student: random.randint(1, 100) for student in names}
# print(student_scores)
# passed_students = {student: score for (student, score) in student_scores.items() if score > 60}
# print(passed_students)
student_dict = {
    'student': ['Angela', 'James', 'Lily'],
    'score': [56, 76, 98]
}

student_df = pandas.DataFrame(student_dict)
# print(student_df)

# for (key, value) in student_df.items():
#     print(key)
for (index, row) in student_df.iterrows():
    print(row.score)
