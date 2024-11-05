from logging import Logger
from typing import Any, Dict, NamedTuple

import pytest

from fundraiseup.service.mlapi import load_models

logger = Logger(__name__)

load_models(["predict_smart_fee_covering"])


class TestCase(NamedTuple):
    url: str
    data: Dict[str, Any]


test_cases = (
    TestCase(
        url="/predict_smart_fee_covering",
        data={
            'company_key': 'ABXBVMVA',
            'client_time_zone': 'America/Denver',
            'client_ip_country': 'US',
            'checkout_default_amount': 2500,
            'ua_major': '0',
            'ch_pres_mean': 26250.00,
            'page_view_num': 1,
            'os': 'iOS',
            'preset_frequency': '"annual"',
            'client_device_pixel_ratio': 2.00,
            'checkout_currency': 'USD',
            'client_weekday': '1',
            'client_ip_connection_type': 'Cable/DSL',
            'ua_history_length': 3
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
    assert response_body['fee_covering'] in ['defaultYes', 'defaultNo']
