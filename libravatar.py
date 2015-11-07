# get libravatar from FAS Id
# Author : threebean 
import hashlib
import urllib
 
def libravatar(username, size):
    openid = "http://%s.id.fedoraproject.org/" % username
    query = urllib.urlencode({'s': size, 'd': 'retro'})
    hash = hashlib.sha256(openid).hexdigest()
    template = "https://seccdn.libravatar.org/avatar/%s?%s"
    return template % (hash, query)
 
print libravatar('decause', size=128)
