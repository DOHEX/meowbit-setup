import sys
sys.path.insert(0,'/app/lib')
import network
import upip

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)  # 创建WLAN对象
    wlan.active(True)                    # 激活接口
    wlan.connect(ssid, password)         # 连接到网络

    while not wlan.isconnected():
        pass  # 等待直到连接成功

    print('Network config:', wlan.ifconfig())  # 打印IP配置信息

# 使用你的WiFi凭据替换下面的SSID和密码
connect_to_wifi('你的SSID', '你的密码')
