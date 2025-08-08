import pytest
import yaml
from pages.user_api import UserAPI
from common.assert_util import AssertUtil


@pytest.fixture(scope="session")
def env_config(request):
    """动态加载环境配置"""
    env = request.config.getoption("--env", default="dev")
    # 修改: 明确指定文件编码为utf-8
    with open(f"./configs/env_{env}.yaml", encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config

@pytest.fixture
def user_api(env_config):
    """创建UserAPI实例"""
    return UserAPI(env_config)

@pytest.fixture
def assert_util():
    """创建断言工具实例"""
    return AssertUtil()

@pytest.fixture
def login_session(user_api):
    """已登录的UserAPI实例的session"""
    # 登录获取session
    login_response = user_api.login("byhy", "88888888")
    # 设置cookie
    user_api.set_cookies(login_response.cookies)
    return user_api

#该fixture暂时未调用,调用时，pytest会自动寻找该fixture并执行
@pytest.fixture
def login_token(user_api):
    """获取登录token"""
    res = user_api.login("用户名", "正确密码")
    return res.json()["token"]

# 添加命令行参数
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="指定测试环境: dev 或 prod")


import shutil
import os

def pytest_sessionfinish(session, exitstatus):
    """测试会话结束后执行，将environment.xml复制到allureResults文件夹"""
    # 源文件路径
    source_file = os.path.join(os.path.dirname(__file__), "environment.xml")
    # 目标文件夹路径
    target_dir = os.path.join(os.path.dirname(__file__), "allureResults")
    
    # 确保目标文件夹存在
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # 目标文件路径
    target_file = os.path.join(target_dir, "environment.xml")
    
    # 复制文件
    try:
        shutil.copy2(source_file, target_file)
        print(f"成功将environment.xml复制到{target_dir}")
    except Exception as e:
        print(f"复制environment.xml失败: {e}")