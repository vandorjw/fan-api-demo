from django.test import TestCase
from .models import Fan


class FanModelTest(TestCase):

    def setUp(self):
        self.fan = Fan.objects.create(name='test')

    def test_direction_forward_to_reverse(self):
        initial_direction = self.fan.direction_state
        while initial_direction != Fan.DIRECTION__FORWARD:
            self.fan.direction_next()
            initial_direction = self.fan.direction_state

        self.assertEqual(Fan.DIRECTION__FORWARD, initial_direction)
        self.fan.direction_next()
        self.assertEqual(Fan.DIRECTION__REVERSE, self.fan.direction_state)

    def test_direction_reverse_to_forward(self):
        initial_direction = self.fan.direction_state
        while initial_direction != Fan.DIRECTION__REVERSE:
            self.fan.direction_next()
            initial_direction = self.fan.direction_state

        self.assertEqual(Fan.DIRECTION__REVERSE, initial_direction)
        self.fan.direction_next()
        self.assertEqual(Fan.DIRECTION__FORWARD, self.fan.direction_state)

    def test_speed_OFF_SLOW(self):

        initial_speed = self.fan.speed_state
        while initial_speed != Fan.SPEED__OFF:
            self.fan.speed_next()
            initial_speed = self.fan.speed_state

        self.assertEqual(Fan.SPEED__OFF, initial_speed)
        self.fan.speed_next()
        self.assertEqual(Fan.SPEED__SLOW, self.fan.speed_state)

    def test_speed_SLOW_MEDIUM(self):
        initial_speed = self.fan.speed_state
        while initial_speed != Fan.SPEED__SLOW:
            self.fan.speed_next()
            initial_speed = self.fan.speed_state

        self.assertEqual(Fan.SPEED__SLOW, initial_speed)
        self.fan.speed_next()
        self.assertEqual(Fan.SPEED__MEDIUM, self.fan.speed_state)

    def test_speed_MEDIUM_FAST(self):
        initial_speed = self.fan.speed_state
        while initial_speed != Fan.SPEED__MEDIUM:
            self.fan.speed_next()
            initial_speed = self.fan.speed_state

        self.assertEqual(Fan.SPEED__MEDIUM, initial_speed)
        self.fan.speed_next()
        self.assertEqual(Fan.SPEED__FAST, self.fan.speed_state)

    def test_speed_FAST_OFF(self):
        initial_speed = self.fan.speed_state
        while initial_speed != Fan.SPEED__FAST:
            self.fan.speed_next()
            initial_speed = self.fan.speed_state

        self.assertEqual(Fan.SPEED__FAST, initial_speed)
        self.fan.speed_next()
        self.assertEqual(Fan.SPEED__OFF, self.fan.speed_state)

    def test_speed_does_not_effect_direction(self):
        initial_direction = self.fan.direction_state
        self.fan.speed_next()
        self.assertEqual(initial_direction, self.fan.direction_state)
