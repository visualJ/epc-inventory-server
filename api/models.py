from django.db import models
from rest_framework import serializers

'''
class RfidTag(models.Model):
    header = models.IntegerField(default=0)
    domainManager = models.IntegerField(primary_key=True, default=0)
    objectClass = models.IntegerField(primary_key=True, default=0)
    serialNumber = models.BigIntegerField(primary_key=True, default=0)

    def __str__(self):
        return ",".join(self.header, self.domainManager, self.objectClass, self.serialNumber)


class RfidTagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('header', 'domainManager', 'objectClass', 'serialNumber')
'''


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    header = models.SmallIntegerField(default=0)
    domainManager = models.IntegerField(default=0)
    objectClass = models.IntegerField(default=0)
    serialNumber = models.BigIntegerField(default=0)

    location = models.IntegerField(default=0)
    position = models.IntegerField(default=0)

    def __str__(self):
        return ",".join(map(str, [self.id, self.name, self.header, self.domainManager, self.objectClass, self.serialNumber, self.location, self.position]))


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'header', 'domainManager', 'objectClass', 'serialNumber', 'location', 'position')
