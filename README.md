it's required to declare env variables below:
1) TG_API_TOKEN
2) TG_CHAT_ID

```
export TG_API_TOKEN=<tg api token>
export TG_CHAT_ID=<tg chanel ID>
```

```
source .env
docker build -t bot:latest .
docker run -d -it \
  -e TG_API_TOKEN=$TG_API_TOKEN \
  -e TG_CHAT_ID=$TG_CHAT_ID \
  --name thai_kl_embassy bot

docker logs thai_kl_embassy
```
