# -*- coding: utf8 -*-

import top

api = top.TaoAPI(url="http://gw.api.taobao.com/router/rest",appkey="你的的key",secret="你的secret")

tpwd_param={"url":"http://m.taobao.com","text":"超值活动，惊喜活动多多"}

api.set_api_info(method="taobao.wireless.share.tpwd.create",tpwd_param=tpwd_param)#设置api信息 api方法 参数

print(api.get())


