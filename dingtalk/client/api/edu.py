# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from dingtalk.client.api.base import DingTalkBaseAPI


class Edu(DingTalkBaseAPI):

    # def list_ids(self, _id=0):
    #     """
    #     获取子部门ID列表
    #
    #     :param _id: 父部门id(如果不传，默认部门为根部门，根部门ID为1)
    #     :return: 子部门ID列表数据
    #     """
    #     return self._get(
    #         '/topapi/edu/dept/list',
    #         {'id': _id,
    #          'page_size': 30,
    #          'page_no': 1,
    #          'super_id': _id},
    #         result_processor=lambda x: x['result']
    #     )

    def list(self, super_id=0):
        """
        调用本接口查看某个部门下的所有子部门列表
        """
        data = {'page_size': 30, 'page_no': 1}
        if super_id != 0:
            data['super_id'] = super_id
        return self._get(
            '/topapi/edu/dept/list',
            data,
            result_processor=lambda x: x['result']
        )

    def get_dept(self, dept_id, lang='zh_CN'):
        """
        获取部门详情

        """
        return self._get(
            '/topapi/edu/dept/get',
            {'dept_id': dept_id},
            result_processor=lambda x: x['result']['detail']
        )

    def get_user(self, class_id, role, userid):
        return self._get(
            '/topapi/edu/user/get',
            {'class_id': class_id, 'role': role, 'userid': userid},
            result_processor=lambda x: x['result']['details']
        )

    def get_relation(self, class_id, from_userid):
        return self._get(
            '/topapi/edu/user/relation/get',
            {'class_id': class_id, 'from_userid': from_userid},
            result_processor=lambda x: x['result']['relations']
        )

    def get_list(self, class_id, role='student'):
        """
获取班级人员
        @param class_id:
        @param role: teacher：老师,guardian：监护人,student：学生
        """
        page_no = 1
        rt_list = []
        while True:
            rt = self._get(
                '/topapi/edu/user/list',
                {'page_size': 30, 'page_no': page_no, 'role': role, 'class_id': class_id},
                result_processor=lambda x: x['result']
            )
            rt_list.extend(rt['details'])
            if not rt['has_more']:
                break
            else:
                page_no = page_no + 1
        return rt_list
    #
    # def create(self, department_data):
    #     """
    #     创建部门
    #
    #     :param department_data: 部门信息
    #     :return: 创建的部门id
    #     """
    #     if 'id' in department_data:
    #         raise AttributeError('不能包含Id')
    #     return self._post(
    #         '/department/create',
    #         department_data,
    #         result_processor=lambda x: x['id']
    #     )
    #
    # def update(self, department_data):
    #     """
    #     更新部门
    #
    #     :param department_data: 部门信息
    #     :return: 已经更新的部门id
    #     """
    #     if 'id' not in department_data:
    #         raise AttributeError('必须包含Id')
    #     return self._post(
    #         '/department/update',
    #         department_data,
    #         result_processor=lambda x: x['id']
    #     )
    #
    # def delete(self, _id):
    #     """
    #     删除部门
    #
    #     :param _id: 部门id。（注：不能删除根部门；不能删除含有子部门、成员的部门）
    #     :return:
    #     """
    #     return self._get(
    #         '/department/delete',
    #         {'id': _id}
    #     )
    #
    # def list_parent_depts_by_dept(self, _id):
    #     """
    #     查询部门的所有上级父部门路径
    #
    #     :param _id: 希望查询的部门的id，包含查询的部门本身
    #     :return: 该部门的所有父部门id列表
    #     """
    #     return self._get(
    #         '/department/list_parent_depts_by_dept',
    #         {'id': _id},
    #         result_processor=lambda x: x['parentIds']
    #     )
    #
    # def list_parent_depts(self, user_id):
    #     """
    #     查询指定用户的所有上级父部门路径
    #
    #     :param user_id: 希望查询的用户的id
    #     :return: 按顺序依次为其所有父部门的ID，直到根部门
    #     """
    #     return self._get(
    #         '/department/list_parent_depts',
    #         {'userId': user_id},
    #         result_processor=lambda x: x['department']
    #     )
