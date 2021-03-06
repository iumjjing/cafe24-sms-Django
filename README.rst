=============================
Cafe24 SMS module for Django
=============================

Python 2 & 3 compatible

.. image:: https://travis-ci.org/iumjjing/cafe24-sms-Django.svg?branch=master
    :target: https://travis-ci.org/iumjjing/cafe24-sms-Django/
.. image:: https://coveralls.io/repos/github/iumjjing/cafe24-sms-Django/badge.svg?branch=feature%2Ftravis
    :target: https://coveralls.io/github/iumjjing/cafe24-sms-Django?branch=feature%2Ftravis

- Source code: `<https://github.com/iumjjing/cafe24-sms-Django>`_
- Distribution: `<https://pypi.python.org/pypi/cafe24-sms-Django>`_
- Maintainer: `<https://github.com/hwshim0810>`_

Installation
------------

You can install the library directly from pypi using pip:

.. code-block:: shell

    $ pip install cafe24-sms-Django

Edit your settings.py file:

.. code-block:: python

    CAFE24_SMS_SETTINGS = {
        # Required
        'USER_ID': 'Your cafe24 id',
        'SECURE_KEY': 'Your secure key',
        'SENDER': 'Your telephone number ex) 000-0000 or 000-0000-0000',

        # Optional (If you want using default value, delete lines)
        'REQUEST_TIMEOUT': 30.0,
        'TEST_MODE': False,
        'CHARSET': 'euc-kr',
        'TIMEZONE': 'Asia/Seoul',
    }

Dependencies
------------

- Python 2.7 or 3.4+
- Django 1.11+

Quickstart
----------

Send sms message to use shortcut function

.. code-block:: python

    import cafe24_sms

    try:
        # Send single SMS
        cafe24_sms.send_message(message='message', receiver='will receive telephone number or number list')

    except SMSModuleException as e:
        print(e)

- Send function returning Tuple(Result code, Remaining sms count)
- If message byte length over 90, Message will be send lms type.
- Receiver format: Single number('000-000-000') or Number list(['000-000-000','000-000-000'])

More usage
----------

Send / Reserve SMS message

.. code-block:: python

    from django.utils import timezone

    import cafe24_sms

    try:
        # Reserve single SMS
        cafe24_sms.reserve_message(
            message='message',
            receiver='will receive telephone number or number list',
            reservation_time=timezone.now(),
        )

        # Send multiple SMS
        cafe24_sms.send_message(
            message='message',
            receiver=['telephone number', '...'],
        )

        # Reserve multiple SMS
        cafe24_sms.reserve_message(
            message='message',
            receiver=['telephone number', '...'],
            reservation_time=timezone.now(),
        )

        # Send message repeat 3 times, gap 15 minutes
        cafe24_sms.send_message(
            message='message',
            receiver='telephone number',
            rpt_num=3,
            rpt_time=15,
        )

    except SMSModuleException as e:
        print(e)



--------------

Check the result of sent SMS.

.. code-block:: python

    from django.utils import timezone

    import cafe24_sms

    data = cafe24_sms.result_check(start_date=timezone.now())

    total_count = data.get_total_count()
    result_records = data.get_records()


- If you need more detail, see method doc.

Contributors
------------

See https://github.com/iumjjing/cafe24-sms-Django/graphs/contributors
