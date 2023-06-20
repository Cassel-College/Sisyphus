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

    if [ "$(ls -A frp_0.33.0_linux_amd64.tar.gz 2>/dev/null)" ]; then
        echo "Soft frps was download."
    else
        echo "Download soft: frp_0.33.0_linux_amd64.tar.gz."
        wget https://github.com/fatedier/frp/releases/download/v0.33.0/frp_0.33.0_linux_amd64.tar.gz
        # wget https://github.com/fatedier/frp/releases/download/v0.33.0/frp_0.33.0_linux_amd64.tar.gz 2>/dev/null
    fi

    if [ "$(ls -A frp_0.33.0_linux_amd64.tar.gz 2>/dev/null)" ]; then
        if [ "$(ls -l | grep frp_0.33.0_linux_amd64 | grep "^d" 2>/dev/null)" ]; then
            echo "Has soft Decompression folder. Delete..."
            rm -rf frp_0.33.0_linux_amd64
        else
            echo "No Soft Decompression folder."
        fi
        echo "Decompression frp_0.33.0_linux_amd64.tar.gz"
        tar -zxvf frp_0.33.0_linux_amd64.tar.gz 1&2>/dev/null
    else
        echo "Error:No soft frp_0.33.0_linux_amd64.tar.gz."
    fi

    cd frp_0.33.0_linux_amd64
    echo "Now in: $(pwd)"
    temp_path=$(pwd | grpe "frp_0.33.0_linux_amd64")

    if [ "${temp_path}" ];
    then
        frps_ini_file="./frps.ini"
        echo "Delete old frps config file: ${frps_ini_file}"
        rm -f "${frps_ini_file}"

        echo "Create new frps config file: ${frps_ini_file}"
        touch "${frps_ini_file}"
        echo "Edit new frps config file."
        echo "[common]" >> "${frps_ini_file}"

        echo "# frp监听的端口，默认是7000，可以改成其他的" >> "${frps_ini_file}"
        echo "bind_port = 7000" >> "${frps_ini_file}"
        echo "# 授权码，请改成更复杂的" >> "${frps_ini_file}"
        echo "token = 12345678" >> "${frps_ini_file}"
        echo "" >> "${frps_ini_file}"
        echo "# frp管理后台端口，请按自己需求更改" >> "${frps_ini_file}"
        echo "dashboard_port = 7500" >> "${frps_ini_file}"
        echo "# frp管理后台用户名和密码，请改成自己的" >> "${frps_ini_file}"
        echo "dashboard_user = admin" >> "${frps_ini_file}"
        echo "dashboard_pwd = admin" >> "${frps_ini_file}"
        echo "enable_prometheus = true" >> "${frps_ini_file}"
        echo "" >> "${frps_ini_file}"
        echo "# frp日志配置" >> "${frps_ini_file}"
        echo "log_file = /var/log/frps.log" >> "${frps_ini_file}"
        echo "log_level = info" >> "${frps_ini_file}"
        echo "log_max_days = 3" >> "${frps_ini_file}"
        echo "" >> "${frps_ini_file}"

        echo "copy frps to /usr/bin."
        cp frps /usr/bin

        echo "copy frps config file to /etc/frp."
        mkdir -p /etc/frp
        cp frps.ini /etc/frp

        echo "copy systemd/frps.service to /usr/lib/systemd/system/."
        cp systemd/frps.service /usr/lib/systemd/system/

        cd -
        echo "Now in: $(pwd)"
    else
        echo "install frps failed. Please try again."
    fi
    echo "Delete soft install file and folder."
    rm -f frp_0.33.0_linux_amd64.tar.gz
    rm -rf frp_0.33.0_linux_amd64
fi