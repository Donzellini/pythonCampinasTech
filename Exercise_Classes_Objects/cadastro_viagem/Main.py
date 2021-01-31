from Destination import Destination
import sys

print("--------------------")
print(" AGÊNCIA DE VIAGENS\n")
print("     OUTRO MUNDO")
print("--------------------\n")

name_traveler = input("Seja bem-vindo! Como você se chama?\n")

list_menu = [ "0-) Sair"
             ,"1-) Ver Destinos"
             ,"2-) Viagens Agendadas\n"]

list_travels = []

while True:
        for option in list_menu:
                print(option)

        chosen_option = int(input(f"{name_traveler}, escolha uma das opções:\n"))

        if chosen_option == 0:
                        print("Você saiu do sistema.")
                        sys.exit()

        elif chosen_option == 1:
                print(f"{name_traveler}, para onde você quer viajar?\n")

                list_places = [  "0-) Sair"
                                ,"1-) Japão"
                                ,"2-) Croácia"
                                ,"3-) Espanha"
                                ,"4-) Noruega\n"]

                for place in list_places:
                        print(place)

                chosen_place = int(input("Escolha um dos lugares: "))
                
                if chosen_place == 0:
                        print("Você saiu do sistema.")
                        sys.exit()
                else:
                        print(f"{name_traveler}, você irá para {list_places[chosen_place]}\n")
                        travel = Destination(name=name_traveler,local=chosen_place)
                        list_travels.append(travel)

        elif chosen_option == 2:
                for travel in list_travels:
                        print(f"{name_traveler} - {list_places[chosen_place]}")

