from django.db import models
from category.models import Category

# Create your models here.
class Blogs(models.Model):
    name = models.CharField(max_length= 255)
    descriptions = models.TextField()
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #ไม่สามารถลบหมวดหมู๋ก่อนลบประเภทบทความได้
    writer = models.CharField(max_length=225)
    views = models.IntegerField(default=0) #ยอดวิวเริ่มต้น
    image = models.ImageField(upload_to="blogsImages",blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name