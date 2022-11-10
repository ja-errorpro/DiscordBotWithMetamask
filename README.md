# Discord帳號連接MetaMask錢包 

![python3.8+](https://img.shields.io/badge/python-3.8%2B-green)

## 安裝套件

```bash
pip3 install -r requirements.txt
```

## 請先修改config.json

```json
{
	"token":"<discord-bot-token-here>",
	"prefix":"d!",
	"Admin":"<the-owner's-discord-id>",
	"host":"<your-hostname-or-ip-address>",
	"port":"<port>"
}
```

## 啟動Flask

```bash
python3 flaskapp.py
```

## 啟動Discord Bot

```bash
python3 bot.py
```