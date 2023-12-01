import requests
import logging
from typing import Optional, Dict

logger = logging.getLogger(__name__)


def get_exchange_rate(currency_code: str) -> Optional[float]:
    """
    Fetches the exchange rates for the given currency code relative
    to the EUR (base currency):

    The API that is used in the solution where the data is fetched:

    EUR: https://open.er-api.com/v6/latest/EUR
    USD: https://open.er-api.com/v6/latest/USD
    GBP: https://open.er-api.com/v6/latest/GBP

    Args:
    currency_code (str): The currency code to fetch the exchange rate for.

    Returns:
    float: The exchange rate for the given currency code, or None if not found.
    """
    try:
        response = requests.get(f"https://open.er-api.com/v6/latest/EUR")
        rates = response.json().get('rates', {})
        rate = rates.get(currency_code, None)
        if rate is not None:
            logger.info(f"Exchange rate for {currency_code}: {rate}")
        else:
            logger.warning(f"No exchange rate found for {currency_code}")
        return rate
    except requests.RequestException as e:
        logger.error(f"Error fetching exchange rate for {currency_code}: {e}")
        return None


def fetch_exchange_rates() -> Dict[str, float]:
    """
    Fetches exchange rates for all currencies relative to EUR.

    The API that is used in the solution where the data is fetched:

    EUR: https://open.er-api.com/v6/latest/EUR
    USD: https://open.er-api.com/v6/latest/USD
    GBP: https://open.er-api.com/v6/latest/GBP

    Returns:
    Dict[str, float]: A dictionary of currency codes and their exchange rates.
    """
    try:
        response = requests.get("https://open.er-api.com/v6/latest/EUR")
        return response.json().get('rates', {})
    except requests.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        return {}
