import logging

import pytest
import requests

logger = logging.getLogger(__name__)


def test_monthly_upsell():
    response = requests.post(
        "http://mlapi:8000/predict_monthly_upsell",
        json={
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
    )
    logger.debug(response.json())
    assert response.status_code == 200
    assert response.json()["show_upsell"] in ["yes", "no", "default"]

