# -*- coding:utf-8 -*-


from setuptools import setup, find_packages

setup(
    name = "demo"
    , version = "0.2"

    , packages = find_packages(
        'src'  # 定位到src目录下
        , exclude = ["*.tests", "*.tests.*", "tests.*", "tests"]  # 排除
    )
    , package_dir = {'': 'src'}  # 告知distutils包在src中

    , package_data = {
        '' : ['*.txt']  # 所有包
        , 'demo': ['data/*.bin']  # demo包
    }
)
