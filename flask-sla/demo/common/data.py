# coding:utf-8
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from demo.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_ECHO

def db_query(sql, settings=None, echo=None):
    """
    执行增删改 SQL 语句
    Args:
        sql: SQL 语句
        settings: 数据库连接字符串
        echo: 是否输出 SQL 语句

    Returns:
        执行结果
    """
    if settings is None:
        settings = SQLALCHEMY_DATABASE_URI

    if echo is None:
        echo = SQLALCHEMY_ECHO

    return create_engine(settings, echo=echo).connect().execute(text(sql)).fetchall()

def db_execute(sql, settings=None, echo=None):
    """
    执行增删改 SQL 语句
    Args:
        sql: SQL 语句
        settings: 数据库连接字符串
        echo: 是否输出 SQL 语句

    Returns:
        影响行数
        """
    if settings is None:
        settings = SQLALCHEMY_DATABASE_URI

    if echo is None:
        echo = SQLALCHEMY_ECHO

    return create_engine(settings, echo=echo).connect().execute(text(sql)).rowcount