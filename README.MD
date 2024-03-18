## 介绍
基于python的 Giwifi自动认证
    可用于 河南理工大学 HPU
          岭南师范学院 LNU


## 使用
- ip(可选) -> 默认为192.168.99.120


```
pip install pycryptodome
pip install requests
pip install bs4
```

```
python master.py username password ip(可选)
```

```
.\master.exe username password ip(可选)
```

## 其他实现

nodejs实现
- [GiraffeLe/Auto-Giwifi](https://github.com/GiraffeLe/Auto-Giwifi)
利用cloudflare workers 和 curl 实现 (小闪存路由器推荐使用)
- [mcitem/auth-giwifi-workers](https://github.com/mcitem/auth-giwifi-workers)
