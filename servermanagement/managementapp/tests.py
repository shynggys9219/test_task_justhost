# from django.test import TestCase
from django.urls import reverse_lazy, reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import VPS

# Create your tests here.
class VPSTests(APITestCase):
    
    def test_create_vps(self):
        user = User(username="shynggys", password="Qw3rty123.")
        user.save()
        url = reverse_lazy('vps-list')
        
        data = {"cpu":10, "ram":6000, "hdd":1200, "status":"STARTED"}
        self.client.force_login(user=user)
        # self.client.
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_vps_detail(self):
        user = User(username="shynggys", password="Qw3rty123.")
        user.save()
        data = {"cpu":10, "ram":6000, "hdd":1200, "status":"STARTED"}
        self.client.force_login(user=user)
        url = reverse_lazy('vps-list')
        self.client.post(url, data, format="json")
        response = self.client.get("/api/vps/1/")
        self.assertEqual(response.data, {'url': 'http://testserver/api/vps/1/', "cpu":10, "ram":6000, "hdd":1200, "status":"STARTED"})

        