from rest_framework import serializers
from tienda.models import Categoria, Producto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

    def validate_nombre(self, value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError(
                'El nombre de la categoría no puede contener números.'
            )
        return value.strip().title()


class ProductoSerializer(serializers.ModelSerializer):
    categoria = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Categoria.objects.filter(activa=True)
    )

    class Meta:
        model = Producto
        fields = ('id', 'nombre', 'precio', 'stock', 'categoria')

    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError('El precio debe ser mayor a 0.')
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError('El stock no puede ser negativo.')
        return value

    def validate(self, attrs):
        if attrs.get('stock') == 0 and attrs.get('precio') and attrs.get('precio') > 1000:
            raise serializers.ValidationError(
                'Un producto sin stock no puede tener un precio mayor a $1000.'
            )
        return attrs

    def create(self, validated_data):
        print(f'[LOG] Nuevo producto: {validated_data["nombre"]}')
        return Producto.objects.create(**validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['categoria'] = instance.categoria.nombre
        data['disponible'] = instance.stock > 0
        return data