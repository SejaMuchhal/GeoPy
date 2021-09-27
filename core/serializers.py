from rest_framework import serializers

class AddressSerializer(serializers.Serializer):
    address = serializers.CharField(
        required=True
    )
    output_format = serializers.CharField(
        required=True
    )
    