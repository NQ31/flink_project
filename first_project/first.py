'''
Date         : 2022-06-19 22:38:58
LastEditors  : huangxiaoqi <huangxiaoqi@zeek.one>
LastEditTime : 2022-06-19 22:43:15
Descripttion : flink 第一个测试项目
FilePath     : /flink_project/first_project/first.py
'''
from pyflink.table import (EnvironmentSettings, TableEnvironment, TableDescriptor,Schema, DataTypes, FormatDescriptor)
from pyflink.table.expressions import lit, col
from pyflink.table.udf import udtf
