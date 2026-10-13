# Adresy grupowe w ETS6 krok po kroku

Przycisk i aktor zaczynają współpracować dopiero po połączeniu ich obiektów komunikacyjnych wspólnym adresem grupowym. Instrukcja powstała z filmu grouping.mp4 (2:55 min, nagranie ekranu ETS6 z komentarzem lektora, projekt „My first project”); transkrypcja i tłumaczenie są na stronie [Film ETS6: transkrypcja](grouping-transkrypcja.md).

**O co chodzi (lektor):** adresy grupowe to adresy wirtualne, przez które urządzenia na magistrali komunikują się ze sobą. Urządzenia dodane wcześniej do struktury budynku same nic nie robią, dopóki ich obiekty nie zostaną połączone wspólnym adresem.

## Punkt wyjścia

Projekt ma budynek „Main building” z piętrami Floor 1 i Floor 2. Na Floor 1 są pomieszczenia Bathroom, Cabinet, Children, Kitchen i Living room. W salonie (Living room) są trzy urządzenia Siemens:

| Adres fizyczny | Urządzenie | Program aplikacyjny |
| --- | --- | --- |
| 1.1.- | Zasilacz N 125/02 (5WG1 125-1AB02) | brak, zasilacz nie ma programu |
| 1.1.1 | Aktor przełączający N 567/01 (8 A), 4 kanały | 25 A4 Binary, Flash before Off |
| 1.1.2 | Interfejs przycisków UP 220/21 | 07 B0 S2 On-off-toggle/Dim/Shu/Value |

Cel: przycisk (kanały A i B interfejsu 1.1.2) ma włączać i wyłączać dwa obwody światła na kanałach A i B aktora 1.1.1.

## Krok 1. Otwórz panel adresów grupowych

1. W ETS6 otwórz projekt i zostaw u góry panel **Buildings**.
2. Otwórz panel **Group Addresses**. Pojawi się pod spodem z pustym drzewem, w którym jest tylko „Dynamic Folders”.
3. Adresy tworzy się tak samo jak elementy struktury budynku: zaznaczasz element nadrzędny i dodajesz elementy podrzędne.

## Krok 2. Utwórz grupy główne

ETS nie narzuca struktury adresów. W filmie grupy główne to funkcje centralne i piętra domu.

1. W panelu Group Addresses kliknij **Add Main Groups**.
2. W oknie wpisz nazwę w polu Name. Przyciskiem **+** po prawej dodajesz kolejne wiersze, czyli kilka grup naraz.
3. Wpisz trzy grupy: **Central functions**, **Floor 1**, **Floor 2**.
4. W „Generate Addresses” zostaw **Fill up (use first free)**. ETS nada wtedy pierwsze wolne numery. Inne opcje to Append (dopisz na końcu) i Start with (zacznij od podanego numeru).
5. Kliknij OK. Powstają grupy główne: **0 Central functions**, **1 Floor 1**, **2 Floor 2**.

## Krok 3. Utwórz grupy środkowe

1. Zaznacz **0 Central functions** i kliknij **Add Middle Groups**.
2. Dodaj trzy wiersze: **Lighting control**, **Dimming control**, **Sunblind control** (w filmie jest literówka „Sunbling”).
3. OK. Powstają: **0/0 Lighting control**, **0/1 Dimming control**, **0/2 Sunblind control**.
4. W panelu Properties grupy widać m.in. opcję **Pass through Line Coupler** (przepuszczanie przez sprzęgło liniowe) i **Security: Automatic**.
5. Prawy przycisk myszy na grupie pokazuje menu z opcjami Add Middle Groups, Copy/Paste, Paste Special, **Export Group Addresses** i **Import Group Addresses**. Lektor radzi: jeśli na drugim piętrze też potrzebne są oświetlenie i ściemnianie, skopiuj grupy środkowe i wklej je do grupy głównej **2 Floor 2**.

## Krok 4. Utwórz adresy grupowe

