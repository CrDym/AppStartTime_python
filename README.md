adb shell "logcat | grep START" 查看监听
adb shell am start -W -n +包/包ity 启动app 并且 查看时间
adb shell am force-stop +包名 关闭app
adb shell input keyevent 3   home 键返回