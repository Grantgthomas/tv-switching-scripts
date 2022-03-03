C:/Users/gamad/Documents/Projects/MultiMonitorTool.exe /TurnOff \\.\DISPLAY2
C:/Users/gamad/Documents/Projects/MultiMonitorTool.exe /Switch \\.\DISPLAY1 \\.\DISPLAY2
Start-Process -FilePath "Rainmeter.exe" -WorkingDirectory "C:\Program Files\Rainmeter"
Start-Process -FilePath "wallpaper32.exe" -WorkingDirectory "C:\Program Files (x86)\Steam\steamapps\common\wallpaper_engine"
Start-Process -FilePath "RestartRainmeter" -WorkingDirectory "C:\Program Files\Rainmeter"
get-process ui32 | %{ $_.closemainwindow() }
get-process ui32 | %{ $_.closemainwindow() }