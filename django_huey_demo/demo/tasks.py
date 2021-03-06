import requests
from django.conf import settings
from huey import crontab
from huey.contrib.djhuey import db_periodic_task

from demo.models import Word


@db_periodic_task(crontab(hour="18", minute="00"), retries=2, retry_delay=20)
def fetch_daily_word():
    r = requests.get(
        f"https://api.wordnik.com/v4/words.json/wordOfTheDay?api_key={settings.WORDNIK_API_KEY}")
    if r.status_code == 200:
        data = r.json()
        Word.objects.create(
            word=data["word"],
            part_of_speech=data["definitions"][0]["partOfSpeech"],
            definition=data["definitions"][0]["text"],
            example=data["examples"][0]["text"]
        )
    else:
        raise Exception("Unable to fetch data from Wordnik API")
