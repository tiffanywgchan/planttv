from django.db import models

class PlantData(models.Model):
	ANALOG_TO_TEMPERATURE = 0.5
	analog_value = models.IntegerField(blank=False, null=False)
	timestamp = models.DateTimeField(auto_now=True)

	@property
	def to_display(self):
		return "%d - %s" % (self.temperature, self.timestamp.strftime('%Y-%m-%d %H:%M:%S'))

	@property
	def temperature(self):
		return PlantData.to_temp(self.analog_value)

	@staticmethod
	def to_temp(analog_value):
		return analog_value * PlantData.ANALOG_TO_TEMPERATURE
