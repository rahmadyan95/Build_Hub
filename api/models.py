from django.db import models

class Product(models.Model):  # Ensure this is 'Product' and not 'Barang'
    photo_url = models.TextField()  # URL gambar barang (TEXT)
    product_name = models.CharField(max_length=225)  # Nama barang (maksimal 225 karakter)
    quantity = models.IntegerField()  # Kuantitas barang (integer)
    unit_value = models.CharField(max_length=50)  # Nilai satuan (misalnya 'M3', 'Kg')
    status = models.CharField(max_length=10)  # Status (sale atau rent)
    price = models.FloatField()  # Harga barang (float)
    description = models.TextField(default='No description')  # Keterangan barang (TEXT)

    def __str__(self):
        return self.product_name  # Menampilkan nama produk
