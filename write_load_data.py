import pickle
import send_reference_message

srm = send_reference_message

# file = '/home/ubuntu/important_data/pastSwapData.txt'   ########
file = "pastSwapData.txt"

#받은 데이터 분류
def split_data(text) :
  data = text.split(',')
  symbol = data[0]
  swapRate = float(data[1])            #입력받은 데이터의 type 체크
  return symbol, swapRate
  

def write_data(data) :
  symbol, swapRate = split_data(data)
  with open(file, "rb") as f:
    body = pickle.load(f)
  

  if symbol in body : 
    srm.send_before_data(symbol, body[symbol])
    body[symbol] = swapRate
    

    with open(file, 'wb') as f:
      pickle.dump(body, f)

    after_data = load_rate_data(symbol)
    srm.send_after_data(after_data)
  else :
    srm.wrong_symbol()
    
def load_data() :
  with open(file, "rb") as f:
    index = pickle.load(f)

  return index    #dictionary

def load_rate_data(symbol) :
  with open(file, "rb") as f:
    index = pickle.load(f)

  swapRate = index[symbol]
  return swapRate    #float

def load_data_pretty() :
  index = load_data()
  text = ''
  for key, val in index.items():
    text2 = "{key} : {value}\n".format(key=key,value=val)
    text = text + text2

  return text