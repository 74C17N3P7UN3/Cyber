from global_utils import base64_decode, xor_bytes

original_data = "El Psy Congroo".encode("ascii")
encrypted_data = base64_decode("IFhiPhZNYi0KWiUcCls=")
encrypted_flag = base64_decode("I3gDKVh1Lh4EVyMDBFo=")

enc_key = xor_bytes(original_data, encrypted_data)

flag_bytes = xor_bytes(enc_key, encrypted_flag)
print(flag_bytes.decode("ascii"))
