import http.client 
import json
import authorization
import contractAdress

headers = authorization.headers


def klayBalance(account) :   #string
  conn = http.client.HTTPSConnection("node-api.klaytnapi.com")
  payload = contractAdress.getKlayBalance[account]

  conn.request("POST", "/v1/klaytn", payload, headers)
  res = conn.getresponse()
  data = res.read()
  info = data.decode("utf-8")
  info = json.loads(info)
  balanceHex = info['result']
  result = int(balanceHex, 16)
  for i in range(18) :
    result = result / 10

  return result   #float

def tokenBalance(account, tokenAdress) :     #string
  conn = http.client.HTTPSConnection("kip7-api.klaytnapi.com")

  conn.request("GET", f"/v1/contract/{tokenAdress}/account/{account}/balance", headers=headers)
  res = conn.getresponse()
  data = res.read()
  info = data.decode("utf-8")
  info = json.loads(info)
  balanceHex = info['balance']
  decimalPoint = info['decimals']
  result = int(balanceHex, 16)
  for i in range(decimalPoint) :
    result = result / 10

  return result    #float



