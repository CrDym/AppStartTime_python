# @Author: cherong 
# @Date: 2018-06-28 13:04:49 
# @Last Modified by:   cherong 
# @Last Modified time: 2018-06-28 13:04:49 
import os
import time
import csv
#app类
class App(object):
    def __init__(self):
        self.content =''
        self.startTime = 0

    #启动APP
    def LaunchApp(self):
        cmd = "adb shell am start -W -n com.fangmi.weilan/.activity.StartActivity"
        self.content = os.popen(cmd)
    #停止APP
    def StopApp(self):
        cmd = "adb shell am force-stop com.fangmi.weilan"   # 冷启动
        #cmd = "adb shell input keyevent 3"  #热启动
        os.popen(cmd)
    #获取启动时间
    def GetLaunchTime(self):
        for line in self.content.readlines():
            if "ThisTime" in line:
                self.startTime = line.split(":")[1]
                break
        return self.startTime

#控制类
class Controller(object):
    def __init__(self,count):
        self.app = App()
        self.counter = count
        self.alldata = [("timestamp","elapsedtime")]

    # 单次测试
    def testprocess(self):
        self.app.LaunchApp()
        time.sleep(3)
        elapsedtime =self.app.GetLaunchTime()
        self.app.StopApp()
        time.sleep(3)
        currentTime =self.getCurrentTime()
        self.alldata.append((currentTime,elapsedtime))

    # 多次执行测试过程
    def run(self):
        while self.counter >0:
            self.testprocess()
            self.counter = self.counter-1

    # 获取当前时间戳
    def getCurrentTime(self):
        currentTime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        return currentTime
    #将结果写入csv文件
    def SaveDataToCSV(self):
        csvfile =open('startTime.csv','w',encoding='utf-8',newline='')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()

if __name__ == "__main__":
    controller = Controller(2)
    controller.run()
    controller.SaveDataToCSV()


