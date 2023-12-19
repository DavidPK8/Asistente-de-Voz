import speech_recognition as sr
import subprocess
import pyautogui
import webbrowser
import psutil

recognizer = sr.Recognizer()
proceso = None
saludo = """
Hola Martin
Hola Daga
Hola Paul"""

comandos = {
    "abre notepad": lambda: subprocess.Popen(["notepad.exe"]),
    "abre google": lambda: webbrowser.open("https://www.google.com"),
    "abre facebook": lambda: webbrowser.open("https://www.facebook.com"),
    "abre youtube": lambda: webbrowser.open("https://www.youtube.com"),
    "saludar amiguitos": lambda: pyautogui.write(saludo),
    "abrir casa": lambda: subprocess.Popen([r"D:\OperaGX\opera.exe"]),
    "abre lol": lambda: subprocess.Popen([r"D:\LEAGUE OF LEGENDS\Riot Games\Riot Client\RiotClientServices.exe"]),
    "abre word": lambda: subprocess.Popen([r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"]),
    "cerrar notepad": lambda: cerrar_proceso("notepad.exe"),
    "cerrar word": lambda: cerrar_proceso("WINWORD.EXE"),
    "imagen": lambda: subprocess.run(['start', 'explorer', r"C:\Users\jorge\Desktop\Jeremex.jpg"], shell=True)
}

def ejecutarComando(comando):
    global proceso
    accion = comandos.get(comando)
    if accion:
        accion()
    else: 
        print("Comando no reconocido")

def cerrar_proceso(nombre_proceso):
    for proc in psutil.process_iter(['pid', 'name']):
        if nombre_proceso.lower() in proc.info['name'].lower():
            try:
                proceso = psutil.Process(proc.info['pid'])
                proceso.terminate()
                print(f"Proceso {nombre_proceso} cerrado exitosamente.")
            except Exception as e:
                return print(f"No se pudo cerrar el proceso {nombre_proceso}: {e}")

def escucharComandos():
    with sr.Microphone() as source:
        print("En que te puedo ayudar...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        comando = recognizer.recognize_google(audio, language="es-ES")
        print(f"Comando reconocido: {comando}")
        ejecutarComando(comando.lower())
    except sr.UnknownValueError:
        print("No se pudo entender el comando")
    except sr.RequestError as e:
        print(f"Error al realizar la solicitud: {e}")

while True:
    escucharComandos()