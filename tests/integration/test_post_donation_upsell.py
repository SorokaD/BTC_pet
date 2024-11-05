from logging import Logger
from typing import Any, Dict, NamedTuple

import pytest

from fundraiseup.service.mlapi import load_models

logger = Logger(__name__)

load_models(["predict_post_donation_upsell"])


class TestCase(NamedTuple):
    url: str
    data: Dict[str, Any]


positive_test_cases = (
    TestCase(
        url="/predict_post_donation_upsell",
        data={
            "company_key": "key",
            "checkout_amount": 1000,
            "checkout_currency": "USD",
            "checkout_in_usd_amount": 1000,
            "client_ip_region": "region",
            "client_ip_country": "country",
            "client_time_zone": "timezone",
            "client_hour": 1,
            "client_weekday": 1,
            "client_ip_city": "city",
            "client_locale": "locale",
            "ua_name": "name",
            "ua_language": "language",
            "ua_country": "country",
            "device": "device",
            "device_model": "model",
            "os": "Windows",
            "utm_source": "source",
        },
    ),
)


negative_test_cases = (
    TestCase(
        url="/predict_post_donation_upsell",
        data={
            "company_key": "key",
            "checkout_amount": 300000,
            "checkout_currency": "USD",
            "checkout_in_usd_amount": 300000,
            "client_ip_region": "region",
            "client_ip_country": "country",
            "client_time_zone": "timezone",
            "client_hour": 1,
            "client_weekday": 1,
            "client_ip_city": "city",
            "client_locale": "locale",
            "ua_name": "name",
            "ua_language": "language",
            "ua_country": "country",
            "device": "device",
            "device_model": "model",
            "os": "Windows",
            "utm_source": "source",
        },
    ),
)


@pytest.mark.parametrize("url,data", positive_test_cases)
def test_post_donation_upsell_positive(local_fastapi_client, url: str, data: Dict[str, Any]) -> None:
    response = local_fastapi_client.post(url, json=data)
    response_body = response.json()
    logger.info(response_body)
    assert response.status_code == 200

    assert response_body["use_predict"]
    assert response_body["pdu_amount"] > 0
    assert response_body["pdu_amount"] < 1000
    assert response_body["pdu_amount"] % 100 == 0

    assert response_body["raw_score"] > 0.0


@pytest.mark.skip
@pytest.mark.parametrize("url,data", negative_test_cases)
def test_post_donation_upsell_negative(local_fastapi_client, url: str, data: Dict[str, Any]) -> None:
    response = local_fastapi_client.post(url, json=data)
    response_body = response.json()
    logger.info(response_body)
    assert response.status_code == 200

    assert not response_body["use_predict"]
    assert response_body["pdu_amount"] is None
    assert response_body["raw_score"] is None
