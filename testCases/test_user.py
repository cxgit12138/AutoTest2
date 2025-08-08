#测试用例类，
# 使用pytest框架编写登录和客户相关接口的测试用例
import pytest
import yaml
import allure


# 加载测试数据
with open("./data/test_data.yaml", "r", encoding="utf-8") as f:
    test_data = yaml.safe_load(f)



class TestUser:
    @pytest.mark.parametrize("test_case", test_data["login_tests"])
    @allure.epic("登录模块")
    def test_login(self, user_api,assert_util,test_case):
        #动态设置测试用例的描述
        allure.dynamic.description(test_case.get('description', ''))

        username = test_case["username"]
        password = test_case["password"]
        expected_ret = test_case["expected_ret"]
        expected_msg = test_case.get("expected_msg")
        # 测试步骤
        response = user_api.login(username, password)

        # 断言验证
        assert_util.assert_json_key_exists(response.json(), "ret")
        assert_util.assert_equal(response.json()["ret"], expected_ret)
        if expected_msg:
            assert_util.assert_json_key_exists(response.json(), "msg")
            assert_util.assert_equal(response.json()["msg"], expected_msg)

class TestCustomer:
    @pytest.mark.parametrize("test_case", test_data["list_customers_tests"])
    @allure.epic("客户模块")
    @allure.feature("查询客户列表")
    def test_list_customers(self, login_session,assert_util,test_case):
        # 动态设置测试用例的描述
        allure.dynamic.description(test_case.get('description', ''))

        pagesize = test_case["pagesize"]
        pagenum = test_case["pagenum"]
        keywords = test_case["keywords"]
        expected_ret = test_case["expected_ret"]
        # 测试步骤
        response = login_session.list_customers(pagesize, pagenum, keywords)

        # 断言验证
        assert_util.assert_json_key_exists(response.json(), "ret")
        assert_util.assert_equal(response.json()["ret"], expected_ret)
        if expected_ret == 0:
            assert_util.assert_json_key_exists(response.json(), "retlist")
            assert_util.assert_json_key_exists(response.json(), "total")

    @pytest.mark.parametrize("test_case", test_data["add_customer_tests"])
    @allure.epic("客户模块")
    @allure.feature("添加客户")
    def test_add_customer(self, login_session,assert_util,test_case):
        # 动态设置测试用例的描述
        allure.dynamic.description(test_case.get('description', ''))

        name = test_case["name"]
        phonenumber = test_case["phonenumber"]
        address = test_case["address"]
        expected_ret = test_case["expected_ret"]
        # 测试步骤
        response = login_session.add_customer(name, phonenumber, address)

        # 断言验证
        assert_util.assert_json_key_exists(response.json(), "ret")
        assert_util.assert_equal(response.json()["ret"], expected_ret)