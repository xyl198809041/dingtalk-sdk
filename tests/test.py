from dingtalk import AppKeyClient

client=AppKeyClient('ding8ebd56e729af6c4324f2f5cc6abecb85','dingtiqtbir6iyph6guc','OeBB6VCC_tL77vkhTma71mvBKYq4YjyPFbV3XwWoc3Uvq6PNzVI9flVDXL24SmPY')
list=client.department.list_ids()
d=client.department.get(str(list[1]))
print(d)