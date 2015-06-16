import sys, urllib, json

if len(sys.argv)!=2:
  print "Usage: python %s <access_token>" % (sys.argv[0])
  quit()

url = 'https://graph.facebook.com/v2.0/fql'
q = "SELECT target_id FROM connection WHERE source_id=me() AND is_following='true' AND target_type='user'"
access_token = sys.argv[1]
param = urllib.urlencode({'q':q,'access_token':access_token})

response = urllib.urlopen(url+"?"+param)
data = json.load(response)
response.close()

if 'error' in data:
  print "Error: ", data['error']['message']
  quit()

url = 'https://graph.facebook.com/v2.3'
count = 0

for ids in data['data']:
  for key, value in ids.iteritems():
    count += 1
    response = urllib.urlopen(url+"/"+value+"?fields=name&access_token="+access_token)
    temp = json.load(response)
    response.close()
    for k, v in temp.iteritems():
      if(k == 'error'):
        print "Account disabled"
        print "id : ", value
        continue
      print k, ':', v
    print ""

print "Total count: ", count
