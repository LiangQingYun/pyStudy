### selenium官方文档
https://selenium-python.readthedocs.io/index.html
谷歌浏览器驱动下载 : https://chromedriver.storage.googleapis.com/index.html?path=113.0.5672.63/

### 浏览器(旧版本)
旧版本chrome下载地址 :  https://downzen.com/en/windows/google-chrome/versions/

### 浏览器版本回退
卸载不完全问题 
使用n++编辑  rm.reg  , 后执行 , 在安装旧版本
```angular2html
Windows Registry Editor Version 5.00
 
;WARNING, this file will remove Google Chrome registry entries  
 
;from your Windows Registry. Consider backing up your registry before
 
; using this file: http://support.microsoft.com/kb/322756
 
; To run this file, save it as 'remove.reg' on your desktop and double-click it.
 
[-HKEY_LOCAL_MACHINE\SOFTWARE\Classes\ChromeHTML] 
 
[-HKEY_LOCAL_MACHINE\SOFTWARE\Clients\StartMenuInternet\chrome.exe] 
 
[HKEY_LOCAL_MACHINE\SOFTWARE\RegisteredApplications]
 
"Chrome"=-
 
[-HKEY_CURRENT_USER\SOFTWARE\Classes\ChromeHTML] 
 
[-HKEY_CURRENT_USER\SOFTWARE\Clients\StartMenuInternet\chrome.exe] 
 
[HKEY_CURRENT_USER\SOFTWARE\RegisteredApplications]
 
"Chrome"=-
 
[-HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Uninstall\Chrome]
 
[-HKEY_CURRENT_USER\Software\Google\Update\Clients\{8A69D345-D564-463c-AFF1-A69D9E530F96}]
 
[-HKEY_CURRENT_USER\Software\Google\Update\ClientState\{8A69D345-D564-463c-AFF1-A69D9E530F96}]
 
[-HKEY_CURRENT_USER\Software\Google\Update\Clients\{00058422-BABE-4310-9B8B-B8DEB5D0B68A}]
 
[-HKEY_CURRENT_USER\Software\Google\Update\ClientState\{00058422-BABE-4310-9B8B-B8DEB5D0B68A}]
 
[-HKEY_LOCAL_MACHINE\SOFTWARE\Google\Update\ClientStateMedium\{8A69D345-D564-463c-AFF1-A69D9E530F96}]
 
[-HKEY_LOCAL_MACHINE\SOFTWARE\Google\Update\Clients\{8A69D345-D564-463c-AFF1-A69D9E530F96}]
 
[-HKEY_LOCAL_MACHINE\SOFTWARE\Google\Update\ClientState\{8A69D345-D564-463c-AFF1-A69D9E530F96}]
 
[-HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Google\Update\Clients\{8A69D345-D564-463c-AFF1-A69D9E530F96}]

```
### selenium 驱动下载  ,对应浏览器版本
`windows只有32位版本`  
下载地址 :
Chrome WebDriver：https://sites.google.com/a/chromium.org/chromedriver/downloads     https://chromedriver.storage.googleapis.com/index.html?path=113.0.5672.63/
Firefox WebDriver：https://github.com/mozilla/geckodriver/releases  
Edge WebDriver：https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/  
Safari WebDriver：https://webkit.org/blog/6900/webdriver-support-in-safari-10/  



