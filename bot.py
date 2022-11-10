
import json
import interactions
from async_timeout import timeout
import sqlite3

# con = sqlite3.connect('wallet.db')
# cur = con.cursor()

with open('config.json', 'r') as f:
    config = json.load(f)

host = config['host']
port = config['port']
# etherscan_api_key = config['etherscan_api_key']
# wallet_address = config['wallet_address']

bot = interactions.Client(
    token=config['token'],
    intents=interactions.flags.Intents.ALL,
    presence=interactions.ClientPresence(
        activities=[interactions.presence.PresenceActivity(name='Made by 暻餃劂',type=0)],
        status='online',
        afk=False
    )
)

@bot.command(name='setwallet', description='連接你的MetaMask錢包到Discord帳號')
async def setwallet(ctx):
    await ctx.send('請查閱私訊')
    await ctx.author.send('請點擊以下連結連接你的MetaMask錢包')
    await ctx.author.send('http://'+str(host)+':'+str(port)+'/'+str(ctx.author.id))




@bot.event
async def on_ready():
    print('Now: ', bot.me.name)

if __name__ == '__main__':
    bot.start()