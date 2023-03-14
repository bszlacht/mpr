
# Sprawozdanie LAB1
## Jak zostały przeprowadzone badania? <br />
Każda komunikacja została powtórzona N = 1000 razy. Czas został pomieżony jako czas wszystkich N pomiarów podzielony przez N. <br />
**Wykresy poszczególnych wyników:**
Poniżej wykresy dla komunikacji buferowanej. Pozwala ona wysyłającemu procesowi na przechowywanie wiadomości w jego pamięci przed wysłaniem jej. Pozwala to na pracowanie w tym samym momencie kiedy wiadomość jest wysyłana. W ten sam sposób proces odbierający może odebrać wiadomość kiedy będzie miał czas. Minusem tego sposobu komunikacji jest dodatkowy narzut pamięci jaki musimy zurzyć na alokację buferów.
![alt_text](https://github.com/bszlacht/mpr/blob/main/plots/bs12.png)<br />
![alt_text](https://github.com/bszlacht/mpr/blob/main/plots/bs21.png)<br />
Poniżej wykresy dla komunikacji standardowej (synchronicznej).
![alt_text](https://github.com/bszlacht/mpr/blob/main/plots/ss12.png)<br />
![alt_text](https://github.com/bszlacht/mpr/blob/main/plots/ss21.png)<br />
**Porównanie różnych metod komunikacji w tych samych środowiskach:**<br />
```diff
@@ Kolor niebieski: Standard Send @@
- Kolor czerwony: Buffered Send
```
![alt_text](https://github.com/bszlacht/mpr/blob/main/plots/comparisononenode.png)<br />
![alt_text](https://github.com/bszlacht/mpr/blob/main/plots/twonodescomparison.png)<br />



