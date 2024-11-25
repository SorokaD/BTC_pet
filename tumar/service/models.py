from typing import Literal

from pydantic import BaseModel, ValidationError, model_validator  # type: ignore


class ErrorMessage(BaseModel):
    message: str


class ModelRequest(BaseModel):
    category: str
    symbol: str
    price: float
    time: int
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "category": "price",
                    "symbol": "BTCUSDT",
                    "price": 10000.0,
                    "time": 1631510400,
                }
            ]
        }
    }


class ModelResponse(BaseModel):
    use_predict: bool
    symbol: str
    side: str
    quantity: float


class MonthlyUpsellRequest(BaseModel):
    event_time: str

    company_name: str

    client_weekday: int
    client_hour: int
    client_time_zone: str
    client_locale: str
    client_ip_country: str
    client_ip_region: str
    client_ip_city: str

    is_mobile: bool
    is_tablet: bool
    device: str
    device_model: str
    ua_name: str
    ua_language: str
    ua_country: str

    utm_source: str
    utm_campaign: str

    checkout_campaign_key: str
    checkout_currency: str

    checkout_amount: int
    checkout_in_usd_amount: int
    checkout_currency_rate: float
    checkout_default_amount: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "event_time": "2021-09-01T12:00:00",
                    "company_name": "TEST",
                    "client_weekday": 4,
                    "client_hour": 20,
                    "client_time_zone": "Africa/Johannesburg",
                    "client_locale": "en-US",
                    "client_ip_country": "ZA",
                    "client_ip_region": "Western Cape",
                    "client_ip_city": "Cape Town",
                    "is_mobile": False,
                    "is_tablet": False,
                    "device": "",
                    "device_model": "",
                    "ua_name": "Edge",
                    "ua_language": "en",
                    "ua_country": "US",
                    "utm_source": "thunderbird.net",
                    "utm_campaign": "test",
                    "checkout_campaign_key": "TEST",
                    "checkout_currency": "USD",
                    "checkout_amount": 100,
                    "checkout_in_usd_amount": 5,
                    "checkout_currency_rate": 20,
                    "checkout_default_amount": 100,
                }
            ]
        }
    }


class MonthlyUpsellResponse(BaseModel):
    id: int
    show_upsell: Literal["yes", "no", "default"]
    score: float
    meta: dict[str, str]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "show_upsell": "yes",
                    "score": 0.8,
                    "meta": {
                        "model_name": "predict_monthly_upsell",
                        "model_version": "0.1.2",
                        "algorithm_name": "catboost",
                    },
                },
            ]
        }
    }


class SubscriptionUpsellRequest(BaseModel):
    date: str
    touchpoint: Literal["email", "portal"]
    company_key: str
    recurring_key: str
    currency: str
    charge_amount: float
    charge_amount_in_usd: float
    payment_method: str
    installment: int = 0

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "date": "2021-09-01",
                    "touchpoint": "email",
                    "company_key": "TEST",
                    "recurring_key": "TEST",
                    "currency": "USD",
                    "charge_amount": 100,
                    "charge_amount_in_usd": 5,
                    "payment_method": "card",
                    "installment": 0,
                }
            ]
        }
    }


class SubscriptionUpsellResponse(BaseModel):
    id: int
    use_predict: bool = False
    upgrade_buttons: list[int] | None = None
    raw_score: list[float] | None = None
    meta: dict[str, str]

    @model_validator(mode="after")
    @classmethod
    def check_upgrade_buttons(cls, values):
        if not values.use_predict:
            if values.upgrade_buttons or values.raw_score:
                raise ValidationError("Upgrade buttons are provided for non-upsell")
        else:
            if not values.upgrade_buttons or not values.raw_score:
                raise ValidationError("Upgrade buttons are not provided for upsell")
        return values

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "use_predict": True,
                    "upgrade_buttons": [100, 200, 300],
                    "raw_score": [0.8, 0.2, 0.1],
                    "meta": {
                        "model_name": "predict_subscription_upsell",
                        "model_version": "0.1.2",
                        "algorithm_name": "quantile",
                    },
                },
                {
                    "id": 1,
                    "use_predict": False,
                    "upgrade_buttons": None,
                    "raw_score": None,
                    "meta": {
                        "model_name": "predict_subscription_upsell",
                        "model_version": "0.1.2",
                        "algorithm_name": "quantile",
                    },
                },
            ]
        }
    }


class BaseRequest(BaseModel):
    ...


class BaseResponse(BaseModel):
    ...


