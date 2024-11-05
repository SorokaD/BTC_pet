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
        "date": "2024-05-01",
        "touchpoint": "email",
        "company_key": "DSADA",
        "recurring_key": "FSASD",
        "currency": "USD",
        "charge_amount": 2.0,
        "charge_amount_in_usd": 50.0,
        "payment_method": "card",
        "installment": 0
    }

    return JSON.stringify(payload);
}

function getUrl() {
    return "http://10.26.71.1:8000/predict_subscription_upsell";
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