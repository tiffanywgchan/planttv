from django.db import models

class PlantData(models.Model):
	analog_value = models.IntegerField(blank=False, null=False)
	timestamp = models.DateTimeField(auto_now=True)

	@property
	def to_display(self):
		return "%d - %s" % (self.analog_value, self.timestamp.strftime('%Y-%m-%d %H:%M:%S'))
