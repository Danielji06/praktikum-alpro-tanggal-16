def max_value(data):
    return max(data)

def min_value(data):
    return min(data)

def average(data):
    return sum(data) / len(data)
# Program utama
# input user

n = int(input("Masukkan n: "))
data = []
for i in range(n):
    angka = int(input("Masukkan angka: "))
    data.append(angka)
maksimum = max_value(data)
print(f"Nilai maksimum: {maksimum}")
minimum = min_value(data)
print(f"Nilai minimum: {minimum}")
rata_rata = average(data)
print(f"Nilai rata-rata: {rata_rata:.2f}")
print("Urut ascending:", end= " ")
data.sort()
print(data)
print("Urut descending: ", end= " ")
data.sort(reverse=True)
print(data)