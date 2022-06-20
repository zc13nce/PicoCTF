import hashlib
import base64

key_part_static1_trail = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trail = "xxxxxxxx"
key_part_static2_trail = "}"
key_full_template_trail = key_part_static1_trail + key_part_dynamic1_trail + key_part_static2_trail

username_trail = b"ANDERSON"

potential_dynamic_key = ""

# where out input begins:
offset = 23

# positions in username_trail
positions = [4, 5, 3, 6, 2, 7, 1, 8]

for p in positions:
    potential_dynamic_key += hashlib.sha256(username_trail).hexdigest()[p]

key = key_part_static1_trail + potential_dynamic_key + key_part_static2_trail
print(key)
print(len(key))
