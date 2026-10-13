class File_manager:
        
    def write_file(self, file_name, content):
        
        try:
            with open(file_name, "w") as file:
                file.writelines(content)
            
        except Exception as e:
            print(f"could not write file: {e}")

    def append_file(self, file_name, content):

        try:
            with open(file_name, "a") as file:
                file.writelines("\n" + content)
            
        except Exception as e:
            print(f"could not append file: {e}")

    def read_file(self, file_name):

        try:
            with open(file_name, "r") as file:
                return file.readlines()
        except FileNotFoundError as e:
            print("file not found")
            
        except Exception as e:
            print(f"could not read file: {e}")

    def print_file(self, file_name):

        try:
            with open(file_name, "r") as file:
                for line in file:
                    print(line.strip())

        except FileNotFoundError as e:
            print("file not found")
            
        except Exception as e:
            print(f"could not read file: {e}")