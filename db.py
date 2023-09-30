import psycopg2
import logging
from config import config
# , get_db_creds

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