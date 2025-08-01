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
list_names = []
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


def main():
    f = None
    try:
        f = open("attendance_weekday_500.txt", encoding='utf-8')
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
    lines = f.readlines()

    init_data(lines)
    count_training(lines)

    set_point()

    for name in list_names:
        set_bonus_point_per_person(name)
        set_grade_per_person(name)
        show_info_per_person(name)

    show_removed_player()


def set_point():
    for name in list_names:
        if name == "":
            continue
        for day in list_days:
            dict_points[name] += dict_add_point[day] * dict_cnt_training[name][day]

def count_training_per_line(name_person, day):
    if day == "wednesday":
        dict_cnt_training_wed[name_person] += 1
    elif day == "saturday" or day == "sunday":
        dict_cnt_training_weekend[name_person] += 1

    dict_cnt_training[name_person][day] += 1

def count_training(lines):
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 2:
            count_training_per_line(parts[0], parts[1])

def init_data_in_line(name_person, day):
    global cnt_people

    if name_person not in dict_people_to_id:
        cnt_people += 1
        dict_people_to_id[name_person] = cnt_people
        list_names.append(name_person)
        dict_cnt_training_wed[name_person] = 0
        dict_cnt_training_weekend[name_person] = 0
        dict_points[name_person] = 0
        dict_cnt_training[name_person] = {}
        for _day in list_days:
            dict_cnt_training[name_person][_day] = 0

def init_data(lines):
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 2:
            init_data_in_line(parts[0], parts[1])


def show_removed_player():
    print("\nRemoved player\n==============")
    for name_person in list_names:
        if dict_cnt_training_wed[name_person] != 0 or dict_cnt_training_weekend[name_person] != 0:
            continue
        if dict_grade[name_person] is GRADE_NORMAL:
            print(name_person)


def show_info_per_person(name_person):
    print(f"NAME : {name_person}, POINT : {dict_points[name_person]}, GRADE : {dict_grade[name_person]}")


def set_grade_per_person(name_person):
    if dict_points[name_person] >= THRE_POINT_GOLD:
        dict_grade[name_person] = GRADE_GOLD
    elif dict_points[name_person] >= THRE_POINT_SILVER:
        dict_grade[name_person] = GRADE_SILVER
    else:
        dict_grade[name_person] = GRADE_NORMAL


def set_bonus_point_per_person(name_person):
    if dict_cnt_training[name_person]["wednesday"] > THRE_COUNT_WED:
        dict_points[name_person] += BONUS_POINT_WED
    if dict_cnt_training[name_person]["saturday"] + dict_cnt_training[name_person]["sunday"] > THRE_COUNT_WEEKEND:
        dict_points[name_person] += BONUS_POINT_WEEKEND


if __name__ == "__main__":
    main()