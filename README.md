# GraduationDesign

## 部署
安装虚拟机 pip install virtualenv

创建虚拟机 virtualenv .env

进入虚拟机 source .env/bin/activate

安装依赖 pip install -r requirements.txt

修改config.py 设置数据库信息 自行创建数据库

运行deploy.py 自动生成数据表

运行程序 FLASK_APP=app.py flask run

## 接口
name 用户名
password 密码
tel 联系方式
id 商品编号
userid 用户id
title 商品名
details 商品描述
price 商品价格
tag 商品类型
img_file 图片
time 时间
flag 0求购 1出售
