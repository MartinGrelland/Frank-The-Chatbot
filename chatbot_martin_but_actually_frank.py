import time
now = time.ctime()

# Kommentar: koden importerer modulen"time" og bruker funksjonen "ctime()" for å hente gjeldende tidspunkt og lagre det i variblen "now"


qna = {
    "hi":"hey",
    "how are you":"i am fine",
    "what is your name":"my name is Frank",
    "how old are you":"i am 1 years old",
    "what is the time now" : now,
}

# Kommentar: oppretter en ordbok som inneholder spørsmål og svar du kan stille et spørsmål og få svar fra ordboken basert på nøklene i ordboken



def typewriter_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)  # Adjust the delay as per your preference
    print()

# Kommentar: Skriver ut hver bokstav i en tekststreng en etter en med en liten forsinkelse mellom hver bokstav, og gir dermed en "skrivemaskin-effekt"



typewriter_effect("Bot: Hello! I am chatbot. I can answer questions. What would you like to ask me?")

# Kommentar: Skriver ut en tekststreng som om det var en skrivemaksin som skriver den ut bokstav for bokstav, med en liten forsinkelse mellom hver bokstav



while True:
    print('Input question here: ', end='')
    qs = str(input())

    if qs == "quit":
        typewriter_effect('Good bye')
        break
    elif qs in qna:
        typewriter_effect("Processing...")
        typewriter_effect("Bot: " + qna[qs])
    else:
        typewriter_effect("Bot: Sorry, I don't have an answer to that question.")

# Kommentar: Lar brukeren stille spørsmål tin en chatbot og få svar fra den