class PDURequest(BaseRequest):
    company_key: str

    checkout_amount: int
    checkout_currency: str
    checkout_in_usd_amount: int

    client_ip_region: str
    client_ip_country: str
    client_time_zone: str
    client_hour: int
    client_weekday: int
    client_ip_city: str
    client_locale: str

    ua_name: str
    ua_language: str
    ua_country: str
    device: str
    device_model: str
    os: str
    utm_source: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "company_key": "TEST",
                    "checkout_amount": 100,
                    "checkout_currency": "USD",
                    "checkout_in_usd_amount": 5,
                    "client_ip_region": "Western Cape",
                    "client_ip_country": "ZA",
                    "client_time_zone": "Africa/Johannesburg",
                    "client_hour": 20,
                    "client_weekday": 4,
                    "client_ip_city": "Cape Town",
                    "client_locale": "en-US",
                    "ua_name": "Edge",
                    "ua_language": "en",
                    "ua_country": "US",
                    "device": "",
                    "device_model": "",
                    "os": "Windows",
                    "utm_source": "thunderbird.net",
                }
            ]
        }
    }


class PDUResponse(BaseResponse):
    use_predict: bool
    pdu_amount: int | None
    raw_score: float | None
    meta: dict[str, str]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "use_predict": True,
                    "pdu_amount": 100,
                    "raw_score": 0.8,
                    "meta": {
                        "model_name": "predict_post_donation_upsell",
                        "model_version": "0.1.2",
                        "algorithm_name": "catboost",
                    },
                },
                {
                    "use_predict": False,
                    "pdu_amount": None,
                    "raw_score": None,
                    "meta": {
                        "model_name": "predict_post_donation_upsell",
                        "model_version": "0.1.2",
                        "algorithm_name": "catboost",
                    },
                },
            ]
        }
    }


class DefaultInputRequest(BaseRequest):
    company_key: str
    checkout_campaign_key: str

    client_locale: str
    client_time_zone: str
    client_ip_country: str
    client_ip_region: str
    client_ip_city: str

    device: str
    device_model: str
    os: str

    ua_name: str
    ua_language: str
    ua_country: str
    utm_source: str

    checkout_currency: str
    checkout_currency_rate: float

    client_hour: int
    client_weekday: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
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
            ]
        }
    }


class DefaultInputResponse(BaseResponse):
    use_predict: bool
    default_amount: dict[str, int]
    meta: dict[str, str]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "use_predict": True,
                    "default_amount": {
                        "once": 100,
                        "monthly": 200,
                    },
                    "meta": {
                        "model_name": "predict_default_input",
                        "model_version": "0.1.4",
                        "algorithm_name": "lightgbm",
                    },
                },
                {
                    "use_predict": False,
                    "default_amount": {},
                    "meta": {
                        "model_name": "predict_default_input",
                        "model_version": "0.1.4",
                        "algorithm_name": "lightgbm",
                    },
                },
            ]
        }
    }


class SmartFeeCoveringRequest(BaseRequest):
    company_key: str
    client_time_zone: str
    client_ip_country: str
    checkout_default_amount: int
    ua_major: str
    ch_pres_mean: float
    page_view_num: int
    os: str
    preset_frequency: str
    client_device_pixel_ratio: float
    checkout_currency: str
    client_weekday: str
    client_ip_connection_type: str
    ua_history_length: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "company_key": "TEST",
                    "client_time_zone": "Africa/Johannesburg",
                    "client_ip_country": "ZA",
                    "checkout_default_amount": 100,
                    "ua_major": "1",
                    "ch_pres_mean": 0.5,
                    "page_view_num": 10,
                    "os": "Windows",
                    "preset_frequency": "monthly",
                    "client_device_pixel_ratio": 1.5,
                    "checkout_currency": "USD",
                    "client_weekday": "4",
                    "client_ip_connection_type": "wifi",
                    "ua_history_length": 10,
                }
            ]
        }
    }


class SmartFeeCoveringResponse(BaseResponse):
    use_predict: bool
    fee_covering: Literal["defaultYes", "defaultNo"]
    raw_score: float | None
    meta: dict[str, str]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "use_predict": True,
                    "raw_score": 0.8,
                    "meta": {
                        "model_name": "predict_smart_fee_covering",
                        "model_version": "0.1.2",
                        "algorithm_name": "catboost",
                    },
                },
                {
                    "use_predict": False,
                    "raw_score": None,
                    "meta": {
                        "model_name": "predict_smart_fee_covering",
                        "model_version": "0.1.2",
                        "algorithm_name": "catboost",
                    },
                },
            ]
        }
    }


class DefaultAmountRequest(DefaultInputRequest):
    pass


class DefaultAmountResponse(BaseModel):
    use_predict: bool
    default_amount: dict[str, int]
    presets: dict[str, list[int]]
    meta: dict[str, str]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "use_predict": True,
                    "default_amount": {
                        "once": 100,
                        "monthly": 200,
                    },
                    "presets": {
                        "once": [100, 200, 300, 400, 500, 600],
                        "monthly": [200, 300, 400, 500, 600, 700],
                    },
                    "meta": {
                        "model_name": "predict_default_amounts",
                        "model_version": "0.1.4",
                        "algorithm_name": "lightgbm",
                    },
                },
                {
                    "use_predict": False,
                    "default_amount": {},
                    "presets": {},
                    "meta": {
                        "model_name": "predict_default_amounts",
                        "model_version": "0.1.4",
                        "algorithm_name": "lightgbm",
                    },
                },
            ]
        }
    }


