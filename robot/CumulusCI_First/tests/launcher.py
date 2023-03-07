import sys

from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By
from robot.api.deco import keyword
from robot.api.exceptions import *
import random,string,os
from selenium import webdriver
from jproperties import Properties
@keyword(name = 'Create Profile')
def create_profile(certificate_name):
    configs = Properties()
    with open(os.path.realpath(os.path.join(os.path.dirname(__file__), '../','settings.properties')), 'rb') as config_file:
        configs.load(config_file)
    cert_dir=os.path.realpath(os.path.join(os.path.dirname(__file__), '../certificates/'))
    cert=os.path.join(cert_dir,f'{certificate_name}_FFP')
    if not os.path.exists(cert):
        raise FileNotFoundError('Certificate not found')
    options = webdriver.FirefoxOptions()
    if configs.get('EXECUTION_PLATFORM').data=='local':
        pass
    else:
        options.headless=True
    options.set_preference('profile', cert)
    options.set_preference("security.default_personal_cert", "Select Automatically")
    options.set_preference("toolkit.startup.max_resumed_crashes", "10")
    options.set_preference("security.sandbox.content.level", 4)
    options.accept_insecure_certs = True
    options.set_preference("webdriver.log.init",True)
    return options

@keyword(name = 'Get Certificate Path')
def get_certificate_path(certificate_name):
    cert_dir=os.path.realpath(os.path.join(os.path.dirname(__file__), '../certificates/'))
    cert=os.path.join(cert_dir,f'{certificate_name}_FFP')
    if not os.path.exists(cert):
        raise FileNotFoundError('Certificate not found')
    return cert


def capabilities():
    capability = {"acceptInsecureCerts": True}
    return capability

@keyword(name='Raise Exception But Continue Excecution')
def throw_continuable_exception():
    raise ContinuableFailure()

@keyword(name='Get Random String Lower Case Value')
def get_random_string_lower_case_value(length):
    return ''.join(random.sample(string.ascii_lowercase, length))
