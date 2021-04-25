from rest_framework import serializers
from books.models import Book
from django.contrib.auth.models import User


class UerSeroalizer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username","email","password","password2"]

    def save(self , **kwargs):
        user = User(
            username = self.validated_data.get("username"),
            email = self.validated_data.get("email")
        )

        if self.validated_data.get("password") != self.validated_data.get("password2"):
            raise serializers.ValidationError({
                "password" : "password miss match"
            })

        else:
            user.set_password(self.validated_data.get("password"))
            user.save()






class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title","content","author")
