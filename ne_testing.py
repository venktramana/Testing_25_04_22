##a = [1, 2, 3, 4, 5, 6]
##
##
##b = [3, 4, 5,6,7,8]
##
##
##c = dict(zip(a,b))
##
##print(c)
##
##
##
##from collections import defaultdict
##
##
##d = list(c.items())
##
##print(d)
##
##
##
##dup = [1, 1, 2, 3, 4, 5, 6, 7,  7, 8, 8]
##
##e = []
##
##for i in dup:
##    if i not in e:
##        e.append(i)
##print(e)
##
##
##dup_dup = [1,1, 2,3, 4, 5, 15, 20, 30]
##
##x = set(dup)
### {1,2,3,4}
##y = set(dup_dup)
##
##if x & y:
##    print (x & y)




##import request
##from bs4 import BeautifulSoup
##import json
##a = {"data":{"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver","avatar":"https://reqres.in/img/faces/2-image.jpg"},"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}
##print(a)
##print(type(a))
##
##b = request.get(a)
##c = BeautifulSoup(b.content, 'json.parser')
##
##d = c.find_a
##print(d)
##
##f = json.load



import json

json_data = '{"data":{"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver","avatar":"https://reqres.in/img/faces/2-image.jpg"},"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}'


print(type(json_data))

x = json.loads(json_data)
print(type(x))


print(x)
print(x['data']['id'])
print(type(x['data']))




