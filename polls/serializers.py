from rest_framework import serializers
from dashboard.models import Dashboard


class PollSerializer(serializers.ModelSerializer):
	class Meta:
		model = Dashboard
		fields = ('question', 'pub_date', 'choices')


