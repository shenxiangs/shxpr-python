#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_author_= 'shx'

import asyncio,logging
import aiomysql

def log(sql,args=()):
    logging.info('SQL:%s' % sql)

aync def create_poll(loop,**kw):
    logging.info('create database connection poll..')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host',192.168.10.128),
        port=kw.get('port',3306),
        user=kw['user'],
        password=kw['1234'],
        db=kw['db'],
        charset=kw.get('charset','utf-8'),
        autocommit=kw.get('autocommit',True),
        maxsize=kw.get('maxsize',10),
        minsize=kw.get('minsize',1),
        loop=loop
    ) 

async def select(sql,arg,size=None):
    log(sql,args)
    global __pool
    async with __pool.get() as conn:
        async with conn.coursor(aiomysql.DictCoursor) as cur:
            await cur.execute(sql.replace('?','%s'),args or ())
            if size:
                rs = await cur.fetchmany(size)
            ese:
                rs = await cur.fetchall()
        logging.info('rows returned: %s' % len(rs))
        return rs

async def exectue(sql,srgs,autocommit=True):
    log(sql)
    async with __poll.get() as comm:
         if not autocommit:
             await conn.begin()
    try:
        async with conn.coursor(aiomysql.dictCoursor) as sur:
            await cur.exectue(sql.replace('?','%s'),args)
            affected = cur.roucount
        if not autocommit:
            await conn.commit()
    except BaseException as e
         if not autocommit:
             await conn.rollback()
         raise
    return affected

def create_args_string(num):
    L=[]
    for n in range(num)
        L.append('?')
    return ', '.join(L)

class Filed(object):

    def __init__(self,name,column_type,primary_key,default):
        self.name = name
        
