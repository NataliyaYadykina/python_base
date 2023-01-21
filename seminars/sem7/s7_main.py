from s7_controllers import process_func

def run(data):
    final_data = process_func(data)
    print(final_data)

if __name__ == '__main__':
    run('1100/25-22*3/2+120*8')
    # run([1100, "/", 25, "-", 22, "*", 3, "/", 2, "+", 120, "*", 8])