from diaries.AbstractDiary import AbstractDiary


class KeisukeDiary(AbstractDiary):
    def get_date(self):
        return "2022-12-06"

    def get_summary(self):
        return "課題が多すぎてだるい。ゲームしたい"

    def get_author(self):
        return "太田圭祐"
