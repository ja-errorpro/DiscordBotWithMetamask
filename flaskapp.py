from flask import Flask, render_template, request
import sqlite3

con = sqlite3.connect('wallet.db',check_same_thread=False)
cur = con.cursor()

def get_wallet(discord_id: str):
    try:
        cur.execute("SELECT wallet_address FROM wallet WHERE discord_id = ?", (discord_id,))
        rets = cur.fetchone()
        ret = rets[0]
        return ret
    except:
        return False

def set_wallet(discord_id: str, wallet: str):

    cur.execute("INSERT INTO wallet VALUES (?, ?)", (discord_id, wallet))
    con.commit()


app = Flask(__name__)

@app.route('/<discord_id>')
def index(discord_id):
    return render_template('index.html', discord_id=discord_id)

@app.route('/sync', methods=['POST'])
def sync():
    discord_id = request.json['discord_id']
    wallet_address = request.json['wallet_address']
    if get_wallet(str(discord_id))!=False:
        return 'Wallet already set'
    else:
        set_wallet(str(discord_id), str(wallet_address))
        return 'Wallet set'

@app.route('/read',methods=['POST'])
def read():
    discord_id = request.form['discord_id']
    if get_wallet(discord_id):
        return get_wallet(discord_id)
    else:
        return 'Wallet not set'

if __name__ == '__main__':
    cur.execute("CREATE TABLE IF NOT EXISTS wallet (discord_id text, wallet_address text)")
    app.run()

