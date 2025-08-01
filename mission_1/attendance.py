BONUS_POINT_WEEKEND = 10
BONUS_POINT_WED = 10
THRE_COUNT_WEEKEND = 9
THRE_COUNT_WED = 9
THRE_POINT_SILVER = 30
THRE_POINT_GOLD = 50
GRADE_NORMAL = "NORMAL"
GRADE_SILVER = "SILVER"
GRADE_GOLD = "GOLD"
dict_people = {}
cnt_people = 0

# dat[사용자ID][요일]
cnt_training = [[0] * 100 for _ in range(100)]
points = [0] * 100
grade = [""] * 100
names = [''] * 100
cnt_training_wed = [0] * 100
cnt_training_weekend = [0] * 100

ID_MON = 0
ID_TUE = 1
ID_WED = 2
ID_THU = 3
ID_FRI = 4
ID_SAT = 5
ID_SUN = 6


dict_index = {
    "monday" : ID_MON,
    "tuesday" : ID_TUE,
    "wednesday" : ID_WED,
    "thursday" : ID_THU,
    "friday" : ID_FRI,
    "saturday" : ID_SAT,
    "sunday" : ID_SUN,
}

dict_add_point = {
    "monday" : 1,
    "tuesday" : 1,
    "wednesday" : 3,
    "thursday" : 1,
    "friday" : 1,
    "saturday" : 2,
    "sunday" : 2,
}


def input2(name_person, day):
    global cnt_people

    if name_person not in dict_people:
        cnt_people += 1
        dict_people[name_person] = cnt_people
        names[cnt_people] = name_person

    id_person = dict_people[name_person]
    if day == "wednesday":
        cnt_training_wed[id_person] += 1
    elif day == "saturday" or day == "sunday":
        cnt_training_weekend[id_person] += 1

    cnt_training[id_person][dict_index[day]] += 1
    points[id_person] += dict_add_point[day]

def input_file():
    try:
        with open("attendance_weekday_500.txt", encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split()
                if len(parts) == 2:
                    input2(parts[0], parts[1])

        for id_person in range(1, cnt_people + 1):
            set_point(id_person)
            set_grade(id_person)
            show_info(id_person)

        show_removed_player()

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


def show_removed_player():
    print("\nRemoved player")
    print("==============")
    for id_day in range(1, cnt_people + 1):
        if cnt_training_wed[id_day] != 0 or cnt_training_weekend[id_day] != 0:
            continue
        if grade[id_day] is GRADE_NORMAL:
            print(names[id_day])


def show_info(id_person):
    print(f"NAME : {names[id_person]}, POINT : {points[id_person]}, GRADE : {grade[id_person]}")


def set_grade(id_person):
    if points[id_person] >= THRE_POINT_GOLD:
        grade[id_person] = GRADE_GOLD
    elif points[id_person] >= THRE_POINT_SILVER:
        grade[id_person] = GRADE_SILVER
    else:
        grade[id_person] = GRADE_NORMAL


def set_point(id_person):
    if cnt_training[id_person][ID_WED] > THRE_COUNT_WED:
        points[id_person] += BONUS_POINT_WED
    if cnt_training[id_person][ID_SAT] + cnt_training[id_person][ID_SUN] > THRE_COUNT_WEEKEND:
        points[id_person] += BONUS_POINT_WEEKEND


if __name__ == "__main__":
    input_file()