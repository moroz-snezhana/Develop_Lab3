#Пункт 1
import http.client
import json

conn = http.client.HTTPConnection("167.172.172.227:8000")
conn.request('GET', '/number/12',)
# Выполнен запрос на сервер методом GET по определенному адресу

#Пункт 1
otv = conn.getresponse().read().decode()
otv_json = json.loads(otv)
print("Задание 1: ", otv_json['number'])

#Пункт 2
conn.request('GET', '/number/?option=12',)
otv = conn.getresponse().read().decode()
otv_json1 = json.loads(otv)
print("Задание 2.1: ", otv)
otv2 = otv_json1['number'] - otv_json['number']
print("Задание 2.2: ", otv2)

#Пункт 3
head={'Content-Type': 'application/x-www-form-urlencoded'}
conn.request("POST","/number/", "option=12", headers=head)
q=conn.getresponse()
otv=q.read().decode()
otv3=json.loads(otv)
otv3=otv3["number"]
print("Задание 3: ", otv, int(otv2+otv3))

#Пункт 4
headers = {'Content-type':'application/json'}
body = json.dumps({'option':12})
conn.request('PUT', '/number/', body, headers)
otv = conn.getresponse().read().decode()
otv4 = json.loads(otv)
otv4=otv4["number"]
print("Задание 4: ", otv, int((otv2+otv3)+otv4))

#Пункт 5
body = json.dumps({'option':12})
conn.request('DELETE','/number/', body)
otv = conn.getresponse().read().decode()
otv5= json.loads(otv)
print("Задание 5: ", otv, int((otv5['number'] - otv4) ))

conn.close
