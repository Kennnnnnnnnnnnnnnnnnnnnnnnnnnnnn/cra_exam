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

    def update_count(self, day):
        self.dict_cnt_per_day[day] += 1
        if day == "wednesday":
            self.cnt_training_wed += 1
        elif day == "saturday" or day == "sunday":
            self.cnt_training_weekend += 1
