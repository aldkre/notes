import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Java notes",
    page_icon="colapsed",
    initial_sidebar_state="collapsed",
    menu_items={}
)

st.header("JAVA")

typy_danych, pojecia, metody = st.tabs(["Typy danych", "Podstawowe pojęcia", "Metody"])

with typy_danych:
    typ_prymitywny, typ_referencyjny = st.columns(2)
    with typ_prymitywny:
        st.subheader("Typy prymitywne")

        st.caption("""
        Wartości prymitywne w Javie to podstawowe typy danych, które nie są obiektami.\n Java obsługuje osiem typów prymitywnych, a każdy z nich ma swoje specyficzne właściwości. Oto one:
        """)

        st.caption("""
        1. **byte**:
        - **Rozmiar**: 8 bitów
        - **Zakres**: -128 do 127
        - **Domyślna wartość**: 0
        
        --------------------------------
    
        2. **short**:
       - **Rozmiar**: 16 bitów
       - **Zakres**: -32,768 do 32,767
       - **Domyślna wartość**: 0
       
       --------------------------------
    
        3. **int**:
       - **Rozmiar**: 32 bity
       - **Zakres**: -2^31 do 2^31-1
       - **Domyślna wartość**: 0
       
       ```java
        int liczba = 42;
        ```
        
        --------------------------------
    
        4. **long**:
       - **Rozmiar**: 64 bity
       - **Zakres**: -2^63 do 2^63-1
       - **Domyślna wartość**: 0L
       
       --------------------------------
    
        5. **float**:
       - **Rozmiar**: 32 bity
       - **Precyzja**: 6-7 cyfr znaczących
       - **Domyślna wartość**: 0.0f
       
       --------------------------------
    
        6. **double**:
       - **Rozmiar**: 64 bity
       - **Precyzja**: 15-16 cyfr znaczących
       - **Domyślna wartość**: 0.0d
       
        ```java
        double pi = 3.14;
        ```
        
        --------------------------------
    
        7. **char**:
       - **Rozmiar**: 16 bitów
       - **Zakres**: 0 do 65,535 (reprezentacja Unicode znaków)
       - **Domyślna wartość**: '\\u0000' (null char)
       
        ```java
        char litera = 'A';
        ```
        
        --------------------------------
    
        8. **boolean**:
       - **Rozmiar**: 1 bit
       - **Wartości**: true lub false
       - **Domyślna wartość**: false
       
        ```java
        boolean prawda = true;
        ```
       --------------------------------
       --------------------------------
       W przeciwieństwie do obiektów, wartości prymitywne nie mają metod ani atrybutów. 
       Są przechowywane bezpośrednio na stosie, co oznacza, że są bardziej wydajne pod względem pamięci i 
       przetwarzania niż obiekty.
       

        """)

    with typ_referencyjny:
        st.subheader("Typy referencyjne")

        st.caption("""
        To typy złożone, zdefiniowane w bibliotekach standardowych języka Java 
        oraz tworzone przez programistów poprzez pisanie klas. Do typów złożonych zaliczają się także tablice.
        
        1. **String** Używany do reprezentacji ciągów znaków:
       - **Zakres**: Nieograniczony (ilość znaków zależy od dostępnej pamięci)
       - **Domyślna wartość**: null
       
        String nie jest wartością prymitywną w Javie. Jest to obiekt reprezentujący sekwencję znaków i jest instancją klasy `java.lang.String`. 
        Chociaż String wygląda na typ prosty i jest używany w sposób, który wydaje się prosty, 
        jest to w rzeczywistości obiekt klasy, co oznacza, że ma metody i może być manipulowany za pomocą różnych operacji.
        
        --------------------------------

        2. **Array** Tablica, która może przechowywać wiele elementów tego samego typu:
        - **Zakres**: Zależny od typu elementu tablicy
        - **Domyślna wartość**: null
        
        ```java
        int[] liczby = {1, 2, 3, 4, 5};
        ```

        --------------------------------

        3. **Class (Obiekt)** Obiekty klas są instancjami klas, które mogą mieć pola (zmienne) i metody:
        - **Zakres**: Zależny od klasy
        - **Domyślna wartość**: null
        
        ```java
        public class Osoba 
        {
            String imie;
            int wiek;

            public Osoba(String imie, int wiek) 
            {
                this.imie = imie;
                this.wiek = wiek;
            }
        }

        Osoba osoba1 = new Osoba("Jan", 30);
        ```
        
        --------------------------------
        
        4. **Interface**: Interfejsy definiują metody, które muszą zostać zaimplementowane przez klasy.
        
        - Interfejs definiuje zestaw metod, które klasa musi zaimplementować, ale nie zawiera implementacji tych metod.
        ```java
        interface Zwierze 
        {
            void dzwiek();
        }

        class Pies implements Zwierze 
        {
            public void dzwiek() 
            {
                System.out.println("Hau Hau");
            }
        }
        ```
        
        - Klasa, która implementuje interfejs, musi zdefiniować wszystkie metody zawarte w interfejsie.
        ```java
        Pies pies = new Pies();
        pies.dzwiek(); // Wyświetli: Hau Hau
        ```
        Różnica między **klasą abstrakcyjną** a **interfejsem** w Javie:
        - **Klasa abstrakcyjna** może zawierać zarówno metody abstrakcyjne (bez implementacji), jak i konkretne (z implementacją). Klasa abstrakcyjna może mieć zmienne instancji.
        ```java
        abstract class Zwierze 
        {
            abstract void dzwiek();
            void oddychaj() 
            {
                System.out.println("Oddycha...");
            }
        }
        ```
        
        - **Interfejs** definiuje tylko nagłówki metod (do Javy 8, gdy wprowadzono domyślne metody). Interfejsy są bardziej ogólne, klasy abstrakcyjne mogą posiadać więcej szczegółów.
        ```java
        interface Zwierze 
        {
            void dzwiek();
        }
        ```

        --------------------------------

        5. **Collections (Kolekcje)**: Java Collections Framework zawiera struktury danych takie jak List, Set, Map.
        ```java
        List<String> lista = new ArrayList<>();
        Set<Integer> zbior = new HashSet<>();
        Map<String, Integer> mapa = new HashMap<>();
        ```
        
        --------------------------------

        6. **Enums**: Enumy to specjalne typy klas używane do reprezentowania grupy stałych.
        ```java
        public enum Dzien 
            {
                PONIEDZIALEK, WTOREK, SRODA, CZWARTEK, PIATEK, SOBOTA, NIEDZIELA
            }

        Dzien dzien = Dzien.PONIEDZIALEK;
        ```        
        Domyślne wartości dla typów referencyjnych są zawsze `null`, co oznacza brak obiektu.
        
        """)

    st.divider()
    st.caption("""
    
    Główną różnicą pomiędzy typami prymitywnymi a typami referencyjnymi jest to, 
    że zmienne typów prymitywnych przechowują w pamięci komputera konkretne wartości, 
    natomiast zmienne typu referencyjnego przechowują adresy obiektów w pamięci.
    
    Przechowywanie danych: 
    - ***rejestry***
    - ***stos*** RAM, referencje do obiektów, szybki i efektywny sposób przydzielania pamięci
    - ***sterta*** RAM, obiekty, wolniejszy sposób
    - ***obszar stałych*** bezpośrednio w kodzie, ROM
    - ***obszar spoza RAM***
    
    W C++ obiekty da się umieszczać na stosie - potrzeba określenia rozmiaru i czasu życia
    
    Typy nieprymitywne oferują wiele funkcji i możliwości, które umożliwiają tworzenie bardziej złożonych 
    i dynamicznych aplikacji.
    
    Obiekty wysokich precyzji: BigInteger, BigDecimal

    
    **Obiekt**:
    - Jest instancją klasy. Kiedy tworzysz obiekt, rezerwujesz pamięć i przypisujesz wartości do jego pól.
    - Obiekt istnieje w pamięci i można na nim wywoływać metody.
    - Przykład tworzenia obiektu:
     
      ```java
      KlasaMoja mojObiekt = new KlasaMoja();
      ```
    
    **Referencja**:
    - Jest zmienną, która przechowuje adres obiektu w pamięci.
    - Referencje wskazują na obiekty, ale same nie przechowują danych obiektowych.
    - Można mieć wiele referencji do jednego obiektu.
    - Przykład przypisania referencji:
     
      ```java
      KlasaMoja innaReferencja = mojObiekt; // obie referencje wskazują na ten sam obiekt
      ```
    
    W skrócie:
    - **Obiekt** to rzeczywista instancja klasy zawierająca dane.
    - **Referencja** to zmienna wskazująca na obiekt.
    
    """)

