from mission_2.person import Person


# dat[사용자ID][요일]
dict_grade = {}
list_names = []
list_people = []
GRADE_NORMAL = "NORMAL"


def destroy_data():
    del list_names[:]
    del list_people[:]


def get_person(name_person):
    person = None
    for person in list_people:
        if name_person == person.name:
            break
    return person

def main():
    f = None
    try:
        f = open("attendance_weekday_500.txt", encoding='utf-8')
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
    lines = f.readlines()

    init_data(lines)
    count_training(lines)

    for name in list_names:
        get_person(name).set_point()
        show_info_per_person(name)

    show_removed_player()
    destroy_data()



def count_training_per_line(name_person, day):
    get_person(name_person).update_count(day)

def count_training(lines):
    for line in lines:
        parts = line.strip().split()
        if len(parts) != 2:
            continue
        count_training_per_line(parts[0], parts[1])


def init_data_in_line(name_person):
    if name_person in list_names:
        return

    list_people.append(Person(name_person))

    list_names.append(name_person)

def init_data(lines):
    for line in lines:
        parts = line.strip().split()
        if len(parts) != 2:
            continue
        init_data_in_line(parts[0])


def show_removed_player():
    print("\nRemoved player\n==============")
    for name_person in list_names:
        person = get_person(name_person)
        if person.cnt_training_wed != 0 or person.cnt_training_weekend != 0:
            continue
        if person.grade is GRADE_NORMAL:
            print(name_person)


def show_info_per_person(name_person):
    person = get_person(name_person)
    print(f"NAME : {name_person}, POINT : {person.point}, GRADE : {person.grade}")


if __name__ == "__main__":
    main()