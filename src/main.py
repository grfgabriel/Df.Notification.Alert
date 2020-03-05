from azure.servicebus import ServiceBusService, Message, Topic, Rule, DEFAULT_RULE_NAME
from conf.settings import TELEGRAM_TOKEN
from pprint import pprint
import telepot

bus_service = ServiceBusService(
service_namespace='dfmessage',
shared_access_key_name='meu_token',
shared_access_key_value='+JWuf875RyazD1Cj8/ezM49LiPk08c+B0lm/I4nqx98=')

topic_name= 'notifications/alerts/telegram/application_error_notification'
consumer_name = 'telegram_publisher'

bus_service.create_topic(topic_name)

bus_service.create_subscription(topic_name, consumer_name)

bot = telepot.Bot(TELEGRAM_TOKEN)
# me = bot.getMe()                  #telegram informations;
message_recived = bot.getUpdates()       #recived message sent to bot;
chat_id = message_recived[0]['message']['chat']['id']

def send_message(text_message):
    bot.sendMessage(chat_id, text_message)
    pprint(text_message)



while True:

    event_recived = bus_service.receive_subscription_message(topic_name, consumer_name, peek_lock=False)
    
    if event_recived is not None:
        send_message(event_recived.body)
        print(event_recived.body)
