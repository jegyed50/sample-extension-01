ej_local_number_1 = 0
call_parameter_number_list: List[number] = []
def ej_add(numbers_list: List[number]):
    global ej_local_number_1
    ej_local_number_1 = 0
    ej_index_1 = 0
    while ej_index_1 <= len(numbers_list) - 1:
        basic.show_number(numbers_list[ej_index_1])
        basic.pause(500)
        ej_local_number_1 = ej_local_number_1 + numbers_list[ej_index_1]
        ej_index_1 += 1
    return ej_local_number_1

def on_button_pressed_a():
    global call_parameter_number_list
    call_parameter_number_list = [1, 2, 3]
    ej_add(call_parameter_number_list)
    basic.show_number(ej_local_number_1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    pass
basic.forever(on_forever)
