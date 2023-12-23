import json

path__m = 'accounts/qwen__keyn/your_instagram_activity/messages/inbox/qwen___keyn_17901421271777730/message_1.json'
path__f = 'accounts/qwen__keyn/connections/followers_and_following/following.json'
path_a = 'approved.html'

with open(path__m, 'r') as f__m,open(path__f, 'r') as f__f, open(path_a, 'w') as f_a:
    data1 = json.load(f__m)
    data2 = json.load(f__f)
    l_a = []
    for i in data1['messages']:
      found = False
      if i['sender_name'] == 'qwen___keyn':
        if 'share' in i:
            for j in data2['relationships_following']:
              if i['share']['original_content_owner']==j['string_list_data'][0]['value']:
                found = True
                break
            if not found:
                f_a.write(f"<a href={i['share']['link']}>{i['share']['original_content_owner']}</a><br>\n")