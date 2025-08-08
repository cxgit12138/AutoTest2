#基础API类
#定义接口基类、封装公共方法、简化测试用例编写
from common.request_util import RequestUtil

class BaseAPI:
    def __init__(self, env_config):
        self.request = RequestUtil(env_config['base_url'])
        self.headers = {"Content-Type": "application/json"}
        self.cookies = {}
        
    def set_headers(self, key, value):
        """设置headers
        Args:
            key: headers的key
            value: headers的value
        """
        self.headers[key] = value
        
    def set_cookies(self, cookies):
        """设置cookies
        Args:
            cookies: 可以是字典或requests.cookies.RequestsCookieJar对象
        """
        if hasattr(cookies, 'get_dict'):
            self.cookies = cookies.get_dict()
        elif isinstance(cookies, dict):
            self.cookies = cookies
        else:
            raise TypeError("cookies must be a dict or RequestsCookieJar")