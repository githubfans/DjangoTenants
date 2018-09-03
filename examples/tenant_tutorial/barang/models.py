from django.db import models
from django.contrib.auth.models import User
# from datetime import datetime


# class PostCategory(models.Model):

#     cid = models.AutoField(primary_key=True, unique=True)
#     nama_kategori = models.CharField(max_length=30)
#     deskripsi_kategori = models.CharField(max_length=200)
#     updated_at = models.DateTimeField(null=True, editable=True)
#     created_by = models.ForeignKey(User, null=True, editable=True, on_delete=False)

#     def __str__(self):
#         return self.nama_kategori


class Post(models.Model):
    '''
    Barang item

    '''
    id = models.AutoField(primary_key=True, unique=True)
    kode_barang = models.CharField(max_length=30, editable=False, default='-')
    kategori = models.ForeignKey('self', on_delete=models.CASCADE, null=True, default='0')
    nama_barang = models.CharField(max_length=100)
    deskripsi = models.CharField(max_length=250, null=True)
    set_kategori = models.BooleanField(default=False)
    updated_at = models.DateTimeField(null=True, editable=True, auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, editable=True, default=0, on_delete=models.CASCADE)

    auto_create_schema = True

    def __str__(self):
        return self.nama_barang
