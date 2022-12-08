from diaries.DiarySample import DiarySample
from diaries.SakaiDiary import SakaiDiary
# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
    DiarySample(),
    SakaiDiary(),
]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
