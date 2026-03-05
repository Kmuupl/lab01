import datetime
import sys

def info():
    name = "Anna"
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    version = sys.version

    print(f"Cześć! Mam na imię {name}.")
    print(f"Aktualna data i godzina: {date}")
    print(f"Wersja Pythona: {version}")

if __name__ == "__main__":
    info()