import re
import os

archivo=input("archivo axfr: ")
ip=open(archivo,"r")
ip_candidates = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", ip.read())
for ip in ip_candidates:
        os.system("echo "+ip+" >> "+archivo+"listaip")
