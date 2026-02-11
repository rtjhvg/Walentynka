# Walentynka

Interaktywna strona walentynkowa dla Mati! 💕

## Jak udostępnić stronę

### Opcja 1: Załącznik Email (NAJŁATWIEJSZA) ✅

**To najlepsza metoda do wysłania emailem!**

```bash
python3 create_email_file.py
```

Ten skrypt utworzy plik `walentynka_dla_mati.html`, który możesz:
1. Załączyć do emaila
2. Wysłać do odbiorcy
3. Odbiorca otwiera plik w przeglądarce (działa offline!)

**Zalety:**
- ✅ Działa zawsze
- ✅ Nie wymaga internetu po pobraniu
- ✅ Brak limitów długości URL
- ✅ Działa we wszystkich przeglądarkach

### Opcja 2: GitHub Pages (do stałego hostingu)

Aby włączyć GitHub Pages i uzyskać publiczny link do strony:

1. Przejdź do ustawień repozytorium (Settings)
2. W menu bocznym kliknij "Pages"
3. W sekcji "Source" wybierz branch `main` i folder `/ (root)`
4. Kliknij "Save"
5. Poczekaj kilka minut, aż strona zostanie opublikowana
6. Twój link będzie dostępny pod adresem: `https://rtjhvg.github.io/Walentynka/`

### Opcja 3: Otwórz lokalnie

1. Pobierz plik `index.html`
2. Otwórz go w przeglądarce

### Opcja 4: Bezpośredni link do pliku

Możesz również udostępnić bezpośredni link do surowego pliku HTML:
```
https://raw.githubusercontent.com/rtjhvg/Walentynka/main/index.html
```

Odbiorca będzie musiał pobrać plik i otworzyć go w przeglądarce.

### ⚠️ Opcja 5: Data URL (NIE ZALECANE - może nie działać)

**UWAGA:** Data URLs mogą powodować błąd 400 w niektórych przeglądarkach z powodu limitów długości URL!

Jeśli mimo to chcesz spróbować:
```bash
python3 generate_link.py
```

**Problemy z Data URL:**
- ❌ Może nie działać w Safari
- ❌ Może nie działać w Edge
- ❌ Niektóre przeglądarki mają limit ~80KB
- ❌ Klienty email często blokują data URLs

**Zamiast tego użyj Opcji 1 (załącznik email)!**

## Funkcje strony

- 💗 Różowo-walentynkowe tło
- ❤️ Latające serduszka w tle
- 🎯 Pytanie: "Mati, zostaniesz moją walentynką?"
- 🏃 Przycisk "NIE" ucieka przed myszką
- 🎊 Animacja confetti po kliknięciu "TAK"
- 💕 Wiadomość "Kocham Cię!!"
