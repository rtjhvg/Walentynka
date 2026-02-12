#!/usr/bin/env python3
"""
Skrypt do generowania emaila z linkiem do strony walentynkowej.
NIE wymaga pobierania żadnych plików - wysyłasz tylko link!
"""

import sys

def generate_link_email():
    """Generuje gotowy email z linkiem do GitHub Pages"""
    
    # Link do GitHub Pages (może już działać lub wymaga włączenia)
    github_pages_url = "https://rtjhvg.github.io/Walentynka/"
    raw_file_url = "https://raw.githubusercontent.com/rtjhvg/Walentynka/copilot/add-simple-html-page/index.html"
    
    email_template = f"""
╔══════════════════════════════════════════════════════════════════════╗
║              📧 EMAIL Z LINKIEM (BEZ POBIERANIA!) 💕                ║
╚══════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ NAJŁATWIEJSZA OPCJA - WYŚLIJ TYLKO LINK! ✨

Nie musisz nic pobierać ani instalować!
Po prostu skopiuj gotowy email poniżej i wyślij! 🚀

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DO: Mati 💕

TEMAT: Mam dla Ciebie pytanie... 💖

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TREŚĆ EMAILA:

Cześć! 💕

Przygotowałem dla Ciebie coś specjalnego na Walentynki... 🌹

Kliknij w ten link, aby zobaczyć moją niespodziankę:

🔗 {github_pages_url}

To interaktywna strona z ważnym pytaniem dla Ciebie! 💝
Działa od razu w przeglądarce - nie musisz nic pobierać! ✨

PS: Są tam latające serduszka! ❤️

Z miłością,
Twój Walentynik 💘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️  WAŻNE - PRZECZYTAJ PRZED WYSŁANIEM:

Opcja 1: Jeśli GitHub Pages jest już włączony ✅
   → Użyj linku powyżej: {github_pages_url}
   → Link działa od razu!

Opcja 2: Jeśli GitHub Pages NIE jest jeszcze włączony ⚙️
   → Musisz najpierw włączyć GitHub Pages (zobacz instrukcje poniżej)
   → To zajmie 2 minuty i link będzie działać na zawsze!

Opcja 3: Link awaryjny (działa zawsze, ale trzeba pobrać plik) 🔄
   → Użyj tego zamiast: {raw_file_url}
   → Dodaj do emaila: "Prawym klikiem na link → Zapisz jako... → Otwórz w przeglądarce"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 JAK WŁĄCZYĆ GITHUB PAGES (jednorazowo, 2 minuty):

1. Idź na: https://github.com/rtjhvg/Walentynka/settings/pages

2. W sekcji "Source" wybierz:
   - Branch: copilot/add-simple-html-page
   - Folder: / (root)

3. Kliknij "Save"

4. Poczekaj 2-3 minuty

5. Odśwież stronę - zobaczysz "Your site is live at..."

6. ✅ GOTOWE! Link {github_pages_url} działa!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 ALTERNATYWNE WERSJE EMAILA:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WERSJA 1: KRÓTKA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Cześć Mati! 💕

Mam dla Ciebie walentynkową niespodziankę! 
Kliknij tutaj: {github_pages_url}

Z miłością ❤️

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WERSJA 2: ROMANTYCZNA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Kochana Mati! 💖

W tym szczególnym dniu chciałbym zadać Ci bardzo ważne pytanie...
Przygotowałem dla Ciebie coś wyjątkowego! ✨

Kliknij w ten link i zobacz, co chcę Ci powiedzieć:
{github_pages_url}

Strona jest pełna latających serduszek i magii! 🌹
Czekam na Twoją odpowiedź z niecierpliwością! 💘

Twój wielbiciel 💕

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WERSJA 3: ZABAWNA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Hej Mati! 👋💕

Znalazłem w internecie ciekawą stronę... 🤔
Podobno jest tam jakieś ważne pytanie dla Ciebie!

{github_pages_url}

Ostrzegam - są tam latające serduszka! ❤️
PS: Spróbuj kliknąć przycisk "NIE" - jest trochę nieśmiały! 😏

Pozdrawiam! 🎉

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ GOTOWE! Skopiuj wybraną wersję i wyślij!

Zalety tego rozwiązania:
  💚 Nie musisz nic pobierać
  💚 Nie musisz instalować Pythona
  💚 Nie musisz załączać plików
  💚 Link działa na każdym urządzeniu
  💚 Odbiorca klika i od razu widzi stronę!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    # Zapisz do pliku
    output_file = "email_link_tylko.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(email_template)
    
    print(email_template)
    print(f"\n💾 Email zapisany do pliku: {output_file}")
    print(f"📧 Otwórz plik i skopiuj treść do emaila!")
    
    return True

def check_github_pages_status():
    """Sprawdź czy można przetestować link GitHub Pages"""
    print("\n" + "="*70)
    print("🔍 SPRAWDZANIE STATUSU GITHUB PAGES")
    print("="*70)
    print()
    print("Aby sprawdzić czy Twój link działa:")
    print()
    print("1. Otwórz w przeglądarce:")
    print("   https://rtjhvg.github.io/Walentynka/")
    print()
    print("2. Jeśli widzisz stronę walentynkową - ✅ DZIAŁA!")
    print("   Możesz wysłać link!")
    print()
    print("3. Jeśli widzisz błąd 404 - ⚠️ Musisz włączyć GitHub Pages")
    print("   (zobacz instrukcje w wygenerowanym emailu)")
    print()
    print("="*70)

def main():
    """Główna funkcja"""
    print("\n🎀 Generator Emaila z Linkiem (Bez Pobierania!) 💕")
    print("="*70)
    print()
    
    # Wygeneruj email
    if generate_link_email():
        print()
        # Sprawdź status
        check_github_pages_status()
        print()
        print("━"*70)
        print("✅ GOTOWE! Email z linkiem jest przygotowany!")
        print("━"*70)
        return True
    else:
        return False

if __name__ == "__main__":
    if main():
        sys.exit(0)
    else:
        sys.exit(1)
