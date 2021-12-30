from rest_framework import serializers

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):

        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        for position in positions:
            StockProduct(stock=stock, product=position['product'], quantity=position['quantity'], price=position['price'],).save()
        return stock

    def update(self, instance, validated_data):

        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)
        for position in positions:
            # product = stock.positions.get(product=position['product'])
            # product.quantity = position['quantity']
            # product.price = position['price']
            # product.save(update_fields=['quantity', 'price'])
            product = position.pop('product')
            stock.positions.update_or_create(product=product, defaults=position)
        return stock
