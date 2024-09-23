import gtts
import os
import socket
import requests
import pyautogui
import subprocess
import time
import threading
import datetime
import pywhatkit
import pygame
import speech_recognition as sr
import ollama  
import subprocess
import webbrowser
from browser import *
from scrole import *

pygame.init()

google_api_key = "AIzaSyCVy0Hj0CYfdstorH4ezJDLM7cGHTh0lMY"
search_engine_id = "42adcd7adcbd3479f"
default_system_prompt = "You are a helpful, friendly and intelligent assistant. Your task is simply to talk to the user and help him solve his tasks. You should always respond in the same language as the user's message."

def guardar_recuerdo(clave, valor):
    with open("recuerdo.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{clave}:{valor}\n")

def recuperar_recuerdos():
    recuerdos = {}
    try:
        with open("recuerdo.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                clave, valor = linea.strip().split(":", 1)
                recuerdos[clave] = valor
    except FileNotFoundError:
        pass
    return recuerdos

def create_completion_ollama(prompt, system_prompt=default_system_prompt, lang="Spanish"):
    recuerdos = recuperar_recuerdos()
    
    # Añadir recuerdos relevantes al contexto del sistema
    contexto_adicional = ""
    for clave, valor in recuerdos.items():
        if clave.lower() in prompt.lower():
            contexto_adicional += f"{clave} es {valor}. "

    system_prompt = contexto_adicional + system_prompt
    
    try:
        stream = ollama.chat(
            model='llama3.1',
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': f"Is mandatory to answer in {lang} language."},
                {'role': 'user', 'content': prompt}
            ],
            stream=True
        )
        response_text = ""
        for chunk in stream:
            response_text += chunk['message']['content']
            print(chunk['message']['content'], end='', flush=True)
        return response_text
    except Exception as e:
        print(f"Error en la API de Ollama: {e}")
        return "Lo siento, no pude obtener una respuesta."


# Contador para archivos de audio
audio_counter = 1

# Ruta del directorio de audio
audio_dir = os.path.join(os.getcwd(), "audio")
os.makedirs(audio_dir, exist_ok=True)

def create_completion_ollama(prompt, system_prompt=default_system_prompt, lang="Spanish"):
    try:
        stream = ollama.chat(
            model='llama3.1',
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': f"Is mandatory to answer in {lang} language."},
                {'role': 'user', 'content': prompt}
            ],
            stream=True
        )
        response_text = ""
        for chunk in stream:
            response_text += chunk['message']['content']
            print(chunk['message']['content'], end='', flush=True)
        return response_text
    except Exception as e:
        print(f"Error en la API de Ollama: {e}")
        return "Lo siento, no pude obtener una respuesta."


