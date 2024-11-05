from logging import Logger
from typing import Any, Dict, NamedTuple

import pytest

from fundraiseup.service.mlapi import load_models

logger = Logger(__name__)

load_models(["predict_smart_fee_covering_v2"])


class TestCase(NamedTuple):
    url: str
    data: Dict[str, Any]


test_cases = (
    TestCase(
        url="/predict_smart_fee_covering/v2",
        data={
            "company_key": "AGZKYDGZ",
            "session_lifetime": 1029,
            "session_start_source": "google",
            "event_num": 5,
            "client_lifetime": 11778,
            "client_locale": "en-CA",
            "client_time_zone": "America/Toronto",
            "client_ip_country": "CA",
            "client_ip_region": "Ontario",
            "client_battery_level": 1.00,
            "page_view_num": 1,
            "device": "",
            "device_model": "",
            "os": "Windows",
            "ua_name": "Chrome",
            "ua_language": "en",
            "ua_country": "US",
            "ua_history_length": 4,
            "element_locale": "en-CA",
            "checkout_currency": "CAD",
            "checkout_default_amount_usd": 21.94,
            "checkout_amount_usd": 45.43
        },
    ),
)


@pytest.mark.parametrize("url,data", test_cases)
def test_smart_fee_covering(local_fastapi_client, url: str, data: Dict[str, Any]) -> None:
    response = local_fastapi_client.post(url, json=data)
    response_body = response.json()
    logger.info(response_body)
    assert response.status_code == 200
    assert response_body['raw_score'] >= 0
    assert response_body['fee_covering'] in ['defaultYes', 'defaultNo', None]
