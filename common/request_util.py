#封装HTTP请求工具类RequestUtil，
# 统一处理接口请求发送和响应接收
import requests
from common.logger import logger

class RequestUtil:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
    
    def send_request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"请求: {method} {url}")
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                timeout=kwargs.pop('timeout', 10),
                **kwargs
            )
            logger.debug(f"响应: {response.status_code}\n{response.text[:500]}")
            return response
        except Exception as e:
            logger.error(f"请求异常: {str(e)}")
            raise