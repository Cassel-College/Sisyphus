#!/bin/bash

# 指定要查找ini文件的路径
path="/usr/lib/systemd/system/"

# 检查路径是否存在
if [ ! -d "$path" ]; then
  echo "路径不存在"
  exit 1
fi

# 查找frps文件
if [ "$(ls -A $path/frps.service 2>/dev/null)" ]; then
    echo "frps was install."
else
    echo "frps was not install"
    sh ./../install/frps.sh
fi

systemctl enable frps
systemctl start frps