from rest_framework import serializers

from APP.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('name','reg_no')

