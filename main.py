import sys
from db_requests import init_db

def main():
    init_db()
    args = sys.argv
    length = len(args)
    if length == 1:
        pass
    elif length > 1:
        command = args[1]
        print(command)
        if length == 3:
            print("text: " + str(args[2]))

if __name__ == '__main__':
    main()
