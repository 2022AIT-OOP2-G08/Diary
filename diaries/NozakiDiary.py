from diaries.AbstractDiary import AbstractDiary


class NozakiDiary(AbstractDiary):
    def get_date(self):
        return "2022-12-14"

    def get_summary(self):
        return "GitHubの使い方がよくわからなかった。"

    def get_author(self):
        return "野崎宇宙"