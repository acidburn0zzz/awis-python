import datetime
import urllib
import hmac
import hashlib
import base64

#Query Options  # refer to AWIS API reference for full details.
Action = "UrlInfo" 
Url = "www.huffingtonpost.com/"
ResponseGroup = "TrafficData"

#Config Options
PATH_TO_SECRET = 'c:\\users\\john\\aws-secret.txt' #Path to ANSI encoded text file with secret.
AWSAccessKeyId = "AKIAJVPTTW3SPGN4OKQQ" #Enter your AWS access id.

#Don't edit below.
f = open('c:\\users\\john\\aws-secret.txt') 
secret = (f.read())
SignatureVersion = "2"
SignatureMethod = "HmacSHA256"
ServiceHost = "awis.amazonaws.com"
PATH = "/"

def create_timestamp():
    now = datetime.datetime.now()
    timestamp = now.isoformat()
    return timestamp

def create_uri(params):
    params = [(key, params[key])
        for key in sorted(params.keys())]
    return urllib.urlencode(params)

def create_signature():
    Uri = create_uri(params)
    msg = "\n".join(["GET", ServiceHost, PATH, Uri])
    hmac_signature = hmac.new(secret, msg, hashlib.sha256)
    signature = base64.b64encode(hmac_signature.digest())
    return urllib.quote(signature)

params = {
    'Action':Action,
    'Url':Url,
    'ResponseGroup':ResponseGroup,
    'SignatureVersion':SignatureVersion,
    'SignatureMethod':SignatureMethod,
    'Timestamp': create_timestamp(),
    'AWSAccessKeyId':AWSAccessKeyId,
    }

uri = create_uri(params)
signature = create_signature()

url = "http://%s/?%s&Signature=%s" % (ServiceHost, uri, signature)

print url
