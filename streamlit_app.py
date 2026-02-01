import streamlit as st
import telebot
import google.generativeai as genai
import time

# --- CONFIGURATION DES CLÉS ---
# Remplace bien ces valeurs si tu les as changées
TOKEN = "8543306413:AAGnwDxqVDIvs4YI7QQO_QHm0sAmnGMAD14"
AI_KEY = "AIzaSyCRbP7DOZuekCo7n0SA5sOYAA6ahfdboOU"

# --- INITIALISATION ---
genai.configure(api_key=AI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(TOKEN)

# Interface Streamlit
st.set_page_config(page_title="Bot Telegram IA", page_icon="🤖")
st.title("🤖 Status du Bot Life OS")
st.write("Le bot utilise Google Gemini 1.5 Flash.")

# --- LOGIQUE DU BOT ---
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    try:
        # 1. On affiche dans les logs Streamlit que le message est reçu
        print(f"Message reçu de {message.from_user.first_name}: {message.text}")
        
        # 2. Appel à l'IA Gemini
        response = model.generate_content(message.text)
        
        # 3. Envoi de la réponse sur Telegram
        bot.reply_to(message, response.text)
        
    except Exception as e:
        error_msg = f"Erreur rencontrée : {str(e)}"
        print(error_msg)
        bot.reply_to(message, "Désolé, j'ai eu un petit bug. Réessaie !")

# --- BOUTON DE LANCEMENT ---
if st.button('🚀 DEMARRER LE BOT'):
    st.success("Le bot est maintenant en ligne ! Tu peux lui parler sur Telegram.")
    st.info("Note : Si tu fermes cet onglet, le bot risque de s'arrêter après un moment.")
    
    # Le paramètre non_stop=True permet au bot de ne pas crash si Telegram a une micro-coupure
    bot.infinity_polling(non_stop=True, timeout=90)
