from os import environ
import os


SESSION_CONFIGS = [
    dict(
        name='lottery_survey',
        display_name="Lottery Survey",
        num_demo_participants=1,
        app_sequence=['lottery_survey']
    ),
]

INSTALLED_APPS = ['otree', 'lottery_survey']

ROOMS = [
    dict(
        name='lottery_survey_room',
        display_name='Lottery Survey Room',
        participant_label_file='_rooms/lottery_survey_room.txt'
    ),
]


SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

LANGUAGE_CODE = 'en'

REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '4309283859282'
