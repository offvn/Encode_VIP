import os
import marshal
import logging
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
red = '\033[91m'
os.system("clear")
banner = yellow+"""
\033[1;95m╭─⋞─────────────────────────────────────────────────────╮
\033[1;31m██╗  ██╗██████╗ ████████╗  ████████╗ ██████╗  ██████╗ ██╗     
\033[1;32m██║  ██║██╔══██╗╚══██╔══╝  ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
\033[1;33m███████║██║  ██║   ██║        ██║   ██║   ██║██║   ██║██║     
\033[1;34m██╔══██║██║  ██║   ██║        ██║   ██║   ██║██║   ██║██║     
\033[1;30m██║  ██║██████╔╝   ██║        ██║   ╚██████╔╝╚██████╔╝███████╗
\033[1;37m╚═╝  ╚═╝╚═════╝    ╚═╝        ╚═╝    ╚═════╝  ╚═════╝ 
\033[1;37m Youtube : \033[1;32mhttps://youtube.com/@HDT-TOOL
\033[1;37m Nhóm Zalo : \033[1;32mhttps://zalo.me/g/bprmyn080
\033[1;37m Link Tool: \033[1;32m https://user-traffic.net/eNc0R
\033[1;95m╰─────────────────────────────────────────────────────⋟─╯ 
\033[1;37m────────────────────────────────────────────────────────────\n"""+clear
print(banner)
def mode1(files, string):
    s = open(files).read()
    z = []
    for i in s:
        z.append(ord(i))
    pea = []
    for i in z:
        pea.append(string.replace("'", "").replace('"', '')*i)
    file = """
# Thách Thằng Lồn Nào Dec Được
# Ông Trùm HDT-TOOL Thách Con Chó Nào Dec Đó

d={};exec("".join([chr(len(i)) for i in d]))
    """.format(pea)
    open(files.replace(".py", "encrypted.py"), "w").write(file)
    logging.info(" saved as "+files.replace(".py", "encrypted.py"))
    print("File Được Lưu Thành Công '{}'".format(
        files.replace(".py", "encrypted.py")))


def mode2(file):
    x = open(file).read()
    m = compile(x, '', 'exec')
    k = marshal.dumps(m)
    l = open('encoded-'+file, 'w')
    l.write('import marshal\n')
    l.write('exec(marshal.loads('+repr(k)+"))")
    l.close()
    print('File Được Lưu Thành Công \'encoded-{}\''.format(file))
while True:
    print(lgreen+"""
               Số 2 : Encode Marshall
+---------------------------------------------------------+
 """+clear)
    number = int(input("Nhập Số -->"))

    if number == 1:
        file = input("Nhập File Muốn Encode: ")
        string = input("Nhập Tên File Muốn Lưu : ")
        mode1(file, string)

    elif number == 2:
        file = input("Nhập File Muốn Encode : ")
        mode2(file)

    elif number == 3:
        break

    else:
        print(red + "[ERROR!]" + clear + " Invalid input, please try again.")

