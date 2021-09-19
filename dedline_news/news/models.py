from django.db import models
from django.urls import reverse

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Sarlavhasi')
    content = models.TextField(blank=True, verbose_name='Matni')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan sanasi')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Yangilangan sanasi')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_published = models.BooleanField(default=True, verbose_name='Chop qilinganligi')

    category = models.ForeignKey('Category',on_delete=models.PROTECT,null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"

    def myFunc(self):
        return "News modeli funksiyasi"

class Category(models.Model):
    title = models.CharField(max_length=150,db_index=True,verbose_name='Kategoriya nomi')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

    def get_absolute_url(self):
        return reverse('category',kwargs={"category_id":self.pk})