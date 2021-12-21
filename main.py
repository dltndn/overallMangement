import telegram
import text_info
import telegram_information

ti = text_info
i = telegram_information

bot = telegram.Bot(token=i.my_token)


text = ti.periodicText()
bot.sendMessage(chat_id=i.chat_id, text=text)

# import pickle
# import write_load_data


# wl = write_load_data
# file = "pastSwapData.txt"

# with open(file, "rb") as f:
#   body = pickle.load(f)

# body = {
#   'kxrp-kdaiLp' : 1.0284,
#   'kxrp-klayLp' : 0.6941,
#   'kwbtc-ksdLp' : 48990,
#   'kokoa-klayLp' : 0.172,
#   'keth-kusdtLp' : 3804.8,
#   'cla-klayLp' : 7.348
# }

# with open(file, 'wb') as f:
#   pickle.dump(body, f)

# text = wl.load_data_pretty()
# print(text)






# import telegram
# from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
# import write_load_data
# import telegram_information
# import send_reference_message
# import text_info

# srm = send_reference_message
# i = telegram_information
# ti = text_info


# wl = write_load_data
# token=i.my_token

# bot = telegram.Bot(token=token)

# #도움말 관련 답장
# def help_text(update, context) :
#   update.message.reply_text("잠시만 기다려 주세요!")
#   text = srm.helper_to_order()
#   bot.sendMessage(chat_id=i.chat_id, text=text)

# #get whole data
# def get_whole_data(update, context) :
#   update.message.reply_text("잠시만 기다려 주세요!")
#   text = ti.periodicText()
#   bot.sendMessage(chat_id=i.chat_id, text=text)

# #LP swap rate data 변경 or load specific LP data
# def change_data(update, context): 
#   loaded_data = update.message.text   #string
#   if "," in loaded_data :
#     wl.write_data(loaded_data)
#   else :
#     if "-" in loaded_data :
#       update.message.reply_text("잠시만 기다려 주세요!")
#       text = ti.specLpText(loaded_data)
#       bot.sendMessage(chat_id=i.chat_id, text=text)
#     else :
#       srm.wrong_symbol()
  
  
# #get LP swap rate data
# def get_Lp_swap_rate(update, context): 
#   update.message.reply_text("잠시만 기다려 주세요!")
#   text = wl.load_data_pretty()
#   bot.sendMessage(chat_id=i.chat_id, text=text)


# updater = Updater(token, use_context=True)

# help_handler = CommandHandler('help', help_text)
# updater.dispatcher.add_handler(help_handler)

# get_whole_data_handler = CommandHandler('getdata', get_whole_data)
# updater.dispatcher.add_handler(get_whole_data_handler)

# get_Lp_swap_rate_handler = CommandHandler('getrate', get_Lp_swap_rate)
# updater.dispatcher.add_handler(get_Lp_swap_rate_handler)

# change_data_handler = MessageHandler(Filters.text & (~Filters.command), change_data)
# updater.dispatcher.add_handler(change_data_handler)

# updater.start_polling(timeout=3)
# updater.idle()