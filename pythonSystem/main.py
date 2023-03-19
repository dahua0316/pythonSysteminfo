# -*- coding: utf-8 -*-
import SystemInfo
import psutil


if __name__ == '__main__':
        print(SystemInfo.GetGpuInfo())
        print(SystemInfo.GetCpuInfo())
        print(SystemInfo.GetMemInfo())
        print(SystemInfo.GetProcess("unity.exe"))
        print(psutil.Process(4748).memory_percent())

