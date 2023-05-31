print('NAMA : WA ODE IKA FEBRYANTI \nNIM : E1E120022 \n')


def hitung_bilangan_positif(list_bilangan):
    if not isinstance(list_bilangan, list):
        raise ValueError("Inputan bukanlah list")
    jml_positif = 0
    bilangan_positif = []

    for bilangan in list_bilangan:
        if isinstance(bilangan, int) and bilangan > 0:
            jml_positif += 1
            bilangan_positif.append(bilangan)
    return jml_positif,bilangan_positif



# Meminta pengguna untuk memasukkan list bilangan

while True:
    input_list = input("Masukkan list bilangan, pisahkan dengan koma: ")
    list_angka = [int(x) for x in input_list.split(",")]

    try:
        hasil_jml, bilangan_positif = hitung_bilangan_positif(list_angka)
        if hasil_jml > 0:
            print("\n")
            print(f"Jumlah Bilangan Positif: {hasil_jml:2d}")
            print("Bilangan Positif dalam List: ", end="")
            print(*bilangan_positif, sep=", ")
            print()
        else:
            print("Tidak ada bilangan positif dalam list ini.")
    except ValueError as e:
        print("Error:", str(e))

    ulang = input("Apakah Anda ingin memasukkan inputan ulang? (Yes/No): ")
    if ulang.lower() != 'yes':
        break


jml_positif = hitung_bilangan_positif(list_angka)
print("Jumlah bilangan positif:", jml_positif)
