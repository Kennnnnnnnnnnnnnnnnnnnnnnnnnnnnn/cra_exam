from mission_2.person import Person


# dat[사용자ID][요일]
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
        person = get_person(name)
        person.set_point()
        person.show_info()

    show_removed_player()
    destroy_data()


def count_training(lines):
    for line in lines:
        parts = line.strip().split()
        if len(parts) != 2:
            continue
        get_person(parts[0]).update_count(parts[1])

def init_data(lines):
    for line in lines:
        parts = line.strip().split()
        if len(parts) != 2:
            continue
        if parts[0] in list_names:
            continue
        list_people.append(Person(parts[0]))
        list_names.append(parts[0])


def show_removed_player():
    print("\nRemoved player\n==============")
    for name_person in list_names:
        person = get_person(name_person)
        if person.cnt_training_wed != 0 or person.cnt_training_weekend != 0:
            continue
        if person.grade is GRADE_NORMAL:
            print(name_person)


if __name__ == "__main__":
    main()