from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from counselors.models import Counselor

class CounselorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Counselor
        
        fields = (
            'id', 'email', 'username', 'created_at', 'updated_at',
            'first_name', 'last_name', 'email', 'phone', 'county', 'cpf',
            'password', 'confirm_password',
        )

        read_only_fields = (
            'created_at', 'updated_at',
        )

        def create(self, validated_data):
            return Counselor.objects.create(**validated_data)

        def update(self, counselor, validated_data):
            counselor.username = validated_data.get('username', counselor.username)
            
            counselor.save()

            password = validated_data.get('password', None)
            confirm_password = validated_data.get('confirm_password', None)

            # TEMPORARY PASSWORD VALIDATION
            if password and confirm_password and password == confirm_password:
                counselor.set_password(password)
                counselor.save()

            update_session_auth_hash(self.context.get('request'), counselor)

            return counselor