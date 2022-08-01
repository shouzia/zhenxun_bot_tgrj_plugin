from nonebot.adapters.onebot.v11 import Message, MessageSegment
from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from services.log import logger
from utils.manager import withdraw_message_manager
from configs.config import Config
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
__plugin_version__ = 0.1
__plugin_author__ = 'Shouzi'
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["舔狗日记", "tgrj"],
}


tgrj = on_regex("^(舔狗日记|tgrj)$", priority=5, block=True)

url = "http://ovooa.com/API/tgrj/api.php"


@tgrj.handle()
async def send_video(bot: Bot, event: Event, state: T_State):
    mp4 = requests.get(url)
    data = mp4.text
    await tgrj.send(data)
