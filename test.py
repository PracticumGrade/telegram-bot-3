from unittest.mock import patch

try:
    import requests
except ImportError:
    raise AssertionError('Модуль requests не установлен. Посмотрите в README, что нужно для этого сделать.')

try:
    import telegram
    from telegram import Bot
    from telegram.ext import Updater
except ImportError:
    raise AssertionError('Модуль telegram не установлен. Посмотрите в README, что нужно для этого сделать.')

try:
    import dotenv
except ImportError:
    raise AssertionError('Модуль dotenv не установлен. Посмотрите в README, что нужно для этого сделать.')
