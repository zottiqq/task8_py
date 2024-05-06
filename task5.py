import random

drop_norm = ["жвачка", "кек", "кислинка"]
drop_rare = ["плюмбус", "палка", "кола"]
drop_epic = ["ракета", "дигл", "волшебная палочка"]
drop_legend = ["авп", "леон кемстыч", "спайк"]

kf_norm = 0.6
kf_rare = 0.2
kf_epic = 0.195
kf_legend = 0.005

cout_norm = 0
cout_rare = 0
cout_epic = 0
cout_legend = 0

drop_list = []

for i in range(20):
    rand = random.random()
    if rand < kf_norm:
        item = random.choice(drop_norm)
        drop_list.append(("обычный", item))
        cout_norm += 1
    elif rand < kf_norm + kf_rare:
        item = random.choice(drop_rare)
        drop_list.append(("редкий", item))
        cout_rare += 1
    elif rand < kf_norm + kf_rare + kf_epic:
        item = random.choice(drop_epic)
        drop_list.append(("эпический", item))
        cout_epic += 1
    else:
        item = random.choice(drop_legend)
        drop_list.append(("легендарный", item))
        cout_legend += 1


for quality, item in drop_list:
    if quality == "обычный":
        print(f"\033[0m{quality}: {item}")
    elif quality == "редкий":
        print(f"\033[94m{quality}: {item}")
    elif quality == "эпический":
        print(f"\033[95m{quality}: {item}")
    elif quality == "легендарный":
        print(f"\033[93m{quality}: {item}")

print()
print('ВЫПАЛО ОБЫЧНЫХ:', cout_norm)
print('ВЫПАЛО РЕДКИХ:', cout_rare)
print('ВЫПАЛО ЭПИЧЕСКИХ:', cout_epic)
print('ВЫПАЛО ЛЕГЕНДАРНЫХ:', cout_legend)
if cout_legend > 1:
    print("БОЛЬШАЯ УДАЧА!!!!")
elif cout_epic > 3:
    print("УДАЧА!!")


