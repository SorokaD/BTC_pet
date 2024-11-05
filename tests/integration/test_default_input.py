from logging import Logger
from typing import Any, Dict, NamedTuple

import pytest

from fundraiseup.service.mlapi import load_models

logger = Logger(__name__)

load_models(["predict_default_input"])


class TestCase(NamedTuple):
    url: str
    data: Dict[str, Any]


positive_test_cases = (
    TestCase(
        url="/predict_default_input",
        data={
            "company_key": "TEST",
            "checkout_campaign_key": "TEST",
            "client_locale": "en-US",
            "client_time_zone": "Africa/Johannesburg",
            "client_ip_country": "ZA",
            "client_ip_region": "Western Cape",
            "client_ip_city": "Cape Town",
            "device": "",
            "device_model": "",
            "os": "Windows",
            "ua_name": "Edge",
            "ua_language": "en",
            "ua_country": "US",
            "utm_source": "thunderbird.net",
            "checkout_currency": "ZAR",
            "checkout_currency_rate": 19.061460494995117,
            "client_hour": 20,
            "client_weekday": 4
        },
    ),
)


negative_test_cases = (
    TestCase(
        url="/predict_default_input",
        data={
            "company_key": "TEST",
            "checkout_campaign_key": "TEST",
            "client_locale": "en-US",
            "client_time_zone": "Africa/Johannesburg",
            "client_ip_country": "ZA",
            "client_ip_region": "Western Cape",
            "client_ip_city": "Cape Town",
            "device": "",
            "device_model": "",
            "os": "Windows",
            "ua_name": "Edge",
            "ua_language": "en",
            "ua_country": "US",
            "utm_source": "thunderbird.net",
            "checkout_currency": "ZAR",
            "client_hour": 20,
            "client_weekday": 4
        },
    ),
)


@pytest.mark.parametrize("url,data", positive_test_cases)
def test_default_input_positive(local_fastapi_client, url: str, data: Dict[str, Any]) -> None:
    response = local_fastapi_client.post(url, json=data)
    response_body = response.json()
    logger.info(response_body)
    assert response.status_code == 200
    assert response_body["use_predict"]
    assert type(response_body["default_amount"]) is dict
    assert type(response_body["default_amount"]["monthly"]) is int
    assert type(response_body["default_amount"]["once"]) is int
    assert type(response_body["meta"]) is dict


@pytest.mark.parametrize("url,data", negative_test_cases)
def test_default_input_negative_no_currency_rate(local_fastapi_client, url: str, data: Dict[str, Any]) -> None:
    response = local_fastapi_client.post(url, json=data)
    assert 400 <= response.status_code <= 500
