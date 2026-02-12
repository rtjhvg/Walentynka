#!/usr/bin/env python3
"""
Skrypt do generowania data URL dla strony walentynkowej.
Data URL może być skopiowany i wklejony bezpośrednio w przeglądarkę lub wysłany emailem.
"""

import base64
import urllib.parse
import sys

def generate_data_url(html_file_path):
    """Generuje data URL z pliku HTML"""
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Kodowanie HTML do base64
        html_bytes = html_content.encode('utf-8')
        html_base64 = base64.b64encode(html_bytes).decode('utf-8')
        
        # Tworzenie data URL
        data_url = f"data:text/html;charset=utf-8;base64,{html_base64}"
        
        return data_url, len(data_url)
    
    except FileNotFoundError:
        print(f"❌ Błąd: Nie znaleziono pliku {html_file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Błąd: {str(e)}")
        sys.exit(1)

def main():
    print("🎀 Generator linku walentynkowego 💕")
    print("=" * 50)
    
    html_file = "index.html"
    output_file = "shareable_link.txt"
    
    # Generowanie data URL
    print(f"📄 Czytam plik {html_file}...")
    data_url, url_length = generate_data_url(html_file)
    
    print(f"✅ Data URL wygenerowany pomyślnie!")
    print(f"📏 Długość URL: {url_length:,} znaków")
    
    # Zapisywanie do pliku
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("💕 WALENTYNKOWY LINK - SKOPIUJ I WKLEJ DO PRZEGLĄDARKI LUB EMAILA 💕\n")
        f.write("=" * 80 + "\n\n")
        f.write("INSTRUKCJA:\n")
        f.write("1. Skopiuj cały link poniżej (od 'data:' do końca)\n")
        f.write("2. Wklej go w pasek adresu przeglądarki i naciśnij Enter\n")
        f.write("3. Lub wyślij go w emailu - odbiorca może kliknąć i otworzyć w przeglądarce\n\n")
        f.write("UWAGA: Link jest bardzo długi, ale zawiera całą stronę!\n")
        f.write("=" * 80 + "\n\n")
        f.write("LINK:\n\n")
        f.write(data_url)
        f.write("\n\n")
        f.write("=" * 80 + "\n")
        f.write(f"Długość linku: {url_length:,} znaków\n")
        f.write("=" * 80 + "\n")
    
    print(f"💾 Link zapisany do pliku: {output_file}")
    print("\n📋 INSTRUKCJA:")
    print("   1. Otwórz plik 'shareable_link.txt'")
    print("   2. Skopiuj cały link (bardzo długi!)")
    print("   3. Wklej w przeglądarkę lub wyślij emailem")
    print("\n✨ Gotowe! Możesz teraz udostępnić link! 💕")
    
    # Wyświetlenie pierwszych i ostatnich znaków jako podgląd
    print(f"\n🔍 Podgląd linku:")
    if url_length > 100:
        print(f"   {data_url[:50]}...{data_url[-50:]}")
    else:
        print(f"   {data_url}")

if __name__ == "__main__":
    main()
