import subprocess
output = subprocess.check_output('netsh wlan show profile | findstr Todos', shell=True).splitlines()
ssid_s = []
senhas = []
csv = []
for s in output:
    ssid_s.append(str(s[29:],"utf-8"))
output = []
for s in ssid_s:
    output.append(subprocess.check_output('netsh wlan show profile name="'+s+'" key=clear | findstr Conteúdo', shell=True).splitlines())
for s in output:
    senhas.append(str(s)[40:-2])
for ss, senha in zip(ssid_s,senhas):
    csv.append(ss + ";" + senha)
subprocess.check_output('echo '+ str(csv)+" >> %HOMEPATH%\Desktop\senhaspy.txt", shell=True)
