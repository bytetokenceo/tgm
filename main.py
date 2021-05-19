import telebot
import time
import random
import string
from hashlib import sha256

bot = telebot.TeleBot("1701554758:AAHoZy5VjLuczaTHZOYqfzfcVg4iY2WuZ1U")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,"Welcome!")
    bot.reply_to(message, "/create - create wallet")
    bot.reply_to(message, "/import - import wallet")

@bot.message_handler(commands=['create'])
def send_welcome(message):
    try:
        letters = string.ascii_letters
        address = ''.join(random.choice(letters) for i in range(34))
        address_pk = address+"OK6w8FIZMpZUHolaM782!!!"
        pk = sha256(address_pk.encode('utf-8')).hexdigest()
        f = open(address + ".txt", "w")
        f.write("0.0")
        f = open(address + ".txt", "r")
        blnc = float(f.read())
        bot.reply_to(message, "Wallet created!")
        bot.reply_to(message, "Your receiving address - " + address)
        bot.reply_to(message, "Your private key - " + pk)
        bot.reply_to(message, "Your balance - " + str(blnc))
        bot.reply_to(message, "/help - show wallet cmd list")
    except Exception:
        bot.reply_to(message, "Error")
        pass

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message,"Cmd list:")
    bot.reply_to(message, "/send - send coins")
    bot.reply_to(message, "/balance - show your balance")
    bot.reply_to(message, "/mine - mine TGM")

@bot.message_handler(commands=['balance'])
def send_w(message):
    try:
        cid = message.chat.id
        addr = bot.send_message(cid, "Type your receiving address:")
        bot.register_next_step_handler(addr, echo_a)
    except Exception:
        bot.reply_to(message, "Error")
        pass

def echo_a(message):
    try:
        address = message.text
        frec = open(address + ".txt", "r")
        balance = float(frec.read())
        bot.reply_to(message, "Your balance - " + str(balance) + " TGM")
    except Exception:
        bot.reply_to(message, "Error")
        pass

@bot.message_handler(commands=['mine'])
def send_wwwwa(message):
    try:
        cid = message.chat.id
        addr = bot.send_message(cid, "Type your receiving address:")
        bot.register_next_step_handler(addr, echo_aminer)
    except Exception:
        bot.reply_to(message, "Error")
        pass

def echo_aminer(message):
    try:
        address = message.text
        reward = 0.01
        bot.reply_to(message, "Mining started! Just wait for payout!")
        time.sleep(3600)
        frec = open(address + ".txt", "r")
        balance = float(frec.read())
        rewarded = balance + reward
        with open(address + ".txt", 'w') as e:
            e.write(str(rewarded))
        bot.reply_to(message, "Rewarded!!! Your new balance - " + str(rewarded) + " TGM")
    except Exception:
        bot.reply_to(message, "Error")
        pass

@bot.message_handler(commands=['import'])
def send_a(message):
    try:
        cid20 = message.chat.id
        addrr = bot.send_message(cid20, "Type your receiving address:")
        bot.register_next_step_handler(addrr, echo_i)
    except Exception:
        bot.reply_to(message, "Error")
        pass
def echo_i(message):
    try:
        addressd = message.text
        address_pkk = addressd + "OK6w8FIZMpZUHolaM782!!!"
        pkeyy = sha256(address_pkk.encode('utf-8')).hexdigest()
        cid30 = message.chat.id
        addrkeyy = bot.send_message(cid30, "Type your private key:")
        bot.register_next_step_handler(addrkeyy, echo_ii, pkeyy, addressd)
    except Exception:
        bot.reply_to(message, "Error")
        pass
def echo_ii(message , pkeyy , addressd):
    try:
        if message.text == pkeyy:
            address_vv = addressd
            bot.reply_to(message, "Wallet imported successful!")
            frecz = open(address_vv + ".txt", "r")
            balance = float(frecz.read())
            bot.reply_to(message, "Your balance - " + str(balance) + " TGM")
        else:
            bot.reply_to(message, "Fail")
    except Exception:
        bot.reply_to(message, "Error")
        pass

@bot.message_handler(commands=['send'])
def send_a(message):
    try:
        cid2 = message.chat.id
        addr = bot.send_message(cid2, "Type YOUR receiving address:")
        bot.register_next_step_handler(addr, echo_w)
    except Exception:
        bot.reply_to(message, "Error")
        pass
def echo_w(message):
    try:
        address = message.text
        address_pkk = address + "OK6w8FIZMpZUHolaM782!!!"
        pkey = sha256(address_pkk.encode('utf-8')).hexdigest()
        cid3 = message.chat.id
        addrkey = bot.send_message(cid3, "Type YOUR private key:")
        bot.register_next_step_handler(addrkey, echo_ww, pkey, address)
    except Exception:
        bot.reply_to(message, "Error")
        pass
def echo_ww(message , pkey , address):
    try:
        if message.text == pkey:
            address_v = address
            bot.reply_to(message, "Verification successful!")
            cid4 = message.chat.id
            receiver = bot.send_message(cid4, "Type RECEIVER address:")
            bot.register_next_step_handler(receiver, echo_www, address_v)
        else:
            bot.reply_to(message, "Fail")
    except Exception:
        bot.reply_to(message, "Error")
        pass
def echo_www(message , address_v):
    try:
        receiver = message.text
        address_y = address_v
        cid5 = message.chat.id
        amount = bot.send_message(cid5, "Type amount of coins:")
        bot.register_next_step_handler(amount, echo_wwww, address_y, receiver)
    except Exception:
        bot.reply_to(message, "Error")
        pass

def echo_wwww(message , address_y , receiver):
    try:
        frec = open(address_y + ".txt", "r")
        balance = float(frec.read())
        amnt = float(message.text)
        if amnt < 0:
            print("Fail")
        if amnt > balance:
            bot.reply_to(message, "Fail")
        else:
            if amnt < 0:
                bot.reply_to(message, "Fail")
            else:
                frecr = open(receiver + ".txt", "r")
                balance_receiver = float(frecr.read())
                sending = balance - amnt
                receiving = balance_receiver + amnt
                with open(receiver + ".txt", 'w') as e:
                    e.write(str(receiving))
                bot.reply_to(message, "New receiver balance - " + str(receiving) +" TGM")
                with open(address_y + ".txt", 'w') as ios:
                    ios.write(str(sending))
                bot.reply_to(message, "Your new balance - " + str(sending) + " TGM")
                bot.reply_to(message, "Transaction successfully!")
    except Exception:
        bot.reply_to(message, "Error")
        pass


bot.polling()