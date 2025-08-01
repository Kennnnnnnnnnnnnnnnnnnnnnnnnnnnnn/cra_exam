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
