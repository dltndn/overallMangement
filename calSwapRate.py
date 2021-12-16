import getLpApiData
import contractAdress

klayBalance = getLpApiData.klayBalance
tokenBalance = getLpApiData.tokenBalance

#kaly - usdt swap rate
def klayKusdtSwapRate(symbol, LPsymbol) :
  LpAdress = contractAdress.klayLpAdress[LPsymbol]
  tokenAdress = contractAdress.tokenAdress[symbol]
  
  klayIndex = klayBalance(LPsymbol)
  tokenIndex = tokenBalance(LpAdress, tokenAdress)

  rate = tokenIndex / klayIndex
  rate = round(rate, 4)
  strRate = str(rate)
  text = strRate + ' kusdt'
  return text, rate      #str, float

#klay - token swap rate
def klayTokenSwapRate(symbol, LPsymbol) :   #string
  LpAdress = contractAdress.klayLpAdress[LPsymbol]
  tokenAdress = contractAdress.tokenAdress[symbol]
  
  klayIndex = klayBalance(LPsymbol)
  tokenIndex = tokenBalance(LpAdress, tokenAdress)

  rate = klayIndex / tokenIndex
  rate = round(rate, 4)
  strRate = str(rate)
  text = strRate + ' klay'
  return text, rate      #str, float

#token - token swap rate
def tokenSwapRate(symbol, stdTokenSymbol, LPsymbol) :  #string
  LpAdress = contractAdress.tokenLpAdress[LPsymbol]
  tokenAdress = contractAdress.tokenAdress[symbol]
  stdTokenAdress = contractAdress.tokenAdress[stdTokenSymbol]

  tokenIndex = tokenBalance(LpAdress, tokenAdress)
  stdTokenIndex = tokenBalance(LpAdress, stdTokenAdress)

  rate = stdTokenIndex / tokenIndex
  rate = round(rate, 4)
  strRate = str(rate)
  text = strRate + ' ' + stdTokenSymbol
  return text, rate        #str, float