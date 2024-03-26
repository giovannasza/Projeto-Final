from lib.funcao import room_function, equipment_function

function_choice = int(input("""\nQual o setor que você quer entrar ?
      1 - Sala
      2 - Equipamento\n: """))

if function_choice == 1:
    room_function()
elif function_choice == 2:
    equipment_function()
