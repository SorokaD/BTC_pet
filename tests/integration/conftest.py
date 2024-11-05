import os

import pytest


@pytest.fixture(scope="module")
def local_fastapi_client():
    os.environ["MODELS"] = "predict_default_amounts"

    from fastapi.testclient import TestClient

    from fundraiseup.service.mlapi import app, load_models

    client = TestClient(app)
    yield client
