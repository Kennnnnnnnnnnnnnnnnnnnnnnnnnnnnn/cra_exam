from mission_2.constants import list_days

dict_add_point = {
    "monday" : 1,
    "tuesday" : 1,
    "wednesday" : 3,
    "thursday" : 1,
    "friday" : 1,
    "saturday" : 2,
    "sunday" : 2,
}
BONUS_POINT_WEEKEND = 10
BONUS_POINT_WED = 10
THRE_COUNT_WEEKEND = 9
THRE_COUNT_WED = 9
THRE_POINT_SILVER = 30
THRE_POINT_GOLD = 50
GRADE_NORMAL = "NORMAL"
GRADE_SILVER = "SILVER"
GRADE_GOLD = "GOLD"

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
        self._point = 0
        self._grade = ""

    def update_count(self, day):
        self.dict_cnt_per_day[day] += 1
        if day == "wednesday":
            self.cnt_training_wed += 1
        elif day == "saturday" or day == "sunday":
            self.cnt_training_weekend += 1

    def set_point(self):
        for day in list_days:
            self._point += dict_add_point[day] * self.dict_cnt_per_day[day]
        if self.dict_cnt_per_day["wednesday"] > THRE_COUNT_WED:
            self._point += BONUS_POINT_WED
        if self.dict_cnt_per_day["saturday"] + self.dict_cnt_per_day["sunday"] > THRE_COUNT_WEEKEND:
            self._point += BONUS_POINT_WEEKEND
        self._set_grade()

    def _set_grade(self):
        if self._point >= THRE_POINT_GOLD:
            self._grade = GRADE_GOLD
        elif self._point >= THRE_POINT_SILVER:
            self._grade = GRADE_SILVER
        else:
            self._grade = GRADE_NORMAL

    @property
    def point(self):
        return self._point

    @property
    def grade(self):
        return self._grade
