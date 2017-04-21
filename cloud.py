# coding: utf-8

from leancloud import Engine
from leancloud import LeanEngineError
import json

from app import app


engine = Engine(app)


@engine.define
def hello(**params):
    if 'name' in params:
        return 'Hello, {}!'.format(params['name'])
    else:
        return 'Hello, LeanCloud!'


@engine.before_save('Todo')
def before_todo_save(todo):
    content = todo.get('content')
    if not content:
        raise LeanEngineError('内容不能为空')
    if len(content) >= 240:
        todo.set('content', content[:240] + ' ...')

@engine.define
def _messageReceived(**params):
    # params = {
    #     'fromPeer': 'Tom',
    #     'receipt': false,
    #     'groupId': null,
    #     'system': null,
    #     'content': '{"_lctext":"耗子，起床！","_lctype":-1}',
    #     'convId': '5789a33a1b8694ad267d8040',
    #     'toPeers': ['Jerry'],
    #     '__sign': '1472200796787,a0e99be208c6bce92d516c10ff3f598de8f650b9',
    #     'bin': false,
    #     'transient': false,
    #     'sourceIP': '121.239.62.103',
    #     'timestamp': 1472200796764,
    # }
	    # 可以用继承的方式定义 leancloud.Object 的子类
	class Todo2(leancloud.Object):
	    pass
	# 或者用以下的方式定义子类
	# Todo = leancloud.Object.extend('Todo')
	todo = Todo2()
	todo.set('title', '工程师周会')
	todo.set('content', '每周工程师会议，周一下午2点')
	todo.save()

    print('_messageReceived start')
    content = json.loads(params['content'])
    print('text:', content)
    processed_content = '12345'
    print('_messageReceived end')
    # 必须含有以下语句给服务端一个正确的返回，否则会引起异常
    return {
        'content': processed_content,
    }