1. Zaznacz **0/0 Lighting control** i kliknij **Add Group Addresses**.
2. Dodaj dwa adresy: **Light 1** i **Light 2** (w filmie „Ligth”).
3. OK. Powstają **0/0/1 Light 1** i **0/0/2 Light 2**. Na tym etapie nie mają typu danych ani powiązań, a w kolumnie „No. of…” jest 0.
4. Uwaga: lektor mówi o światłach „pierwszego piętra” w salonie, ale na ekranie adresy trafiają do 0/0 Lighting control w grupie Central functions. W swoim projekcie lepiej trzymać światła pomieszczenia w grupie jego piętra (np. 1/0/1), a w Central functions zostawić funkcje dla całego domu (to wniosek własny, nie z filmu).

## Krok 5. Ustaw parametry przycisku

1. W Buildings zaznacz **1.1.2 Push button interface** i otwórz zakładkę **Parameters**.
2. W sekcji kanałów A + B ustaw:
   - Function of channels A + B: **Inputs, separately configurable**
   - Operation of input: **Send switching status / Binary value**
   - Switching value when contact is closed: **On**
   - Switching value when contact is open: **Off**
   - Send switching value after bus voltage… (powrót napięcia magistrali): **No**
3. W zakładce **Group Objects** pojawiają się obiekty **21 Channel A, Status (On/Off)** i **26 Channel B, Status (On/Off)**. Mają 1 bit i flagi C, R, W, T.

## Krok 6. Połącz adresy z obiektami przycisku

Lektor opisuje to jako przeciąganie obiektów komunikacyjnych na adresy grupowe; w filmie przeciągany jest adres na obiekt, efekt jest ten sam. Cel: **górny lewy** klawisz (kanał A) steruje światłem 1, **dolny lewy** (kanał B) światłem 2.

1. Przeciągnij adres **0/0/1 Light 1** z panelu Group Addresses na obiekt **21 Channel A**. ETS pokazuje podpowiedź „Link with 0/0/1 Light 1”.
2. Przeciągnij **0/0/2 Light 2** na obiekt **26 Channel B**.
3. Adresy dostają typ danych **switch, 1 bit** (DPT 1.001), a licznik powiązań zmienia się na 1. Pierwszy obiekt połączony z adresem nadaje mu typ.

## Krok 7. Połącz adresy z obiektami aktora

Lektor: wyjście **A** aktora załącza światło 1, wyjście **B** światło 2.

1. Zaznacz **1.1.1 Switching actuator**, zakładka **Group Objects**. Widać obiekty 0 Status direct mode, **3 Switch, Channel A**, **7 Switch, Channel B**, 11 Switch, Channel C i 15 Switch, Channel D.
2. Przeciągnij **0/0/1** na obiekt **3 Switch, Channel A**, a **0/0/2** na obiekt **7 Switch, Channel B**.
3. W kolumnie Group Address obiektów pojawiają się 0/0/1 i 0/0/2, a przy adresach w panelu Group Addresses licznik powiązań to **2**: nadawca (przycisk) i odbiorca (aktor).
4. Sprawdzenie (lektor): rozwiń adres w Group Addresses, a zobaczysz pod nim połączone urządzenia. Z drugiej strony, przy obiektach urządzenia widać, z jakimi adresami są powiązane.

## Co z tego wynika

- Nacisk kanału A przycisku wysyła telegram „On/Off” na 0/0/1, a aktor włącza lub wyłącza kanał A. Kanał B działa tak samo przez 0/0/2.
- Układ trzypoziomowy z filmu to: grupa główna = funkcje centralne albo piętro, grupa środkowa = rodzaj funkcji (oświetlenie, ściemnianie, rolety), adres = konkretny obwód.
- Kolejność pracy w ETS: najpierw struktura adresów, potem parametry urządzeń, na końcu łączenie obiektów z adresami przez przeciąganie. Wgranie do urządzeń (Download) to osobny krok, którego film nie pokazuje.
