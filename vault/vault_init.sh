export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN="myroot"
vault secrets enable database
vault write database/config/postgresql \
  plugin_name=postgresql-database-plugin \
  allowed_roles="dbuser" \
  connection_url="postgresql://{{username}}:{{password}}@db:5432/postgres" \
  username="vaultuser" \
  password="vaultpassword"

vault write database/roles/dbuser \
  db_name="postgresql" \
  max_ttl="10m" \
  creation_statements="CREATE USER \"{{name}}\" WITH SUPERUSER ENCRYPTED PASSWORD '{{password}}' VALID UNTIL '{{expiration}}'; GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO \"{{name}}\";" \
  revocation_statements="REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM \"{{name}}\"; DROP OWNED BY \"{{name}}\"; DROP ROLE \"{{name}}\";"