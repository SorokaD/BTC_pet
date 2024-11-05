from logging import Logger
from typing import Any, Dict, NamedTuple

import pytest

from fundraiseup.service.mlapi import load_models

logger = Logger(__name__)

load_models(["predict_monthly_upsell"])


class TestCase(NamedTuple):
    url: str
    data: Dict[str, Any]


positive_test_cases = (
    TestCase(
        url="/predict_monthly_upsell",
        data={
            "event_time": "2024-04-01T00:00:00Z",
            "company_name": "company",
            "client_weekday": 1,
            "client_hour": 2,
            "client_time_zone": "timezone",
            "client_locale": "locale",
            "client_ip_country": "country",
            "client_ip_region": "region",
            "client_ip_city": "city",
            "is_mobile": True,
            "is_tablet": False,
            "device": "device",
            "device_model": "model",
            "ua_name": "name",
            "ua_language": "language",
            "ua_country": "country",
            "utm_source": "source",
            "utm_campaign": "campaign",
            "checkout_campaign_key": "key",
            "checkout_currency": "USD",
            "checkout_amount": 100,
            "checkout_in_usd_amount": 100,
            "checkout_currency_rate": 1.0,
            "checkout_default_amount": 100,
        },
    ),
)


@pytest.mark.parametrize("url,data", positive_test_cases)
def test_monthly_upsell_positive(local_fastapi_client, url: str, data: Dict[str, Any]) -> None:
    response = local_fastapi_client.post(url, json=data)
    response_body = response.json()
    logger.info(response_body)
    assert response.status_code == 200
    assert response_body["show_upsell"] in ["yes", "no", "default"]
