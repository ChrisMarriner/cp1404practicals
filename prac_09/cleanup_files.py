"""
CP1404/CP5632 Practical
Demos of various os module examples
Christopher Marriner
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('Lyrics/Christmas')
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    string = ""
    for character in enumerate(filename):
        new_string = string + character
        print(new_string)
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


def demo_walk(filenames, directory_name):
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
    for filename in filenames:
        full_name = os.path.join(directory_name, filename)
        new_name = os.path.join(directory_name, get_fixed_filename(filename))
        os.rename(full_name, new_name)


main()
# demo_walk()
