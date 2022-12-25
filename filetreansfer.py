import os ,shutil
dic_extension = {
    #'audio_extension' : ('.mp3' , '.m4a','.wav','.flac'),
    'video_extension' : ('.mp4','.mkv','.MKV','.flv','.mpeg'),
    'doc_extension' : ('.doc','.pdf','.txt')
}


folderpath = input('input the path with : ')

def file_folder(folder_path , file_extension):
    files = []
    for file in os.listdir(folder_path):
        for extension in file_extension:
            if file.endswith(extension):
                files.append(file)
    return files
#   return [file for file in os.listdir(folder_path) for extension in file_extension if file.endswith(extension)]

#print(file_folder(folderpath , video_extension))

for extension_type,extension_name in dic_extension.items():
    foldername = extension_type.split('_')[0] + 'files'
    folder_path = os.path.join(folderpath,foldername)
    os.mkdir(folder_path)
    for item in (file_folder(folderpath , extension_name )):
        item_path = os.path.join(folderpath,item)
        item_new_path = os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path) 
    # print('calling file finder')
    # print(file_folder(folderpath , extension_name))



