import os
b=os.getcwd()
c = 0

while c <= 140:

    

    c +=1

    

    c = str(c)
    a = 'If I' + c +' = 1 And I' + str(int(c)+14)   + ' = 1 And I' + str(int(c)+28) + '  = 1 And I' + str(int(c)+42) + '  = 1 And I'  + str(int(c)+56) + ' = 1  ' +   'Then \n    IWin = 1\n ElseIf Ib' + c + ' = 1 And Ib' + str(int(c)+14) +'  = 1 And Ib' + str(int(c)+28)+'  = 1 And Ib' + str(int(c)+42) + '  = 1 And Ib'+ str(int(c)+56) + '  = 1 Then \n    IBWIn = 1\nEnd If\n'

    nm = open(b + "/vb1.txt","a+")
    nm.write (a)
    c = int(c)


    
    
    
        
        


