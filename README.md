## Anki Deck Audio Creator

### Description

With deck.py you can **generate an Anki Deck with audio files** from a file in this format:

<table><tbody><tr><td>Target language words</td><td>Translated words</td></tr><tr><td>word1</td><td>parola1</td></tr><tr><td>word2</td><td>parola2</td></tr></tbody></table>

Check the input.csv file for example. 

_NOTE: File input.csv was generated with the help of_ [_https://cooljugator.com/ro/list_](https://cooljugator.com/ro/list)

### How it works

Just execute deck.py to get the output.csv you can import in Anki.

`python deck.py`

All audio files will be created in /audio subdirectory. 

On Windows 10, I had to move all of them to C:\\Users\\user\\AppData\\Roaming\\Anki2\\MyUser\\collection.media before importing the CSV into Anki.

### **Features**

*   Automatic generate audio with Google Translate.
*   Create an Anki compatible csv, ready to import.
