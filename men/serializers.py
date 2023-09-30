from rest_framework import serializers
from .models import Men
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io




# 10 # 11 # 12
class MenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # user = serializers.SlugField()
    class Meta:
        model = Men
        fields = "__all__"

################################################################################

# 8 # 9 
# class MenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Men
#         fields = "__all__"

###########################################################################

# 7
# class MenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Men
#         fields = "__all__"

############################################################################

# 6
# class MenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Men
#         fields = "__all__"


###########################################################################

# 5
# class MenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=225)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only = True)
#     time_update = serializers.DateTimeField(read_only = True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()

#     def create(self, validated_data):
#         return Men.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.time_update = validated_data.get('update', instance.time_update)
#         instance.is_published = validated_data.get('is_published', instance.is_published)
#         instance.cat_id = validated_data.get('cat_id', instance.cat_id)
#         instance.save()
#         return instance



####################################################################################

# 4
# class MenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=225)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only = True)
#     time_update = serializers.DateTimeField(read_only = True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()


####################################################################################

# 3
# class MenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

# class MenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length = 255)
#     content = serializers.CharField()

# def encode():
#     model = MenModel('Cristiano Ronaldo', 'Content: Cristiano Ronaldo')
#     model_sr = MenSerializer(model)
#     print(model_sr.data, type(model_sr.data,), sep = '\n')    
#     json = JSONRenderer().render(model_sr.data)
#     print(json)

# def decode():
#     stream =  io.BytesIO(b'{"title":"Cristiano Romaldo","content":"Content: Cristiano Ronaldo"}')
#     data = JSONParser().parse(stream)
#     serializer = MenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)

    
