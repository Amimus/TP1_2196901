import pytest
from pathlib import Path
import sys

path_root = Path(__file__).parents
for p in path_root:
    print(p)
#sys.path.append(str(path_root))
print(f' pathes : -- {path_root}')
from api.app import create_app
from api.config import TestingConfig


@pytest.fixture
def app():
    app = create_app(config_object=TestingConfig)

    with app.app_context():
        yield app


@pytest.fixture
def flask_test_client(app):
    with app.test_client() as test_client:
        yield test_client
