from fastapi.testclient import TestClient

from fundraiseup.service.mlapi import load_models

load_models(["predict_default_frequency"])


def test_predict_default_frequency(local_fastapi_client: TestClient) -> None:
    response = local_fastapi_client.post(
        "/predict_default_frequency",
        json={
            "source": "modal_co",
            "company_key": "TEST",
            "element_key": "TEST",
            "checkout_campaign_key": "TEST",
            "checkout_currency": "USD",
            "checkout_in_usd_amount": 500,
            "client_locale": "en-US",
            "client_time_zone": "Africa/Johannesburg",
            "client_ip_country": "ZA",
            "client_ip_region": "Western Cape",
            "client_ip_city": "Cape Town",
            "client_ip_as_name": "AS",
            "device": "",
            "device_model": "",
            "os": "Windows",
            "ua_name": "Edge",
            "ua_language": "en",
            "ua_country": "US",
            "utm_source": "google",
            "client_hour": 20,
            "client_weekday": 4,
        },
    )
    response_body = response.json()
    print(response_body)
    assert response.status_code == 200
    assert response_body["use_predict"]
    assert "default_frequency" in response_body
    default_frequency = response_body["default_frequency"]
    assert default_frequency in ["once", "monthly"]