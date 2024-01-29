# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","myproject.settings")

import django

django.setup()

import random

from curd.models import employees
from random import *
from faker import Faker
faker=Faker()
y=employees()
def fakemployees():
    f_empno=randint(200,999)
    f_empname=faker.name()
    f_age=randint(19,45)
    f_salary=(20000,45000)
    f_adress=faker.city()
    f_email=faker.email()
    emp=employees.objects.get_or_create()

for i in  range(0,10):
    fakemployees()