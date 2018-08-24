from django.contrib import admin
# from .models import PostCategory, Post
from .models import Post
import datetime


# class PostCategoryAdmin(admin.ModelAdmin):

#     list_display = ('nama_kategori', 'deskripsi_kategori', 'created_by', 'updated_at')
#     search_fields = ['nama_kategori', 'deskripsi_kategori']

#     # actions = notne

#     def save_model(self, request, obj, form, change):
#         if form.is_valid():
#             user = request.user
#             stock = form.save(commit=False)
#             stock.created_by = user.id
#             stock.updated_at = datetime.datetime.now()
#             stock.save()


class PostAdmin(admin.ModelAdmin):

    # list_display = ('nama_barang', 'kode_barang', 'kategori', 'created_by', 'updated_at')
    list_display = ('nama_barang', 'kode_barang', 'created_by', 'updated_at')
    # search_fields = ['kategori__nama_kategori', 'kategori__deskripsi_kategori', 'nama_barang']
    search_fields = ['nama_barang', 'kode_barang']
    # actions = notne

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            user = request.user
            stock = form.save(commit=False)
            stock.created_by = user
            stock.updated_at = datetime.datetime.now()
            stock.save()
            suffix = stock.nama_barang.replace(' ', '')
            # suffix = suffix.decode('utf-8').lower()
            suffix = suffix.lower()
            stock.kode_barang = '{0}.{1}.{2}.{3}' . format(suffix[:3], stock.created_by_id, stock.kategori_id, stock.id)
            # stock.kode_barang = '{0}.{1}.{2}' . format(suffix[:3], stock.created_by_id, stock.id)
            stock.save()

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(created_by=request.user)

    # def has_change_permission(self, request, obj=None):
    #     if not obj:
    #         # the changelist itself
    #         return True
    #     return obj.user == request.user


admin.site.register(Post, PostAdmin)
# admin.site.register(PostCategory, PostCategoryAdmin)
