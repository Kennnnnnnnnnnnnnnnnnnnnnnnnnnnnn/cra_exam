import pytest

from mission_2.attendance import init_data, list_people, count_training, destroy_data


@pytest.mark.parametrize("entry1, entry2, entry3, cnt_mon, cnt_fri, cnt_wed, cnt_sat", [
    ('Ethan friday','Ethan monday', 'Ethan monday', 2, 1, 0, 0),
    ('Ethan wednesday','Ethan saturday', 'Ethan monday', 1, 0, 1, 1),
])
def test_count_simple(entry1, entry2, entry3, cnt_mon, cnt_fri, cnt_wed, cnt_sat):
    lines = [entry1, entry2, entry3]
    init_data(lines)
    count_training(lines)
    person = None
    for person in list_people:
        if person.name == 'Ethan':
            break
    assert person.dict_cnt_per_day["monday"] == cnt_mon
    assert person.dict_cnt_per_day["friday"] == cnt_fri
    assert person.dict_cnt_per_day["wednesday"] == cnt_wed
    assert person.dict_cnt_per_day["saturday"] == cnt_sat
    destroy_data()


@pytest.mark.parametrize("entry1, entry2, entry3, point", [
    ('Ethan friday','Ethan monday', 'Ethan monday', 3),
    ('Ethan wednesday','Ethan saturday', 'Ethan monday', 6),
])
def test_point_simple(entry1, entry2, entry3, point):
    lines = [entry1, entry2, entry3]
    init_data(lines)
    count_training(lines)
    person = None
    for person in list_people:
        if person.name == 'Ethan':
            person.set_point()
            break
    assert person.point() == point
    destroy_data()


def test_grade():
    lines = ['Charlie tuesday',
            'Charlie monday',
            'Charlie tuesday',
            'Charlie friday',
            'Charlie saturday',
            'Charlie wednesday',
            'Charlie thursday',
            'Charlie monday',
            'Charlie thursday',
            'Charlie saturday',
            'Charlie friday',
            'Charlie sunday',
            'Charlie thursday',
            'Charlie tuesday',
            'Charlie wednesday',
            'Charlie thursday',
            'Charlie sunday',
            'Charlie saturday',
            'Charlie friday',
            'Charlie wednesday',
            'Charlie monday',
            'Charlie sunday',
            'Charlie thursday',
            'Charlie friday',
            'Charlie monday',
            'Charlie thursday',
            'Charlie tuesday',
            'Charlie friday',
            'Charlie wednesday',
            'Charlie wednesday',
            'Charlie friday',
            'Charlie wednesday',
            'Charlie sunday',
            'Charlie sunday',
            'Charlie thursday',
            'Charlie tuesday',
            'Charlie tuesday',
            'Charlie monday']
    init_data(lines)
    count_training(lines)
    person = None
    for person in list_people:
        if person.name == 'Charlie':
            person.set_point()
            break
    assert person.grade() == "GOLD"
    destroy_data()