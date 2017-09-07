#!/usr/bin/env bash

# 代码更新
git pull


# 建立一个软连接
ln -s -f /root/bbs/bbs.conf /etc/supervisor/conf.d/bbs.conf


# 重启服务器
sudo service mongod restart
sudo service supervisor restart

# 友好提示
echo 'deploy success'