# import jpegify as jpg
import config
import jpegify
import time
import urllib
from slackclient import SlackClient

token = config.API_TOKEN

sc = SlackClient(token)

def print_channels():
    channels = sc.api_call('channels.list')
    for c in channels.get('channels'):
        print(c.get('name'), '(' + c.get('id') + ')')

def print_bot_id():
    users = sc.api_call('users.list')
    for user in users.get('members'):
        if user['name'] == config.NAME:
            print(user['id'])

def generate_ssl_context():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx

def download_from_link(link):
    urllib.request.urlretrieve(link, 'image.png')

def parse_message(data):
    tag = '<@' + config.BOT_ID + '>'
    # Parse data to ensure the bot was tagged and it contains an image.
    if(len(data) > 0):
        event = data[0]
        if event['type'] == 'message':
            if event['subtype'] == 'file_share' and tag in event['text']:
                print('Tagged in message')
                link = event['file']['url_private_download']
                print('Link found:', link)
                # Try to download
                send_message = True
                try:
                    download_from_link(link)
                    print("Downloaded successfully")
                except:
                    send_message = False
                    print("Error downloading from slack")
                # Make and send shittier image
                if(send_message):
                    new_image = jpegify.bify(2, 'Unknown.jpg')
                    sc.api_call('files.upload', channel = event['channel'], text = "FTFY B", file = new_image)

                print('------------------------------')

def list_clean(data, n):
    if len(data) > 0:
        event  = data[0]
        for k in event.keys():
            if type(event[k]) == dict:
                print(k + ':')
                list_clean([event[k]], n+1)
            else:
                print('|'*n + k + ':', event[k])
        print('-------------------------------------')

def list_dirty(data):
    if len(data) > 0:
        event  = data[0]
        for k in event.keys():
            print(k + ':', event[k])
        print('-------------------------------------')

def listen():
    # Connect to real time messenger API
    if sc.rtm_connect():
        while True:
            time.sleep(1)
            # Parse data, display in terminal
            data = sc.rtm_read()
            list_clean(data, 0)
            parse_message(data)
    else:
        print("Lost connection")
listen()
