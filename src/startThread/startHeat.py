#!-*- coding:utf8 -*-
from src.testStability.initHeatResource import InitHeatResource
import threading

class StartHeat(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self,name='startHeat')

    def run(self):
        InitHeatResource().getStabilityheatAccountResource()
