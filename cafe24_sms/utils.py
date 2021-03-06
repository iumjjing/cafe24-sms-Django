from django.utils import timezone
from django.utils.timezone import is_aware
from django.utils.timezone import make_aware

import pytz

from .settings import module_settings


def get_local_datetime(datetime):
    user_tz_name = module_settings.TIMEZONE or timezone.get_current_timezone_name()
    user_tz = pytz.timezone(user_tz_name)

    if datetime.tzinfo:
        return datetime.astimezone(user_tz)
    else:
        system_tz = timezone.get_current_timezone()
        return system_tz.localize(datetime).astimezone(user_tz)


def trans_string_to_datetime(date, date_format):
    ret = timezone.datetime.strptime(date, date_format)
    if not is_aware(ret):
        # Cafe24's result timezone is Asia/Seoul
        return make_aware(ret).replace(tzinfo=pytz.timezone('Asia/Seoul'))
    return ret
