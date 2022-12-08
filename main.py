from diaries.DiarySample import DiarySample
from diaries.NakazimaDiary import NakazimaDiary
# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
    DiarySample(),
    NakazimaDiary(),
]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
