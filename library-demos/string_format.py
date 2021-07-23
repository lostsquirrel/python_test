# -*- coding:utf-8 -*-
"""
Created on 2015-02-04

@author: lisong
"""
import datetime

order_no = '123'
print(type(order_no))
message = "订单不存在(order_no:%s)" % order_no
print(message)
order_no = ''
message = '''订单不存在(order_no:%s)''' % order_no
print(message)
p = {'a': '1', 'b': '2', 'c': '3'}

print('%(c)s, %(b)s' % p)


def xx(**o):
    print(o, type(o))


xx(**p)
p1 = {'rating': '1',
      'update_time': datetime.datetime(2015, 3, 20, 17, 26, 11, 749481),
      'order_no': None,
      'author_mobile': None,
      'object_type': None,
      'object_name': None,
      'object_id': None,
      'content': 'update2',
      'is_valid': True,
      'author_avatar': None,
      'communication_rank': '3',
      'create_time': datetime.datetime(2015, 3, 20, 17, 26, 11, 749443),
      'punctual_rank': '2',
      'images': ['/img/f99f0546cb081d89103d4b0469302cd7.jpg', '/img/599d3abde9e043bc476124b502486258.jpg'],
      'author_id': 3,
      'professional_rank': '3',
      'id': '19',
      'is_block': False}

p2 = {'rating': '1',
      'update_time': datetime.datetime(2015, 3, 20, 17, 35, 12, 743729),
      'order_no': '1426087766830154',
      'author_mobile': '18683591672',
      'object_type': 'sample',
      'object_name': '333333333333',
      'object_id': '28', 'content': '2',
      'is_valid': 1,
      'author_avatar':
          '/img/af7762b2aafc3e53077aa0a461b6c7cf.jpg',
      'create_time': datetime.datetime(2015, 3, 20, 16, 14, 12),
      'punctual_rank': '4',
      'author_id': 3,
      'professional_rank': '5',
      'id': 19,
      'is_block': 0,
      'communication_rank': '1'}

sql = '''
        UPDATE evaluate SET is_block = %(is_block)s, is_valid = %s(is_valid)s,
        content = %(content)s, rating = %(rating)s, communication_rank = %(communication_rank)s,
        professional_rank = %(professional_rank)s, punctual_rank = %(punctual_rank)s, 
        update_time = %(update_time)s
        WHERE id = %(id)s
        '''

print('UPDATE evaluate SET is_block = %(is_block)s, is_valid = %(is_valid)s,' % p1)
print(sql % p1)
