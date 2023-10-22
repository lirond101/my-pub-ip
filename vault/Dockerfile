FROM hashicorp/vault@sha256:ccbb5fde9d55b3dc57cf8694dea9c988ba0127b205661b652b5264f8d5901a58

RUN mkdir -p /app/config

# WORKDIR /app/config

COPY ./vault_init.sh /app/config/vault_init.sh

RUN chmod +x /app/config/vault_init.sh

# CMD [ "./app/config/vault_init.sh"]