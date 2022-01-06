"""
----------------------------------------------------------------------------
    ##     ##        ###        ########
    ###   ###       ## ##       ##     ##
    #### ####      ##   ##      ##     ##
    ## ### ##     ##     ##     ##     ##
    ##     ##     #########     ##     ##
    ##     ## ### ##     ## ### ##     ## ###
    ##     ## ### ##     ## ### ########  ###

MAD - M1ch3al Autonomous Drone

Author: SIROLA RENATO
 Email: renato.sirola@gmail.com
----------------------------------------------------------------------------
"""

import datetime
import time
import calendar
from datetime import timedelta
from datetime import datetime


def epoch2date(epoch):
    t = time.gmtime(epoch)
    return datetime(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)


DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"


def date2epoch(date):
    return int(calendar.timegm(date.timetuple()))


def date2string(dt):
    return dt.strftime(DATETIME_FORMAT)


def date2string_with_format(date, date_format):
    return date.strftime(date_format)


def string2date(date_string):
    return datetime.strptime(date_string, DATETIME_FORMAT)


def string2date_with_format(date_string, date_format):
    return datetime.strptime(date_string, date_format)


def from_str(description, is_utc=True):
    if is_utc:
        now = datetime.utcnow()
    else:
        now = datetime.now()
    if description.strip() == 'midnight':
        return datetime(now.year, now.month, now.day)
    if description.strip() == 'yesteday midnight':
        return datetime(now.year, now.month, now.day) - timedelta(days=1)
    if description.strip() == 'now':
        return now

