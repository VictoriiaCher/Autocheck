import shutil
import base64


def create_backup(path, file_name, employee_residence):
    with open(path+'/'+ file_name, 'wb') as b_file:
        list_residence = [f'{key} {value}\n' for key,value in employee_residence.items()]
        for i in list_residence:
            message_bytes = i.encode()
            b_file.write(message_bytes)
    archive_name = shutil.make_archive('backup_folder', 'zip', path)    
    return archive_name  

path = 'folder'
file_name = 'file.bin'
employee_residence = {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}

create_backup(path, file_name, employee_residence)

