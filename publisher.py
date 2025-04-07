import requests
import telegram
from dotenv import load_dotenv
import os
import random


def get_last_comic_num():
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    num = response.json()['num']
    return num


def get_random_comics():
    url_template = 'https://xkcd.com/{}/info.0.json'
    last_number = get_last_comic_num()
    number = random.randint(0, last_number)
    url = url_template.format(number)
    response = requests.get(url)
    response.raise_for_status()
    comics = response.json()
    description = comics['alt']
    img_url = comics['img']
    img_response = requests.get(img_url)
    img_response.raise_for_status()
    image = img_response.content
    return description, image


def main():
    load_dotenv()
    chat_id = os.environ['CHAT_ID']
    tg_token = os.environ['TG_TOKEN']
    description, image = get_random_comics()
    bot = telegram.Bot(tg_token)
    bot.send_photo(chat_id=chat_id, photo=image, caption=description)


if __name__ == '__main__':
    main()