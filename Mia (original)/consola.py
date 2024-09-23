import os
import socket
import requests
import pyautogui
import subprocess
import time
import threading
import datetime
import pywhatkit
import ollama  
import webbrowser
#from aplications import calc


google_api_key = "AIzaSyCVy0Hj0CYfdstorH4ezJDLM7cGHTh0lMY"
search_engine_id = "42adcd7adcbd3479f"
default_system_prompt = "You are a helpful, friendly and smart assistant. Your task is to simply talk to the user and help him solve his tasks. You should always respond in the same language as the user's message. and you were programmed by geremy, "

def pensar(prompt, system_prompt=default_system_prompt, lang="Spanish"):
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
    texto_guardar = ""

    def escuchar_comando():
        comando = input("Escribe tu comando: ").strip().lower()
        print(f"Comando detectado: {comando}")
        return comando

    def establecer_recordatorio(tiempo, mensaje):
        while True:
            ahora = datetime.datetime.now()
            if ahora.hour == tiempo.hour and ahora.minute == tiempo.minute:
                print("Recordatorio:", mensaje)
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
        print(texto)

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
            print(f"Texto guardado en {nombre_archivo}")
         except Exception as e:
            print(f"Error al intentar guardar en {nombre_archivo}: {e}")

    def tomar_screenshot():
        screenshot = pyautogui.screenshot()
        ruta_destino = os.path.join("C:/Users/Physco/Documents/Proyectos/MIA 2.0/Screeshots", "screenshot.png")
        screenshot.save(ruta_destino)
        print("Captura de pantalla tomada y guardada")

    def bloquear_pantalla():
        os.system("rundll32.exe user32.dll,LockWorkStation")
        print("Pantalla bloqueada")

    def abrir_rastreo_en_nueva_terminal():
        script_path = os.path.join("C:/Users/Physco/Documents/Proyectos/MIA 2.0", "rastreo.py")
        subprocess.Popen(['start', 'python', script_path], shell=True)
        print("Activando los ojos, ya lo puedo ver estimado geremy")

    def leer_archivo():
        try:
            with open("dia_de_hoy.txt", "r") as file:
                contenido = file.read()
            print("Esto es lo que tengo anotado para hoy: " + contenido)
        except FileNotFoundError:
            print("El archivo dia_de_hoy.txt no existe.")

    def anotar_en_archivo(texto):
        with open("dia_de_hoy.txt", "a") as file:
            file.write(texto + "\n")
        print("He anotado: " + texto)

    def iniciar_modo_estudio():
        webbrowser.open('https://web.whatsapp.com/')
        time.sleep(1)

        webbrowser.open('https://music.youtube.com/')
        time.sleep(1)

        webbrowser.open('https://chat.openai.com/')
        time.sleep(2)

        pyautogui.press('volumeup', presses=10)  
        time.sleep(1)
        pyautogui.press('volumedown', presses=4)

    def buenos_dias():
    # Obtener la fecha actual
        fecha_actual = datetime.datetime.now().strftime('%A, %d de %B del %Y')
        print(f"Buenos días. Hoy es {fecha_actual}")
    
    # Leer el archivo dia.txt
        try:
            with open("dia.txt", "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
            print(f"Esto es lo que tienes anotado para hoy: {contenido}")
        except FileNotFoundError:
            print("No encontré el archivo dia.txt. Asegúrate de crearlo o guardarlo con anotaciones para el día de hoy.")

    def modo_juego():
        print("Modo Juego activado.")
    
        os.system("start spotify")
        print("Abriendo Spotify...")

        pyautogui.press("volumedown", presses=30)  
        pyautogui.press("volumeup", presses=18)    
        print("Volumen ajustado al 60%")

        plataforma = input("¿Qué quieres jugar? (Steam/Epic Games): ").strip().lower()

        if plataforma == "steam":
            os.system("start Steam.exe")
            print("Abriendo Steam...")
        elif plataforma == "epic games":
            os.system("start epicgameslauncher")
            print("Abriendo Epic Games...")
        else:
            print("No reconocí la opción. Intenta con Steam o Epic Games.")

    while True:
        comando = escuchar_comando()

        if comando == "":
            print("No entendí el comando. ¿Puedes repetirlo?")
        elif 'apagar' in comando:
            print("Hasta pronto, apagado.....")
            break
        elif 'reproduce' in comando:
            cancion = comando.replace('reproduce', '').strip()
            print("Reproduciendo " + cancion)
            reproducir_cancion(cancion)
        elif 'hora' in comando:
            hora_actual = datetime.datetime.now().strftime('%H:%M:%S')
            print("La hora actual es: " + hora_actual)
        elif 'gracias' in comando:
            print("Un gusto, ¿necesita algo más?")
        elif 'apaga' in comando:
            print("Entendido")
        elif 'abre' in comando:
            aplicacion = comando.replace('abre', '').strip()
            os.system(f"start {aplicacion}")
            print(f"Abriendo {aplicacion}")
        elif 'recordatorio' in comando:
            hora_recordatorio = int(input("Ingrese la hora del recordatorio (0-23): "))
            minuto_recordatorio = int(input("Ingrese el minuto del recordatorio (0-59): "))
            mensaje_recordatorio = input("Ingrese el mensaje del recordatorio: ")
            tiempo_recordatorio = datetime.datetime.now().replace(hour=hora_recordatorio, minute=minuto_recordatorio, second=0, microsecond=0)
            thread_recordatorio = threading.Thread(target=establecer_recordatorio, args=(tiempo_recordatorio, mensaje_recordatorio))
            thread_recordatorio.start()
            print("Recordatorio establecido para las " + str(hora_recordatorio) + ":" + str(minuto_recordatorio))
        elif 'mi ip' in comando:
            ip = obtener_ip()
            print(f"Tu dirección IP es: {ip}")
        elif 'pregunta' in comando:
            pregunta = comando.replace('pregunta', '').strip()
            print(f"Buscando en internet sobre: {pregunta}")
            respuesta = buscar_en_internet(pregunta)
            print(respuesta)
        elif 'captura la pantalla' in comando:
            tomar_screenshot()
        elif 'bloquear pantalla' in comando:
            bloquear_pantalla()
        elif 'ojos' in comando:
            abrir_rastreo_en_nueva_terminal()
        elif 'qué hay para hoy' in comando:
            leer_archivo()
        elif 'anota' in comando:
            nueva_nota = input("¿Qué quieres que anote? ").strip()
            if nueva_nota:
                anotar_en_archivo(nueva_nota)
        elif 'guardar' in comando and texto_guardar:
            nombre_archivo = input("¿Dónde lo quieres guardar? (nombre de archivo): ").strip()
            guardar_en_archivo(nombre_archivo, texto_guardar)
            texto_guardar = ""
        elif 'envía mensaje' in comando:
            contacto = input("¿A quién quieres enviarle un mensaje? ").strip()
            mensaje = input("¿Qué mensaje quieres enviarle? ").strip()
            enviar_mensaje_whatsapp(contacto, mensaje)
        elif 'modo estudio' in comando:
            iniciar_modo_estudio()
        elif 'modo juego' in comando:
            modo_juego()
            print("Modo estudio activado. Aplicaciones abiertas y volumen al 60%")
        elif 'calculadora' in comando:
            #calc()
            print("He abierto la calculadora")
        elif 'buenos días' in comando:
            buenos_dias()
        elif 'responde' in comando:
            pregunta = comando.replace('responde', '').strip()
            respuesta = pensar(pregunta)
            print(f"\nRespuesta de Ollama: {respuesta}")
            if 'guarda' in comando:
                nombre_archivo = input("¿Dónde lo quieres guardar? (nombre de archivo): ").strip()
                guardar_en_archivo(nombre_archivo, respuesta)
        else:
            print("Pensando...")
            respuesta_llama = pensar(comando)
            hablar(respuesta_llama)
            texto_guardar = respuesta_llama  

iniciar_asistente()


