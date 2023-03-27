import csv
import requests
import os
from gtts import gTTS

# Specificare i percorsi dei file di input e output
input_file = "input.csv"
output_file = "output.csv"
audio_folder = "audio"

# Creare la cartella audio se non esiste già
if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)

# Aprire il file di input e leggerne le righe
with open(input_file, "r", encoding="iso-8859-2") as file:
    reader = csv.reader(file)
    rows = [row for row in reader]

# Creare una lista di dizionari contenenti il front e il back delle carte
cards = []

for row in rows:
    # Estrai la parola dal front della carta
    word = row[0]

    # Crea il percorso del file audio
    audio_file = os.path.join(audio_folder, f"{word}.mp3")

    # Scarica il file audio se non esiste già
    if not os.path.exists(audio_file):
        tts = gTTS(text=word, lang='ro')
        tts.save(audio_file)

    # Aggiungi la carta alla lista di carte
    cards.append({"Front": row[0], "Back": row[1], "Audio": audio_file})

# Aprire il file di output e scrivere le carte nel formato richiesto da Anki
with open(output_file, "w", newline="", encoding="iso-8859-2") as file:
    writer = csv.DictWriter(file, fieldnames=["Front", "Back", "Audio"])
    writer.writeheader()
    for card in cards:
        writer.writerow(card)