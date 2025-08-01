from abc import ABC, abstractmethod

from mission_2.constants import list_days, GRADE_NORMAL, GRADE_SILVER, GRADE_GOLD


# abstract strategy
class Result(ABC):
    @abstractmethod
    def set_point(self):    pass
    def set_grade(self):    pass
    def is_lazy(self):    pass

# concrete strategy
class ResultBaseball(Result):
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

    def __init__(self, dict_cnt):
        self._point = 0
        self._grade = ""
        self.dict_cnt = dict_cnt
        self.cnt_training_wed = self.dict_cnt["wednesday"]
        self.cnt_training_weekend = self.dict_cnt["saturday"] + self.dict_cnt["sunday"]

    def set_point(self):
        for day in list_days:
            self._point += self.dict_add_point[day] * self.dict_cnt[day]
        if self.dict_cnt["wednesday"] > self.THRE_COUNT_WED:
            self._point += self.BONUS_POINT_WED
        if self.dict_cnt["saturday"] + self.dict_cnt["sunday"] > self.THRE_COUNT_WEEKEND:
            self._point += self.BONUS_POINT_WEEKEND

    def set_grade(self):
        if self._point >= self.THRE_POINT_GOLD:
            self._grade = GRADE_GOLD
        elif self._point >= self.THRE_POINT_SILVER:
            self._grade = GRADE_SILVER
        else:
            self._grade = GRADE_NORMAL

    def is_lazy(self):
        if self.cnt_training_wed != 0 or self.cnt_training_weekend != 0:
            return False
        return True if self.grade is GRADE_NORMAL else False

    @property
    def point(self):
        return self._point

    @property
    def grade(self):
        return self._grade

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
        self.result = None

    def update_count(self, day):
        self.dict_cnt_per_day[day] += 1

    def set_point(self):
        self.result = ResultBaseball(self.dict_cnt_per_day)
        self.result.set_point()
        self.result.set_grade()

    def show_info(self):
        print(f"NAME : {self.name}, POINT : {self.result.point}, GRADE : {self.result.grade}")


    def is_lazy(self):
        return self.result.is_lazy()

    def point(self):
        return self.result.point

    def grade(self):
        return self.result.grade
