from gempaterkini.gempaUPDATE import gempaTerkini

if __name__ == '__main__':
    gempa_indonesia = gempaTerkini("https://bmkg.go.id")
    print('Deskripsi class gempa indonesia', gempa_indonesia.description)
    gempa_indonesia.run()