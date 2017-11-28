import functools
import hashlib

import redis

from config import REDIS_HOST, REDIS_PORT, DEFULT_SALT
from flask import request, jsonify, app, make_response, Flask, Response
from flask import json
from flask_restful import abort

from app.exception.FormErrorException import formErrorException
from app.exception.global_error_handle import handle_error

app = Flask(__name__)


def require(*required_args):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            for arg in required_args:
                if arg not in request.json:
                    return formErrorException()

            return func(*args, **kw)

        return wrapper

    return decorator


_redis_cache = redis.Redis(connection_pool=redis.ConnectionPool(REDIS_HOST, REDIS_PORT, db=1))
_redis_db = redis.StrictRedis(REDIS_HOST, REDIS_PORT, db=2)


class RedisDB:
    def __init__(self, conn=_redis_db):
        self.conn = conn

    def set(self, key, value, expire=None):
        self.conn.set(key, value, expire)

    def hget(self, name, key):
        ret = self.conn.hget(name, key)
        if ret:
            ret = ret.decode('utf-8')
        return ret

    def hset(self, name, key, value):
        self.conn.hset(name, key, value)


class RedisCache(RedisDB):
    def __init__(self):
        super().__init__(_redis_cache)


#md5加盐加密
def _hashed_with_salt(info, salt):
    m = hashlib.md5()
    m.update(info.encode('utf-8'))
    m.update(salt)
    return m.hexdigest()

#对登录密码进行加密
def hashed_login_pwd(pwd):
    return _hashed_with_salt(pwd,DEFULT_SALT)

