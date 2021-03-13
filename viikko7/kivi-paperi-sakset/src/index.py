from pelitehdas import Pelitehdas

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        peli = {"a": Pelitehdas.pvp(), "b": Pelitehdas.pv_ai(), "c": Pelitehdas.pv_ai_impr()}
        
        if vastaus not in peli:
            break
        
        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
        peli[vastaus].pelaa()

if __name__ == "__main__":
    main()
