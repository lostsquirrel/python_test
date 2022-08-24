import os
import pathlib
import unittest
from dotenv import dotenv_values, load_dotenv

current_path = pathlib.Path(__file__).parent.resolve()
env_path = os.path.join(current_path, '.env')


class DotEnvTest(unittest.TestCase):

    def test_load_values(self):

        env_config = dotenv_values(env_path)

        for k, v in env_config.items():
            print(f'{k}: {v}')

    def test_load_dotenv(self):

        load_dotenv(env_path)
        for env_key in ["FOO", "BAR"]:
            print(f'{env_key}: {os.getenv(env_key)}')
