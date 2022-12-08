from diaries.AbstractDiary import AbstractDiary


class NakazimaDiary(AbstractDiary):
    def get_date(self):
        return "2023-01-01"

    def get_summary(self):
        return "今年のおみくじは大吉だった。去年は凶だったのでとても嬉しい。"

    def get_author(self):
        return "なかじま"
