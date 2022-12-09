from diaries.AbstractDiary import AbstractDiary


class UnoDairy(AbstractDiary):
    def get_date(self):
        return "2022-12-07"

    def get_summary(self): 
        return "毎回、確率統計がわからない。"

    def get_author(self):
        return "宇野"
