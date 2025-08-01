dict_add_point = {
    "monday" : 1,
    "tuesday" : 1,
    "wednesday" : 3,
    "thursday" : 1,
    "friday" : 1,
    "saturday" : 2,
    "sunday" : 2,
}

class Person:
    def __init__(self, name):
        self.name = name
        self.dict_cnt_per_day = {
            "monday": 0,
            "tuesday": 0,
            "wednesday": 0,
            "thursday": 0,
            "friday": 0,
            "saturday": 0,
            "sunday": 0,
        }
        self.cnt_training_wed = 0
        self.cnt_training_weekend = 0
        self.point = 0

    def update_count(self, day):
        self.dict_cnt_per_day[day] += 1
        if day == "wednesday":
            self.cnt_training_wed += 1
        elif day == "saturday" or day == "sunday":
            self.cnt_training_weekend += 1

    def _set_point(self):
        self.point += dict_add_point[day] * person.dict_cnt_per_day[day]