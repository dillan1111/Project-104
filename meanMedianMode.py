from collections import Counter
import csv

def get_mean(total, n_num):
    mean = total / n_num
    print(f"Mean (Average) is -> {mean}")

def get_median(n_num, just_weight):
    if n_num % 2 == 0:
        median1 = float(just_weight[n_num//2])
        median2 = float(just_weight[n_num//2 - 1])
        median = (median1 + median2) / 2
    else:
        median = float(just_weight[n_num//2])
    print(f"Median is -> {median}")

def get_mode(just_weight):
    
    data = Counter(just_weight)
    group = {
        "75-85": 0,
        "85-95": 0,
        "95-105": 0,
        "105-115": 0,
        "115-125": 0,
        "125-135": 0,
        "135-145": 0,
        "145-155": 0,
        "155-165": 0,
        "165-175": 0                       
    }
    for weight, occurence in data.items():
        if 75 < weight < 85:
            group["75-85"] += occurence
        elif 85 < weight < 95:
            group["85-95"] += occurence
        elif 95 < weight < 105:
            group["95-105"] += occurence
        elif 105 < weight < 115:
            group["105-115"] += occurence
        elif 115 < weight < 125:
            group["115-125"] += occurence
        elif 125 < weight < 135:
            group["125-135"] += occurence
        elif 135 < weight < 145:
            group["135-145"] += occurence
        elif 145 < weight < 155:
            group["145-155"] += occurence
        elif 155 < weight < 165:
            group["155-165"] += occurence
        elif 165 < weight < 175:
            group["165-175"] += occurence
    mode_range, mode_occurence = 0, 0
    for range, occurence in group.items():
        if occurence > mode_occurence:
            mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
    mode = float((mode_range[0] + mode_range[1]) / 2)
    print(f"Mode is -> {mode}")

with open('SOCR-HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)


file_data.pop(0)

total = 0
n_num = len(file_data)
just_weight= []

for person_data in file_data:
    total += float(person_data[2])
    just_weight.append(float(person_data[2]))

just_weight.sort()

get_mean(total, n_num)
get_median(n_num, just_weight)
get_mode(just_weight)