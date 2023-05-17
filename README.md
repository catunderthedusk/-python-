# -python-
用python模拟鼠标点击网页，实现自动WiFi连接action\n
具体上用了selenuim库来实现简单的进入网页，输入账号，用ActionChains来输入密码。\n
并通过检测网页id元素实现了是否已经登录，是否登录成功。\n
单独运行大概50mb\n
可以通过自己调节来实现，多久重新登录一次\n
环境：python3.11.2 selenium4.9.1 （新版本应该可以兼容）chrome版本113.0.5672.93 chromedriver版本113.0.5672.63\n


