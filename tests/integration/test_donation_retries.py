from logging import Logger
from typing import Any, Dict, NamedTuple

import pytest

from fundraiseup.service.mlapi import load_models

logger = Logger(__name__)

load_models(["predict_donation_retries"])


class TestCase(NamedTuple):
    url: str
    data: Dict[str, Any]


test_cases = (
    TestCase(
        url="/predict_donation_retries",
        data={
            "subscription_datetime": "2023-11-30T21:08:00+00:00",
            "first_failed_datetime": "2024-06-26T12:23:43+00:00",
            "subscriptionterms_currency": "USD",
            "subscriptionterms_amount_in_usd": 2680,
            "subscriptionterms_payment_method": "creditCard",
            "subscriptionterms_brand": "MasterCard",
            "subscriptionterms_timezone": "America/New_York",
            "subscriptionterms_customer_address_country_code": "",
            "subscriptionterms_customer_address_city": "",
            "subscriptionterms_customer_address_region": "",
            "subscriptionterms_customer_title": "",
            "subscriptionterms_validation_email_validated": "true",
            "subscriptionterms_period": "monthly"
        },
    ),
)


@pytest.mark.parametrize("url,data", test_cases)
def test_smart_fee_covering(local_fastapi_client, url: str, data: Dict[str, Any]) -> None:
    response = local_fastapi_client.post(url, json=data)
    response_body = response.json()
    logger.info(response_body)
    assert response.status_code == 200
    assert response_body['raw_score_day'] >= 0
    assert response_body['raw_score_hour'] >= 0
    assert type(response_body['next_datetime']) is str
