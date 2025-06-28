import requests
import time

# === 🔐 TELEGRAM SETUP ===
BOT_TOKEN = "***YOUR_BOT_TOKEN***"
CHAT_ID = "***YOUR_CHAT_ID***"

# === 🚦 MEMORY FLAG TO PREVENT REPEATED ALERTS ===
last_signal = None

# === 🚀 FUNCTION TO CHECK OPTIONS LOGIC ===
def check_signal():
    global last_signal

    # === 🧪 SAMPLE LOGIC (Replace later with live NSE logic)
    nifty_price = 23400
    fake_oi_pe = 900000
    fake_oi_ce = 2000000

    # === 📈 Buy / Sell Signal Logic
    buy_signal = fake_oi_pe > 800000 and nifty_price > 23350
    sell_signal = fake_oi_ce > 1800000 and nifty_price < 23450

    # === ✅ Telegram Alert Logic (Only on NEW signal)
    if buy_signal and last_signal != "BUY":
        send_telegram("🔥 Buy Confirmed by Option Booster!")
        last_signal = "BUY"

    elif sell_signal and last_signal != "SELL":
        send_telegram("🔻 Sell Confirmed by Option Booster!")
        last_signal = "SELL"

    elif not buy_signal and not sell_signal:
        last_signal = None

# === 📬 SEND TELEGRAM ALERT ===
def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    try:
        response = requests.post(url, data=data)
        print("✅ Alert Sent:", msg)
    except Exception as e:
        print("❌ Telegram Send Error:", e)

# === 🔁 LOOP: Check every 1 minute ===
print("🔄 Booster Running... (Ctrl+C to stop)")
while True:
    check_signal()
    time.sleep(60)

