from diaries.DiarySample import DiarySample
from diaries.UnoDiary import UnoDairy
# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
    DiarySample(),
    UnoDairy(),
]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
