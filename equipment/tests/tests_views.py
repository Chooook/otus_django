from django.test import TestCase

from equipment.models import Equipment, Category
from user.models import MyUser


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


class TestEquipmentDetail(TestCase):

    def test_response_status_code(self):
        self.category = Category.objects.create(name='test_category')
        # equipment not saved to db
        self.equipment = Equipment(item_type='test_equipment',
                                   category=self.category)
        response = self.client.get(f'/equipment/detail/1')
        self.assertEqual(response.status_code, 404)
        # equipment saved to db
        self.equipment = Equipment.objects.create(item_type='test_equipment',
                                                  category=self.category)
        response = self.client.get(f'/equipment/detail/{self.equipment.pk}')
        self.assertEqual(response.status_code, 200)


class TestIndex(TestCase):

    def test_permissions(self):
        # as guest
        response = self.client.get('')
        self.assertEqual(response.status_code, 302)
        MyUser.objects.create_user(username='user', password='1234')
        self.client.login(username='user', password='1234')
        # as user
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.client.logout()
        # as guest again
        response = self.client.get('')
        self.assertEqual(response.status_code, 302)
