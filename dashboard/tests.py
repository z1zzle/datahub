from django.test import TestCase, Client
from django.urls import reverse
from dashboard.models import ShapeDataLayerYearStats
from shapes.models import Type, Shape
from datalayers.models import Datalayer
from django.contrib.gis.geos import Polygon
import json



class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        self.test_type1 = Type.objects.create(id=1, key='Test Type 1', position=1)
        self.test_type2 = Type.objects.create(id=2, key='Test Type 2', position=2)

        self.test_shape1 = Shape.objects.create(id=1, parent_id=None,
                                                name='Test Shape 1',
                                                type=self.test_type1,
                                                geometry=Polygon.from_bbox(
                                                    (0, 0, 1, 1)))
        self.test_shape2 = Shape.objects.create(id=2, parent_id=self.test_shape1.id,
                                                name='Test Shape 1',
                                                type=self.test_type2,
                                                geometry=Polygon.from_bbox(
                                                    (0, 0, 1, 2)))

        self.test_datalayer1 = Datalayer.objects.create(name='Test Datalayer 1',
                                                       key='test_dl1')
        self.test_datalayer2 = Datalayer.objects.create(name='Test Datalayer 2',
                                                       key='test_dl2')

        ShapeDataLayerYearStats.objects.create(shape_id=self.test_shape1.id,
                                               data_layer=self.test_datalayer1.key,
                                               year=2020, value=7)
        ShapeDataLayerYearStats.objects.create(shape_id=self.test_shape2.id,
                                               data_layer=self.test_datalayer1.key,
                                               year=2021, value=2)
        ShapeDataLayerYearStats.objects.create(shape_id=self.test_shape1.id,
                                               data_layer=self.test_datalayer2.key,
                                               year=2020, value=7)


    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


    def test_info_map_base(self):
        response = self.client.get(reverse('info_map'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('datalayers', response.context)
        self.assertIn('min_year', response.context)
        self.assertIn('max_year', response.context)
        self.assertIn('types', response.context)
        self.assertIn('datahub_center_x', response.context)
        self.assertIn('datahub_center_y', response.context)
        self.assertIn('datahub_center_zoom', response.context)
        self.assertIn('presets', response.context)


    def test_get_dl_count_for_year_shapes(self):
        response = self.client.get(reverse('get_dl_count_for_year_shapes'),
                                   {'data_layers': f"{self.test_datalayer1.key},"
                                                   f"{self.test_datalayer2.key}",
                                    'type_id': self.test_shape2.id,
                                    'year': 2021,})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn('shape_dl_dict', data)
        self.assertIn('shape_missing_dl_dict', data)
        self.assertIn('geometries', data)
        self.assertIn('names', data)
        expected_dl_dict = {str(self.test_shape2.id): [[self.test_datalayer1.name, self.test_datalayer1.key]]}
        expected_missing_dl_dict = {str(self.test_shape2.id): [[self.test_datalayer2.name, self.test_datalayer2.key]]}
        self.assertEqual(data['shape_dl_dict'], expected_dl_dict)
        self.assertEqual(data['shape_missing_dl_dict'],
                         expected_missing_dl_dict)
        self.assertEqual(data['names'][str(self.test_shape2.id)], self.test_shape2.name)


    def test_temporal_trend_base(self):
        response = self.client.get(reverse('temporal_trend'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('types', response.context)
        self.assertIn('datalayers', response.context)
        self.assertIn('datahub_center_x', response.context)
        self.assertIn('datahub_center_y', response.context)
        self.assertIn('datahub_center_zoom', response.context)


    def test_get_shapes_by_type(self):
        response = self.client.get(reverse('get_shapes_by_type'),
                                   {'type_id': self.test_type1.id})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data[0]['name'], self.test_shape1.name)


    def test_slider_base(self):
        response = self.client.get(reverse('slider'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('types', response.context)
        self.assertIn('datalayers', response.context)
        self.assertIn('datahub_center_x', response.context)
        self.assertIn('datahub_center_y', response.context)
        self.assertIn('datahub_center_zoom', response.context)
        self.assertIn('presets', response.context)


    def test_get_dl_value_for_year_shapes(self):
        response = self.client.get(reverse('get_dl_value_for_year_shapes'),
                                   {'data_layer_key': self.test_datalayer2.key,
                                    'year': 2020,
                                    'shape_type': self.test_type1.id})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn('geometries', data)
        self.assertIn('names', data)
        self.assertIn('dl_values', data)
        self.assertIn(self.test_shape1.geometry.geojson, data['geometries'].values())
        self.assertIn(self.test_shape1.name, data['names'].values())
        self.assertEqual(data['dl_values'].get(str(self.test_shape1.id)), 7)
