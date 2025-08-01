BONUS_POINT_WEEKEND = 10
BONUS_POINT_WED = 10
THRE_COUNT_WEEKEND = 9
THRE_COUNT_WED = 9
THRE_POINT_SILVER = 30
THRE_POINT_GOLD = 50
GRADE_NORMAL = "NORMAL"
GRADE_SILVER = "SILVER"
GRADE_GOLD = "GOLD"
dict_people_to_id = {}
cnt_people = 0

# dat[사용자ID][요일]
dict_cnt_training = {}
dict_points = {}
dict_grade = {}
names = [""] * 100
dict_cnt_training_wed = {}
dict_cnt_training_weekend = {}

list_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
dict_add_point = {
    "monday" : 1,
    "tuesday" : 1,
    "wednesday" : 3,
    "thursday" : 1,
    "friday" : 1,
    "saturday" : 2,
    "sunday" : 2,
}


def build_statistics(name_person, day):
    global cnt_people

    if name_person not in dict_people_to_id:
        cnt_people += 1
        dict_people_to_id[name_person] = cnt_people
        names[cnt_people] = name_person
        dict_cnt_training_wed[name_person] = 0
        dict_cnt_training_weekend[name_person] = 0
        dict_points[name_person] = 0
        dict_cnt_training[name_person] = {}
        for _day in list_days:
            dict_cnt_training[name_person][_day] = 0

    if day == "wednesday":
        dict_cnt_training_wed[name_person] += 1
    elif day == "saturday" or day == "sunday":
        dict_cnt_training_weekend[name_person] += 1

    dict_cnt_training[name_person][day] += 1
    dict_points[name_person] += dict_add_point[day]

def main():
    f = None
    try:
        f = open("attendance_weekday_500.txt", encoding='utf-8')
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

    lines = f.readlines()
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 2:
            build_statistics(parts[0], parts[1])

    for id_person in range(1, cnt_people + 1):
        set_bonus_point(id_person)
        set_grade(id_person)
        show_info(id_person)

    show_removed_player()


def show_removed_player():
    print("\nRemoved player\n==============")
    for id_person in range(1, cnt_people + 1):
        name_person = names[id_person]
        if dict_cnt_training_wed[name_person] != 0 or dict_cnt_training_weekend[name_person] != 0:
            continue
        if dict_grade[name_person] is GRADE_NORMAL:
            print(name_person)


def show_info(id_person):
    name_person = names[id_person]
    print(f"NAME : {name_person}, POINT : {dict_points[name_person]}, GRADE : {dict_grade[name_person]}")


def set_grade(id_person):
    name_person = names[id_person]
    if dict_points[name_person] >= THRE_POINT_GOLD:
        dict_grade[name_person] = GRADE_GOLD
    elif dict_points[name_person] >= THRE_POINT_SILVER:
        dict_grade[name_person] = GRADE_SILVER
    else:
        dict_grade[name_person] = GRADE_NORMAL


def set_bonus_point(id_person):
    name_person = names[id_person]
    if dict_cnt_training[name_person]["wednesday"] > THRE_COUNT_WED:
        dict_points[name_person] += BONUS_POINT_WED
    if dict_cnt_training[name_person]["saturday"] + dict_cnt_training[name_person]["sunday"] > THRE_COUNT_WEEKEND:
        dict_points[name_person] += BONUS_POINT_WEEKEND


if __name__ == "__main__":
    main()