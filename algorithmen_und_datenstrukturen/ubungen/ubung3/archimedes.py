



def archimedes1(k):
    s = 2 ** 0.5
    t = 2
    Ecken = 4
    U_Schranke = 0
    O_Schranke = 0
    
    for i in range(k):
        s_ = (2 - (4 - s ** 2 ) ** 0.5) ** 0.5
        t_ = 2/t * (((4 + t ** 2) ** 0.5  - 2))
        Ecken = Ecken * 2
        s = s_
        t = t_
        U_Schranke = Ecken/2 * s
        O_Schranke = Ecken/2 * t
        print("Untere Schranke: ", U_Schranke,", Obere Schranke: ", O_Schranke, ", Differenz: ", O_Schranke - U_Schranke, ", Anzahl der Ecken: ", Ecken)
        return U_Schranke, O_Schranke
        


#b)
# Beim 131072-Eck wird die Differenz negativ, die obere Schranke ist kleiner geworden als die untere; da hier die 2 - (4 - s ** 2) ** 0.5 anfängt, unter der Auslöschung zu leiden, da 4 ** 0.5 - (s** 2) ** 0.5 so
# klein wird, dass die Zahlen ungenau werden und auf Dauer wieder abweichen. Bei 536870912 werden alle Werte 0.0, sodass keine Differenz mehr sichtbar ist. Hier ist # der Unterschied derart gering geworden, dass ihn der Computer nicht mehr erkennen kann. Der Interpreter spuckt auch einen Division by Zero-Fehler aus.

#c)
#S(2n)=s(n)/sqrt(2 + sqrt(4-s(n)^2)) = sqrt(2 - sqrt(4-s(n)^2)); pro Verdoppelung erhält man ca. 0,5 Dezimalstellen





def archimedes2(k):
    s = 2 ** 0.5
    t = 2
    Ecken2 = 4
    U_Schranke = 0
    O_Schranke = 0
    
    for i in range(k):
        s_ = s/((2 + (4 - s ** 2) ** 0.5 ) ** 0.5)
        t_ = 2 * t / ((4 + t ** 2) ** 0.5 + 2)
        Ecken2 = Ecken2 * 2
        s = s_
        t = t_
        U_Schranke2 = Ecken2/2 * s
        O_Schranke2 = Ecken2/2 * t
        print("Untere Schranke: ", U_Schranke2,", Obere Schranke: ", O_Schranke2, ", Differenz: ", O_Schranke2 - U_Schranke2, ", Anzahl der Ecken: ", Ecken2)
    return U_Schranke2, O_Schranke2

def testArchimedes1(n):
    t_checked = 0
    for i in range(n):
        archimedes1(n)
        t_checked = 2 * U_Schranke / ((4 - U_Schranke ** 2) ** 0.5)
        if t_checked != O_Schranke:
            print ("Fehler")
        
def testArchimedes2(n):
    t_checked = 0
    for i in range(n):
        archimedes2(n)
        t_checked = 2 * U_Schranke2/ ((4 - U_Schranke2 ** 2) ** 0.5)
        if t_checked != O_Schranke2:
            break
    
        
if __name__ == "__main__":   
    import math
    
    archimedes1(k)
    archimedes2(k)
    testArchimedes1(n)
    testArchimedes2(n)
    
