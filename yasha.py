import vk_api
import random
import time
import re
import datetime
import data

# Токен группы
token = 'b6350f067b8b6f7f86090e36f9a05fe26e640a595b190c709bd65855d17e6dd5ca05ff2bd0b1347cb1fce'

# Подключение
vk  = vk_api.VkApi(token=token)

# Авторизация
vk._auth_token()

name = 'Яша'
days = data.days
months = data.months

# Счёт непрочитанных сообщений
while True:
	try:
		# Кол-во сообщений
		messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
		if messages['count'] >= 1:
			id = messages["items"][0]["last_message"]["from_id"]
			body = messages["items"][0]["last_message"]["text"]

			if body.lower() == "начать":
				vk.method("messages.send", {"peer_id": id, "message": '🦁 Привет!\nДавайте начнём знакомиться!', "random_id": random.randint(1, 2147483647)})

			elif body.lower() == "привет" or body.lower() == "хай" or body.lower() == "дарова" or body.lower() == "здрасте":
				vk.method("messages.send", {"peer_id": id, "message": '🦁 ' + body, "random_id": random.randint(1, 2147483647)})

			elif body.lower() == "кто я?":
				vk.method("messages.send", {"peer_id": id, "message": "🦁 Ты самый преданный ценитель игр!", "random_id": random.randint(1, 2147483647)})

			elif body.lower() == "яша" or body.lower() == "яш" or body.lower() == "яшик" or body.lower() == "яков" or body.lower() == "яшник":
				vk.method("messages.send", {"peer_id": id, "message": "🦁 Чем могу быть любезен?", "random_id": random.randint(1, 2147483647)})

			elif re.findall('помо+', body):
				vk.method("messages.send", {"peer_id": id, "message": "🦁 Нужна помощь?", "random_id": random.randint(1, 2147483647)})

			elif body.lower() == "дата сегодня":
				today = datetime.datetime.today()
				day = today.strftime("%e")
				num = int(today.strftime("%w"))
				month = today.strftime("%b")
				year = today.strftime("%Y")
				vk.method("messages.send", {"peer_id": id, "message": "🦁 Сегодня " + day + " " + month + ", " + year + ' г. , ' + days[num] , "random_id": random.randint(1, 2147483647)})

			elif body.lower() == "дата завтра":
				tommorrow = datetime.datetime.today() + datetime.timedelta(days=1)
				day = tommorrow.strftime("%e")
				num = int(tommorrow.strftime("%w"))
				month = tommorrow.strftime("%b")
				year = tommorrow.strftime("%Y")
				vk.method("messages.send", {"peer_id": id, "message": "🦁 Завтра " + day + " " + month + ", " + year + ' г. , ' + days[num] , "random_id": random.randint(1, 2147483647)})

			elif body.lower() == "голос":
				vk.method("messages.send", {"peer_id": id, "message": "🦁 Ррррррр!", "random_id": random.randint(1, 2147483647)})

			elif body.lower() == "кто ты?" or body.lower() == "как тебя зовут" or body.lower() == "ты кто?":
				introduce = '🦁 Меня зовут ' + name + '.\n Я - бот этого паблика, где публикуются новости о Java играх и не только.\n Рад, что тебе интересно. 😊'
				vk.method("messages.send", {"peer_id": id, "message": introduce, "random_id": random.randint(1, 2147483647)})

			else:
				vk.method("messages.send", {"peer_id": id, "message": "🦁 Команда \"" + str(body.lower()) + '\" мне не знакома', "random_id": random.randint(1, 2147483647)})
	except Exception as E:
		time.sleep(1)