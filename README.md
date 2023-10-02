# my-pub-ip
> Make sure you have Docker installed and that you are in the ROOT folder
1. Build the Docker image locally
   ```shell script
   $ docker build -t lirondadon/my-pub-ip:<tag> .
   ```

2. Run the Docker container with the mandatory env variables
   ```shell script
   $ docker run -it -p 5000:5000 lirondadon/my-pub-ip:<tag>
   ```

3. If no errors appear in the log, the app should run on `http://localhost:5000`

4. Enjoy!

Configure Vault:
On PostgreSQL:
postgres=# CREATE ROLE vaultuser WITH LOGIN SUPERUSER PASSWORD 'vaultpassword';

Vault in dev mode:
$ export VAULT_ADDR='http://127.0.0.1:8200'
$ export VAULT_TOKEN="myroot"
$ vault secrets enable database
$ vault write database/config/postgresql \
    plugin_name=postgresql-database-plugin \
    allowed_roles="dbuser" \
    connection_url="postgresql://{{username}}:{{password}}@db:5432/postgres" \
    username="vaultuser" \
    password="vaultpassword"

$ vault write database/roles/dbuser \
    db_name="postgresql" \
    max_ttl="10m" \
    creation_statements="CREATE USER \"{{name}}\" WITH SUPERUSER ENCRYPTED PASSWORD '{{password}}' VALID UNTIL '{{expiration}}'; GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO \"{{name}}\";" \
    revocation_statements="REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM \"{{name}}\"; DROP OWNED BY \"{{name}}\"; DROP ROLE \"{{name}}\";"

# https://developer.hashicorp.com/vault/api-docs/secret/databases

$ curl \
    --header "X-Vault-Token: myroot" \
    --request GET \
    http://127.0.0.1:8200/v1/database/config/postgresql

$ curl \
    --header "X-Vault-Token: myroot" \
    http://127.0.0.1:8200/v1/database/creds/dbuser