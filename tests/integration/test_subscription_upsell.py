from logging import Logger
from typing import Any, Dict, NamedTuple

import pytest

from fundraiseup.service.mlapi import load_models

logger = Logger(__name__)

load_models(["predict_subscription_upsell"])


class TestCase(NamedTuple):
    url: str
    data: Dict[str, Any]


test_cases = (
    TestCase(
        url="/predict_subscription_upsell",
        data={
            "date": "2021-01-01",
            "touchpoint": "email",
            "company_key": "company",
            "recurring_key": "recurring",
            "currency": "USD",
            "charge_amount": 10.0,
            "charge_amount_in_usd": 10.0,
            "payment_method": "card",
            "installment": 0,
        },
    ),
)


@pytest.mark.parametrize("url,data", test_cases)
def test_subscription_upsell(local_fastapi_client, url: str, data: Dict[str, Any]) -> None:
    response = local_fastapi_client.post(url, json=data)
    response_body = response.json()
    logger.info(response_body)
    assert response.status_code == 200
    if response_body["use_predict"]:
        assert "upgrade_buttons" in response_body
        assert sorted(response_body["upgrade_buttons"]) == response_body["upgrade_buttons"]
