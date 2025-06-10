# abstract-puzzel-generator

> Der Puzzler beginnt in der oberen linken Ecke – dort, wo Ordnung entsteht. Mit ruhiger Hand zieht er den Rahmen, wie ein Maler den Rand seiner Leinwand. Im Uhrzeigersinn schließt sich die Welt. Dann füllt sich das Bild – Schicht um Schicht, dem Kreis folgend, der sich zur Mitte windet. Am Ende bleibt nur ein letztes Teil – das Herz des Ganzen, das leise in seine Mitte sinkt.

* Das Program simuliert das sich wiederholende Anlegen eines Puzzelteils. Hierbei nimmt das Program erst wahllos ein Puzzleteil aus einem unendlichen Vorrat und gibt es blau gefaerbt an der console aus.
Dann werden die seiten des puzzelteils die an schon zuvor angelegte teile stossen, gelb eingefaerbt und eine zeit lang ueberlegt (duration in seconds) was zu tun ist. Die passenden Seiten des angelegten Teils werden dann gruen gefaerbt, und nicht passenden werden passend gemacht und rot gefaerbt. Am ende steht jeder noch blaugefaerbten seite eine rot- oder gruengefarbte Seite gegenuber die den regel des puzzles entsprechen.*             

`
python main.py [once: bool] [width: int] [height: int] [duration in seconds: float]
`
`
python main.py true 82 22 1
`

