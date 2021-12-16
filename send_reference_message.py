import telegram
import telegram_information

i = telegram_information

bot = telegram.Bot(token=i.my_token)

#write_load_data.py
def wrong_symbol() :
  text = '잘못된 이름입니다. 다시 작성하세요.\n'
  bot.sendMessage(chat_id=i.chat_id, text=text)

def send_before_data(symbol, swapRate) :   #string, float
  swapRate = str(swapRate)
  text = symbol + ': ' + swapRate + '-> '
  bot.sendMessage(chat_id=i.chat_id, text=text)

def send_after_data(swapRate) :            #float
  swapRate = str(swapRate)
  text = '변경된 값: ' + swapRate + '\n변경 완료'
  bot.sendMessage(chat_id=i.chat_id, text=text)

#printToTelegram.py
def helper_to_order() :
  text = 'LP swap rate 수정양식: (symbol-symbolLp),(변경된 값)\n' + '/getdata : 전체 데이터 호출\n' + '/getrate : 현재 비율 호출\n'
  return text