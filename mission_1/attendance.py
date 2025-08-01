dict_people = {}
cnt_people = 0

# dat[사용자ID][요일]
cnt_training = [[0] * 100 for _ in range(100)]
points = [0] * 100
grade = [0] * 100
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


def input2(w, wk):
    global cnt_people

    if w not in dict_people:
        cnt_people += 1
        dict_people[w] = cnt_people
        names[cnt_people] = w

    id2 = dict_people[w]
    if wk == "wednesday":
        cnt_training_wed[id2] += 1
    elif wk == "saturday" or wk == "sunday":
        cnt_training_weekend[id2] += 1

    cnt_training[id2][dict_index[wk]] += 1
    points[id2] += dict_add_point[wk]

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
        if grade[id_day] not in (1, 2) and cnt_training_wed[id_day] == 0 and cnt_training_weekend[id_day] == 0:
            print(names[id_day])


def show_info(id_person):
    print(f"NAME : {names[id_person]}, POINT : {points[id_person]}, GRADE : ", end="")
    if grade[id_person] == 1:
        print("GOLD")
    elif grade[id_person] == 2:
        print("SILVER")
    else:
        print("NORMAL")


def set_grade(id_person):
    if points[id_person] >= 50:
        grade[id_person] = 1
    elif points[id_person] >= 30:
        grade[id_person] = 2
    else:
        grade[id_person] = 0


def set_point(id_person):
    if cnt_training[id_person][ID_WED] > 9:
        points[id_person] += 10
    if cnt_training[id_person][ID_SAT] + cnt_training[id_person][ID_SUN] > 9:
        points[id_person] += 10


if __name__ == "__main__":
    input_file()