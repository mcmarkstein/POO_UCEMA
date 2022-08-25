# pylint: disable-all

import unittest
import os
from app_flask import app_on

class TestFlaskOption(unittest.TestCase):
    def test_app_on_with_ENV_of_FLASK_APP_development(self):
        os.environ['ENV_of_FLASK_APP'] = 'desarrollo'
        self.assertEqual(app_on(), "Iniciando en modo de desarrollo...")

    def test_app_on_with_ENV_of_FLASK_APP_production(self):
        os.environ['ENV_of_FLASK_APP'] = 'produccion'
        self.assertEqual(app_on(), "Iniciando en modo de produccion...")

    def test_app_on_with_no_ENV_of_FLASK_APP(self):
        del os.environ['ENV_of_FLASK_APP']
        try:
            app_on()
        except KeyError:
            self.fail("Tu probrama debería funcionar sin la variable ENV_of_FLASK_APP definida")
        self.assertEqual(app_on(), "Iniciando en modo vacio...")
