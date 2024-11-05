import { check, sleep } from "k6";
import http from "k6/http";

export const options = {
    // duration: '1m',
    vus: 1,
    userAgent: "k6-load-testing",
    stages: [
        // Linearly ramp up from 1 to 50 VUs during first minute
        { target: 50, duration: "0s" },
        // Hold at 50 VUs for the next 3 minutes and 30 seconds
        // {target: 100, duration: "10s"},
        // {target: 150, duration: "20s"},
        // Linearly ramp down from 50 to 0 50 VUs over the last 30 seconds
        { target: 250, duration: "60s" },
        // Total execution time will be ~5 minutes
    ],
};

function getPayload() {
    const payload = {
        "event_time": "",
        "company_name": "string",
        "client_weekday": 0,
        "client_hour": 0,
        "client_time_zone": "America/New_York",
        "client_locale": "en_GB",
        "client_ip_country": "US",
        "client_ip_region": "NY",
        "client_ip_city": "NY",
        "is_mobile": true,
        "is_tablet": true,
        "device": "string",
        "device_model": "string",
        "ua_name": "string",
        "ua_language": "string",
        "ua_country": "string",
        "utm_source": "string",
        "utm_campaign": "string",
        "checkout_campaign_key": "string",
        "checkout_currency": "string",
        "checkout_amount": 0,
        "checkout_in_usd_amount": 0,
        "checkout_currency_rate": 0,
        "checkout_default_amount": 0
    }

    return JSON.stringify(payload);
}

function getUrl() {
    return "http://10.26.71.1:8000/predict_monthly_upsell/v2";
}

export default function () {
    const res = http.post(getUrl(), getPayload(), {
        headers: {
            "content-type": "application/json"
        },
    });
    check(res, {
        "is status 200": (r) => {
            console.log(r.body);
            return r.status === 200;
        },
    });
    sleep(1);
}