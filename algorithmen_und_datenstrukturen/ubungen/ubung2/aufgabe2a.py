a,b = 1, 2
# relation <
if( a + 1 <= b and b - 1 <= a ): print("relation < erledigt")

# relation >
a , b = 2 , 1
if( a - 1 <= b and not a <= b ): print("relation > erledingt")

# relation >=
a, b = 2, 1
if( (a - 1 <= b and not a <= b) or a <= b and b <= a): print("relation >= erledigt")

#relation == 
a , b = 1 , 1
if( a <= b and b <= a): print("relation == erledigt")

#relation !=
a,b = 1,2
if( not (a <= b and b <= a)): print("relation != erledigt")