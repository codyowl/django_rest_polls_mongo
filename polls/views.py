from django.shortcuts import render
from polls.serializers import PollSerializer
from polls.models import Poll

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


@api_view(['GET', 'POST'])
def polls_list(request):
	if request.method == 'GET':
		polls = Poll.objects.all()
		serializer = PollSerializer(polls, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		question = request.POST.get['question']
		pub_date = request.POST.get['pub_date']
		choices = request.POST.get['choices']

		serializer = PollSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			final_serializer = JsonSerializer(question, pub_date, choices)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def JsonSerializer(question, pub_date, choices):
	final_json = {}
	final_json['question'] = question
	final_json['pub_date'] = pub_date
	final_json['choices'] = choices

	return final_json


