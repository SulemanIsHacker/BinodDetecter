import os
def isBinod(filename):
    with open(filename) as f:
        file_Content = f.read()
        if "Binod".lower() in file_Content:
            return True
        else:
            return False
if __name__ == '__main__':
    dir_contents = os.listdir()
    for item in dir_contents:
        print(item)
        flag = isBinod(item)
        if flag:
            print(f"Binod Detected in {item}")
        else:
            print(f"Binod not detected in {item}")