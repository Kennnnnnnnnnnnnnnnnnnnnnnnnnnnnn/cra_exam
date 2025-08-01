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


def get_lines(name):
    f = None
    try:
        f = open(name, encoding='utf-8')
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
    lines = f.readlines()
    return lines

def main():
    lines = get_lines("attendance_weekday_500.txt")

    list_lazy = []
    init_data(lines)
    count_training(lines)

    for name in list_names:
        person = get_person(name)
        person.set_point()
        person.show_info()
        if person.is_lazy():
            list_lazy.append(name)

    print("\nRemoved player\n==============")
    for name_person in list_lazy:
        print(name_person)
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


if __name__ == "__main__":
    main()