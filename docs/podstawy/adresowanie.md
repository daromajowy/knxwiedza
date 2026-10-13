# Adresowanie i działanie grup

Każde urządzenie KNX ma jeden adres fizyczny, a funkcje łączy się adresami grupowymi: czujnik wysyła telegram na adres grupy, a każdy aktor zapisany do tej grupy wykonuje polecenie. Knx.org tego nie opisuje, więc cały rozdział to wiedza ogólna z zakresu kursu KNX Basic.

## Dwa rodzaje adresów

| Cecha | Adres fizyczny | Adres grupowy |
| --- | --- | --- |
| Format | obszar.linia.urządzenie, np. 1.1.5 | 3-poziomowy główna/środkowa/podgrupa, np. 1/0/1 (też 2-poziomowy lub wolny) |
| Zakres | 0–15 . 0–15 . 0–255 | 0–31 / 0–7 / 0–255 |
| Ile na urządzenie | dokładnie jeden | wiele, przypisanych do obiektów komunikacyjnych |
| Do czego | programowanie w ETS i diagnostyka | codzienna praca instalacji: polecenia i statusy |
| Kto go używa | ETS i instalator | czujniki i aktory między sobą |

## Jak działa grupa, krok po kroku

1. W ETS tworzysz adres grupowy, np. 1/0/1 „Salon – sufit wł/wył”.
2. Przeciągasz go na obiekt komunikacyjny przycisku (nadawca) i na obiekt kanału aktora (odbiorca).
3. Wgrywasz konfigurację; każde urządzenie zapisuje swoją tablicę adresów grupowych i powiązań z obiektami.
4. Naciśnięcie przycisku wysyła telegram zapisu (GroupValueWrite) na 1/0/1 z wartością 1 (DPT 1.001 = włącz).
5. Telegram słyszy cała linia, ale reagują tylko urządzenia, które mają 1/0/1 w swojej tablicy. Sprzęgła przepuszczają go do innych linii tylko wtedy, gdy ta grupa jest w ich tablicy filtrów.
6. Aktor włącza światło i wysyła status na osobny adres, np. 1/0/2, z którego korzysta wizualizacja i dioda w przycisku.

## Zasady warte zapamiętania

- **Jedna grupa, jedna funkcja, jeden typ danych.** Nie mieszaj w jednej grupie wł/wył (DPT 1.001) z jasnością w % (DPT 5.001).
- **Jeden do wielu.** Jeden telegram może sterować wieloma aktorami, np. „wszystkie światła wył” to jeden adres przypisany do wielu kanałów.
- **Wiele do jednego.** Obiekt może słuchać kilku adresów (przycisk lokalny i wyłącznik centralny), ale wysyła tylko na pierwszy przypisany, tzw. adres wysyłający.
- **Trzy rodzaje telegramów grupowych:** zapis (polecenie), odczyt (pytanie o stan) i odpowiedź.
- **Flagi obiektu** decydują, co obiekt może: K komunikacja, O odczyt, Z zapis, T transmisja, A aktualizacja, I inicjalizacja (w ETS po angielsku C, R, W, T, U, I).
- **Oddzielaj polecenie od statusu**, np. 1/0/1 steruje, 1/0/2 mówi, jaki jest stan.
- **Układ trzech poziomów ustal na początku projektu.** Popularny wariant: grupa główna = rodzaj funkcji (1 oświetlenie, 2 rolety, 3 HVAC), środkowa = piętro lub strefa, podgrupa = konkretna funkcja w pomieszczeniu.

## Po co są grupy

- **Brak centralnego sterownika.** Przycisk i aktor rozmawiają bezpośrednio przez adres grupowy, więc światło działa także wtedy, gdy padnie serwer lub wizualizacja.
- **Funkcje centralne i sceny.** Kanał przekaźnika może słuchać np. „Salon sufit”, „Centralne wyłączenie” i „Scena Wyjście” jednocześnie.
- **Zmiany bez kucia ścian.** Żeby przycisk sterował innym światłem, zmieniasz przypisanie adresu w ETS, a nie okablowanie.
- **Wspólny język dla reszty systemu.** Wizualizacje i aplikacje korzystają z tych samych adresów grupowych, importowanych z projektu ETS.

Układ poziomów można też odwrócić: piętro / funkcja / obwód, np. 1/0/3 = Parter / Oświetlenie / Salon sufit. Ważne, by trzymać się jednego układu w całym projekcie.

## Przykład: adresy grupowe salonu

| Adres | Nazwa | DPT | Nadawca | Odbiorcy |
| --- | --- | --- | --- | --- |
| 1/0/1 | Salon sufit wł/wył | 1.001 | przycisk w salonie | aktor, kanał A |
| 1/0/2 | Salon sufit status | 1.001 | aktor, kanał A | dioda przycisku, wizualizacja |
| 1/1/1 | Salon ściemnianie względne | 3.007 | przycisk w salonie | ściemniacz |
| 1/1/2 | Salon jasność w % | 5.001 | wizualizacja | ściemniacz |
| 1/0/100 | Wszystkie światła wył | 1.001 | przycisk przy wyjściu | wszystkie kanały aktorów światła |
