#!/usr/bin/env python3
"""
Skrypt generujący gotowy szablon emaila z pytaniem walentynkowym.
Tworzy pełny tekst emaila gotowy do skopiowania i wysłania.
"""

import os
import sys
from datetime import datetime

def create_email_template():
    """Generuje szablon emaila z walentynką"""
    
    # Sprawdź czy plik HTML istnieje
    html_file = "walentynka_dla_mati.html"
    if not os.path.exists(html_file):
        print("⚠️  Plik walentynka_dla_mati.html nie istnieje!")
        print("   Najpierw uruchom: python3 create_email_file.py")
        return False
    
    # Pobierz rozmiar pliku
    file_size = os.path.getsize(html_file)
    file_size_kb = file_size / 1024
    
    # Szablon emaila
    email_template = f"""
╔══════════════════════════════════════════════════════════════╗
║           📧 GOTOWY EMAIL DO SKOPIOWANIA 💕                  ║
╚══════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DO: Mati 💕

TEMAT: Mam dla Ciebie pytanie... 💖

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TREŚĆ WIADOMOŚCI:

Cześć! 💕

Przygotowałem dla Ciebie coś specjalnego na Walentynki... 🌹

Załączam plik HTML, który możesz otworzyć w przeglądarce.
To interaktywna strona z ważnym pytaniem! 💝

📎 ZAŁĄCZNIK: walentynka_dla_mati.html ({file_size_kb:.1f} KB)

JAK OTWORZYĆ:
1. Pobierz załączony plik na komputer
2. Kliknij dwukrotnie, aby otworzyć w przeglądarce
3. Ciesz się animacjami i odpowiedz na pytanie! 😊

PS: Strona działa bez internetu i ma latające serduszka! ❤️

Z miłością,
Twój Walentynik 💘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INSTRUKCJA DLA CIEBIE:
1. Skopiuj powyższą treść (od "DO:" do końca wiadomości)
2. Wklej do nowego emaila
3. Załącz plik: walentynka_dla_mati.html
4. Wyślij! 💕

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️  WAŻNE:
   • Nie zapomnij załączyć pliku walentynka_dla_mati.html!
   • Plik znajduje się w tym samym folderze co ten skrypt
   • Możesz edytować treść emaila według własnych upodobań 💝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    # Zapisz do pliku
    output_file = "email_template.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(email_template)
    
    # Wyświetl na ekranie
    print(email_template)
    
    print(f"\n✅ Email zapisany do pliku: {output_file}")
    print(f"📧 Możesz teraz otworzyć plik i skopiować treść do emaila!")
    print(f"\n💡 TIP: Możesz też bezpośrednio skopiować treść z ekranu powyżej!")
    
    return True

def create_alternative_templates():
    """Tworzy alternatywne wersje emaila"""
    
    alternatives = """

╔══════════════════════════════════════════════════════════════╗
║        📝 ALTERNATYWNE WERSJE TREŚCI EMAILA 💕              ║
╚══════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WERSJA 1: KRÓTKA I ZWIĘZŁA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Cześć Mati! 💕

Załączam dla Ciebie walentynkową niespodziankę! 🌹
Otwórz załączony plik w przeglądarce i zobacz co przygotowałem! 😊

Z miłością ❤️

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WERSJA 2: ROMANTYCZNA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Kochana Mati! 💖

W tym szczególnym dniu chciałbym zadać Ci bardzo ważne pytanie...
Przygotowałem dla Ciebie coś wyjątkowego - interaktywną stronę 
pełną latających serduszek i magii! ✨

Otwórz załączony plik i zobacz, co chcę Ci powiedzieć. 🌹
Obiecuję, że to będzie coś, czego nie zapomnisz! 💝

Czekam na Twoją odpowiedź z niecierpliwością! 💘

Twój wielbiciel 💕

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WERSJA 3: ZABAWNA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Hej Mati! 👋💕

Znalazłem na internecie ten dziwny plik HTML... 🤔
Podobno jest tam jakieś ważne pytanie dla Ciebie! 

Możesz sprawdzić? Otwórz załącznik w przeglądarce! 😄
(Ostrzegam - są tam latające serduszka! ❤️)

PS: Przycisk "NIE" jest trochę nieśmiały... 😏

Pozdrawiam! 🎉

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    # Dodaj do pliku
    with open("email_template.txt", 'a', encoding='utf-8') as f:
        f.write(alternatives)
    
    print(alternatives)
    print("\n✨ Alternatywne wersje dodane do email_template.txt!")

def main():
    """Główna funkcja"""
    print("🎀 Generator Szablonu Email Walentynkowy 💕")
    print("=" * 60)
    print()
    
    # Utwórz główny szablon
    if create_email_template():
        print()
        # Dodaj alternatywne wersje
        create_alternative_templates()
        print()
        print("━" * 60)
        print("✅ GOTOWE! Wszystko przygotowane do wysłania!")
        print("━" * 60)
        return True
    else:
        return False

if __name__ == "__main__":
    if main():
        sys.exit(0)
    else:
        sys.exit(1)
