# 设置git clone加速，只对github.com
git config --global http.https://github.com.proxy socks5://127.0.0.1:1080

# 取消git clone取消代理
git config --global --unset http.https://github.com.proxy