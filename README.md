# Abstrakter Puzzle-Generator

Dieses Programm generiert und zeigt abstrakte Puzzles im Terminal an.

## Verwendung

Um das Programm auszuführen, verwenden Sie den folgenden Befehl in Ihrem Terminal:
```bash
python main.py [ARGUMENTE]
```

Das Programm akzeptiert mehrere Kommandozeilenargumente, um die Puzzle-Generierung anzupassen.

## Argumente

Das Verhalten des Skripts wird hauptsächlich durch fünf Schlüsselparameter gesteuert, die mithilfe des (nicht bereitgestellten) Moduls `argv_helper.py` aus den Kommandozeilenargumenten geparst werden. Die genaue Syntax zur Übergabe dieser Argumente (z.B. über Flags wie `--name wert` oder als positionale Argumente wie `wert1 wert2`) sowie deren Standardwerte sind in `argv_helper.py` definiert. Im Folgenden wird beschrieben, was jeder dieser fünf Parameter steuert:

1.  **`count`** (Anzahl):
    *   **Beschreibung**: Gibt die Anzahl der zu generierenden Puzzles an.
    *   **Verhalten**:
        *   Wenn `count` eine positive ganze Zahl ist (z.B. `5`), generiert das Programm genau diese Anzahl an Puzzles und wird dann beendet. Die über Argumente spezifizierten `max_width` (als Breite), `max_height` (als Höhe) und `opposite_key` werden für all diese Puzzles verwendet.
        *   Wenn `count` `0` oder eine negative Zahl ist, geht das Programm in eine Endlosschleife über und generiert unbegrenzt neue Puzzles. In diesem Modus:
            *   Die Breite (`w`) und Höhe (`h`) für jedes Puzzle werden zufällig innerhalb der Grenzen von `max_width` und `max_height` gewählt.
            *   Der `opposite_key` für jedes Puzzle wird ebenfalls zufällig aus den verfügbaren `OPPOSITE_KEYS` (definiert in `opposite_piece_keys.py`) gewählt.

2.  **`max_width`** (Maximale Breite / Breite):
    *   **Beschreibung**: Beeinflusst die Breite der generierten Puzzles.
    *   **Verhalten**:
        *   Wenn `count > 0` (feste Anzahl von Puzzles): Dieser Wert wird als die **tatsächliche Breite** für alle generierten Puzzles verwendet.
        *   Wenn `count <= 0` (Endlosmodus): Dieser Wert dient als **maximale Breite**. Die Breite für jedes Puzzle (`w`) wird dann zufällig zwischen 1 und `max_width` (einschließlich) gewählt.

3.  **`max_height`** (Maximale Höhe / Höhe):
    *   **Beschreibung**: Beeinflusst die Höhe der generierten Puzzles.
    *   **Verhalten**:
        *   Wenn `count > 0` (feste Anzahl von Puzzles): Dieser Wert wird als die **tatsächliche Höhe** für alle generierten Puzzles verwendet.
        *   Wenn `count <= 0` (Endlosmodus): Dieser Wert dient als **maximale Höhe**. Die Höhe für jedes Puzzle (`h`) wird dann zufällig zwischen 1 und `min(aktuelle_zufällige_Breite, max_height)` (einschließlich) gewählt.

4.  **`sleep_time`** (Schlafzeit):
    *   **Beschreibung**: Dieser Wert wird an den `PieceKeyPiecePrinter` übergeben und beeinflusst wahrscheinlich die Verzögerung beim Drucken einzelner Teile oder Puzzle-Segmente, was die Animationsgeschwindigkeit der Darstellung steuert.
    *   **Verhalten**: Eine Fließkommazahl (z.B. `0.5` für eine halbe Sekunde).
    *   **Hinweis**: Das Programm enthält auch eine feste Pause von `time.sleep(4)` (4 Sekunden) nachdem jedes vollständige Puzzle angezeigt wurde, bevor der Bildschirm für das nächste Puzzle gelöscht wird.

5.  **`opposite_key`** (Schlüssel für Gegenteile):
    *   **Beschreibung**: Bestimmt die Logik oder den Typ der "entgegengesetzten" Teile (definiert durch `OPPOSITE_PIECE_KEY_DIGITS` und `OPPOSITE_KEYS` aus `opposite_piece_keys.py`), die bei der Puzzle-Generierung verwendet werden.
    *   **Verhalten**:
        *   Dieses Argument sollte einem gültigen Schlüssel entsprechen, der im Modul `opposite_piece_keys.py` definiert ist.
        *   Wenn `count > 0` (feste Anzahl von Puzzles): Der angegebene `opposite_key` wird für alle generierten Puzzles verwendet.
        *   Wenn `count <= 0` (Endlosmodus): Der als Kommandozeilenargument angegebene `opposite_key` wird für die Puzzle-Generierung innerhalb der Endlosschleife **nicht verwendet**. Stattdessen wird für jedes in diesem Modus generierte Puzzle ein zufälliger `opposite_key` aus den verfügbaren `OPPOSITE_KEYS` gewählt.

## Beispiele

Die folgenden Beispiele veranschaulichen, wie Sie diese Parameter konzeptionell verwenden könnten. Die tatsächliche Kommandozeilensyntax (z.B. ob Flags wie `--count` oder `-c` verwendet werden, oder ob es sich um positionale Argumente handelt) hängt davon ab, wie `argv_helper.py` implementiert ist.

*   **Generiere 3 Puzzles, jedes mit einer festen Breite von 10 und Höhe von 8, unter Verwendung von 'KEY_X' (angenommener gültiger Schlüssel) für die Teilelogik und einer schnellen Animationsgeschwindigkeit (0.05s):**
    ```bash
    # Hypothetische Syntax unter Annahme von Flags:
    python main.py --count 3 --width 10 --height 8 --sleep 0.05 --key KEY_X
    ```

*   **Starte im Endlosmodus, generiere Puzzles mit zufälligen Dimensionen (bis zu 20 breit, bis zu 15 hoch) und zufälliger Teilelogik, mit einer langsameren Animationsgeschwindigkeit (0.5s):**
    ```bash
    # Hypothetische Syntax unter Annahme von Flags:
    python main.py --count 0 --max-width 20 --max-height 15 --sleep 0.5
    # Hinweis: Ein hier übergebenes --key Argument würde im Endlosmodus für die eigentliche Puzzle-Generierung ignoriert werden,
    # da bei jeder Iteration ein zufälliger Schlüssel gewählt wird.
    ```

Nach jeder Puzzle-Generierung gibt das Programm die verwendete Breite, Höhe und den numerischen Repräsentanten des `opposite_key` aus, z.B. `10 : 8 : 1`.