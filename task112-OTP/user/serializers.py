from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import PostCrud


class UserLoginSerializers(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13)
    
    def validate_phone_number(self, value):
        if not ((value.startswith('09') or value.startswith("+98"))
                and value.isnumeric() and (len(value)==11 or 13)):
            raise ValidationError('Phone number is not valid')
        return value
        
        
class UserVeifySerializers(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13)
    otp = serializers.CharField(max_length=6)

    def validate_phone_number(self, value):
        if not ((value.startswith('09') or value.startswith("+98"))
                and value.isnumeric() and (len(value)==11 or 13)):
            raise ValidationError('Phone number is not valid')
        return value
        
    def validate_otp(self, value):
        if not (value.isnumeric() and len(value)==6):
            raise ValidationError("otp in not valid")
        return value
        
# # mr-sabet:

# class UserDataValidation(serializers.Serializer):
#     phone_number = serializers.CharField(max_length=13)
#     otp = serializers.CharField(max_length=6)
    
#     def validate(self, attrs):
#         if not ((attrs['phone_number'].startswith('09') or attrs['phone_number'].startswith('+98'))
#                 and attrs['phone_number'].isnumeric() and (len(attrs['phone_number'])== 11 or 13)):
#             raise ValidationError('Phone number is not valid')
#         if not (attrs["otp"].isnumeric() and len(attrs["otp"])==6):
#             raise ValidationError("otp in not valid")
#         return attrs


class PostCrudSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=250)
    text = serializers.CharField(max_length=999)
       
    class Meta:
        model = PostCrud
        fields = "__all__"
        read_only_fields = ["owner" , "created_at", "modified_at", "slug"]
        