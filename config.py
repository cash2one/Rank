﻿# coding: utf-8
__author__ = 'liufei'

import sys
import os
import platform
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
reload(sys)
sys.setdefaultencoding('utf8')

class config:
    def __init__(self, driverConfig, proxy=""):
        # 1 - 本地浏览器配置代理；2 - windows测试机配置代理；
        if proxy:
            try:
                iparray = proxy.split(":")
                ip, port = iparray[0], int(iparray[1])
            except:
                proxy, ip, port = "获取代理失败, 请检查代理配置!", "", ""
        else:
            proxy, ip, port = "获取代理失败, 请检查代理配置!", "", ""

        print "当前使用的代理服务器：%s" % proxy
        if driverConfig == "web_firefox":
            profile = webdriver.FirefoxProfile()
            profile.set_preference("network.proxy.type", 1)
            profile.set_preference("network.proxy.http", ip)
            profile.set_preference("network.proxy.http_port", port)
            profile.update_preferences()
            try:
                self.driver = webdriver.Firefox(
                    # executable_path="%s/drivers/" % os.environ["HOME"],
                    firefox_profile=profile,
                    )
            except Exception, e:
                assert False, e

        elif driverConfig == "web_remote":
            PROXY = proxy
            webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
                "httpProxy":PROXY,
                "ftpProxy":PROXY,
                "sslProxy":PROXY,
                "noProxy":None,
                "proxyType":"MANUAL",
                "class":"org.openqa.selenium.Proxy",
                "autodetect":False
            }
            try:
                self.driver = webdriver.Remote(
                    "http://192.168.56.101:4444/wd/hub",
                    webdriver.DesiredCapabilities.FIREFOX)
            except Exception, e:
                assert False, e

        elif driverConfig == "h5_firefox":
            profile = webdriver.FirefoxProfile()
            profile.set_preference("network.proxy.type", 1)
            profile.set_preference("network.proxy.http", ip)
            profile.set_preference("network.proxy.http_port", port)
            profile.set_preference(
                "general.useragent.override",
                "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4"
            )
            profile.update_preferences()
            try:
                self.driver = webdriver.Firefox(
                    # executable_path= "%s/drivers/" % os.environ["HOME"],
                    firefox_profile=profile,
                    )
            except Exception, e:
                assert False, e

        elif driverConfig == "h5_chrome":
            if platform.system() == "Darwin":
                chromedriver = "%s/drivers/" % os.environ["HOME"]
            elif platform.system() == "Windows":
                chromedriver = "C:\chromedriver\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = chromedriver
            mobile_emulation = {"deviceName": "Google Nexus 5"}
            option = webdriver.ChromeOptions()
            option.add_experimental_option("mobileEmulation", mobile_emulation)
            option.add_argument('--proxy-server=%s' % proxy)
            try:
                self.driver = webdriver.Chrome(
                    # executable_path=chromedriver,
                    chrome_options=option)
            except Exception, e:
                assert False, e

        elif driverConfig == "h5_remote_firefox":
            profile = webdriver.FirefoxProfile()
            profile.set_preference("network.proxy.type", 1)
            profile.set_preference("network.proxy.http", ip)
            profile.set_preference("network.proxy.http_port", port)
            profile.set_preference(
                "general.useragent.override",
                "Mozilla/5.0 (Linux; Android 5.1.1; Mi-4c Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36"
            )
            profile.update_preferences()
            try:
                self.driver = webdriver.Remote(
                    command_executor="http://192.168.56.101:4444/wd/hub",
                    browser_profile=profile,
                    desired_capabilities=DesiredCapabilities.FIREFOX)
            except Exception, e:
                assert False, e

        elif driverConfig == "h5_remote_chrome":
            mobile_emulation = {"deviceName": "Google Nexus 5"}
            options = webdriver.ChromeOptions()
            options.add_argument('--proxy-server=%s' % proxy)
            options.add_experimental_option("mobileEmulation", mobile_emulation)
            try:
                self.driver = webdriver.Remote(
                    command_executor="http://192.168.56.101:4444/wd/hub",
                    desired_capabilities=options.to_capabilities())
            except Exception, e:
                assert False, e

        self.driver.implicitly_wait(30)
        self.driver.set_script_timeout(30)
        self.driver.set_page_load_timeout(100)