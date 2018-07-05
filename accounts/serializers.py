from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    '''
        Create user
    '''
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8)
    phone_number = serializers.CharField(min_length=12)
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def create(self, validated_data):
        phone_number = validated_data.pop('phone_number')
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        context = {"first_name": first_name, "last_name": last_name, "phone_number": phone_number}
        user = User.objects.create_user(validated_data['email'],
                                        validated_data['password'],
                                        **context)
        return user

    class Meta:
        model = User
        fields = ('id', 'password', 'first_name', 'last_name', 'email', 'phone_number')
        extra_kwargs = {
            'password': {'write_only': True}
        }


class UserSummarySerializer(serializers.ModelSerializer):
    '''
        Get details of user
    '''
    class Meta:
        model = User
        exclude = ('password', 'is_superuser', 'is_active', 'is_admin', 'groups', 'user_permissions')
