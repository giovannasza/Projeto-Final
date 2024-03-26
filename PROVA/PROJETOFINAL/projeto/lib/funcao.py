from database import rooms, equipments

def show_rooms():
    print(rooms)
    room_function()

def create_room():
    room_name = input("/n Qual o nome da sala? ")
    if equipments:
        max_room_id = max(entry["id"] for entry in rooms)
    else:
        max_room_id = 0
    room_number = int(input("/n Qual o número da sala? ")) 

    new_room = {
            "id": max_room_id + 1,
            "number": room_number,
            "name": room_name
        }   
    rooms.append(new_room)

    room_function()

def update_room():
    update_room_id = int(input("\nQual o índice da sala que você deseja atualizar? "))

    room_to_update = None
    for room in rooms: 
        if room["id"] == update_room_id:
            room_to_update = room
            break
    
    if room_to_update is None:
        print("Valor não encontrado!")
    else:
        new_name = input("\nQual o novo nome? ")
        new_number = int(input("\nQual o novo número? "))
        
        room_to_update["name"] = new_name
        room_to_update["number"] = new_number

    room_function()

def delete_room():
    delete_room_id = int(input("\nID que você deseja deletar: "))
    
    for room in rooms: 
        if room["id"] == delete_room_id:
            rooms.remove(room)
            print("Sala removida com sucesso.")
            break
    else:
        print("Sala não encontrada.")
    room_function()

# equipments

def show_equipments():
    print(equipments)
    equipment_function()

def create_equipment():
    equipment_type = input("/n Qual o tipo do novo equipamento? ")
    if equipments:
        max_id = max(entry["id"] for entry in equipments)
    else:
        max_id = 0
    if equipments:
        max_inventory = max(entry["inventory"] for entry in equipments)
    else:
        max_inventory = 0
    room_id = int(input("/n Qual o ID da sala? ")) 

    new_equipment = {
            "id": max_id + 1,
            "inventory": max_inventory + 1,
            "type": equipment_type,
            "room_id": room_id
        }   
    equipments.append(new_equipment)

    equipment_function()

def update_equipment():
    update_id = int(input("\nQual o índice do equipamento que você deseja atualizar? "))

    equip_to_update = None
    for equipment in equipments: 
        if equipment["id"] == update_id:
            equip_to_update = equipment
            break
    
    if equip_to_update is None:
        print("Valor não encontrado!")
    else:
        new_type = input("\nQual o novo tipo? ")
        new_room_id = int(input("\nQual o novo ID da sala? "))
        
        equip_to_update["room_id"] = new_room_id
        equip_to_update["type"] = new_type

    equipment_function()

def delete_equipment():
    delete_id = int(input("\nID que você deseja deletar: "))
    
    for equipment in equipments: 
        if equipment["id"] == delete_id:
            equipments.remove(equipment)
            print("Equipamento removido com sucesso.")
            break
    else:
        print("Equipamento não encontrado.")
    equipment_function()

def search_equipment():
    id_to_search = int(input("\nQual o índice que você deseja buscar? "))

    for equipment in equipments: 
        if equipment["id"] == id_to_search:
            print(equipment)
            
            break

    equipment_function()

def change_room_equip():
    id_to_change = int(input("\nQual o índice que você deseja trocar? "))

    for equipment in equipments: 
        if equipment["id"] == id_to_change:
            new_room_id = int(input("Qual a sala que você deseja mudar? "))
            equipment["room_id"] = new_room_id
            
            break
    equipment_function()

def room_function():
    print("""
    Visualizar lista [1]
    Adicionar [2]
    Atualizar [3]
    Deletar [4]
    Sair [5]
    """)
    index = int(input(': '))
    if index == 1:
        show_rooms()

    elif index == 2:
        create_room()

    elif index == 3:
        update_room()

    elif index == 4:
        delete_room()
    elif index == 5:
        print("\nSaindo...")
    else:
        print("\nO valor inserido é inválido.")

def equipment_function():
    print("""
    Visualizar lista [1]
    Adicionar [2]
    Atualizar [3]
    Deletar [4]
    Buscar [5]
    Trocar de sala [6]
    Sair [7]
    """)
    index = int(input(': '))
    if index == 1:
        show_equipments()

    elif index == 2:
        create_equipment()

    elif index == 3:
        update_equipment()

    elif index == 4:
        delete_equipment()

    elif index == 5:
        search_equipment()

    elif index == 6:
        change_room_equip()

    elif index == 7:
        print("\nSaindo...")
    else:
        print("\nO valor inserido é inválido.")
