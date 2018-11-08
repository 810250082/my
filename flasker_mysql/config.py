# -*- coding:utf-8 -*-


# 应用配置参数类
class Config():
    # 数据库设置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/my_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 回话设置
    SECRET_KEY = '\xbfh`mX\x18\xe7\x89\x19u\x8a\xb2\xf0R\xf8\xf4\xbd!\xe0n]\x97\xb9a'


# 配置app
def create_app(app):
    # 注册蓝图
    from app.test import test
    app.register_blueprint(test, url_prefix="/mytest")

    return app





