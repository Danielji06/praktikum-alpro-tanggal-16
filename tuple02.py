nota = {
    'nama_toko': 'Maju jaya Lancar berkah',
    'pelanggan': '16-05-2023',
    'barang': [
        {
            'nama-barang': 'penghapus',
            'harga_satuan': 5000,
            'jumlah': 4,
            'subtotal': 20000,
        },
        {   'nama-barang': 'Spidol hitam',
            'harga_satuan': 10000,
            'jumlah': 200,
            'subtotal': 2_000_000,
        }
    ],
    "total_transaksi": 2_020_000,
}

print(nota.keys())
print(nota["barang"][0].keys())
print(nota.values())
print(nota.items)
print('====')

for key, value in nota.items():
    print(f"{key}\t: {value}")

for key, value in nota['barang'][0].items():
    print(f"{key}\t: {value}")

print('===============')
for barang in nota['barang']:
    for key, value in barang.items():
        print(f"{key}\t: {value}")