from file_manager import File_manager

fs = File_manager()

if __name__ == "__main__":
    fs.write_file("test.txt", "This is great content!!!")
    fs.append_file("test.txt", "This is a second line")
    print(fs.read_file("test.txt"))
    fs.print_file("test.txt")