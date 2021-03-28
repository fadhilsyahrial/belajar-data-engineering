class Karyawan:

    ##Class Attributes
    kelas_karyawan = "Tetap"

    def __init__  (self, nama = None, divisi = None, tenur = None):

        ##Instance Attributes
        self.nama = nama
        self.divisi = divisi
        self.tenur = tenur

    # class method
    @classmethod
    def kelas_karyawan2 (cls):
        print (f"{cls.kelas_karyawan} kontrak")   
    
    # Instance Method
    def promotion_flag (self, promoted):
        print (self.nama,"status",promoted)

karyawan1 = Karyawan ("Debi","Product",2)
karyawan2 = Karyawan ("Ika","Business",1)

print (karyawan1.nama, karyawan2.nama)
print (karyawan2.kelas_karyawan)
print (karyawan1.kelas_karyawan)
print (karyawan2.kelas_karyawan2)
