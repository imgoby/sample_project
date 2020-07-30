import re


with open('Main.Designer.cs','r',encoding='utf8')as f:
    txt = f.read()


btn = re.findall('this\.(.*?)\.Tag = "HMI\.A\d_.*?\d;BOOL";',txt)
tag = {bt:re.findall(bt+'\.Tag = "HMI\.(.*?);BOOL',txt)[0] for bt in btn}


for t in tag:
    for s in ',.)_ ;"':
        txt = txt.replace(t+s,'btn_'+tag[t]+s)

with open('Main.Designer.cs','w',encoding='utf8')as f:
    f.write(txt)

with open('Main.cs','r',encoding='utf8')as f:
    txt = f.read()

for t in tag:
    for s in ',.)_ ;"':
        txt = txt.replace(t+s,'btn_'+tag[t]+s)

with open('Main.cs','w',encoding='utf8')as f:
    f.write(txt)
    
  
with open('Main.Designer.cs','r',encoding='utf8')as f:
    txt = f.read()  
tbx = re.findall('this\.textBox(.*?).Tag = ".+"', txt)
tbxtag = {'textBox'+t:re.findall('textBox'+t+'\.Tag = "(.*?);',txt)[0].split('.')[1] for t in tbx}
for t in tbxtag:
    for s in ',.)_ ;"':
        txt = txt.replace(t+s,'tbx_'+tbxtag[t]+s)
with open('Main.Designer.cs','w',encoding='utf8')as f:
    f.write(txt)
    
with open('Main.cs','r',encoding='utf8')as f:
    txt = f.read()
for t in tbxtag:
    for s in ',.)_ ;"':
        txt = txt.replace(t+s,'tbx_'+tbxtag[t]+s)
with open('Main.cs','w',encoding='utf8')as f:
    f.write(txt)
save = '''axis2_0_pos :REAL; 
axis2_1_pos :REAL; 
axis2_2_pos :REAL; 
axis2_3_pos :REAL; 
axis2_4_pos :REAL; 
axis2_5_pos :REAL; 
axis2_6_pos :REAL; 
axis2_7_pos :REAL; 
axis2_8_pos :REAL; 
axis2_9_pos :REAL; 

axis1_up_pos :REAL;  
axis1_down_pos :REAL;  
axis1_down_pos2 :REAL;  
axis3_open_pos :REAL;
axis3_close_pos :REAL; 

axis1_safe1_pos :REAL;  
axis1_safe2_pos :REAL;  

axis1_abs_vel2 :REAL; 
axis1_abs_vel :REAL; 
axis1_abs_vel1 :REAL; 
axis2_abs_vel :REAL; 
axis3_abs_vel :REAL; 
axis1_jog_vel :REAL; 
axis2_jog_vel :REAL; 
axis3_jog_vel :REAL; 
First_val AT%MD200 :INT; 
Sce_val AT%MD204 :INT; 
Sampling AT%MD208 :INT; 
Sampling2 AT%MD209 :INT; 
count_all AT%MD504:REAL; 

SJ_Motor_Tor_Max:INT;
XZ_Motor_Tor_Max:INT;
SF_Motor_Tor_Max:INT;
SJ_Motor_Tor_Max_2:INT;
'''
'''
for t in tag:
    txt = txt.replace('"'+t+'"','"'+t.replace('MAIN.','')+'"')

with open('Main.Designer.cs','w',encoding='utf8')as f:
    f.write(txt)
with open('Main.Designer.cs','r',encoding='utf8')as f:
    txt = f.read()
tag = re.findall('Tag = "(.*?)";',txt)
for t in tag:
    if t.split(';')[0] in save:
        txt = txt.replace('"'+t+'"','"SAVE.'+t.replace('MAIN.','')+'"')
    else:
        txt = txt.replace('"'+t+'"','"HMI.'+t.replace('MAIN.','')+'"')

'''
