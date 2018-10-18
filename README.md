# 袋鼠打印--树莓派控制打印机程序

## 此程序是袋鼠打印项目的硬件部分，主要功能是通过树莓派控制打印机，实现对袋鼠打印APP上订单的打印。
#### 原理说明：
此程序是袋鼠打印的硬件部分，此程序通过对rooins的数据库中的订单进行循环查询，将订单中处于等待打印状态的订单数据同步到树莓派中，
然后调用树莓派中的`lpr`命令对订单进行打印。
#### 注意：
   此程序是rooins项目的硬件部分，使用此程序之前请确保已经部署好rooins项目(https://github.com/hopeaktian/rooins.git)
   此程序使用的数据库为rooins项目中的数据库，请在使用此程序之前确保数据库已经成功运行。

### 软件架构：
1. python 2.7
2. sqlalchemy ORM 数据库对象关系映射
### 硬件条件：
1. 树莓派(其他基于linux的硬件平台也可以)，需配置好internet网络连接
2. 打印机，并成功连接树莓派。

### 安装与配置环境：
1. clone 此代码到树莓派任意目录：\
`git clone https://github.com/hopeaktian/rooins-raspberry.git`
2. 首先须确定已经在树莓派上安装 `lpr` 命令, 并调试好打印机，确保`lpr`命令能成功打印文件。(已经在树莓派安装lpr的请跳过此步骤) \
`apt install lpr`
3. 在 `config.py` 里面配置好数据库的信息
4. 创建虚拟Python环境，请先检查树莓派系统中是否安装virtualenv命令，没有此命令的请用一下命令安装。\
`sudo apt-get install virtualenv -y`
然后创建python2.7的虚拟环境使用以下命令 \
`virtualenv env`
5. 安装软件依赖包：安装之前先激活python虚拟环境 \
激活环境： `source ./env/bin/activate` \
安装依赖包： `pip install -r requirements.txt`
### 使用说明
1. 首次使用时请务必执行初始化程序, 用于删除为git提交空目录时创建占位文件。\
`sh init.sh`
2. 运行软件 \
打开树莓派终端，并进入软件根目录，执行以下命令以运行后台脚本，程序将会在后台保持运行。
`sh start.sh`
3. 终止程序 \
`sh stop.sh`


### 软件目录介绍
```
rooins-raspberry/
├── config.py                   数据库配置文件
├── init.sh                     初始化脚本，首次运行，请执行。
├── log                         日志目录,软件运行的所有日志在此目录中
│   ├── download_error_log      下载错误日志
│   ├── download_log            下载成功日志
│   ├── print_access_log        打印成功日志
│   ├── print_error_log         打印错误日志
│   ├── ToPrint_filename        （特殊文件！）保存等待打印订单的文件名,此文件对非常重要，请勿随意修改，或删除此文件。

├── main.py                     主程序
├── model.py                    数据库模型
├── README.md                   
├── requirements.txt            python依赖包
├── start.sh                    启动脚本
└── User_Files                  文件下载目录
    ├── Finished_Print          已经完成打印的文件目录，To_Print目录中打印完成的订单文件会自动移出到此目录中。
    └── To_Print                预打印文件目录，保存了正处于等待打印的订单文件。
    
```
    
