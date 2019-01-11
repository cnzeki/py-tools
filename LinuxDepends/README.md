## LinuxDepends
查找linux程序的所有依赖库并拷贝到指定目录下，方便程序打包部署。
支持两种工作方式：

### 1. 静态提取
解析`ldd`程序的输出，得到依赖库列表，拷贝到生成目录下
```
python get_depends.py $elf.bin $deploy-dir
```
$elf.bin：可执行程序
$deploy-dir:依赖库生成目录

### 2. 运行时提取
通过读取程序运行时加载的内存映射表生成依赖列表
#### 得到程序的pid
```
ps -ef | grep proc_name
```
#### 得到内存映射列表文件
```
sudo cat /proc/$pid/maps > so.list
```
#### 拷贝依赖
```
python get_depends.py so.list $deploy-dir
```


## 示例

bash 程序的输出如下：

```
[omit]   1: /bin/bash
[ ok ]   2: /lib/x86_64-linux-gnu/ld-2.23.so
[ ok ]   3: /lib/x86_64-linux-gnu/libc-2.23.so
[ ok ]   4: /lib/x86_64-linux-gnu/libdl-2.23.so
[ ok ]   5: /lib/x86_64-linux-gnu/libnsl-2.23.so
[ ok ]   6: /lib/x86_64-linux-gnu/libnss_compat-2.23.so
[ ok ]   7: /lib/x86_64-linux-gnu/libnss_files-2.23.so
[ ok ]   8: /lib/x86_64-linux-gnu/libnss_nis-2.23.so
[ ok ]   9: /lib/x86_64-linux-gnu/libtinfo.so.5.9
[omit]  10: /usr/lib/locale/locale-archive
[omit]  11: /usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache
--------------------------------------------------------------------------------
Total  :11
Success:8
Fail   :0
Omit list:3
          0: /bin/bash
          1: /usr/lib/locale/locale-archive
          2: /usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache
```

拷贝的依赖列表目录如下：

```
-rw-rw-r-- 1 root root  162632 1月  11 13:48 ld-2.23.so
-rw-rw-r-- 1 root root 1868984 1月  11 13:48 libc-2.23.so
-rw-rw-r-- 1 root root   14608 1月  11 13:48 libdl-2.23.so
-rw-rw-r-- 1 root root   93128 1月  11 13:48 libnsl-2.23.so
-rw-rw-r-- 1 root root   35688 1月  11 13:48 libnss_compat-2.23.so
-rw-rw-r-- 1 root root   47600 1月  11 13:48 libnss_files-2.23.so
-rw-rw-r-- 1 root root   47648 1月  11 13:48 libnss_nis-2.23.so
-rw-rw-r-- 1 root root  167240 1月  11 13:48 libtinfo.so.5.9
```

