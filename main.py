import random

welcome_message = "WELCOME TO CUYPY GAMES"
cuypy_position = random.randint(1,5)

print("****************************")
print(f"** {welcome_message} **")
print("****************************")

nama_user =input("masukan nama kamu: ")

bentuk_goa = "|_|"
goa_kosong = [bentuk_goa] * 5 # ini tetap harus kosong
goa = goa_kosong.copy() # ini adalah tempat baru cuypy akan berada

goa[cuypy_position - 1] = "|0_0|"



print(f'''
halo {nama_user} Coba perhatikan goa di bawah ini, apakah kamu melihat cuypy?
{ ' '.join(goa_kosong) }    
''')

pilihan_user = input("menurut kaamu di goa nomor berapa cuypy berada? [1/2/3/4/5]: ")

konfirmasi = input(f"apakah kamu yakin memilih goa nomor {pilihan_user} ? [y/n]: ")


if konfirmasi == "n":
    print("silakan memilih goa yang benar")
    exit()
elif konfirmasi == "y":
    if pilihan_user == str(cuypy_position):
        print(f"{' '.join(goa)}, selamat kamu menang {nama_user}!! cuypy berada di goa nomor {cuypy_position}, dan kamu memilih {pilihan_user} sehingga tebakan kamu benar")
    else:
        print(f"{' '.join(goa)}, sayang sekali kamu kalah {nama_user}!! cuypy berada di goa nomor {cuypy_position}, dan kamu memilih {pilihan_user} sehingga tebakan kamu salah")
else:
    print("silakan memilih goa yang benar")
    exit()