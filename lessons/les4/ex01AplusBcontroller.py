# модуль, объединяющий модули интерфейса view и операций model

import ex01AplusBmodel_sub as ex01AplusBmodel
import ex01AplusBview

def button_click():
    value_a = ex01AplusBview.get_value()
    value_b = ex01AplusBview.get_value()
    ex01AplusBmodel.init(value_a, value_b)
    result = ex01AplusBmodel.do_it()
    ex01AplusBview.view_data(result, 'res')
