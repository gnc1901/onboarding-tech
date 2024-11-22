from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os

# Inicializar el cliente de Slack con el token del bot
client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))

def send_welcome_message(user_id):
    try:
        response = client.chat_postMessage(
            channel=user_id,
            text="¡Bienvenido/a a nuestro workspace de Slack! 🎉 Si necesitas ayuda, visita el canal #soporte."
        )
        print(f"Mensaje enviado a {user_id}: {response['message']['text']}")
    except SlackApiError as e:
        print(f"Error al enviar mensaje: {e.response['error']}")

def main():
    # Aquí podrías agregar lógica para obtener nuevos usuarios
    # Este es un ejemplo de ID de usuario (puedes reemplazarlo con lógica para obtener usuarios dinámicamente)
    new_user_id = "U12345678"  # Reemplaza con un ID de usuario real
    send_welcome_message(new_user_id)

if __name__ == "__main__":
    main()
