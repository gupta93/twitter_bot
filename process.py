import json
from sheets import get_worksheet_object
import queue, time


def process(user,entity):
    flag = False
    if user and entity:
        followers_count = user.get('followers_count', None)
        if followers_count and followers_count >= 1000 and followers_count <= 50000:
            flag = True
        if not flag:
            hashtags = entity.get('hastags',None)
            if hashtags is not None :
                if'mentalhealth' in hashtags or 'mindfulness' in hashtags:
                    flag = True
    return flag

def insert_row(value):
    ws_editor.insert_row(values=value)

def callback(ch, method, properties, body):
    body = json.loads(body)
    user_obj = body.get('user')
    entity_obj = body.get('entities')
    response = False
    username = user_obj.get('screen_name',None)
    exists_flag = users.get(username,None)
    if username and not exists_flag:
        response = process(user_obj,entity_obj)
        print "processed"
    if response:
        users[username] = True
        email = user_obj.get('email','NA')
        followers_count = user_obj.get('followers_count')
        val = [username,email,str(followers_count)]
        insert_row(val)
        print "matched"


if __name__ == "__main__":
    channel = queue.channel
    channel.basic_qos(prefetch_count=10)
    ws_editor = get_worksheet_object()
    users = dict()
    ws_editor.insert_row(values=["Username", "Email", "Followers Count"],index=1)
    channel.basic_consume(callback,
                          queue='twitter',
                          no_ack=True)
    while True:
        try:
            channel.start_consuming()
        except:
            print "timeout"
            time.sleep(5)