from nonebot import on_regex
from services.log import logger
import requests

__zx_plugin_name__ = "舔狗日记"
__plugin_usage__ = """
usage：
    舔狗的一天
    指令：
       舔狗日记|tgrj
""".strip()
__plugin_des__ = "舔狗的一天"
__plugin_cmd__ = ["舔狗日记|tgrj"]
__plugin_version__ = 0.3
__plugin_author__ = 'Shouzi|molanp'
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["舔狗日记", "tgrj"],
}


tgrj = on_regex("^(舔狗日记|tgrj)$", priority=5, block=True)

url = [
   "https://v2.api-m.com/api/dog",
   "https://v.api.aa1.cn/api/tiangou"
   ]


@tgrj.handle()
async def send_video():
   for i in url:
      try:
         try:
            mp4 = requests.get(i)
            try:
               data = mp4.data
            except:
               data = mp4
         except:
            logger.error(f"api： {i} 已失效")
         await tgrj.finish(data)
      except:
         logger.error("api已全部失效")
