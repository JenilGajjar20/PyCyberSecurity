import sys


def identifyFileType(file_path):
    max_magic_len = max(len(magic) for magic in magic_numbers.keys())

    with open(file_path, 'rb') as f:
        file_header = f.read(max_magic_len)

    for magic, file_type in magic_numbers.items():
        if file_header.startswith(magic):
            return file_type

    return "Unknown file type"


def scanForEmbeddedFiles(file_path):
    results = []

    with open(file_path, 'rb') as f:
        file_content = f.read()

    for magic, file_type in magic_numbers.items():
        start_indices = [i for i in range(
            len(file_content)) if file_content.startswith(magic, i)]
        for start_index in start_indices:
            results.append((file_type, start_index))

    return results


def getMagicNumbers(file_path, length=4):
    with open(file_path, 'rb') as f:
        magic_number = f.read(length)
    return magic_number


def main():
    if len(sys.argv) != 2:
        print("Usage: python file_identification.py")
        return

    file_path = sys.argv[1]

    magic_number = getMagicNumbers(file_path, 4)
    print(f"Magic Number: {magic_number.hex().upper()}")

    file_type = identifyFileType(file_path)
    print(f"Primary file type: {file_type}")

    embedded_files = scanForEmbeddedFiles(file_path)
    if embedded_files:
        print("\nEmbedded files detected.")
        for file_type, offset in embedded_files:
            print(f"{file_type} at offset: {offset}")
    else:
        print("No embedded files detected!!")


magic_numbers = {
    b'\xFF\xD8\xFF\xE0': 'JPEG Image',
    b'\x89\x50\x4E\x47': 'PNG Image',
}


if __name__ == '__main__':
    main()
