import json
from datetime import datetime, timedelta, timezone

from django.conf import settings
from django.core.cache import cache

from apps.common.services.cyphers import AESCypher


def is_encrypted_token_valid(encrypted_message):
    """
    encrypted_message should be a string format of JSON data
    the JSON data should have keys: session and timestamp
        {
            "session": "random_string",  # device session
            "created_time": "2021-09-01 00:00:00.000000+0000",
        }
    """

    aes_cipher = AESCypher(settings.AES_KEY)

    try:
        decrypted_message = aes_cipher.decrypt(encrypted_message)
        data = json.loads(decrypted_message)

        # Define the format of the input string
        date_format = "%Y-%m-%d %H:%M:%S.%f%z"
        # Convert string to datetime object
        created_time = datetime.strptime(data["created_time"], date_format)

        # get current time in UTC
        current_time_utc = datetime.now(timezone.utc)
        difference = current_time_utc - created_time

        if difference < timedelta(seconds=30) and cache.get(encrypted_message) is None:
            # set token to cache for 30 seconds, so that it can't be used again
            cache.set(encrypted_message, True, timeout=30)

            return True

        return False
    except Exception as e:
        print("Exception: ", e)
        return False
