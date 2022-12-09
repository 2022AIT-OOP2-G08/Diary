from diaries.AbstractDiary import AbstractDiary


class ItoDirary(AbstractDiary):
    def get_date(self):
        return "2022-12-10"

    def get_summary(self):
        return "課題が終わらないが、他のやることが多すぎて1日が終わった。"

    def get_author(self):
        return "伊藤涼真"
