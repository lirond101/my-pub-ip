import psycopg2
import logging
from config import config
from instance_ips import InstanceIps
logger = logging.getLogger()

def check_db_connection():
    logger.debug("Before connecting to the PostgreSQL database server")
    conn = None
    result = False
    try:
        params = config()
        # (user, password) = get_db_creds()
        # params['user'] = user
        # params['password'] = password
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT version()')
        result = True
        db_version = cur.fetchone()
        logger.info("PostgreSQL database version: %s", db_version)
        cur.close()
    except psycopg2.Error as error:
        logger.error(error)
        result = False
    except Exception as ex:
        logger.exception(ex)
        result = False
    finally:
        if conn is not None:
            conn.close()
    return result

def get_ip_data():
    logger.debug("before executing sql get_ip_data")
    sql = """SELECT read_id, read_time, ip_address FROM my_pub_ip.ips_read_log;"""
    conn = None
    try:
        params = config()
        # (user, password) = get_db_creds()
        # params['user'] = user
        # params['password'] = password
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        fetch_res = cur.fetchall()
        ips = []
        for row in fetch_res:
            ips.append({"read_id": row[0], "read_time": row[1], "ip_address": row[2]})
        cur.close()
        logger.info("get_ip was executed successfully")
    except psycopg2.Error as error:
        logger.error(error)
    except Exception as ex:
        logger.exception(ex)
    finally:
        if conn is not None:
            conn.close()
    return InstanceIps(ips)

def create_ip_data(read_time, ip_address):
    logger.debug("before executing sql create_ip with read_time %s and ip_address %s", str(read_time), ip_address)
    try:
        sql = """INSERT INTO my_pub_ip.ips_read_log(read_time, ip_address) VALUES(%s, %s) RETURNING *;"""
        params = config()
        # (user, password) = get_db_creds()
        # params['user'] = user
        # params['password'] = password
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (read_time, ip_address))
        returning_row = cur.fetchone()
        conn.commit()
        cur.close()
        logger.info("create_ip was executed successfully")
    except psycopg2.Error as error:
        logger.error(error)
    except Exception as ex:
        logger.exception(ex)
    finally:
        if conn is not None:
            conn.close()


# def delete_ip_data(ip_id):
#     logger.debug("before executing sql delete_ip")
#     rows_deleted = 0
#     try:
#         sql = """DELETE FROM postgres.instances WHERE ip_id = (%s);"""
#         params = config()
#         # (user, password) = get_db_creds()
#         # params['user'] = user
#         # params['password'] = password
#         conn = psycopg2.connect(**params)
#         cur = conn.cursor()
#         cur.execute(sql, (ip_id, ))
#         rows_deleted = cur.rowcount
#         conn.commit()
#         cur.close()
#     except psycopg2.Error as error:
#         logger.error(error)
#     except Exception as ex:
#         logger.exception(ex)
#     finally:
#         if conn is not None:
#             conn.close()