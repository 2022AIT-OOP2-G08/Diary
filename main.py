from diaries.DiarySample import DiarySample
from diaries.KeisukeDiary import KeisukeDiary
# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
    DiarySample(),
    KeisukeDiary(),

]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
