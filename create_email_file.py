#!/usr/bin/env python3
"""
Skrypt do tworzenia wersji strony gotowej do wysłania emailem jako załącznik.
Tworzy samodzielny plik HTML, który można wysłać jako załącznik email.
"""

import shutil
import sys

def create_email_attachment():
    """Kopiuje index.html jako wersję do wysłania emailem"""
    try:
        # Kopiuj index.html do nowej nazwy
        shutil.copy('index.html', 'walentynka_dla_mati.html')
        
        print("✅ Sukces!")
        print("=" * 60)
        print("📧 Plik gotowy do wysłania emailem:")
        print("   walentynka_dla_mati.html")
        print()
        print("📋 INSTRUKCJA:")
        print("   1. Znajdź plik 'walentynka_dla_mati.html'")
        print("   2. Załącz go do emaila")
        print("   3. Wyślij do odbiorcy")
        print("   4. Odbiorca otwiera plik w przeglądarce")
        print()
        print("✨ To najlepszy sposób udostępnienia strony! 💕")
        print("=" * 60)
        
        return True
        
    except FileNotFoundError:
        print("❌ Błąd: Nie znaleziono pliku index.html")
        print("   Upewnij się, że uruchamiasz skrypt w folderze repozytorium.")
        return False
    except Exception as e:
        print(f"❌ Błąd: {str(e)}")
        return False

if __name__ == "__main__":
    if create_email_attachment():
        sys.exit(0)
    else:
        sys.exit(1)
