import json

path__f = 'accounts/qwen__keyn/connections/followers_and_following/following.json'
path___f = 'accounts/qwen___keyn/connections/followers_and_following/following.json'
path_h = 'similar.html'

with open(path__f, 'r') as f__f,open(path___f, 'r') as f___f, open(path_h, 'w') as f_h:
    data1 = json.load(f__f)
    data2 = json.load(f___f)
    for i in data1['relationships_following']:
        for j in data2['relationships_following']:
            if i['string_list_data'][0]['value']==j['string_list_data'][0]['value']:
                f_h.write(f"<a href={i['string_list_data'][0]['href']}>{i['string_list_data'][0]['value']}</a><br>\n")