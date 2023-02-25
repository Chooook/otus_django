from django.test import TestCase, SimpleTestCase
from mixer.backend.django import mixer

from .models import Category, Equipment


class TestCategory(TestCase):

    def setUp(self):
        # self.category = Category.objects.create(name='test_category')
        self.category = mixer.blend(Category)

    def test_str(self):
        self.assertEqual(str(self.category), self.category.name)

    def test_has_equipment_false(self):
        self.assertFalse(self.category.has_equipment)

    def test_has_equipment_true(self):
        Equipment.objects.create(item_type='test_equipment',
                                 category=self.category)
        self.assertTrue(self.category.has_equipment)


# use SimpleTestCase if connection to db is not needed to optimise
# it doesn't create db for tests, so they run faster
class TestEquipment(SimpleTestCase):

    def setUp(self):
        # in this case it works with db
        # self.category = Category.objects.create(name='test_category')
        # self.equipment = Equipment.objects.create(item_type='test_equipment',
        #                                           category=self.category)
        # in this case it doesn't work with db (optimisation)
        # use this optimisation if method don't use db
        self.category = Category(name='test_category')
        self.equipment = Equipment(item_type='test_equipment',
                                   category=self.category)

    def test_str(self):
        self.assertEqual(str(self.equipment), 'test_equipment')

    def test_buy(self):
        with self.assertRaises(NotImplementedError):
            self.equipment.buy()
