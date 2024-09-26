from nonebot import on_regex
from services.log import logger
import requests

from typing import Tuple
from nonebot.plugin import PluginMetadata
from zhenxun.configs.config import Config
from zhenxun.configs.path_config import TEMP_PATH
from zhenxun.configs.utils import PluginExtraData, RegisterConfig
from zhenxun.services.log import logger
from zhenxun.utils.http_utils import AsyncHttpx
from zhenxun.utils.message import MessageUtils
from zhenxun.utils.withdraw_manage import WithdrawManager

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


__plugin_meta__ = PluginMetadata(
    name="舔狗日记",
    description="舔狗的一天",
    usage="""
    舔狗日记|tgrj
    示例: 舔狗日记
    """.strip(),
    extra=PluginExtraData(
        author="shouzi",
        version="0.1",
        configs=[
            RegisterConfig(
                key="WITHDRAW_tgrj_MESSAGE",
                value=(0, 1),
                help="自动撤回，参1：延迟撤回tgrj时间(秒)，0 为关闭 | 参2：监控聊天类型，0(私聊) 1(群聊) 2(群聊+私聊)",
                default_value=(0, 1),
                type=Tuple[int, int],
            ),
        ],
    ).dict(),
)


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
