import os
import importlib
from unittest.mock import patch
# from django.test import TestCase
# from unittest import skip
# we have to use tools outside of django, because when it's initialized
# it's too late to change environment variables
from unittest import TestCase, main
from docker_django import settings


class DebugSettingTest(TestCase):

    def test_debug_on(self):
        with patch.dict('os.environ', {'DEBUG': 'true'}):
            importlib.reload(settings)
            assert 'DEBUG' in os.environ
            self.assertEqual(settings.DEBUG, True)

    def test_debug_off(self):
        for value in ('No', 'nO', 'N', 'n', 'false', 'False', 'off', 'oFF', 'Yes', 'YES', 'Y', 'On', '', '1', '0'):
            with patch.dict('os.environ', {'DEBUG': value}):
                importlib.reload(settings)
                assert 'DEBUG' in os.environ
                self.assertEqual(settings.DEBUG, False)


if __name__ == '__main__':
    main()
