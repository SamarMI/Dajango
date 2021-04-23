from django.db import models
from django.contrib.auth.models import User
import uuid



# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=25)


    def __str__(self):
        return self.name

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Isbin(models.Model):
    booknumber = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    authortitle = models.CharField(max_length=255,null=True, blank=True)



    def __str__(self):
        return f"{self.authortitle} authortitle  | booknumber {self.booknumber}"



class Book(models.Model):

    title = models.CharField(max_length=255,null=True, blank=True)
    content = models.TextField(max_length=2848)
    author = models.ForeignKey(User, null=True,blank=True, on_delete=models.CASCADE, related_name="books")
    categories = models.ManyToManyField(Category)
    isbin = models.OneToOneField(Isbin, on_delete=models.CASCADE, null=True, blank=True)
    tag = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
