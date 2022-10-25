def is_equal_string(utf8_string, utf16_string):
    s_from_utf16 = utf16_string.decode('utf-16')
    s_from_utf8 = utf8_string.decode('utf-8')
    return (True if s_from_utf8.casefold()==s_from_utf16.casefold() else False)


utf8_string = b'hello'
utf16_string =b'\xff\xfeh\x00e\x00l\x00l\x00o\x00'

print(is_equal_string(utf8_string, utf16_string))