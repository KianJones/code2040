import json
import datetime
import dateutil.parser
import requests as req
import sys

#registration 'https://github.com/KianJones/code2040' 'kjones43@u.rochester.edu'

jbody = json.dumps({'github': sys.argv[1], 'email': sys.argv[2]})

response = req.post('http://challenge.code2040.org/api/register', data=jbody)

jdata = json.loads(response.text)
print jdata
token=jdata['result']
jtoken = json.dumps({'token':token})

def get_question(url):
    question = req.post(url,data=jtoken)
    print question.text
    return question

def submit_answer(url,body):
    print body
    answer = req.post(url, data=body);
    print answer.text
    return answer

#stage 1

question1 = get_question("http://challenge.code2040.org/api/getstring")

jdata1 = json.loads(question1.text)
revstring = jdata1['result'][::-1]
jbody1 = json.dumps({'token':'sO3XxG9cqZ','string':revstring})

answer1 = submit_answer("http://challenge.code2040.org/api/validatestring",jbody1)


#stage 2

question2 = get_question("http://challenge.code2040.org/api/haystack")
jdata2 = json.loads(question2.text)

i = 0
for item in jdata2['result']['haystack']:
    if item == jdata2['result']['needle']:
        break
    i += 1


jbody2 = json.dumps({'token':token,'needle':i})
answer2 = submit_answer("http://challenge.code2040.org/api/validateneedle",jbody2)

#stage3

question3 = get_question("http://challenge.code2040.org/api/prefix")
jdata3 = json.loads(question3.text)

result = []
prefix = jdata3['result']['prefix']
for item in jdata3['result']['array']:
    if item[:len(prefix)] != prefix:
        result.append(item)


jbody3 = json.dumps({'token':token,'array':result})
answer3 = submit_answer("http://challenge.code2040.org/api/validateprefix",jbody3)

#stage 4
question4 = get_question("http://challenge.code2040.org/api/time")
jdata4 = json.loads(question4.text)

start_date = dateutil.parser.parse(jdata4['result']['datestamp'])
end_date = sdate + datetime.timedelta(seconds=jdata4['result']['interval'])

jbody4 = json.dumps({'token':token, 'datestamp':edate.isoformat()})
answer4 = submit_answer("http://challenge.code2040.org/api/validatetime",jbody4)

responsea = req.post("http://challenge.code2040.org/api/status",data=jbody1)
print responsea.text
