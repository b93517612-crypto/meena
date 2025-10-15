# telegram-render-bot

**Simple Telegram webhook bot (Flask)** — GitHub-ready and Render-deployable.

## फ़ाइलें (Files included)
- `app.py` — Flask app that receives Telegram webhook updates and replies in Hindi.
- `requirements.txt` — Python dependencies.
- `Procfile` — For Gunicorn (Render will use this).
- `.env.example` — Example environment variables.
- `.gitignore` — Common ignores.

---

## तेज़ सेटअप (Quick setup) — हिन्दी में

1. **Bot बनाओ**  
   Telegram पर `@BotFather` से `/newbot` करके `BOT_TOKEN` ले लो।

2. **Repo बनाओ**  
   - लोकल में इस प्रोजेक्ट को git init करके commit करो और GitHub पर push करो:
     ```bash
     git init
     git add .
     git commit -m "Initial commit"
     git branch -M main
     git remote add origin https://github.com/<youruser>/<repo>.git
     git push -u origin main
     ```

3. **Render पर Deploy**  
   - Render.com पर login → **New** → **Web Service** → Connect to GitHub → अपना repo चुनो.  
   - Build command: (usually automatic) or `pip install -r requirements.txt`  
   - Start command: `gunicorn app:app` (Procfile already present)
   - Environment variables (Render dashboard → Environment):
     - `BOT_TOKEN` = `<your telegram bot token>`
     - (Optional) `WEBHOOK_PATH` = `/webhook` (default)

4. **Webhook सेट करो**  
   - Render deploy के बाद तुम्हें एक public URL मिलेगा, जैसे `https://your-service.onrender.com`  
   - webhook URL को Telegram को बताओ (HTTPS ज़रूरी):
     ```bash
     curl -F "url=https://your-service.onrender.com/webhook" https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook
     ```
   - या ब्राउज़र में खोलो:
     ```
     https://your-service.onrender.com/set-webhook?url=https://your-service.onrender.com/webhook
     ```
     (यह route अंदर से Telegram को call करेगा — secure use पर ध्यान दें)

5. **टेस्ट करो**  
   - Telegram में अपने bot को खोलो और `/start` भेजो — bot reply करेगा।
   - Render dashboard → Logs देखें यदि कोई error आए।

---

## Quick setup — English

1. Create a bot with `@BotFather` and get `BOT_TOKEN`.
2. Push this project to GitHub.
3. On Render: New → Web Service → connect repo → set `BOT_TOKEN` environment variable → deploy.
4. After deployment, set webhook:
   ```bash
   curl -F "url=https://your-service.onrender.com/webhook" https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook
   ```
5. Test by sending `/start` to your bot.

---

## Notes & tips
- **Do not** commit your real `BOT_TOKEN` to the repository. Use environment variables.
- If the bot doesn't respond, check Render logs and ensure webhook was set to the correct HTTPS URL.
- This project uses simple `requests` calls to the Telegram HTTP API (no heavy Telegram SDK), so it's lightweight and easy to debug.

---

अगर चाहो तो मैं GitHub पर खुद एक public repo बनाकर files push करने में help कर सकता हूँ (लेकिन उससे पहले तुम्हारा GitHub username और repository name चाहिए)। या मैं तुम्हारे लिए सीधे Render deploy steps में भी detailed commands दे सकता हूँ।
