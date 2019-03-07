# -*- coding: utf-8 -*-
import jenkinsinfo
import reply

try:
    recMsg = jenkinsinfo.consoleinfo()
    if(jenkinsinfo.user_name == "U"):
        toUser = "oyJXO07T6RM7v610Bzd2Zxlv3Vz8" # U:oyJXO07T6RM7v610Bzd2Zxlv3Vz8
    elif(jenkinsinfo.user_name == "Y"):
        toUser = "oyJXO03XskpUoHyh8PY1pYmI0xmY" # U:oyJXO03XskpUoHyh8PY1pYmI0xmY
    else:
        pass

    fromUser = "gh_0c619267e79e"

    reply1 = reply.TextMsg(toUser, fromUser, recMsg)
    reply1.send()  #
    print reply1.send()
except Exception, Argment:
    pass
    # return Argment
