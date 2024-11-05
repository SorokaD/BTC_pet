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
        // Дата создания подписки
        "subscription_datetime": "2023-11-30T21:08:00+00:00",
        "first_failed_datetime": "2024-06-21T12:23:43+00:00",
        "subscriptionterms_currency": "USD",
        // Сумма в центах
        "subscriptionterms_amount_in_usd": 2680,
        "subscriptionterms_payment_method": "creditCard",
        // Brand || ""
        "subscriptionterms_brand": "MasterCard",
        // Как есть из базы
        "subscriptionterms_timezone": "America/New_York",
        "subscriptionterms_customer_address_country_code": "",
        "subscriptionterms_customer_address_city": "",
        "subscriptionterms_customer_address_region": "",
        "subscriptionterms_customer_title": "",
        // Именно строка
        "subscriptionterms_validation_email_validated": "true",
        "subscriptionterms_period": "monthly"
    }

    return JSON.stringify(payload);
}

function getUrl() {
    return "http://10.26.71.1:8000/predict_donation_retries";
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