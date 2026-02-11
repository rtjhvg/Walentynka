# Walentynka

Interaktywna strona walentynkowa dla Mati! 💕

## 📥 Jak pobrać pliki z repozytorium?

> 💡 **Szczegółowy przewodnik:** Zobacz [POBIERANIE.md](POBIERANIE.md) dla pełnych instrukcji krok po kroku z FAQ!

### 🚀 Szybka pomoc: Uruchom skrypt pomocniczy

Jeśli już masz Python, możesz uruchomić:
```bash
python3 download_help.py
```

Ten skrypt wyświetli szczegółowe instrukcje i sprawdzi które pliki już masz!

### Metoda 1: Pobierz całe repozytorium jako ZIP (NAJŁATWIEJSZA) ✅

**Krok po kroku:**

1. **Przejdź na stronę repozytorium:**
   ```
   https://github.com/rtjhvg/Walentynka
   ```

2. **Kliknij zielony przycisk "Code"** (na górze strony)

3. **Wybierz "Download ZIP"**

4. **Rozpakuj pobrany plik** na swoim komputerze

5. **Gotowe!** Wszystkie pliki są teraz na Twoim komputerze

### Metoda 2: Pobierz pojedyncze pliki

**Jeśli potrzebujesz tylko jednego pliku (np. index.html):**

1. Kliknij na plik w repozytorium GitHub
2. Kliknij przycisk **"Raw"** (po prawej stronie, nad kodem)
3. Kliknij prawym przyciskiem myszy → **"Zapisz jako..."**
4. Wybierz lokalizację i zapisz

**Bezpośrednie linki do pobrania:**
- Strona HTML: [index.html](https://raw.githubusercontent.com/rtjhvg/Walentynka/copilot/add-simple-html-page/index.html) (prawy klik → Zapisz jako)
- Skrypt email: [create_email_file.py](https://raw.githubusercontent.com/rtjhvg/Walentynka/copilot/add-simple-html-page/create_email_file.py)
- Generator emaila: [prepare_email.py](https://raw.githubusercontent.com/rtjhvg/Walentynka/copilot/add-simple-html-page/prepare_email.py)

### Metoda 3: Używając Git (dla zaawansowanych)

Jeśli masz zainstalowanego Git:

```bash
git clone https://github.com/rtjhvg/Walentynka.git
cd Walentynka
git checkout copilot/add-simple-html-page
```

### ❓ Nie masz dostępu do komputera?

**Możesz otworzyć stronę bezpośrednio w przeglądarce:**
```
https://raw.githubusercontent.com/rtjhvg/Walentynka/copilot/add-simple-html-page/index.html
```
Prawy klik → "Zapisz jako..." aby pobrać.

---

## Jak udostępnić stronę

### Opcja 1: Załącznik Email (NAJŁATWIEJSZA) ✅

**To najlepsza metoda do wysłania emailem!**

#### Krok 1: Przygotuj plik HTML
```bash
python3 create_email_file.py
```

Ten skrypt utworzy plik `walentynka_dla_mati.html`, który możesz załączyć do emaila.

#### Krok 2: Wygeneruj gotowy email (NOWE! 💕)
```bash
python3 prepare_email.py
```

Ten skrypt utworzy plik `email_template.txt` z **gotowym tekstem emaila**:
- ✉️ Temat emaila
- 📝 Treść wiadomości
- 💡 Instrukcje dla odbiorcy
- 🎨 3 alternatywne wersje (krótka, romantyczna, zabawna)

**Po prostu:**
1. Uruchom `python3 prepare_email.py`
2. Otwórz plik `email_template.txt`
3. Skopiuj wybraną treść do emaila
4. Załącz plik `walentynka_dla_mati.html`
5. Wyślij! 💕

**Zalety:**
- ✅ Gotowy email - nie musisz nic pisać!
- ✅ 3 wersje do wyboru (oficjalna, romantyczna, zabawna)
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
