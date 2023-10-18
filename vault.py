import os
from hvac import Client
from hvac.exceptions import Forbidden, VaultError
from requests.exceptions import ConnectionError
import logging
from config import config

logger = logging.getLogger()

def connect_to_vault():
    """
    Returns an hvac client to communicate with Vault

    :param str vault_url: the vault server url
    :param str vault_token: the vault token
    """
    vault_url = config(section="vault")["server"]
    vault_token = os.environ.get('VAULT_TOKEN')

    return Client(url=vault_url, token=vault_token)

def get_db_creds(path = '/database/creds/dbuser'):
    ''' Read secrets from the given path. '''
    try:
        client = connect_to_vault()
        result = client.read(path)
        user = result['data']['username'].strip()
        password = result['data']['password'].strip()
        return user, password
    except ConnectionError:
        logger.error("Failed connecting to vault server at %s", os.environ.get('VAULT_ADDR'))
    except Forbidden:
        logger.error("Permission denied. Make sure the token is authorized to access %s on vault", path)
    except VaultError as e:
        logger.error("Vault Error: " + e.message)
