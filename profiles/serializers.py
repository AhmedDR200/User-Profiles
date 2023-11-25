from rest_framework import serializers
from .models import Profile, ProfileStatus

# ProfileSerializer class is used to serialize the Profile model.
class ProfileSerializer(serializers.ModelSerializer):

    # user field is a StringRelatedField which means it will display the string representation of the user.
    user = serializers.StringRelatedField(read_only=True)

    # picture field is an ImageField which means it will display the image of the user.
    picture = serializers.ImageField(read_only=True)

    # Meta class is used to specify the model and fields that should be serialized.
    class Meta:
        model = Profile
        fields = '__all__'


# ProfileAvatarSerializer class is used to serialize the picture field of the Profile model.
class ProfileAvatarSerializer(serializers.ModelSerializer):
    
    # Meta class is used to specify the model and fields that should be serialized.
    class Meta:
        model = Profile
        fields = ('picture',)


# ProfileStatusSerializer class is used to serialize the ProfileStatus model.
class ProfileStatusSerializer(serializers.ModelSerializer):
    
    # user_profile field is a StringRelatedField which means it will display the string representation of the user's profile.
    user_profile = serializers.StringRelatedField(read_only=True)

    # Meta class is used to specify the model and fields that should be serialized.
    class Meta:
        model = ProfileStatus
        fields = '__all__'
