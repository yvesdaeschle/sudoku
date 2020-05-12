# My idea to solve the backtracking for the Sudoku solver

## Algorythmus
Funktion FindeLösung (Stufe, Vektor)
  1. wiederhole, solange es noch neue Teil-Lösungsschritte gibt:
     a) wähle einen neuen Teil-Lösungsschritt;
     b) falls Wahl gültig ist:
               I) erweitere Vektor um Wahl;
              II) falls Vektor vollständig ist, return true; // Lösung gefunden!
                  sonst:
                       falls (FindeLösung(Stufe+1, Vektor)) return true; // Lösung!
                       sonst mache Wahl rückgängig; // Sackgasse (Backtracking)!
  2. Da es keinen neuen Teil-Lösungsschritt gibt: return false // Keine Lösung!
  
## Check
- Erstes Feld ohne 0
- Nummer von 1 ab nutzen
  - check: passt in reihe, spalte und square?
    - wenn nicht: nächste zahl bis 9
    - auch 9 nicht, fehler vorher
      - back

- Frage: Wie speicher ich ich die Fehler?

Teilösung (feld, failed):
1. Nächstes freies Feld finden
2. Teillösung testen: 
  - nächste gültige wahl suchen + nicht ungültig ist
  - keine gültige zahl?
    - was falsch: false -> schritt vorher als ungültig speichern
  - fertig? juhu: true
  - Finde nächste Teillösung mit nächsten Feld
  
Was ich brauche:
- schleife für rekursiven call
- next field finden
- check
- dict[array] [feld(x,y)][array]
