import hashlib

REQUESTHASH_SECRET_APPLYING = "2d1fd943fb14bb20dbceb05cff23157d4b2097929f197a4833fed9a36e5b0cbb"
REQUESTHASH_SECRET = "85af4a94ce7a280f69844743212a8b867206ab28946e1e30e6c1a10196609a11"

def getrequesthash(api,sessionID = None,json1 = None):
    basestring = ''
    if sessionID != None:
        basestring = sessionID
    if basestring != None:
        basestring += " "
        basestring = basestring + "/api/" + api#source:api  this.m_param.GetAPI();
    if json1 != None:
        basestring = basestring + " " + json1
    basestring = basestring + ' ' +REQUESTHASH_SECRET
    requesthash = hashlib.sha256(bytes(basestring,encoding="utf-8")).hexdigest()
    return requesthash

