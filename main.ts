let ej_local_number_1 = 0
let ej_index_1 = 0
function ej_add (numbers_list: number[]) {
    ej_local_number_1 = 0
    while (ej_index_1 <= numbers_list.length - 1) {
        ej_local_number_1 = ej_local_number_1 + numbers_list[ej_index_1]
        ej_index_1 += 1
    }
    return ej_local_number_1
}
