from colorama import Fore, Back, Style
# this software is licensed under the GNU General Public License v3.0
# if you paid for this, you got scammed
# github repo: https://github.com/j0912345/pam_properteries_editor
def decode_pam_into_json():
    with open(pam_path, "rb") as pam:
        # this also means that the read pointer is always at the file's start
        this_header = pam.read(len(normal_header))
        if this_header != normal_header:
            print("the header isn't the nornal header (at least for pvz2) but sometimes it's different than normal")


if __name__ == "__main__":
    print("this software is licensed under the GNU General Public License v3.0\n\
if you paid for this, you got scammed\n\
github repo: https://github.com/j0912345/pam_properteries_editor")


    normal_header = b"54\x19\xF0\xBA\x06\x00\x00\x00\x1E\x00\x00\x00\x00\x78\x1E\x78\x1E"
    pam_path = input("path to the file you want to edit: ")
    blocks_to_look_for = b"\xa0"
