from diaries.AbstractDiary import AbstractDiary


class SakaiDiary(AbstractDiary):
    def get_date(self):
        return "2022-12-13"

    def get_summary(self):
        return "アーキテクチャのテストなんとか乗り切った。"

    def get_author(self):
        return "酒井"
