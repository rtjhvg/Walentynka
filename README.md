# Walentynka

Interaktywna strona walentynkowa dla Mati! 💕

## Jak otworzyć stronę

### Opcja 1: GitHub Pages (zalecane)

Aby włączyć GitHub Pages i uzyskać publiczny link do strony:

1. Przejdź do ustawień repozytorium (Settings)
2. W menu bocznym kliknij "Pages"
3. W sekcji "Source" wybierz branch `copilot/add-simple-html-page` i folder `/ (root)`
4. Kliknij "Save"
5. Poczekaj kilka minut, aż strona zostanie opublikowana
6. Twój link będzie dostępny pod adresem: `https://rtjhvg.github.io/Walentynka/`

### Opcja 2: Otwórz lokalnie

1. Pobierz plik `index.html`
2. Otwórz go w przeglądarce

### Opcja 3: Bezpośredni link do pliku

Możesz również udostępnić bezpośredni link do surowego pliku HTML:
```
https://raw.githubusercontent.com/rtjhvg/Walentynka/copilot/add-simple-html-page/index.html
```

Odbiorca będzie musiał pobrać plik i otworzyć go w przeglądarce.

### Opcja 4: Data URL (do wklejenia w email)

Uruchom skrypt `generate_link.py` aby wygenerować gotowy do skopiowania data URL:
```bash
python3 generate_link.py
```

Ten skrypt utworzy plik `shareable_link.txt` zawierający link, który można skopiować i wkleić bezpośrednio w email lub przeglądarkę.

## Funkcje strony

- 💗 Różowo-walentynkowe tło
- ❤️ Latające serduszka w tle
- 🎯 Pytanie: "Mati, zostaniesz moją walentynką?"
- 🏃 Przycisk "NIE" ucieka przed myszką
- 🎊 Animacja confetti po kliknięciu "TAK"
- 💕 Wiadomość "Kocham Cię!!"
