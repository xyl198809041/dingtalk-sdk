import json

from dingtalk import AppKeyClient

client = AppKeyClient('ding8ebd56e729af6c4324f2f5cc6abecb85', 'dingtiqtbir6iyph6guc',
                      'OeBB6VCC_tL77vkhTma71mvBKYq4YjyPFbV3XwWoc3Uvq6PNzVI9flVDXL24SmPY')


def get_classRole_by_userid(userid: int):
    roles = []
    list_parent_depts = client.department.list_parent_depts(userid)
    d_list = [d['parent_dept_id_list'] for d in list_parent_depts if len(d['parent_dept_id_list']) == 7]
    for d in d_list:
        if client.department.get(d[0])['name'] == '老师':
            r_data_list = client.edu.get_user(d[1], 'teacher', userid)
            for r_data in r_data_list:
                roles.append({'name': r_data['name'], 'role': r_data['role'], 'class_id': r_data['class_id'],
                              'admin': json.loads(r_data['feature'])['is_adviser'] == 1})
        elif client.department.get(d[0])['name'] == '家长':
            r_data_list = client.edu.get_relation(d[1], userid)
            for r_data in r_data_list:
                roles.append({'name': client.user.get(r_data['to_userid'])['name']+r_data['relation_name'],
                              'role': 'guardian',
                              'class_id': r_data['class_id']})
    return roles


data = get_classRole_by_userid(194338376035126967)
print(data)
