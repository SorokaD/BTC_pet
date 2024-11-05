import { check, sleep } from "k6";
import http from "k6/http";

export const options = {
    duration: '1m',
    vus: 250,
    userAgent: "k6-load-testing"
};

function getPayload() {
    const payload = {
        "checkout_campaign_key": "TEST",
        "checkout_currency": "USD",
        "checkout_in_usd_amount": 500,
        "client_hour": 20,
        "client_ip_city": "Cape Town",
        "client_ip_country": "ZA",
        "client_ip_region": "Western Cape",
        "client_locale": "en-US",
        "client_time_zone": "Africa/Johannesburg",
        "client_ip_as_name": "AS",
        "client_weekday": 4,
        "company_key": "TEST",
        "device": "",
        "device_model": "",
        "element_key": "TEST",
        "os": "Windows",
        "source": "modal_co",  
        "ua_country": "US",
        "ua_language": "en",
        "ua_name": "Edge",
        "utm_source": "thunderbird.net"
      }

    return JSON.stringify(payload);
}

function getUrl() {
    return "http://10.26.71.1:8000/predict_default_frequency";
}

export default function () {
    const res = http.post(getUrl(), getPayload(), {
        headers: {
            "content-type": "application/json"
        },
    });
    check(res, {
        "is status 200": (r) => {
            return r.status === 200;
        },
    });
    sleep(1);
}