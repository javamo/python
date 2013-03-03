import base64
import hmac
import hashlib

shared_secret = "Kah942*$7sdp0)"
plaintext= "10000GBP2007-10-20Internet Order 123454aD37dJATestMerchant2007-10-11T11:00:00Z"

hm = hmac.new(shared_secret, plaintext, hashlib.sha1)

# output should be x58ZcRVL1H6y+XSeBGrySJ9ACVo=
# make sure you "strip()" the base64 encoded string as Python
# will append a newline to the string

print base64.encodestring(hm.digest()).strip()
