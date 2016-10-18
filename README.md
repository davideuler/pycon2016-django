## 介绍
opsrecorder是PyCon China 2016上面 Django分享的例子。

一个 应用发布管理的小工具，开发、测试人员申请应用发布，运维人员审批，发布后更新状态为已发布。
几分钟做出来的小应用，目前只有提交应用的功能。 

## 应用默认使用sqlite数据库
cd opsrecorder

## 安装依赖
pip install -r requirements.txt

## 启动服务
python ./manage.py runserver 

## 指定绑定IP与端口启动服务
./manage.py runserver 0.0.0.0:8080

## TODO
空的时候把审批的功能，不同角色权限控制的功能加上。
