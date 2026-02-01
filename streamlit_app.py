import streamlit as st
import telebot
import google.generativeai as genai

# --- CONFIG ---
TOKEN = "8543306413:AAGnwDxqVDIvs4YI7QQO_QHm0sAmnGMAD14"
AI_KEY = "AIzaSyCRbP7DOZuekCo7n0SA5sOYAA6ahfdboOU"

genai.configure(api_key=AI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(TOKEN)

st.title("🤖 Status du Bot Telegram")

@bot.message_handler(func=lambda m: True)
def chat(m):
    try:
        res = model.generate_content(m.text)
        bot.reply_to(m, res.text)
    except Exception as e:
        st.error(f"Erreur : {e}")

# --- BOUTON DE LANCEMENT ---
if st.button('Lancer le Bot'):
    st.write("✅ Le bot tourne... Teste-le sur Telegram !")
    # Cette ligne est la correction de ton erreur
    bot.infinity_polling(timeout=60, long_polling_timeout=5)
