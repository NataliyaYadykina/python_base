from hw7_views import get_move_type, get_contact, view_phone_book, get_search_info, get_confirm
from hw7_models import get_data_phone_book, str_contact, add_contact, edit_contact, search_contact, read_phone_book
from hw7_logger import logger

# Выбор действия
def select_move_type(move_type):
    text_book = read_phone_book('hw7_contact_format2.txt')
    lst_contacts = get_data_phone_book(text_book, ',', '\n')
    if move_type == 1:
        view_phone_book(lst_contacts, move_type)
        logger(None, func_name='view_phone_book, move 1')
    elif move_type == 2:
        contact = get_contact(move_type)
        str_contact1 = str_contact(contact, '\n', '\n\n')
        str_contact2 = str_contact(contact, ',', '\n')
        add_contact(str_contact1, 'hw7_contact_format1.txt')
        logger(str_contact1, func_name='add_contact')
        add_contact(str_contact2, 'hw7_contact_format2.txt')
        logger(str_contact2, func_name='add_contact')
    elif move_type == 3:
        search_info = get_search_info(move_type)
        logger(search_info, func_name='get_search_info, move 3')
        result_search = search_contact(search_info, lst_contacts)
        logger(result_search, func_name='search_contact, move 3')
        view_phone_book(result_search, move_type)
        logger(result_search, func_name='view_phone_book, move 3')
    elif move_type == 4 or move_type == 5:
        search_info = get_search_info(move_type)
        logger(search_info, func_name='get_search_info, move 4, 5')
        if search_info.isdigit():
            result_search = search_contact(search_info, lst_contacts)
            logger(result_search, func_name='search_contact, move 4, 5')
            if result_search:
                view_phone_book(result_search, move_type)
                logger(result_search, func_name='view_phone_book, move 4, 5')
                old_contact_str1 = str_contact(result_search[0], '\n', '\n\n')
                logger(old_contact_str1, func_name='str_contact, move 4, 5')
                old_contact_str2 = str_contact(result_search[0], ',', '\n')
                logger(old_contact_str2, func_name='str_contact, move 4, 5')
                if move_type == 4:
                    new_contact = get_contact(move_type)
                    new_contact_str1 = str_contact(new_contact, '\n', '\n\n')
                    logger(new_contact_str1, func_name='str_contact, move 4, 5')
                    new_contact_str2 = str_contact(new_contact, ',', '\n')
                    logger(new_contact_str2, func_name='str_contact, move 4, 5')
                    edit_contact(old_contact_str1, new_contact_str1, 'hw7_contact_format1.txt')
                    logger(new_contact_str1, func_name='edit_contact, move 4, 5')
                    edit_contact(old_contact_str2, new_contact_str2, 'hw7_contact_format2.txt')
                    logger(new_contact_str2, func_name='edit_contact, move 4, 5')
                else:
                    confirm = get_confirm()
                    if confirm == 1:
                        new_contact_str = ''
                        logger('empty', func_name='Empty str for delete contact')
                        edit_contact(old_contact_str1, new_contact_str, 'hw7_contact_format1.txt')
                        logger(old_contact_str1, func_name='edit_contact, delete file 1')
                        edit_contact(old_contact_str2, new_contact_str, 'hw7_contact_format2.txt')
                        logger(old_contact_str2, func_name='edit_contact, delete file 2')
    if move_type != 6:
        process_func()

# Выполнение программы
def process_func():
    move_type = get_move_type()
    select_move_type(move_type)
