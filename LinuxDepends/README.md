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