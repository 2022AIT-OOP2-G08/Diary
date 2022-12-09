from diaries.DiarySample import DiarySample
from diaries.satoshi_diary import satoshi_diary
from diaries.ItoDiary import ItoDirary
# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
    DiarySample(),
    satoshi_diary(),
    ItoDirary(),
]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
