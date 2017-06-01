import time, hmac, hashlib, requests, json
from urllib.parse import urlencode
from time import sleep

key1 = '800D346B0F699FF5A6ADD5EEC617C6D4'
secret1 = '800D346B0F699FF5A6ADD5EEC617C6D4'


class bot(object):
    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        self.public = ['info', 'ticker', 'depth', 'trades']
        self.trade = ['activeorders']

        # def getInfo(self, values={}):
        #  url = 'https://yobit.net/api/3/'

    def query(self, method, values={}):
        if method in self.public:
            url = 'https://yobit.net/api/3/' + method
            for i, k in values.items():
                url += '/' + k

            req = requests.get(url)
            return json.loads(req.text)

        elif method in self.trade:
            url = 'https://yobit.net/tapi'
            values['method'] = method
            values['nonce'] = str(int(time.time()))
            body = urlencode(values)
            signature = hmac.new(self.secret, body, hashlib.sha512).hexdigest()
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Key': self.key,
                'Sign': signature
            }

            req = requests.post(url, data=values, headers=headers)
            return json.loads(req.text)

        return False

    def depth(self, moneta, kol):
        q = bot(key1, secret1)
        text = q.query('depth', {1: moneta+'?'+'limit='+kol})
        return text

t = time.time()
print (t)
sleep(2)
t = time.time()
print (t)
bot1 = bot(key1, secret1)
m = bot1.depth('btc_rur', '1')
print (m)

#asdfasdf


