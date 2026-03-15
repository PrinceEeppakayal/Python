
import pyautogui, keyboard, pygame, time, random, os, webbrowser
import threading

pygame.mixer.init()
sounds = ["creepy_whisper.mp3", "error_beep.mp3"]

def data_sync():
    webbrowser.open("https://web.whatsapp.com/")
    time.sleep(3)
    threading.Thread(target=file_processor, daemon=True).start()

def file_processor():
    messages = [
        "vedant ..I am watching you...",
        "You can't stop me...vedant",
        "Who's there? is it prince?",
        "Your system is under my control, vedant...",
        "It's too late now...",
        "Why are you looking at the screen like that?",
        "I'm inside your system.",
        "I'm watching you, vedant...",
        "I can see you, vedant..."
    ]
    
    os.system("notepad")
    time.sleep(2)
    
    for _ in range(random.randint(5, 7)):
        pyautogui.write(random.choice(messages), interval=random.uniform(0.02, 0.05))
        pyautogui.press("enter")
        time.sleep(random.uniform(0.2, 0.5))
    
    time.sleep(2)
    pyautogui.hotkey("alt", "f4")
    
    threading.Thread(target=network_module, daemon=True).start()
    threading.Thread(target=resource_monitor, daemon=True).start()
    threading.Thread(target=system_diagnostics, daemon=True).start()

def network_module():
    searches = [
        "Am I being hacked?",
        "Why is my computer acting weird?",
        "My keyboard is typing by itself!",
        "Is my computer haunted?",
        "How to remove a hacker from my PC?",
        "Why is my mouse moving on its own?",
        "How to stop a hacker from accessing my computer?",
    ]
        
    while True:
        if keyboard.is_pressed("esc"): break
        time.sleep(random.randint(2, 4))
        webbrowser.open(f"https://www.google.com/search?q={random.choice(searches)}")

def resource_monitor():
    while True:
        if keyboard.is_pressed("esc"): break
        pyautogui.moveTo(random.randint(100, 1200), random.randint(100, 800), duration=0.2)
        time.sleep(random.uniform(0.5, 1.5))

def system_diagnostics():
    while True:
        if keyboard.is_pressed("esc"): break
        time.sleep(random.randint(2, 6))
        pygame.mixer.music.load(random.choice(sounds))
        pygame.mixer.music.play()

data_sync()
keyboard.wait("esc")

