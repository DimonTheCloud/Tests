import csv
SCHOOLS = ["Křenka", "Purkyňka", "Jaroška"]
SCHOOL_MAX_STUDENTS = [3, 2, 2]
NEZARAZEN = "nezařazen"


def load_schools_data_dict(schools):
    data = {}

    for school in schools:
        filename = school + ".csv"
        school_data = []

        with open(filename, "r", encoding = 'UTF-8') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')

            next(reader)

            for row in reader:
                student = row[0]
                preference = int(row[1])
                school_data.append((student, preference))

        data[school] = school_data

    return data


def get_students_results_dict(data):
    result = {}

    for school in data:
        for student, preference in data[school]:
            if student not in result:
                result[student] = NEZARAZEN

    return result

def remove_student_from_all_schools(data, student_name):
    for school in data:
        new_list = []

        for student, preference in data[school]:
            if student != student_name:
                new_list.append((student, preference))

        data[school] = new_list

    return data


def assign_students(data, schools, capacities, results_dict):
    for preference in [1, 2]:
        is_changing = True

        while is_changing:
            is_changing = False

            for i in range(len(schools)):
                school = schools[i]
                j = 0

                while j < capacities[i] and j < len(data[school]):
                    student, pref = data[school][j]

                    if pref == preference:
                        results_dict[student] = school
                        capacities[i] -= 1
                        data = remove_student_from_all_schools(data, student)
                        is_changing = True
                        break

                    j += 1

    return results_dict, capacities






