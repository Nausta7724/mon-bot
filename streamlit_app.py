import streamlit as st
import telebot
import google.generativeai as genai

# --- CONFIGURATION ---
TOKEN = "8543306413:AAGnwDxqVDIvs4YI7QQO_QHm0sAmnGMAD14"
AI_KEY = "AIzaSyCRbP7DOZuekCo7n0SA5sOYAA6ahfdboOU"

# Setup IA et Bot
genai.configure(api_key=AI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(TOKEN)

st.set_page_config(page_title="Life OS Bot", page_icon="🤖")
st.title("🤖 Status du Bot")

# Cette fonction gère les messages
@bot.message_handler(func=lambda m: True)
def chat(m):
    try:
        response = model.generate_content(m.text)
        bot.reply_to(m, response.text)
    except Exception as e:
        st.error(f"Erreur : {e}")

# --- LA VRAIE SOLUTION EST ICI ---
if st.button('🚀 LANCER LE BOT MAINTENANT'):
    st.success("Bot actif ! Parle-lui sur Telegram.")
    # On utilise polling() tout court, sans les arguments qui font planter ton écran
    bot.polling(none_stop=True)
