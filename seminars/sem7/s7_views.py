def step_view(data, step_data, delimeter = '*'):
    print(delimeter * 26)
    print(f'{data} ->> {step_data}')
    print(delimeter * 26 + '\n')

def process_view(data, result):
    print(f'{data} = {result}')