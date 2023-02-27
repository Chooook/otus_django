from rest_framework import serializers

from .models import Equipment, Category, Product, Supplier


class EquipmentSerializer:

    class Meta:
        model = Equipment
        fields = '__all__'


# class CategorySerializer(serializers.HyperlinkedModelSerializer):
#     # if not in root HyperlinkedSerializer is not so usable
#     # because you neet to make url description field like this
#     # so it doesn't differ to ModelSerializer
#     url = serializers.HyperlinkedIdentityField(
#         view_name='equipment:category-detail')
class CategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='equipment:category-detail')

    class Meta:
        model = Category
        fields = '__all__'

    # validation when data comes from API
    name = serializers.CharField(max_length=128)

    # for single field custom validation (with field name in method name)
    def validate_name(self, value):
        if value == 'invalid':
            raise serializers.ValidationError('invalid category name')
        return value

    # for multiple fields custom validation
    def validate(self, attrs):
        if attrs['name'] == 'invalid2':
            raise serializers.ValidationError('invalid2 category name')
        return attrs

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    class ProductSerializer(serializers.ModelSerializer):
        # ForeignKey serialization
        item_type = EquipmentSerializer()
        # m2m field serialization (many variations of related field class)
        # or you can create custom related field class
        suppliers = serializers.StringRelatedField(many=True, read_only=True)
        # using PrimaryKeyRelatedField as default
        # suppliers = SupplierSerializer(many=True)
        # to exclude fields
        exclude = ['description']

        class Meta:
            model = Product
            fields = '__all__'

