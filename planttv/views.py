from django.http import HttpResponse
from django.shortcuts import render
import datetime

from planttv.models import PlantData

def home(request):
	plant_data = PlantData.objects.all().order_by('-timestamp')
	return render(request, 'planttv/home.html', { 'plant_data': plant_data })

def postData(request):
	if request.method == 'POST':
		# create a new plant data entry
		analogValue = int(request.POST.get('analog_value', -1))

		if analogValue != -1:
			pd = PlantData.objects.create(analog_value=analogValue)
			pd.save()
			print(pd)

			return HttpResponse(status=201)
		else:
			print("Didn't receive analog value")
			print(request.POST)
			print(request.GET)
			return HttpResponse(status=400)
	else:
		return HttpResponse('<h1>Post data to this url.</h1>')