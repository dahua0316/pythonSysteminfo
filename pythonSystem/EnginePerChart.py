import time
import matplotlib.pyplot as plt
import os
import psutil
import pynvml
import SystemInfo





class EngineDraw:

    def __init__(self, proName='unity.exe'):
        self.rowName = ["显卡型号", "总显存MB", "已用显存MB", "剩余显存MB", "CPU型号", "内存大小", "监测进程PID",
                        "监测进程名称"]
        self.rowValue = [[0], [0], [0], [0], [0], [0], [0], [0]]
        self.ProName = proName
        # cpu总使用率
        self.TotalcpuOcupancyPercent = []
        # 总GPU占用率
        self.TotalgouMemusedPercent = []
        # 总内存占用率
        self.TotalmenUsedPercent = []
        # 监听应用占用率
        self.ProCpuOcupancyPercent = []
        # 监听内存利用率
        self.ProMempercent = []

    def GetInfo(self):
        self.rowValue[0][0] = SystemInfo.GetGpuInfo()["gpuName"]
        self.rowValue[1][0] = SystemInfo.GetGpuInfo()["gpuMemtotal"]
        self.rowValue[2][0] = SystemInfo.GetGpuInfo()["gpuMemused"]
        self.rowValue[3][0] = SystemInfo.GetGpuInfo()["gpuMemfree"]
        self.rowValue[4][0] = SystemInfo.GetCpuInfo()["cpu_name"]
        self.rowValue[5][0] = SystemInfo.GetMemInfo()["memTotal"]
        self.rowValue[6][0] = SystemInfo.GetProcess(self.ProName)['proPid']
        self.rowValue[7][0] = SystemInfo.GetProcess(self.ProName)['proName']

        return self.rowValue

    def GrawTable(self):
        print(self.rowValue)
        plt.rcParams['font.sans-serif'] = ["SimHei"]  # 显示中文
        fig = plt.figure(num=self.ProName,figsize=(15, 10))
        fig1 = plt.figure(num=self.ProName, figsize=(10, 5))
        # 设备基本信息
        ax1 = fig1.add_subplot(211)
        ax1.axis('tight')
        ax1.axis('off')
        ax1.table(cellText=self.rowValue, rowLabels=self.rowName, loc="upper center", colLoc="right", rowLoc="left")

        # cpu总使用率
        cpuSum = []
        # 内存总占用率
        memSum = []
        # 监听应用cpu和内存占用率
        cpuMonitor = []
        memMonitor = []

        times = []

        while True:
            cpuSumPer = SystemInfo.GetCpuInfo()['used']
            memSumPer = SystemInfo.GetMemInfo()['menUsedPercent']
            cpuMonPer = SystemInfo.GetProcess(self.ProName)['cpuOcupancy']
            memMonPer = psutil.Process(SystemInfo.GetProcess(self.ProName)['proPid']).memory_percent()
            t = time.strftime('%H:%M:%S', time.localtime())

            cpuSum.append(cpuSumPer)
            memSum.append(memSumPer)
            cpuMonitor.append(cpuMonPer)
            memMonitor.append(memMonPer)
            times.append(t)

            # cpuMonitor
            ax2 = plt.subplot(221)
            plt.plot(times, cpuMonitor, label="CPU", color="b")
            plt.ylabel(self.ProName + " CPU 占用率%", fontsize=14)
            plt.xticks(rotation=30, fontsize=8)
            plt.yticks(range(0, 110, 5))

            # memMonitor
            ax3 = plt.subplot(222)
            plt.plot(times,  memMonitor, label="Memory", color="y")
            plt.ylabel(self.ProName + " Memory占用率%", fontsize=14)
            plt.xticks(rotation=30, fontsize=8)
            plt.yticks(range(0, 110, 5))

            # cpuSum
            ax4 = plt.subplot(223)
            plt.plot(times, cpuSum, label="CPU", color="y")
            plt.ylabel("总CPU占用率%", fontsize=14)
            plt.xticks(rotation=30, fontsize=8)
            plt.yticks(range(0, 110, 5))

            # cpuMemory
            ax5 = plt.subplot(224)
            plt.plot(times, memSum, label="Memory", color="y")
            plt.ylabel("总Memory占用率%", fontsize=14)
            plt.xticks(rotation=30, fontsize=8)
            plt.yticks(range(0, 110, 5))

            plt.pause(1)
        plt.ioff()
        plt.show()


if __name__ == '__main__':
    dfsd = EngineDraw()
    dfsd.GetInfo()
    dfsd.GrawTable()
