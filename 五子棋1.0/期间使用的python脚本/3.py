import os
a = os.getcwd()


b = 0
while b <= 196:
    b += 1
    b = str(b)
    

    print (' Private Sub Button' + b +'_Click(sender As Object, e As EventArgs) Handles Button' + b + ' .Click' + "\n" +  "\n" + "If a = 1 Then\n" + "a=2\n I" + b + " = 1\n _int_()\n_win_()\n button" + b + ".Text =  X1" + "\n" + " button" + b + ".Enabled = False \nElse \n     a = 1 \n IB" + b +" = 1\n _int_()\n_win_()\n button" + b +".Text = O \n" + " button" + b + ".Enabled = False"+"\n" + "\n End If" + "\n" + "\n" + "End Sub\n")
    d = ' Private Sub Button' + b +'_Click(sender As Object, e As EventArgs) Handles Button' + b + ' .Click' + "\n" +  "\n" + "If a = 1 Then\n" + "a=2\n I" + b + " = 1\n _int_()\n_win_()\n button" + b + ".Text =  X1" + "\n" + " button" + b + ".Enabled = False \nElse \n     a = 1 \n IB" + b +" = 1\n _int_()\n_win_()\n button" + b +".Text = O \n" + " button" + b + ".Enabled = False"+"\n" + "\n End If" + "\n" + "\n" + "End Sub\n"
    
    
    c = open(a + "/vb.txt","a+")
    c.write(d)
    b = int(b)
    

