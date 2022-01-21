import math
from typing import Any
from discord import *
import random as r
import os
import os.path
import requests
import json
import discord
import webcolors as wc
from PIL import Image, ImageColor
from youtube_dl import *




class no_u():
    null=None

    class math():
        null=None

        def random(num1, num2):
            _return=(r.randint(num1, num2))
            return _return

        def add(num1, num2):
            _return=(float(num1)+float(num2))
            return _return

        def subtract(num1, num2):
            _return=(float(num1)-float(num2))
            return _return
        
        def multiply(num1, num2):
            _return=(float(num1)*float(num2))
            return _return

        def divide(num1, num2):
            _return=(float(num1)/float(num2))
            return _return

        def square(num):
            _return=(float(num)*float(num))
            return _return

        def cube(num):
            _return=(float(num)*float(num)*float(num))
            return _return
        
        def quart(num):
            _return=(float(num)*float(num)*float(num)*float(num))
            return _return
        
        def quint(num):
            _return=(float(num)*float(num)*float(num)*float(num)*float(num))
            return _return
        
        def square_root(num):
            _return=(math.sqrt(num))
            return _return
    


    


class log_utils():
    null=None

    def log(file, text):
        f = open(file, "a")
        f.write(str(text + " \n"))
        f.close()
        return print("[logger] logged '" + text + "' to " + file)
    
    def read(file):
        f = open(file, "r")
        f.read()
        f.close()
        return print("[logger] read " + file)


    

class util():
    class JSON():
        null=None

        def load(file=str):
            _return=(json.load(open(f"./{file}")))
            return _return

        def valuestr(file:str, name:str, value:str):
            """
            allows you to add or change a string value
            

            `file:"filename"` string file name
            `name:"name"` sting name
            `value:"value"` string value
            """
            load=(json.load(open(f"./{file}")))
            load[name] = value
            _return=(json.dump(load, open(f"./{file}", 'w')))
            return _return

        def valuebool(file:str, name:str, value:bool):
            """
            allows you to add or change a bool value
            

            `file:"filename"` string file name
            `name:"name"` sting name
            `value:"value"` bool value True or False
            """
            load=(json.load(open(f"./{file}")))
            load[name] = value
            _return=(json.dump(load, open(f"./{file}", 'w')))
            return _return
        
        def valuefloat(file:str, name:str, value:float):
            """
            allows you to add or change a float value
            

            `file:"filename"` string file name
            `name:"name"` sting name
            `value:"value"` float value
            """
            load=(json.load(open(f"./{file}")))
            load[name] = value
            _return=(json.dump(load, open(f"./{file}", 'w')))
            return _return




class ___cache___():
    class getting():
        def apilinkdefreturn(q):
            r=(requests.get(f'{q}'))
            r1=(r.json())
            return r1




class api():
    def get(link:str):
        e=___cache___.getting.apilinkdefreturn(q=link)
        return e