class DonationRetriesRequest(BaseRequest):
    subscription_datetime: str
    first_failed_datetime: str
    subscriptionterms_currency: str
    subscriptionterms_amount_in_usd: int
    subscriptionterms_payment_method: str
    subscriptionterms_brand: str
    subscriptionterms_timezone: str
    subscriptionterms_customer_address_country_code: str
    subscriptionterms_customer_address_city: str
    subscriptionterms_customer_address_region: str
    subscriptionterms_customer_title: str
    subscriptionterms_validation_email_validated: str
    subscriptionterms_period: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "subscription_datetime": "2023-11-30T21:08:00+00:00",
                    "first_failed_datetime": "2024-07-06T12:23:43+00:00",
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
                    "subscriptionterms_period": "monthly",
                }
            ]
        }
    }


class DonationRetriesResponse(BaseResponse):
    use_predict: bool
    next_datetime: str
    raw_score_day: float | None
    raw_score_hour: float | None
    meta: dict[str, str]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "use_predict": True,
                    "next_datetime": "2024-07-12T12:43:14+00:00",
                    "raw_score_day": 0.8573729044190868,
                    "raw_score_hour": 0.3633262932762778,
                    "meta": {
                        "model_name": "predict_donation_retries",
                        "model_version": "0.1.1",
                        "algorithm_name": "catboost",
                    },
                },
                {
                    "use_predict": False,
                    "next_datetime": "",
                    "raw_score_day": 0.0,
                    "raw_score_hour": 0.0,
                    "meta": {
                        "model_name": "predict_donation_retries",
                        "model_version": "0.1.1",
                        "algorithm_name": "catboost",
                    },
                },
            ]
        }
    }


class DefaultFrequencyRequest(BaseRequest):
    source: Literal["modal_co", "pages"]
    company_key: str
    checkout_campaign_key: str
    element_key: str

    client_locale: str
    client_time_zone: str
    client_ip_country: str
    client_ip_region: str
    client_ip_city: str
    client_ip_as_name: str
    client_hour: int
    client_weekday: int

    device: str
    device_model: str
    os: str
    ua_name: str
    ua_language: str
    ua_country: str
    utm_source: str

    checkout_currency: str
    checkout_in_usd_amount: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
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
                }
            ]
        }
    }


class DefaultFrequencyResponse(BaseResponse):
    use_predict: bool
    default_frequency: str | None
    raw_score: float | None
    meta: dict[str, str]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "use_predict": True,
                    "default_frequency": "monthly",
                    "raw_score": 0.8,
                    "meta": {
                        "model_name": "predict_frequency_order",
                        "model_version": "0.1.2",
                        "algorithm_name": "catboost",
                    },
                },
                {
                    "use_predict": False,
                    "default_frequency": None,
                    "raw_score": -0.1,
                    "meta": {
                        "model_name": "predict_frequency_order",
                        "model_version": "0.1.2",
                        "algorithm_name": "catboost",
                    },
                },
            ]
        }
    }


class SmartFeeCoveringv2Request(BaseRequest):

    company_key: str
    session_lifetime: int
    session_start_source: str
    event_num: int
    client_lifetime: int
    client_locale: str
    client_time_zone: str
    client_ip_country: str
    client_ip_region: str
    client_battery_level: float
    page_view_num: int
    device: str
    device_model: str
    os: str
    ua_name: str
    ua_language: str
    ua_country: str
    ua_history_length: int
    element_locale: str
    checkout_currency: str
    checkout_default_amount_usd: float
    checkout_amount_usd: float

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "company_key": "AYSVKLHR",
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
                    "checkout_amount_usd": 90.43,
                }
            ]
        }
    }


class SmartFeeCoveringv2Response(BaseResponse):
    use_predict: bool
    fee_covering: Literal["defaultYes", "defaultNo"] | None
    raw_score: float | None
    meta: dict[str, str]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "use_predict": True,
                    "fee_covering": "defaultYes",
                    "raw_score": 0.8,
                    "meta": {
                        "model_name": "predict_smart_fee_covering_uplift",
                        "model_version": "0.2.1",
                        "algorithm_name": "uplift",
                    },
                },
                {
                    "use_predict": False,
                    "fee_covering": None,
                    "raw_score": 0.0,
                    "meta": {
                        "model_name": "predict_smart_fee_covering_uplift",
                        "model_version": "0.2.1",
                        "algorithm_name": "uplift",
                    },
                },
            ]
        }
    }
