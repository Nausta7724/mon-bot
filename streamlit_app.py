import streamlit as st
import telebot
import google.generativeai as genai

# --- TES CLÉS ---
TOKEN = "8543306413:AAGnwDxqVDIvs4YI7QQO_QHm0sAmnGMAD14"
AI_KEY = "AIzaSyCRbP7DOZuekCo7n0SA5sOYAA6ahfdboOU"

# --- CONFIG IA ---
genai.configure(api_key=AI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(TOKEN)

st.title("🤖 Status du Bot Telegram")

@bot.message_handler(func=lambda m: True)
def chat(m):
    try:
        # Affiche le message reçu dans la console Streamlit (Logs)
        print(f"Message reçu : {m.text}")
        res = model.generate_content(m.text)
        bot.reply_to(m, res.text)
    except Exception as e:
        st.error(f"Erreur IA : {e}")

# --- LANCEMENT SIMPLIFIÉ (Correction de ton erreur) ---
if st.button('Lancer le Bot'):
    st.success("✅ Le bot est en ligne ! Parle-lui sur Telegram.")
    # On utilise la commande la plus stable pour Streamlit
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
