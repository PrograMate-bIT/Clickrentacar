from django.contrib.auth.models import User
from django.test import TestCase
from .models import Vehicle

class VehicleTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('user1', None, 'test1234')
        self.user2 = User.objects.create_user('user2', None, 'test1234')
       # self.veh = Vehicle.objects.create('123', self.user1, 'brand', 'model', 1987, 4, False)
        #self.veh.owner =

    def test_vehicle_owner(self):
        self.assertEqual(self.veh.owner.id, self.user1.id)
