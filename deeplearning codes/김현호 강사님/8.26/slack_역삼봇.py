import os
import slack

@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']
    print(data)
    print('=====\n')

    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    if 'text' in data.keys() and 'Hello' in data['text']:
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']

        web_client.chat_postMessage(
            channel='#general',
            text=f"Hi <@{user}>!", # 상대방 이름을 넣어 대답한다
            #thread_ts=thread_ts
        )

#slack_token = os.environ["SLACK_API_TOKEN"]
slack_token = 'xoxb-737981300037-726534277715-BrxF5U2Uhvwde2mFIjurftPA'  # Bot User OAuth Access Token
rtm_client = slack.RTMClient(token=slack_token)
rtm_client.start()