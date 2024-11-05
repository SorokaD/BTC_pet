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
    }

    return JSON.stringify(payload);
}

function getUrl() {
    return "http://10.26.71.1:8000/predict_smart_fee_covering/v2";
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