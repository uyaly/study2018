#coding=utf8

import app.mpapi.msgdealer as msgdealer
import app.plugins.autoreply as autoreply

import app.plugins.tuling as tuling
from config import WELCOME_WORD


def deal_with_msg(xmlMsg):
    msg = msgdealer.get_dict_from_xml(xmlMsg)
    content = u'接受到消息类型：%s'
    if msg.get('MsgType') == 'text':
        if msg.get('Content') == u'【收到不支持的消息类型，暂无法显示】':
            content = u'机器人看不懂诶'
        else:
            for reply_fn in [autoreply.get_reply, tuling.get_reply]:
                content = reply_fn(msg.get('Content', ''))
                if not content is None: break
            else:
                content = u'收到：' + msg.get('Content', '')
    elif msg.get('MsgType') == 'event':
        content = WELCOME_WORD
    else:
        content = content%msg.get('MsgType')
    return msgdealer.get_xml('text', msg.get('FromUserName'), msg.get('ToUserName'), content)
