import json
import os
# this software is licensed under the GNU General Public License v3.0
# if you paid for this, you got scammed
# github repo: https://github.com/j0912345/pam_properteries_editor
def decode_pam_into_dict_or_json(normal_header, decode_json = False):
    with open(pam_path, "rb") as pam:
        # this also means that the read pointer is always at the file's start
        this_header = pam.read(len(normal_header))
        # the pam header has a version number in this part of it
        if this_header[4:7] == normal_header[4:7] and (normal_header[0:3]+normal_header[8:16]) != this_header[0:3]+this_header[8:16]:
            print("the header isn't just a version difference from the normal one. this could be a bad sign.")
        elif this_header[4:7] != normal_header[4:7]:
            print("the pam being used as input is a different version than the one this tool is made for (pam ver 6, the one used in pvz2)")


        image_list_data = {}
        # read the image list
        for i in range(0,int.from_bytes(pam.read(2), 'little', signed=False)):
            str_len = int.from_bytes(pam.read(2), 'little', signed=False)
            string = pam.read(str_len).decode("utf-8")

            width = int.from_bytes(pam.read(2), 'little', signed=True)
            height= int.from_bytes(pam.read(2), 'little', signed=True)

            ix = int.from_bytes(pam.read(4), 'little', signed=True)
            iy = int.from_bytes(pam.read(4), 'little', signed=True)
            jx = int.from_bytes(pam.read(4), 'little', signed=True)
            jy = int.from_bytes(pam.read(4), 'little', signed=True)

            anchor_x = int.from_bytes(pam.read(2), 'little', signed=True)
            anchor_y = int.from_bytes(pam.read(2), 'little', signed=True)

            image_list_data[string] = {
                "string": string,
                "width": width,
                "height": height,
                "ix": ix,
                "iy": iy,
                "jx": jx,
                "jy": jy,
                "anchor_x": anchor_x,
                "anchor_y": anchor_y
                }
        print(len(image_list_data))
        print('\nread the image list, starting to read the animation block. this may take a while because\n\
"The animation is coded frame by frame. Each does transfromations on several layers or split sprites."\n\
- the format documentation.\n\
probably won\'t be very fast to decode.\n')
        anim_data_dict = {}
        not_done = True
        # so the loop can stop if it reaches the end of the file
        f_size = os.path.getsize(pam_path)

        animations_in_file = int.from_bytes(pam.read(2), 'little', signed=True)
        anim_data_dict["anim_amount"] = animations_in_file
        while not_done:
            print("new iteration")
            if pam.tell() >= f_size:
                not_done = True
            anim_name_str_len = int.from_bytes(pam.read(2), 'little', signed=True)
            print(anim_name_str_len)
            anim_name_string = pam.read(anim_name_str_len).decode("utf-8")
            # the next 4 bytes are 0, so they can be skipped
            pam.seek(pam.tell()+4)
            fps = int.from_bytes(pam.read(2), 'little', signed=True)
            current_frame = int.from_bytes(pam.read(2), 'little', signed=True)
            frame_to_begin = int.from_bytes(pam.read(2), 'little', signed=True)
            frame_to_end = int.from_bytes(pam.read(2), 'little', signed=True)

            anim_data_dict[anim_name_string] = {
                "anim_name_string": anim_name_string,
                "anim_name_str_len": anim_name_str_len,
                "fps": fps,
                "current_frame": current_frame,
                "frame_to_begin": frame_to_begin,
                "frame_to_end": frame_to_end
                }
            # next it needs to read trasformation block


            print(anim_data_dict)



if __name__ == "__main__":
    print("\nthis software is licensed under the GNU General Public License v3.0\n\
if you paid for this, you got scammed\n\
github repo: https://github.com/j0912345/pam_properteries_editor\n")


    normal_header = b"\x54\x19\xF0\xBA\x06\x00\x00\x00\x1E\x00\x00\x00\x00\x78\x1E\x78\x1E"
    pam_path = "sunflower.pam"#input("path to the file you want to edit: ")

    decode_pam_into_dict_or_json(normal_header, True)
