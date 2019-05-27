import unittest

def archimedes1(k):
    '''first version'''
    s = 2 ** 0.5
    t = 2
    Ecken = 4
    U_Schranke = 0
    O_Schranke = 0
    #Initialisierung
    
    for i in range(k):
        s_ = (2 - (4 - s ** 2 ) ** 0.5) ** 0.5
        t_ = 2/t * (((4 + t ** 2) ** 0.5  - 2))
        Ecken = Ecken * 2
        s = s_
        t = t_
        U_Schranke = Ecken/2 * s
        O_Schranke = Ecken/2 * t
        print("Untere Schranke: ", U_Schranke,", Obere Schranke: ", O_Schranke, ", Differenz: ", O_Schranke - U_Schranke, ", Anzahl der Ecken: ", Ecken)
        
        


#b)
# Beim 131072-Eck wird die Differenz negativ, die obere Schranke ist kleiner geworden als die untere; da hier die 2 - (4 - s ** 2) ** 0.5 anfängt, unter der Auslöschung zu leiden, da 4 ** 0.5 - (s** 2) ** 0.5 so
# klein wird, dass die Zahlen ungenau werden und auf Dauer wieder abweichen. Bei 536870912 werden alle Werte 0.0, sodass keine Differenz mehr sichtbar ist. Hier ist # der Unterschied derart gering geworden, dass ihn der Computer nicht mehr erkennen kann. Der Interpreter spuckt auch einen Division by Zero-Fehler aus.

#c)
#; pro Verdoppelung erhält man ca. 0,5 Dezimalstellen





def archimedes2(k):
    '''Better Version from Exercise'''
    s = 2 ** 0.5
    t = 2
    Ecken2 = 4
    U_Schranke2 = 0
    O_Schranke2 = 0
    #Initialisierung
    
    for i in range(k):
        s_ = s/((2 + (4 - s ** 2) ** 0.5 ) ** 0.5)
        t_ = 2 * t / ((4 + t ** 2) ** 0.5 + 2)
        Ecken2 = Ecken2 * 2
        s = s_
        t = t_
        U_Schranke2 = Ecken2/2 * s
        O_Schranke2 = Ecken2/2 * t
        print("Untere Schranke: ", U_Schranke2,", Obere Schranke: ", O_Schranke2, ", Differenz: ", O_Schranke2 - U_Schranke2, ", Anzahl der Ecken: ", Ecken2)

class TestArchimedes(unittest.TestCase):
    def setUp(self):
        '''creating test data'''
        j = 0
        ObereSchrankenArch1 = []
        ObereSchrankenArch2 = []
        ObereSchrankenTest = []
        for i in range(4, 30):
            ObereSchrankenArch1[j] = archimedes1(i).O_Schranke
            ObereSchrankenArch2[j] = archimedes1(i).O_Schranke2
            ObereSchrankenTest[j] = 2 * i /((4 - i ** 2) ** 0.5)
            j += 1
        # Schranken in "Arrays" geschrieben
        
    def test_archimedes(self):
        '''test both functions'''
        for i in range(30):
            self.assertEqual(ObereSchrankenArch1[i], ObereSchrankenTest[i], 'Fehler')
            self.assertEqual(ObereSchrankenArch2[i], ObereSchrankenTest[i], 'Fehler')
            # Pruefe, ob Array-Eintraege korrekt sind
       
       #Ich bin mir leider nicht ganz sicher, warum der Test nicht läuft, hat das eventuell etwas mit den "Arrays" zu tun?
 








################################################################################################    
        
if __name__ == "__main__":   
   
   import unittest
    
    archimedes1(k)
    archimedes2(k)
    testArchimedes1(n)
    testArchimedes2(n)
    unittest.main()
