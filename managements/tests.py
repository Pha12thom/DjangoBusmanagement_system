from django.test import TestCase
from django.urls import reverse
from .models import Bus

class BusModelTest(TestCase):
    def setUp(self):
        Bus.objects.create(
            name='Test Bus',
            color='Red',
            no_plate='ABC123',
            seats=50,
            departure_city='Nairobi',
            arrival_city='Mombasa',
            departure_time='2024-03-01',
            depart_time='08:00:00'
        )

    def test_bus_details(self):
        test_bus = Bus.objects.get(name='Test Bus')
        self.assertEqual(test_bus.name, 'Test Bus')
        self.assertEqual(test_bus.color, 'Red')
        self.assertEqual(test_bus.no_plate, 'ABC123')
        self.assertEqual(test_bus.seats, 50)
        self.assertEqual(test_bus.departure_city, 'Nairobi')
        self.assertEqual(test_bus.arrival_city, 'Mombasa')
        self.assertEqual(test_bus.departure_time.strftime('%Y-%m-%d'), '2024-03-01')
        self.assertEqual(test_bus.depart_time.strftime('%H:%M:%S'), '08:00:00')

class ViewsTest(TestCase):
    def test_search_results_view(self):
        response = self.client.get(reverse('search_results'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_results.html')

    def test_bus_detail_view(self):
        bus = Bus.objects.create(
            name='Test Bus',
            color='Red',
            no_plate='ABC123',
            seats=50,
            departure_city='Nairobi',
            arrival_city='Mombasa',
            departure_time='2024-03-01',
            depart_time='08:00:00'
        )
        response = self.client.get(reverse('bus_detail', args=[bus.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bus_detail.html')

    # Add more tests for other views as needed
