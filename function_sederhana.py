jumlah_tiket_spiderman = 100
harga_tiket_spiderman = 5000

jumlah_tiket_iron_man = 300
harga_tiket_iron_man = 10000

kota_1 = "Jakarta"
kota_2 = "Surabaya"
kota_3 = "Malang"


def penjualan_tiket (jumlah_tiket, harga_tiket):
  total_penjualan = jumlah_tiket * harga_tiket
  return total_penjualan

def daftar_kota (*nama_kota):
  return nama_kota

print ("Tiket film Spider Man terjual Sebanyak", jumlah_tiket_spiderman, "dengan total pendapatan Rp",penjualan_tiket(jumlah_tiket_spiderman,harga_tiket_spiderman), "di kota", daftar_kota (kota_1,kota_2))
print ("Tiket film Iron Man terjual Sebanyak", jumlah_tiket_iron_man, "dengan total pendapatan Rp",penjualan_tiket(jumlah_tiket_iron_man,harga_tiket_iron_man), "di kota", daftar_kota (kota_1,kota_2,kota_3))
