# Zadania

### Zadanie 1
Wykorzystaj rozwiązanie zadania ze zbiorem iris żeby stworzyć plik, w którym ostatnia kolumna będzie zawierała kategorie (1-3) zamiast nazw gatunków irysów.

### Zadanie 2
Zaimplementuj zapisywanie statystyk do pliku.

### Zadanie 3
Zadbaj o obsługę wyjątków tak, aby w przypadku braku pliku lub wykonania nielegalnej operacji, program wyłączył się elegancko z komunikatem o błędzie, lub kontynuował w pewien wymyślony przez Ciebie sposób.

```python
try:
    f = open("file.txt")
    # operacje
except <nazwa wyjątku>:
    #w przypadku wyjątku
finally:
    f.close()
```

Mechanizm wyjątków możesz również wykorzystać do obsłużenia linijek o złym formacie.