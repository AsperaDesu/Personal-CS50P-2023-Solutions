file1 = input("File name: ")
file2 = file1.lower().strip()
ends = file2[int(file2.rfind(".")) + 1 ::]

match ends:
    case "gif"|"png":
        print(f"image/{ends}")
    case "jpg"|"jpeg":
        print(f"image/jpeg")
    case "pdf" | "zip":
        print(f"application/{ends}")
    case "txt":
        print(f"text/plain")
    case _:
        print("application/octet-stream")
