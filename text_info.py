import calSwapRate
import write_load_data

klayKusdtSwapRate = calSwapRate.klayKusdtSwapRate
klayTokenSwapRate = calSwapRate.klayTokenSwapRate
tokenSwapRate = calSwapRate.tokenSwapRate
wl = write_load_data

def textingKlayPrice() :
  symbol = 'kusdt'
  LPsymbol = 'klay-kusdtLp'
  textIndex, index = klayKusdtSwapRate(symbol, LPsymbol)

  text = 'klay가격 : ' + textIndex + '\n' + '\n'
  return text              #string

def textingTokenPrice(symbol, LPsymbol) :
  stdTokenSymbol = 'kusdt'
  textIndex, index = tokenSwapRate(symbol, stdTokenSymbol, LPsymbol)

  text = symbol + '가격 : ' + textIndex + '\n' + '\n'
  return text              #string

def textingKokoaPrice() :
  textIndex, index1 = klayKusdtSwapRate('kusdt', 'klay-kusdtLp')
  textIndex, index2 = klayTokenSwapRate('kokoa', 'kokoa-klayLp')
  kokoaPrice = index1 * index2
  kokoaPrice = str(round(kokoaPrice, 4))
  text = 'kokoa가격 : ' + kokoaPrice + ' kusdt\n' + '\n'
  return text              #string


def textingTokenLp(symbol, stdTokenSymbol, LPsymbol) :
  textIndex, index = tokenSwapRate(symbol, stdTokenSymbol, LPsymbol)
  pastRate = wl.load_data()
  if LPsymbol in pastRate :

    pastIndex = pastRate[LPsymbol]    #리밸런싱 시점, float

    strPastIndex = str(pastIndex) + ' ' + stdTokenSymbol
    changeIndex = index - pastIndex
    changeIndex = changeIndex / pastIndex
    changeIndex = str(round((changeIndex * 100), 4))
    
    text1 = '    ' + LPsymbol + '풀\n'
    text2 = '현재비율 : ' + textIndex + '\n'
    text3 = '과거비율 : ' + strPastIndex + '\n'
    text4 = '변동률 : ' + changeIndex + ' %\n'
    text = text1 + text2 + text3 + text4 + '\n'
  else :
    text1 = '    ' + LPsymbol + '풀\n'
    text2 = '현재비율 : ' + textIndex + '\n'
    
    text = text1 + text2 + '\n'
  return text              #string

def textingTokenKlayLp(symbol, LPsymbol) :
  textIndex, index = klayTokenSwapRate(symbol, LPsymbol)
  pastRate = wl.load_data()
  if LPsymbol in pastRate :
    
    pastIndex = pastRate[LPsymbol]    #리밸런싱 시점, float

    strPastIndex = str(pastIndex) + ' klay'
    changeIndex = index - pastIndex
    changeIndex = changeIndex / pastIndex
    changeIndex = str(round((changeIndex * 100), 4))
  
    text1 = '    ' + LPsymbol + '풀\n'
    text2 = '현재비율 : ' + textIndex + '\n'
    text3 = '과거비율 : ' + strPastIndex + '\n'
    text4 = '변동률 : ' + changeIndex + ' %\n'
    text = text1 + text2 + text3 + text4 + '\n'
  else :
    text1 = '    ' + LPsymbol + '풀\n'
    text2 = '현재비율 : ' + textIndex + '\n'
    
    text = text1 + text2 + '\n'

  return text            #string


def periodicText() :
  text6 = textingTokenPrice('kwbtc', 'kwbtc-kusdtLp')
  text0 = textingKlayPrice()
  text5 = textingTokenPrice('ksd', 'ksd-kusdtLp')
  text7 = textingTokenLp('kwbtc', 'kusdt', 'kwbtc-kusdtLpP')
  text10 = textingTokenLp('keth', 'kusdt', 'keth-kusdtLp')
  text9 = textingTokenLp('cla', 'kusdt', 'cla-kusdtLpC')
  text11 = textingTokenLp('cla', 'wklay', 'cla-wklayLpC')
  text8 = textingTokenKlayLp('kokoa', 'kokoa-klayLp')
  text3 = textingTokenKlayLp('kfi', 'kfi-klayLp')
  text = text6 + text0 + text5 + text7 + text10 + text9 + text11 + text8 + text3
  return text

#ing
def specLpText(loaded_data) :
  dataList = []
  symbol1, symbol2, LP = wl.split_data2(loaded_data)
  dataList.append(symbol1)
  dataList.append(symbol2)
  dataList.append(LP)
  if "klay" not in dataList :   
    text = textingTokenLp(dataList[0], dataList[1], dataList[2])

  else :
    if symbol1 == "klay" :
      text = textingKlayPrice()

    elif symbol2 == "klay" :
      text = textingTokenKlayLp(dataList[0], dataList[2])

  return text


    
    
  

