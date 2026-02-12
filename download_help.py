#!/usr/bin/env python3
"""
Pomocniczy skrypt do pobrania wszystkich potrzebnych plików walentynkowych.
Wyświetla instrukcje pobierania i linki do plików.
"""

import sys
import os

def print_header():
    """Wyświetl nagłówek"""
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 15 + "📥 INSTRUKCJA POBIERANIA PLIKÓW 💕" + " " * 18 + "║")
    print("╚" + "═" * 68 + "╝")
    print()

def print_separator():
    """Wyświetl separator"""
    print("━" * 70)
    print()

def show_download_instructions():
    """Wyświetl szczegółowe instrukcje pobierania"""
    
    print_header()
    
    print("🎯 WYBIERZ METODĘ POBIERANIA:")
    print()
    
    # Metoda 1: ZIP
    print("📦 METODA 1: Pobierz wszystko jako ZIP (NAJŁATWIEJSZA)")
    print_separator()
    print("1. Otwórz stronę:")
    print("   https://github.com/rtjhvg/Walentynka")
    print()
    print("2. Kliknij zielony przycisk 'Code'")
    print()
    print("3. Wybierz 'Download ZIP'")
    print()
    print("4. Rozpakuj pobrany plik na swoim komputerze")
    print()
    print("✅ Wszystkie pliki będą w jednym folderze!")
    print()
    print_separator()
    
    # Metoda 2: Pojedyncze pliki
    print("📄 METODA 2: Pobierz tylko potrzebne pliki")
    print_separator()
    print("Otwórz poniższe linki i użyj 'Prawy klik → Zapisz jako...'")
    print()
    
    files = {
        "index.html": "Główna strona walentynkowa",
        "create_email_file.py": "Skrypt do tworzenia załącznika email",
        "prepare_email.py": "Skrypt do generowania treści emaila"
    }
    
    base_url = "https://raw.githubusercontent.com/rtjhvg/Walentynka/copilot/add-simple-html-page/"
    
    for filename, description in files.items():
        print(f"📎 {filename}")
        print(f"   {description}")
        print(f"   {base_url}{filename}")
        print()
    
    print_separator()
    
    # Metoda 3: Git
    print("💻 METODA 3: Dla zaawansowanych (Git)")
    print_separator()
    print("Jeśli masz Git, uruchom w terminalu:")
    print()
    print("  git clone https://github.com/rtjhvg/Walentynka.git")
    print("  cd Walentynka")
    print("  git checkout copilot/add-simple-html-page")
    print()
    print_separator()
    
    # Co dalej
    print("📋 CO DALEJ?")
    print_separator()
    print("Po pobraniu plików:")
    print()
    print("1️⃣  Jeśli chcesz tylko otworzyć stronę:")
    print("    → Otwórz plik 'index.html' w przeglądarce")
    print()
    print("2️⃣  Jeśli chcesz wysłać emailem:")
    print("    → Uruchom: python3 create_email_file.py")
    print("    → Uruchom: python3 prepare_email.py")
    print("    → Użyj wygenerowanych plików do emaila")
    print()
    print_separator()
    
    # Pomoc
    print("❓ POTRZEBUJESZ POMOCY?")
    print_separator()
    print("Sprawdź plik README.md dla szczegółowych instrukcji!")
    print()
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 20 + "GOTOWE! Miłego pobierania! 💕" + " " * 19 + "║")
    print("╚" + "═" * 68 + "╝")

def check_current_location():
    """Sprawdź czy użytkownik jest już w folderze z plikami"""
    required_files = ['index.html', 'create_email_file.py', 'prepare_email.py']
    files_present = [f for f in required_files if os.path.exists(f)]
    
    if len(files_present) == len(required_files):
        print("✅ ŚWIETNIE! Jesteś już w folderze z plikami!")
        print()
        print("Znalezione pliki:")
        for f in files_present:
            print(f"  ✓ {f}")
        print()
        print("Możesz teraz użyć tych plików!")
        print()
        return True
    elif len(files_present) > 0:
        print(f"⚠️  Znaleziono tylko {len(files_present)}/{len(required_files)} plików")
        print()
        print("Znalezione:")
        for f in files_present:
            print(f"  ✓ {f}")
        print()
        print("Brakujące:")
        for f in required_files:
            if f not in files_present:
                print(f"  ✗ {f}")
        print()
        print("Pobierz brakujące pliki według instrukcji poniżej:")
        print()
        return False
    else:
        print("ℹ️  Nie znaleziono plików w bieżącym folderze.")
        print()
        print("Użyj poniższych instrukcji aby pobrać pliki:")
        print()
        return False

def main():
    """Główna funkcja"""
    print()
    
    # Sprawdź obecną lokalizację
    already_downloaded = check_current_location()
    
    if not already_downloaded:
        # Pokaż instrukcje pobierania
        show_download_instructions()
    else:
        print("━" * 70)
        print()
        print("💡 NASTĘPNE KROKI:")
        print()
        print("• Otwórz index.html w przeglądarce, aby zobaczyć stronę")
        print("• Uruchom: python3 create_email_file.py")
        print("• Uruchom: python3 prepare_email.py")
        print()
        print("Więcej informacji w README.md")
        print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Do zobaczenia!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Wystąpił błąd: {e}")
        sys.exit(1)
