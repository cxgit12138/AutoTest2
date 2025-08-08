#提供断言工具类AssertUtil，
# 封装各种常用的断言方法，如相等、包含、状态码等断言
from common.logger import logger

class AssertUtil:
    @staticmethod
    def assert_equal(actual, expected, message=None):
        """断言两个值相等"""
        try:
            assert actual == expected
            logger.info(f"断言通过: {actual} == {expected}")
        except AssertionError:
            error_msg = message or f"断言失败: {actual} != {expected}"
            logger.error(error_msg)
            raise AssertionError(error_msg)
    
    @staticmethod
    def assert_in(member, container, message=None):
        """断言成员在容器中"""
        try:
            assert member in container
            logger.info(f"断言通过: {member} 在 {container} 中")
        except AssertionError:
            error_msg = message or f"断言失败: {member} 不在 {container} 中"
            logger.error(error_msg)
            raise AssertionError(error_msg)
    
    @staticmethod
    def assert_status_code(response, expected_code, message=None):
        """断言响应状态码"""
        try:
            assert response.status_code == expected_code
            logger.info(f"断言通过: 状态码 {response.status_code} == {expected_code}")
        except AssertionError:
            error_msg = message or f"断言失败: 状态码 {response.status_code} != {expected_code}"
            logger.error(error_msg)
            raise AssertionError(error_msg)
    
    @staticmethod
    def assert_json_key_exists(response_json, key, message=None):
        """断言JSON中存在指定键"""
        try:
            assert key in response_json
            logger.info(f"断言通过: JSON中存在键 {key}")
        except AssertionError:
            error_msg = message or f"断言失败: JSON中不存在键 {key}"
            logger.error(error_msg)
            raise AssertionError(error_msg)