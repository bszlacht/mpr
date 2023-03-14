
# Sprawozdanie LAB1
## Jak zostały przeprowadzone badania? <br />
Każda komunikacja została powtórzona N = 1000 razy. Czas został pomieżony jako czas wszystkich N pomiarów podzielony przez N. <br />
**Wykresy poszczególnych wyników:**
![alt_text](https://github.com/bszlacht/mpr/blob/main/plots/bs12.png)<br />
![alt_text](https://github.com/bszlacht/mpr/blob/main/plots/bs21.png)<br />
![alt_text](https://github.com/bszlacht/mpr/blob/main/plots/ss12.png)<br />
![alt_text](https://github.com/bszlacht/mpr/blob/main/plots/ss21.png)<br />
**Porównanie różnych metod komunikacji w tych samych środowiskach:**<br />
```diff
@@ Kolor niebieski: Standard Send @@
- Kolor czerwony: Buffered Send
```
![alt_text](https://github.com/bszlacht/mpr/blob/main/plots/comparisononenode.png)<br />
![alt_text](https://github.com/bszlacht/mpr/blob/main/plots/twonodescomparison.png)<br />


