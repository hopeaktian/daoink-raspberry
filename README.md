# 袋鼠打印树莓派控制程序

## 此程序是袋鼠打印项目的硬件部分，主要功能是通过树莓派控制打印机，实现对袋鼠打印APP上订单的打印。

### 软件架构：
1. python 2.7
2. sqlalchemy ORM 数据库对象关系映射
### 硬件条件：
1. 树莓派，需配置好internet网络连接
2. 打印机，并成功连接树莓派。

### 安装：
1. 首先须确定已经在树莓派上安装 `lpr` 命令, 并调试好打印机，确保`lpr`命令能成功打印文件 \
`apt install lpr`
2. 在 `config.py` 里面配置好数据库的信息
3. 安装软件依赖包 \
`pip install -r requirements.txt`
4. 初始化程序, 用于删除git提交空目录时的占位文件，首次运行时请执行。  \
`sh init.sh`
5. 运行软件 \
打开树莓派终端，并进入软件根目录，执行以下命令以运行后台脚本，程序将会在后台保持运行。
`sh start.sh`
6. 终止程序 \
`sh stop.sh`


### 软件目录介绍
```
rooins-raspberry/
├── config.py                   数据库配置文件
├── init.sh                     初始化脚本，首次运行，请执行。
├── log                         日志目录
│   ├── download_error_log      下载错误日志
│   ├── download_log            下载成功日志
│   ├── print_access_log        打印成功日志
│   ├── print_error_log         打印错误日志
│   ├── ToPrint_filename        预打印文件名

├── main.py                     主程序
├── model.py                    数据库模型
├── README.md                   
├── requirements.txt            python依赖包
├── start.sh                    启动脚本
└── User_Files                  文件下载目录
    ├── Finished_Print          已经打印的文件目录
    └── To_Print                预打印文件目录
    
```
    
