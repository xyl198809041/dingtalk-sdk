import json
import time

from dingtalk import AppKeyClient

client = AppKeyClient('ding8ebd56e729af6c4324f2f5cc6abecb85', 'dingtiqtbir6iyph6guc',
                      'OeBB6VCC_tL77vkhTma71mvBKYq4YjyPFbV3XwWoc3Uvq6PNzVI9flVDXL24SmPY')



rt=client.department.listsub('443817063')
# 9班 id=431758564  群id=chat70ea37feee48779aeaaf3bb2e5ccb707
rt = client.wenjuan.list_ids()
data = client.wenjuan.get_data(rt['list'][0]['form_code'])
# data = client.user.get(10086)['mobile']


def get_lvma(wenjuan_data):
    for d in wenjuan_data['forms']:
        if d['label'] == '健康码':
            return d['value'][2:-2]

url=get_lvma(data[0])
print(data)
# aaa = client.chat.send('chat70ea37feee48779aeaaf3bb2e5ccb707',
#                        {"msgtype": "text", "text": {"content": "试一下。"},
#                         "at": {
#                             "atMobiles": [
#                                 "15858291872"
#                             ],
#                             "atUserIds": [
#                                 "194338376035126967"
#                             ],
#                             "isAtAll": False
#                         },
#                         })
# aaa=client.workrecord.add(194338376035126967, int(time.time()), '标题', 'https://class.hzsgz.com/wzx/#/index', {
#     "title": "新人学习2",
#     "content": "产品学习"
# })
# aaa = client.message.asyncsend_v2({
#     "msgtype": "action_card",
#     "action_card": {
#         "title": "晚自习签退",
#         "markdown":
# '''# 晚自修签退
# 是否已接到孩子''',
#         "btn_orientation": "1",
#         "btn_json_list": [
#             {
#                 "title": "已接到",
#                 "action_url": "https://www.taobao.com"
#             },
#             {
#                 "title": "未接到",
#                 "action_url": "https://www.tmall.com"
#             }
#         ]
#     }
# },
#                                   '1307827078',
#                                   ['194338376035126967'])
# aaa = client.edu.get_studentinfo(431758564, 1307827078, )
# aaa = client.message.asyncsend_v2({
#     "msgtype": "text",
#     "text": {
#         "content": '2212'
#     }
# }, 1307827078, [194338376035126967])
#
# print(aaa)
# print(data)
