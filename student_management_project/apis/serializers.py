from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import users, Task

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ['username', 'email', 'password', 'department']
        extra_kwargs = {'password': {'write_only': True}}  

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)



class TaskSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields =['description','due_date','student','status']
