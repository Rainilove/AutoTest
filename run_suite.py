'''
    组织测试套件生成测试报告
    流程:
        1.导包
        2.创建套件对象
        3.创建文件夹,并且使用工具执行套件,将执行的结果写入文件流
'''
import time
import unittest
from BeautifulReport import BeautifulReport
from case.TestShopUser import TestUser

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestUser))

report_file = "{}-result.html".format(time.strftime('%Y%m%d%H%M%S'))
BeautifulReport(suite).report(filename=report_file, description='Chrome', log_path='./report/')
