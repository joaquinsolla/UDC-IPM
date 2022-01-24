#! /usr/bin/python3
# -- coding: utf-8 --

import gettext

from controller import Controller
from view import View
from model import Model
import math


if __name__ == '__main__':

    controller = Controller()
    controller.set_model(Model())
    controller.set_view(View())
    controller.main()