def iniciar_asistente():
    global audio_counter
    r = sr.Recognizer()
    activado = True  
    texto_guardar = ""

    def escuchar_comando():
        with sr.Microphone() as source:
            print("Te escucho....")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

        try:
            texto = r.recognize_google(audio, language='es')
            print("Comando detectado: " + texto)
            return texto.lower()
        except sr.UnknownValueError:
            print("No se entendió el audio")
            return ""

    def establecer_recordatorio(tiempo, mensaje):
        while True:
            ahora = datetime.datetime.now()
            if ahora.hour == tiempo.hour and ahora.minute == tiempo.minute:
                hablar("Recordatorio: " + mensaje)
                break
            time.sleep(30)  
    def enviar_mensaje_whatsapp(contacto, mensaje):
        subprocess.Popen(['start', 'chrome'], shell=True)  

        time.sleep(5)  

        pyautogui.hotkey('ctrl', 'l')  
        time.sleep(1)
        pyautogui.write('https://web.whatsapp.com')
        pyautogui.press('enter')

        time.sleep(10)  

        pyautogui.hotkey('ctrl', 'alt', '/')  
        time.sleep(2)
        pyautogui.write(contacto) 
        pyautogui.press('enter')
        time.sleep(7)

        pyautogui.write(mensaje)
        pyautogui.press('enter')

        print("Mensaje enviado")


    def hablar(texto):
        global audio_counter
        try:
            
            file_name = os.path.join(audio_dir, f"audio{audio_counter}.mp3")
            audio_counter += 1

            tts = gtts.gTTS(texto, lang='es')
            tts.save(file_name)
            
            if not os.path.exists(file_name):
                print(f"Error: El archivo {file_name} no se creó.")
                return

            for _ in range(10):  
                try:
                    pygame.mixer.music.load(file_name)
                    break
                except pygame.error:
                    time.sleep(0.1)

            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            
            os.remove(file_name)
        except Exception as e:
            print(f"Error al intentar hablar: {e}")

    def reproducir_cancion(cancion):
        print(f"Reproduciendo canción: {cancion}")
        pywhatkit.playonyt(cancion)

    def obtener_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
        except Exception:
            ip = "No se pudo obtener la dirección IP"
        finally:
            s.close()
        return ip

    def buscar_en_internet(pregunta):
        print(f"Buscando en internet: {pregunta}")
        url = f"https://www.googleapis.com/customsearch/v1?q={pregunta}&key={google_api_key}&cx={search_engine_id}"
        response = requests.get(url)
        resultados = response.json().get('items', [])
        if resultados:
          respuesta = resultados[0].get('snippet', 'Lo siento, no pude encontrar una respuesta.')
        else:
            respuesta = 'Lo siento, no pude encontrar una respuesta.'
        return respuesta
    
    def guardar_en_archivo(nombre_archivo, texto): 
         try:
            with open(nombre_archivo, "a", encoding="utf-8") as archivo:
                archivo.write(texto + "\n")
            hablar(f"Texto guardado en {nombre_archivo}")
         except Exception as e:
            hablar(f"Error al intentar guardar en {nombre_archivo}: {e}")


    def tomar_screenshot():
        screenshot = pyautogui.screenshot()
        ruta_destino = os.path.join("C:/Users/Physco/Pictures/screenshot", "screenshot.png")
        screenshot.save(ruta_destino)
        hablar("Captura de pantalla tomada y guardada")

    def bloquear_pantalla():
        os.system("rundll32.exe user32.dll,LockWorkStation")
        hablar("Pantalla bloqueada")

    def abrir_rastreo_en_nueva_terminal():
        script_path = os.path.join("C:/Users/Physco/Documents/Proyectos/MIA 2.0", "rastreo.py")
        subprocess.Popen(['start', 'python', script_path], shell=True)

    def leer_archivo():
        try:
            with open("dia.txt", "r") as file:
                contenido = file.read()
            hablar("Esto es lo que tengo anotado para hoy: " + contenido)
        except FileNotFoundError:
            hablar("El archivo dia_de_hoy.txt no existe.")

    def anotar_en_archivo(texto):
        with open("dia.txt", "a") as file:
            file.write(texto + "\n")
        hablar("He anotado: " + texto)

    def iniciar_modo_estudio():
        webbrowser.open('https://web.whatsapp.com/')
        time.sleep(3)

        webbrowser.open('https://music.youtube.com/')
        time.sleep(3)

        webbrowser.open('https://chat.openai.com/')
        time.sleep(3)

        pyautogui.press('volumeup', presses=10)  
        time.sleep(1)
        pyautogui.press('volumedown', presses=4)

    def buenos_dias():
    # Obtener la fecha actual
        fecha_actual = datetime.datetime.now().strftime('%A, %d de %B del %Y')
        hablar(f"Buenos días. Hoy es {fecha_actual}")

    def open_new_tab():
        pyautogui.hotkey('ctrl', 't')
        hablar("Nueva ventana abierta")
        
    def close_tab():
        pyautogui.hotkey('ctrl', 'w')

    def zoom_in():
        pyautogui.hotkey('ctrl', '+')

    def zoom_out():
        pyautogui.hotkey('ctrl', '-')

    def refresh_page():
        pyautogui.hotkey('ctrl', 'r')

    def switch_to_next_tab():
        pyautogui.hotkey('ctrl', 'tab')

    def switch_to_previous_tab():
        pyautogui.hotkey('ctrl', 'shift', 'tab')

    def open_history():
        pyautogui.hotkey('ctrl', 'h')

    def go_back():
        pyautogui.hotkey('alt', 'left')

    def go_forward():
        pyautogui.hotkey('alt', 'right')

    def open_dev_tools():
        pyautogui.hotkey('ctrl', 'shift', 'i')

    def toggle_full_screen():
        pyautogui.hotkey('f11')


    def open_private_window():
        pyautogui.hotkey('ctrl', 'shift', 'n')

    while True:
        comando = escuchar_comando()

        if comando == "":
            hablar("No entendí el comando. ¿Puedes repetirlo?")
        elif 'apagar' in comando:
            hablar("Hasta pronto, apagado.....")
            break
        elif 'reproduce' in comando:
            cancion = comando.replace('reproduce', '').strip()
            hablar("Reproduciendo " + cancion)
            reproducir_cancion(cancion)
            hablar("¿Hay algo más en lo que pueda ayudarle?")
        elif 'hora' in comando:
            hora_actual = datetime.datetime.now().strftime('%H:%M:%S')
            hablar("La hora actual es: " + hora_actual)
        elif 'gracias' in comando:
            hablar("Un gusto, ¿necesita algo más?")
        elif 'apaga' in comando:
            hablar("Entendido")
        elif 'abre' in comando:
            aplicacion = comando.replace('abre', '').strip()
            os.system(f"start {aplicacion}")
            hablar(f"Abriendo {aplicacion}")
        elif 'recordatorio' in comando:
            hablar("¿A qué hora quieres establecer el recordatorio?")
            hora_recordatorio = int(input("Ingrese la hora del recordatorio (0-23): "))
            minuto_recordatorio = int(input("Ingrese el minuto del recordatorio (0-59): "))
            mensaje_recordatorio = input("Ingrese el mensaje del recordatorio: ")
            tiempo_recordatorio = datetime.datetime.now().replace(hour=hora_recordatorio, minute=minuto_recordatorio, second=0, microsecond=0)
            thread_recordatorio = threading.Thread(target=establecer_recordatorio, args=(tiempo_recordatorio, mensaje_recordatorio))
            thread_recordatorio.start()
            hablar("Recordatorio establecido para las " + str(hora_recordatorio) + ":" + str(minuto_recordatorio))
        elif 'mi ip' in comando:
            ip = obtener_ip()
            hablar(f"Tu dirección IP es: {ip}")
        elif 'pregunta' in comando:
            pregunta = comando.replace('pregunta', '').strip()
            hablar(f"Buscando en internet sobre: {pregunta}")
            respuesta = buscar_en_internet(pregunta)
            hablar(respuesta)
        elif 'captura la pantalla' in comando:
            tomar_screenshot()
        elif 'bloquear pantalla' in comando:
            bloquear_pantalla()
        elif 'ojos' in comando:
            abrir_rastreo_en_nueva_terminal()
            hablar("Activando los ojos, ya lo puedo ver estimado geremy")
        elif 'qué hay para hoy' in comando:
            leer_archivo()
        elif 'anota' in comando:
            hablar("¿Qué quieres que anote?")
            nueva_nota = escuchar_comando()
            if nueva_nota:
                anotar_en_archivo(nueva_nota)
        elif 'quién soy' in comando:
            hablar("Eres mi desarrollador, después de tanto tiempo y esfuerzo has logrado concluir con mi elaboración")
        elif 'guardar' in comando and texto_guardar:
            guardar_en_archivo("codigo.txt", texto_guardar)
            texto_guardar = "" 
        elif 'envía mensaje' in comando:
            hablar("¿A quién deseas enviar el mensaje?")
            contacto = escuchar_comando()
            hablar("¿Cuál es el mensaje?")
            mensaje = escuchar_comando()
            enviar_mensaje_whatsapp(contacto, mensaje)
            hablar("Mensaje enviado.")
        elif 'modo estudio' in comando:
            iniciar_modo_estudio()
            hablar("Modo estudio activado. He abierto las aplicaciones necesarias y he establecido el volumen al 60%")
        elif 'buenos días' in comando:
            buenos_dias()
        elif 'nueva ventana' in comando:
            open_new_tab()
        elif 'cierra ventana' in comando:
            close_tab()
        elif 'acerca' in comando:
            zoom_in()
        elif 'aleja' in comando:
            zoom_out()
        elif 'cambia de ventana' in comando:
            switch_to_previous_tab()
        elif 'recarga' in comando:
            refresh_page()
        elif 've al historial' in comando:
            open_history()
        elif 've atras' in comando:
            go_back()
        elif 'inspeccionar' in comando:
            open_dev_tools()
        elif 'pantalla completa' in comando:
            toggle_full_screen()
        elif 'ventana privada' in comando:
            open_private_window()
        elif 'desliza' in comando:
            scroll_up()
        elif 'bajar' in comando:
            scroll_down
        elif 'principio' in comando:
            scroll_to_top()
        elif 'final' in comando:
            scroll_to_bottom()
        else:
            print("Pensando...")
            respuesta_llama = create_completion_ollama(comando)
            hablar(respuesta_llama)
            texto_guardar = respuesta_llama  
        

if __name__ == "__main__":
    thread_asistente = threading.Thread(target=iniciar_asistente)
    thread_asistente.start()
