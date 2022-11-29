it's required to declare env variables below:
1) TG_API_TOKEN
2) TG_CHAT_ID
3) API_LINK

```
export TG_API_TOKEN=<tg api token>
export TG_CHAT_ID=<tg chanel ID>
export API_LINK=https://my.linistry.com/api/CustomerApi/GetAvailabilityAsync?serviceId=3fb796f6-3829-40b9-a549-3feb2b12453a\&startyear=2022\&startmonth=10\&startday=30\&endyear=2022\&endmonth=12\&endday=3\&count=1
```


source .env
docker build -t bot:latest .
docker run -d -it \
  -e TG_API_TOKEN=$TG_API_TOKEN \
  -e TG_CHAT_ID=$TG_CHAT_ID \
  -e API_LINK=$API_LINK \
  --name thai_kl_embassy bot

docker logs thai_kl_embassy
