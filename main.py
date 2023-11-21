from map import Map
import pandas as pd


def generate_map():
    matrix = Map.process_matrix(Map.populate(Map.populate(Map.create_matrix(Map))))
    Map.print_matrix(matrix)
    return matrix


def save_map(map, name):
    df = pd.DataFrame(data=map).T
    df.to_csv(f'{name}.csv')


def read_map(name):
    df = pd.read_csv(name)
    Map.print_matrix(df.values)


program = True

while program:
    run = True
    first = input("'g' to generate new map \n"
                  "'o' to open saved map(only csv)\n"
                  "'c' to end program\n")
    if first == 'g':
        matrix = generate_map()
        while run:
            answer = input("\n's' to save\n"
                           "'r' to repeat\n"
                           "'b' to return\n")
            if answer == 's':
                print("the file will be saved as .csv\n")
                save_file_name = input("type new file name:")
                save_map(matrix, save_file_name)
                print("\nfile created!\n")
                run = False
            elif answer == 'r':
                print('\n')
                matrix = generate_map()
                run = True
            elif answer == 'b':
                run = False
            else:
                run - True
    elif first == 'o':
        open_file_name = input("type complete file name:")
        read_map(open_file_name)
    elif first == 'c':
        program = False
    else:
        program = True
