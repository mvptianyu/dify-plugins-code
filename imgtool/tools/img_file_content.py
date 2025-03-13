from collections.abc import Generator
from typing import Any

import base64
import tempfile
import os

from dify_plugin import Tool,DifyPluginEnv
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin.file.file import File


class ImgFileContent(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        file = tool_parameters.get("file")
        base64_flag = tool_parameters["base64"]

        if not file:
            yield self.create_text_message("")
            return

        envs = DifyPluginEnv()

        if not file.url.startswith("http"):
            file.url = "http://" + envs.REMOTE_INSTALL_HOST + file.url

        content = ""

        try:
            content = base64.b64encode(file.blob).decode('utf-8', errors='ignore')
            if base64_flag == "0":
                content =  file.blob.decode('utf-8', errors='ignore')
        except FileNotFoundError:
            print(f"文件 {image_path} 未找到。")
        except Exception as e:
            print(f"发生错误: {e}")

        yield self.create_text_message(content)
        return
