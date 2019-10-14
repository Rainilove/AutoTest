'''
    项目架构:
    核心:api+case+data

    api 封装请求业务(使用requests向服务器发送请求)
    case 封装unittest 相关实现(调用api的请求业务,参数化调用data中的测试数据,自身还需要实现断言业务)
    data 封装测试数据(一般使用json文件)


    测试报告:report+tools+run_suite.py
    report 保存生成的测试报告
    tools 生成测试报告所使用的第三方工具
    run_suite.py 组织测试套件

    全局文件 : app.py
    app.py 封装程序中常量,全局变量,工具方法
'''

# 封装不同接口中URL相同的前缀(协议+域名)
import os

BASE_URL = 'http://localhost/'

# 项目路径(绝对路径)
# PRO_PATH = os.getcwd()

# 动态获取绝对路径的其他方式
FILE_ABS_PATH = os.path.abspath(__file__)
PRO_PATH = os.path.dirname(FILE_ABS_PATH)
print('app python 文件的绝对路径:', FILE_ABS_PATH)
print('项目的绝对路径:', PRO_PATH)
