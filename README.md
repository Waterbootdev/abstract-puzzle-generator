# Abstrakter Puzzle-Generator

Dieses Programm zeigt die generierung eines abstrakten puzzels animiert im terminal.

    - zuerst 

## Verwendung

Um das Programm auszuführen, verwenden Sie den folgenden Befehl in Ihrem Terminal:
```bash
python main.py [once] [width] [heigth] [sleep_time] 
```

Das Programm akzeptiert mehrere Kommandozeilenargumente, um die Puzzle-Generierung anzupassen.

## Argumente

    once : wenn true wird genau ein puzzle generiert ansonsten geht das program in den endlos modus  
    
    width : horizontal number of tiles
    heigth : vertical number of tiles, height <= width
    sleep_time : time in second that the animation print holds at a given position

    im endlos mode waehlt das program die hoehe und breite random in den grenzen von width und height   

```bash
python main.py true  20 19 1  
```