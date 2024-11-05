from locust import HttpUser, task, TaskSet
'''
for run test use command:
locust -f locustfile.py --host=http://localhost:8000
на stage:
locust -f locustfile.py --host=http://135.148.34.150:8000
с выгрузкой результатов в csv:
locust -f locustfile.py --headless -u 100 -r 10 --run-time 1m --csv=results --host=http://localhost:8000
'''


class SmartFeeCovering(TaskSet):
    smart_fee_covering = {
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

    @task(1)
    def sfc(self):
        response = self.client.post("/predict_smart_fee_covering", json=self.smart_fee_covering)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"


class MonthlyUpsell(TaskSet):
    monthly_upsell = {
        "event_time": "",
        "company_name": "string",
        "client_weekday": 0,
        "client_hour": 0,
        "client_time_zone": "America/New_York",
        "client_locale": "en_GB",
        "client_ip_country": "US",
        "client_ip_region": "NY",
        "client_ip_city": "NY",
        "is_mobile": "true",
        "is_tablet": "true",
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

    @task(1)
    def mu(self):
        response = self.client.post("/predict_monthly_upsell", json=self.monthly_upsell)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"


class DefaultAmounts(TaskSet):
    default_amounts = {
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
        "client_weekday": 4,
    }

    @task(1)
    def da(self):
        response = self.client.post("/predict_default_amounts", json=self.default_amounts)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"


class DefaultInput(TaskSet):
    default_input = {
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
    }

    @task(1)
    def di(self):
        response = self.client.post("/predict_default_input", json=self.default_input)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"


class PostDonationUpsell(TaskSet):
    post_donation_upsell = {
        "company_key": "key",
        "checkout_amount": 1000,
        "checkout_currency": "USD",
        "checkout_in_usd_amount": 1000,
        "client_ip_region": "region",
        "client_ip_country": "country",
        "client_time_zone": "timezone",
        "client_hour": 1,
        "client_weekday": 1,
        "client_ip_city": "city",
        "client_locale": "locale",
        "ua_name": "name",
        "ua_language": "language",
        "ua_country": "country",
        "device": "device",
        "device_model": "model",
        "os": "Windows",
        "utm_source": "source"
    }

    @task(1)
    def pdu(self):
        response = self.client.post("/predict_post_donation_upsell", json=self.post_donation_upsell)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"


class SubscriptionUpsell(TaskSet):
    subscription_upsell = {
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

    @task(1)
    def su(self):
        response = self.client.post("/predict_subscription_upsell", json=self.subscription_upsell)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"


class DonationRetries(TaskSet):
    donation_retries = {
        "subscription_datetime": "2023-11-30T21:08:00+00:00",
        "first_failed_datetime": "2024-06-27T12:23:43+00:00",
        "subscriptionterms_currency": "USD",
        "subscriptionterms_amount_in_usd": 2680,
        "subscriptionterms_payment_method": "creditCard",
        "subscriptionterms_brand": "MasterCard",
        "subscriptionterms_timezone": "America/New_York",
        "subscriptionterms_customer_address_country_code": "",
        "subscriptionterms_customer_address_city": "",
        "subscriptionterms_customer_address_region": "",
        "subscriptionterms_customer_title": "",
        "subscriptionterms_validation_email_validated": "true",
        "subscriptionterms_period": "monthly"
    }

    @task(1)
    def su(self):
        response = self.client.post("/predict_donation_retries", json=self.donation_retries)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"


class WebsiteUser(HttpUser):
    tasks = {DonationRetries: 1}

    def on_start(self):
        """This function will be called when a simulated user starts"""
        pass

    def on_stop(self):
        """This function will be called when a simulated user stops"""
        pass
