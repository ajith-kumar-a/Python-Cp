import os

def deleteFile(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f'{filename} Deleted Sucessfully')
    else:
        print(f"{filename} File not found")

def main():
  filename = input('Enter the file Name which you want to delete : ')
  deleteFile(filename)


if __name__ == '__main__':
  main()