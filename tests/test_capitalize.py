import os
import sys

# Добавить путь к папке package_name в PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'package_name', '..')))

from package_name.capitalize import capitalize

assert capitalize('hello') == 'Hello'

assert capitalize('') == ''

print('Все тесты пройдены!')
