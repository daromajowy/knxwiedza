# Film ETS6: transkrypcja

Komentarz lektora z filmu szkoleniowego `grouping.mp4` (2:55 min), na którym opiera się [instrukcja tworzenia adresów grupowych](ets6-adresy-grupowe.md).

=== "Po polsku"

    Tłumaczenie oryginalnej transkrypcji (13.10.2026). Nazwy elementów ETS6 zostawiono po angielsku, tak jak na ekranie. Znaczniki czasu jak w oryginale.

    **[00:00 – 00:26]** W następnym kroku musimy utworzyć połączenia między urządzeniami dodanymi w poprzedniej części. Do tego służą tak zwane adresy grupowe, czyli adresy wirtualne, dzięki którym wszystkie urządzenia na magistrali mogą się ze sobą komunikować. Do tworzenia adresów grupowych ETS6 ma osobny panel, panel Group Addresses. Na początku jest on pusty, więc musimy

    **[00:26 – 00:41]** tworzyć adresy grupowe krok po kroku. Na szczęście robi się to tak samo jak dodawanie elementów do struktury budynku. Ponieważ nie ma obowiązkowej struktury adresów grupowych, jako grupy główne użyjemy funkcji centralnych i pięter domu.

    **[00:49 – 00:55]** Jako grupy środkowe rozróżniamy sterowanie oświetleniem, sterowanie ściemnianiem i sterowanie roletami.

    **[01:15 – 01:42]** Zakładając, że funkcje oświetlenia i ściemniania są potrzebne również na drugim piętrze, możemy po prostu skopiować te grupy środkowe i wkleić je do grupy głównej drugiego piętra. Ostatnim elementem struktury są właściwe adresy grupowe, które odpowiadają konkretnym funkcjom. Dodajmy więc kilka świateł potrzebnych na pierwszym piętrze. To również działa tak samo jak tworzenie grup głównych i środkowych. Potem możemy już połączyć urządzenia sterujące oświetleniem w salonie.

    **[01:43 – 02:09]** Wystarczy przeciągnąć obiekty komunikacyjne przycisku oraz aktora przełączającego na adres grupowy sterowania oświetleniem w salonie. Zacznijmy od przycisków. Chcemy, żeby górny lewy przycisk włączał i wyłączał światło 1, a dolny lewy przycisk obsługiwał światło 2. Przeciągamy więc obiekt komunikacyjny górnego lewego przycisku na adres grupowy światła 1,

    **[02:10 – 02:39]** a obiekt dolnego lewego przycisku na adres grupowy światła 2. Na koniec trzeba połączyć z oboma światłami również aktor przełączający. Powiedzmy, że wyjście A załącza światło 1. Wystarczy przeciągnąć jego obiekt komunikacyjny na światło 1. Światło 2 będzie załączane przez wyjście B aktora, więc te dwa elementy też łączymy. Jeśli teraz przyjrzymy się bliżej adresom grupowym naszych dwóch świateł w salonie,

    **[02:39 – 02:47]** zobaczymy przy nich połączone urządzenia. Urządzenia także pokazują powiązania z adresami grupowymi połączonych świateł.

=== "Oryginał (EN)"

    Nagranie: grouping.mp4 (2:55). Rozpoznanie mowy: Whisper large-v3-turbo (sherpa-onnx, int8), 13.10.2026. Przerwy bez mowy: 0:41–0:49, 0:55–1:15, 2:47–2:55. Tekst bez poprawek redakcyjnych.

    **[00:00.10 - 00:26.20]** As our next step, we need to create connections between the different devices we added in the previous section. These connections will be handled with the so-called group addresses, the virtual addresses that allow all devices on the bus to communicate with each other. For creating group addresses, ETS6 provides a particular panel, the group addresses panel. Initially, the group addresses panel is empty, so we need to create

    **[00:26.28 - 00:41.42]** group addresses step by step. Luckily, creating group addresses works just like adding elements to the building structure. Since there is no mandatory structure for group addresses, we will use central functions and the floors of the house as the main groups.

    **[00:49.19 - 00:55.25]** As middle groups we differentiate between lighting control, dimming control and sunblind control.

    **[01:15.62 - 01:42.94]** Assuming we need lighting and dimming functions on the second floor as well, we can simply copy and paste those middle groups on the second floor main group. The last element in our structure will be the actual group addresses, which reflect the specific functions. So let's add some of the lights we need for the first floor. Again, this works along the lines of creating the main and middle groups. After that, we're all set to connect the devices for our lighting control in the living room.

    **[01:43.14 - 02:09.79]** All we need to do is drag the group objects of the push button as well as those of the switch actuator onto the group address of the lighting control in the living room. Let's start with the push buttons. What we would like to achieve is that the upper left button turn light 1 on and off, while the lower left button will take care of light 2. So we just need to drag the group object of the upper left button on the group address of light 1.

    **[02:10.02 - 02:39.20]** and the group object of the lower left button on the group address of light 2. Last but not least, the switch actuator needs to be linked to the two lights as well. So let's say, output A switches light 1. All we need to do is to drag its group object on light 1. Light 2 will be switched by output B of the actuator, so we will link these two elements as well. If we have a closer look at the group address of our two lights in the living room now,

    **[02:39.49 - 02:47.22]** We can see the connected devices there. The devices also indicate the links to the respective group addresses of the connected lights.

!!! tip "Słowniczek do tłumaczenia"

    Słowniczek do tłumaczenia: *group address* = adres grupowy, *main group / middle group* = grupa główna / środkowa, *group object* = obiekt komunikacyjny (obiekt grupowy), *switch actuator* = aktor przełączający, *push button* = przycisk, *output* = wyjście (kanał) aktora, *bus* = magistrala.
