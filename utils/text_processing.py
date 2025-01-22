import re 
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter


def limpiar_subtitulos(texto):
    texto_limpio = re.sub(r'\d+\s+\d{2}:\d{2}:\d{2},\d{3}\s+-->\s+\d{2}:\d{2}:\d{2},\d{3}\s*', '', texto)
    texto_limpio = re.sub(r'\.\.\.\s*\n\s*\.\.\.', ' ', texto_limpio)
    texto_limpio = re.sub(r'^\d+\s*$', '', texto_limpio, flags=re.MULTILINE)
    texto_limpio = re.sub(r'\s+', ' ', texto_limpio).strip()
    return texto_limpio

def analyze_dialogues(text, target_words):
    sentences = sent_tokenize(text)
    word_count = Counter()
    sentences_with_words = []
    
    for sentence in sentences:
        words = [word.lower() for word in word_tokenize(sentence) if word.isalpha()]
        matches = [word for word in words if word in target_words]
        if matches:
            word_count.update(matches)
            sentences_with_words.append((limpiar_subtitulos(sentence), matches))
    
    return word_count, sentences_with_words


def normalizar_nombre(pelicula):
    return pelicula.replace(" ", "_").replace(":", "").replace("'", "")

