# list of tuples
data_laundry = [
    # urutan yaitu: no, nama, transaksi terakhir(kg), transaksi terakhir(rp)
    (100, 'Yuan', 10, 60000),
    (129, 'Bambang', 5, 20000), 
    (119, 'Agus', 2, 50000),
    (120, 'Wati', 1, 5000)
]

total = 0
for data in data_laundry:
    print(data[3])
    total = total + data[3]
print(f"total: Rp.{total}")


# urutkan berdasarkan nomor pelanggan
data_laundry.sort(reverse=True)
for data in data_laundry:
    print(f"{data[0]}. {data[1]}")

# urutkan berdasarkan nilai transaksi descending(top spending)
data_laundry.sort(key=lambda x: x[3], reverse=True)
print("Top Spending")
for data in data_laundry:
    print(f"{data[0]}. {data[1]}\t Rp.{data[3]}")