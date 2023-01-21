from s7_models import (
                    get_steps_lst,
                    get_steps_count,
                    process_step
)
from s7_views import step_view, process_view
from s7_loggers import logger


def process_func(values: str):
    lst_steps = get_steps_lst(values)
    logger(lst_steps, func_name='get_steps_lst')

    count_steps = get_steps_count(lst_steps)
    logger(count_steps, func_name='get_steps_count')
    res_lst = lst_steps[:]

    for _ in range(count_steps):
        res_lst = process_step(res_lst)
        # step_view(values, res_lst)
        logger(res_lst, file_path='s7_steps.csv', func_name='process_step')

    # return eval(values)
    process_view(values, res_lst[0])
    logger(res_lst[0], func_name='process_func')
    return res_lst[0]

def user_input() -> str:
    pass