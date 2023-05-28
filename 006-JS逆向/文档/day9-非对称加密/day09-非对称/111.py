# -*- coding: utf-8 -*-
import requests
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import execjs


def index():
    pass


if __name__ == '__main__':
    index()
