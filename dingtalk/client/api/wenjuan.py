# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from dingtalk.client.api.base import DingTalkBaseAPI


class Wenjuan(DingTalkBaseAPI):

    def list_ids(self,biz_type=1):
        """
        获取子部门ID列表

        :param _id: 父部门id(如果不传，默认部门为根部门，根部门ID为1)
        :return: 子部门ID列表数据
        """
        return self._post(
            '/topapi/collection/form/list',
            {
                'biz_type':biz_type,
                'offset': 0,
                'size': 200},
            result_processor=lambda x: x['result']
        )

    def get_data(self, form_code,biz_type=1):
        page_no = 0
        rt_list = []
        while True:
            rt = self._post(
                '/topapi/collection/instance/list',
                {'form_code': form_code, 'offset': page_no, 'size': 100,'biz_type':biz_type},
                result_processor=lambda x: x['result']
            )
            rt_list.extend(rt['list'])
            if not rt['has_more']:
                break
            else:
                page_no = page_no + 1
        return rt_list
