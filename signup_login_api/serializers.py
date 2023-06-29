from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username' , 'email', 'password' ]
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def  validate_password(self,value):
        if len(value)!=8:
            raise serializers.ValidationError("Password should be 8 digit") 
        return value

        
    def create(self, validated_data):
        print("validated_data", validated_data)
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            # first_name=validated_data['first_name'],
            # last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        print(user.password)
        user.save()
        return user
    
    
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

        




