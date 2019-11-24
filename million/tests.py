from django.test import TestCase
from million.models import*
class MillionTestCase(TestCase):
	def setup(self):
		Singer.objects.create(age=17,sex='male')
		Group.objects.create(name='kiss')
		Concert.objects.create(place='berlin')

	def test_validCreatedSinger(self):
		sgr=Singer.objects.get(age=17)
		self.assertEqual(sgr.age,17)
	def test_isemptyStringSinger(self):
		sgr=Singer.objects.get(age=17)
		self.assertEqual(sgr.name,'')
	def	 test_createdGroup(self):
		gr=Group.objects.get(style='rock')
		self.assertEqual(gr.style,'')
		self.assertNotEqual(gr.date,18)
	def test_forkedGroup(self):
		conc=Concert.objects.get(place='berlin')
		gr=Group.objects.get(style='rock')
		self.assertEqual(conc.group_concert,gr.id)


