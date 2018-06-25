"""Serializer class binding with the model.
CRD operations happen via the Serializer class
"""
from rest_framework import serializers
from django.core.validators import validate_email, MinLengthValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """User Serializer
    """

    def validate_name(self, value):
        """Summary

        Args:
            value (str): the name attribute

        Returns:
            str: string representation of a name

        Raises:
            serializers.ValidationError: If the length of the name
            field is less than 2 chars (spaces are considered as a char),
            a validation error is thrown. Visible prominently through
            an api call via command line
        """
        if len(value) < 2:
            raise serializers.ValidationError(
                "Name must have at least 2 chars")
        return value

    def validate_email(self, value):
        """Method to validate an email address

        Args:
            value (str): email address

        Returns:
            str: valid email address
        """
        try:
            validate_email(value)
        except validate_email.ValidationError:
            serializers.ValidationError(
                "Not a valid email address")
        return value

    class Meta:

        """Summary

        Attributes:
            fields (tuple): field pertaining to a model object
            model (obj): model object
        """

        model = User
        fields = ('user_id', 'email', 'name', 'created_at', 'updated_at')
        # read_only_fields = ('created_at', 'updated_at')
