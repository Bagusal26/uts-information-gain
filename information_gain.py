import math

data = [
    ["Cerah","Panas","Tinggi","Lemah","Tidak"],
    ["Cerah","Panas","Tinggi","Kuat","Tidak"],
    ["Mendung","Panas","Tinggi","Lemah","Ya"],
    ["Hujan","Sejuk","Tinggi","Lemah","Ya"],
    ["Hujan","Dingin","Normal","Lemah","Ya"],
    ["Hujan","Dingin","Normal","Kuat","Tidak"],
    ["Mendung","Dingin","Normal","Kuat","Ya"],
    ["Cerah","Sejuk","Tinggi","Lemah","Tidak"],
    ["Cerah","Dingin","Normal","Lemah","Ya"],
    ["Hujan","Sejuk","Normal","Lemah","Ya"],
    ["Cerah","Sejuk","Normal","Kuat","Ya"],
    ["Mendung","Sejuk","Tinggi","Kuat","Ya"],
    ["Mendung","Panas","Normal","Lemah","Ya"],
    ["Hujan","Sejuk","Tinggi","Kuat","Tidak"]
]

atribut = ["Cuaca", "Suhu", "Kelembapan", "Angin"]

def entropy(data):
    total = len(data)
    count = {}

    for row in data:
        label = row[-1]
        if label not in count:
            count[label] = 0
        count[label] += 1

    ent = 0
    for key in count:
        p = count[key] / total
        ent -= p * math.log2(p)

    return ent

def information_gain(data, index):
    total_entropy = entropy(data)
    total = len(data)

    values = {}
    for row in data:
        key = row[index]
        if key not in values:
            values[key] = []
        values[key].append(row)

    weighted_entropy = 0
    for key in values:
        subset = values[key]
        weighted_entropy += (len(subset)/total) * entropy(subset)

    return total_entropy - weighted_entropy

print("Entropy Total:", entropy(data))
print()

for i in range(len(atribut)):
    print("Information Gain", atribut[i], "=", information_gain(data, i))