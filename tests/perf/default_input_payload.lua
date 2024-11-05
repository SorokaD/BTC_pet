wrk.method = "POST"
wrk.body = [[{
    "company_key": "TEST",
    "checkout_campaign_key": "TEST",
    "client_locale": "en-US",
    "client_time_zone": "Africa/Johannesburg",
    "client_ip_country": "ZA", 
    "client_ip_region": "Western Cape",
    "client_ip_city": "Cape Town",
    "device": "",
    "device_model": "",
    "os": "Windows",
    "ua_name": "Edge",
    "ua_language": "en",
    "ua_country": "US",
    "utm_source": "thunderbird.net",
    "checkout_currency": "ZAR",
    "checkout_currency_rate": 19.061460494995117,
    "client_hour": 20,
    "client_weekday": 4
}]]
wrk.headers["Content-Type"] = "application/json"