with pojecia:
    st.caption("""
1. **JVM (Java Virtual Machine)**:
   - JVM to wirtualna maszyna, która tłumaczy kod bajtowy Javy na kod maszynowy w czasie rzeczywistym, umożliwiając uruchamianie aplikacji Java na różnych platformach.

--------------------------------

2. **JDK, JRE, i JVM**:
   - **JRE (Java Runtime Environment)**: Środowisko uruchomieniowe dla aplikacji Java, które zawiera JVM oraz biblioteki i inne pliki potrzebne do uruchomienia programów.
   - **JDK (Java Development Kit)**: Zestaw narzędzi dla programistów, który zawiera JRE, JVM oraz narzędzia do tworzenia aplikacji Java, takie jak kompilator (javac). 
   ***(zawiera funkcje preparacji, kompilacji, linkowania)***
   - **JVM**: Wirtualna maszyna Java, która wykonuje kod bajtowy i umożliwia uruchamianie aplikacji Java na różnych platformach.
   Język programowania kompilowany na język pośredni bajtowy, który w locie kompilowany jest na język maszynowy przez JVM

    
    IDE - integrated development environment (Eclipse, NetBeans, IntelliJ IDEA)
    
--------------------------------

3. **Garbage Collection**:
   - Garbage Collection to proces automatycznego zarządzania pamięcią, który usuwa obiekty, do których nie ma już referencji, aby zwolnić pamięć i zapobiec wyciekom pamięci.

--------------------------------

4. **Polimorfizm**:
   - Polimorfizm to zdolność obiektów do przyjmowania różnych form. W Javie pozwala to na wywoływanie metod na obiektach różnych klas, które dziedziczą z tej samej klasy bazowej, umożliwiając elastyczność i rozszerzalność kodu.

--------------------------------

5. **Dziedziczenie (Inheritance)**:
   - Dziedziczenie to mechanizm, który pozwala jednej klasie (klasa potomna) na przejęcie właściwości i metod innej klasy (klasa bazowa). To ułatwia ponowne użycie kodu, jego rozszerzanie i modyfikowanie.

--------------------------------

6. **Exceptions handling**:
    - Exception handling to mechanizm zarządzania błędami, który umożliwia programistom obsługę wyjątków (błędów) w kontrolowany sposób.
  ```java
  try 
  {
      int[] liczby = {1, 2, 3};
      System.out.println(liczby[10]); // Spowoduje ArrayIndexOutOfBoundsException
  } 
  catch (ArrayIndexOutOfBoundsException e) 
  {
      System.out.println("Błąd: " + e.getMessage());
  }
  ```

--------------------------------

7. **Enkapsulacja**:
    - Enkapsulacja to zasada OOP (Object-Oriented Programming), która polega na ukrywaniu szczegółów implementacyjnych klasy i udostępnianiu tylko publicznych metod dostępowych.
  ```java
  public class Osoba 
  {
      private String imie;
      private int wiek;

      public String getImie() 
      {
          return imie;
      }

      public void setImie(String imie) 
      {
          this.imie = imie;
      }

      public int getWiek() 
      {
          return wiek;
      }

      public void setWiek(int wiek) 
      {
          this.wiek = wiek;
      }
  }
  ```
Enkapsulacja zapewnia kontrolę nad danymi i zapobiega nieautoryzowanemu dostępowi i modyfikacji.

    """)

with metody:
    st.caption("""
- **Metoda statyczna** (oznaczona słowem kluczowym `static`) należy do klasy, a nie do instancji tej klasy. Oznacza to, że można ją wywołać bez tworzenia obiektu klasy.
  ```java
  public class MojaKlasa 
  {
      static void metodaStatyczna() 
      {
          System.out.println("To jest metoda statyczna.");
      }
  }

  // Wywołanie metody statycznej
  MojaKlasa.metodaStatyczna();
  ```
- **Metoda instancji** działa na obiektach klasy i może operować na polach i metodach tej konkretnej instancji.
  ```java
  public class MojaKlasa 
  {
      void metodaInstancji() 
      {
          System.out.println("To jest metoda instancji.");
      }
  }

  // Tworzenie obiektu i wywoływanie metody instancji
  MojaKlasa mojObiekt = new MojaKlasa();
  mojObiekt.metodaInstancji();
  ```
    """)