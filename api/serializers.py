from rest_framework import serializers
from api.models import Candidate, Dropdown, DropdownList


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('id', 'name', 'job_position', 'email', 'hours_per_week',
                'where_found_us', 'country', 'english_level', 'comments')


class DropdownListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropdownList
        fields = ('id', 'text')


class DropdownSerializer(serializers.ModelSerializer):
    dropdown_values = DropdownListSerializer(many=True)


    class Meta:
        model = Dropdown
        fields = ('id', 'field_name', 'dropdown_values')


    def create(self, validated_data):
        dropdown_values = validated_data.pop('dropdown_values')
        dropdown = Dropdown.objects.create(**validated_data)
        for value in dropdown_values:
            DropdownList.objects.create(dropdown=dropdown, **value)
        return dropdown

