import sys, argparse, zlib, marshal, base64, codecs, binascii, time
from os import system, remove
from sys import argv
from random import choice, shuffle
from py_compile import compile as com_pyc


class BannerRun(object):

	def __init__(self, string):
		for i in string + '\n':
			sys.stdout.write(str(i))
			sys.stdout.flush()
			time.sleep(5e-05)


class MainCompile:

	def __init__(self):
		self.puki = []
		self.enco = 'exec((lambda __, _, : _(%s,__))("%s",__import__(\'codecs\').decode))'
		self.pico = []
		self.Main()

	def Main(self):
		system('clear')
		BannerRun(f"\033[1;95m╭─⋞─────────────────────────────────────────────────────╮\n\033[1;31m██╗  ██╗██████╗ ████████╗  ████████╗ ██████╗  ██████╗ ██╗     \n\033[1;32m██║  ██║██╔══██╗╚══██╔══╝  ╚══██╔══╝██╔═══██╗██╔═══██╗██║     \n\033[1;33m███████║██║  ██║   ██║        ██║   ██║   ██║██║   ██║██║     \n\033[1;34m██╔══██║██║  ██║   ██║        ██║   ██║   ██║██║   ██║██║     \n\033[1;30m██║  ██║██████╔╝   ██║        ██║   ╚██████╔╝╚██████╔╝███████╗\n\033[1;37m╚═╝  ╚═╝╚═════╝    ╚═╝        ╚═╝    ╚═════╝  ╚═════╝ \n\033[1;37m Youtube : \033[1;32mhttps://youtube.com/@HDT-TOOL\n\033[1;37m Nhóm Zalo : \033[1;32mhttps://zalo.me/g/bprmyn080\n\033[1;37m Link Tool: \033[1;32m https://user-traffic.net/eNc0R\n\033[1;95m╰─────────────────────────────────────────────────────⋟─╯\n\033[1;34m     ──────────────\033[1;31mTOOL ENCODE\033[1;34m──────────────\n\n\033[1;31m[1] \033[1;32mEncode \033[1;33mCython py3\n\033[1;31m[2] \033[1;32mEncode \033[1;33mLambda utf-16 py3\n\033[1;31m[3] \033[1;32mEncode \033[1;33mLambda bz2_codec py3\n\033[1;31m[4] \033[1;32mEncode \033[1;33mLambda Rot-13 py3\n\033[1;31m[0] \033[1;32mKeluar")
		try:
			inp = int(input(f"\n─⋟ "))
			if inp == 1:
				data = []
				file = input(f"\n\033[0mNama File > \033[0;92m")
				out = input(f"\033[0mOutput File > \033[0;92m")
				BannerRun(f"")
				xos = open(file).read()
				for i in xos:
					data.append(ord(i))
					f = open('cython-38.so', 'w')
					f.write(f"exec(''.join(chr(_) for _ in {data}))")
					f.close()
				scu = open('cython-38.so').read()
				fub = compile(scu, '(Mengentot)', 'exec')
				xuc = repr(marshal.dumps(fub))
				s = open(out, 'w')
				s.write(f"exec(__import__('marshal').loads({xuc}))")
				s.close()
				del data[:]
				com_pyc(out, out)
				remove('cython-38.so')
				print(f"\n\033[0mBerhasil Di Compile\n\nFile Tersimpan Di > \033[0;92m{out}")
				input(f"\n\033[0mTekan Enter Untuk Kembali")
				self.Main()
			elif inp == 2:
				komter = 0
				file = input(f"\n\033[0mNama File > \033[0;92m")
				total = int(input(f"\033[0mLimit > \033[0;92m"))
				if ( total < 5 ):
					out = input(f"\033[0mOutput File > \033[0;92m")
					xos = open(file).read()
					cum = repr(codecs.encode(xos, 'utf-16_be'))
					f = open(out, 'w')
					f.write(self.enco % (cum, 'utf-16_be'))
					f.close()
					while ( total >= komter ):
						sui = open(out).read()
						ses = repr(codecs.encode(sui, 'utf-16_be'))
						f = open(out, 'w')
						f.write(self.enco % (ses,
									 'utf-16_be'))
						f.close()
						print(f"\r\033[0;92m{komter}")
						komter += 1
					print(f"\n\033[0mFile Berhasil Di Compile\n\nFile Tersimpan Di > \033[0;92m{out}\033[0m")
					input(f"\n\033[0mTekan Enter Untuk Kembali")
					self.Main()
				exit(f"\n\033[0mLimit Harus > \033[0;92m5")
			elif inp == 3:
				komter = 0
				file = input(f"\033[0m\nNama File > \033[0;92m")
				total = int(input(f"\033[0mLimit >  \033[0;92m"))
				if ( total < 5 ):
					out = input(f"\033[0mOutput File > \033[0;92m")
					xos = open(file).read().encode('utf-8')
					cum = repr(codecs.encode(xos, 'bz2_codec'))
					f = open(out, 'w')
					f.write(self.enco % (cum, 'bz2_codec'))
					f.close()
					while ( total >= komter ):
						sui = open(out).read().encode('utf-8')
						ses = repr(codecs.encode(sui, 'bz2_codec'))
						f = open(out, 'w')
						f.write(self.enco % (ses,
										 'bz2_codec'))
						f.close()
						print(f"\033[0m{komter}")
						komter += 1
					print(f"\033[0m\nBerhasil Di Compile File Tersimpan Di > \033[0;92m{out}")
					input(f"\033[0m\nTekan Enter Untuk Kembali")
					self.Main()
				exit(f"\n\033[0mLimit Harus > \033[0;92m5")
			elif inp == 4:
				komter = 0
				file = input(f"\n\033[0mNama File > \033[0;92m")
				total = int(input(f"\033[0mLimit > \033[0;92m"))
				if ( total < 10 ):
					out = input(f"\033[0mOutput File > \033[0;92m")
					xos = open(file).read()
					cum = repr(codecs.encode(xos, 'rot_13'))
					f = open(out, 'w')
					f.write(self.enco % (cum, 'rot_13'))
					f.close()
					while ( total >= komter ):
						sui = open(out).read()
						ses = repr(codecs.encode(sui, 'rot_13'))
						f = open(out, 'w')
						f.write(self.enco % (ses,
										 'rot_13'))
						f.close()
						print(f"\r\033[0m{komter}")
						komter += 1
					print(f"\033[0m\nBerhasil Di Compile File Tersimpan Di > \033[0;92m{out}")
					input(f"\n\033[0mTekan Enter Untuk Kembali")
					self.Main()
				exit(f"\n\033[0mLimit Harus > \033[0;92m10")
			#elif inp == 5:
				#komter = 0
				#file = input(f"\n\033[0mNama File > \033[0;92m")
				#total = int(input(f"\033[0mLimit > \033[0;92m"))
				#if ( total < 10 ):
					#out = input(f"\033[0mOutput File > \033[0;92m")
					#xos = open(file).read()
					#cum = repr(codecs.encode(xos, 'cp1026'))
					#f = open(out, 'w')
					#f.write(self.enco % (cum, 'cp1026'))
					#f.close()
					#while ( total >= komter ):
						#sui = open(out).read()
						#ses = repr(codecs.encode(sui, 'cp1026'))
						#f = open(out, 'w')
						#f.write(self.enco % (ses,
										 # 'cp1026'))
						# f.close()
						# print(f"\r\033[0m{komter}")
						#komter += 1
					#print(f"\033[0m\nBerhasil Di Compile File Tersimpan Di > \033[0;92m{out}")
					#input(f"\n\033[0mTekan Enter Untuk Kembali")
					#self.Main()
			elif inp == 0:
				exit(f"\033[0mSelamat Tinggal")
				
				
			else:
				exit(f"\nSalah")
		except (KeyboardInterrupt,EOFError):
			exit(f"\n\033[0mSelamat Tinggal")
		except ValueError:
			exit(f"\n\033[0mHarus Angka")
		except FileNotFoundError:
			exit(f"\n\033[0mNama File Dari > \033[0;92m{file} \033[0mTidak Ada")
			

if __name__ == '__main__':
    MainCompile()