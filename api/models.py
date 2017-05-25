from django.db import models
from rest_framework import serializers


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return "%s: %s" % (self.id, self.name)


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name')
