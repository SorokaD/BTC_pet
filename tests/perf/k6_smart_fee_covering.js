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
        "company_key": "ABXBVMVA",
        "client_time_zone": "America/Denver",
        "client_ip_country": "US",
        "checkout_default_amount": 2500,
        "ua_major": "0",
        "ch_pres_mean": 26250.00,
        "page_view_num": 1,
        "os": "iOS",
        "preset_frequency": "annual",
        "client_device_pixel_ratio": 2.00,
        "checkout_currency": "USD",
        "client_weekday": "5",
        "client_ip_connection_type": "Cable/DSL",
        "ua_history_length": 3
    }

    return JSON.stringify(payload);
}

function getUrl() {
    return "http://10.26.71.1:8000/predict_smart_fee_covering";
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