from django.test import TestCase

from .models import Equipment, Category


class TestEquipmentList(TestCase):

    def test_response_status_code(self):
        response = self.client.get('/equipment/list')
        self.assertEqual(response.status_code, 200)

    def test_response_content(self):
        response = self.client.get('/equipment/list')
        self.assertIn(b'<h1>Equipments</h1>', response.content)

    # some text exists/not exists in HTML text test
    def test_equipment_in_list(self):
        response = self.client.get('/equipment/list')
        self.assertNotIn(b'test_equipment', response.content)
        self.category = Category.objects.create(name='test_category')
        self.equipment = Equipment.objects.create(item_type='test_equipment',
                                                  category=self.category)
        response = self.client.get('/equipment/list')
        self.assertIn(b'test_equipment', response.content)

    # variable exists in context test
    def test_equipment_list_in_context(self):
        response = self.client.get('/equipment/list')
        self.assertIn('equipment_list', response.context)

    # object exists in context item test
    def test_equipment_in_equipment_list(self):
        self.category = Category.objects.create(name='test_category')
        self.equipment = Equipment.objects.create(item_type='test_equipment',
                                                  category=self.category)
        response = self.client.get('/equipment/list')
        self.assertIn(self.equipment, response.context['equipment_list'])
