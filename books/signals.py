from django.db.models.signals import post_save,pre_save,post_delete,pre_delete
from django.dispatch import receiver

from .models import Book , Isbin ,User

@receiver(post_save,sender=Book)

def after_book_creation(sender,instance, created ,*args , **kwargs):
    if created :
        isbin_instance = Isbin.objects.create(authortitle=instance.author.username)
        
        instance.isbin = isbin_instance

        instance.save()

    else:
        print("updating")


