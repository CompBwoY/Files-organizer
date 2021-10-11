import os, shutil

path = "."
_list = os.listdir(path)
file_type = {
    'images':['.png','.jpg','.gif'],
    'audio':['.mp3','.wav','.ogg','.mkv','.wma'],
    'videos':['.mp4','.mkv'],
    'programs':['.exe','.sh','.js','.py','.java'],
    'zip':['.rar','.zip','.cab','.7z','.ace','.arj','.bz2','.gz','.lha','.lzh','.taz','.tgz','.xz','*.txz'],
    'docs':['.doc','.docx','.pdf','.pptx','.pptm','.xlsm',],
    'text':['.txt'],
}

directories = [k for k in file_type]
extensions = [file_type[k] for k in directories]
_type = '.'

for file in _list:
    name, ext = os.path.splitext(file)
    ext = ext[0:]
    print(_type)

    if ext == '':
        continue

    for i in range(len(extensions)):
        for extn in range(len(extensions[i])):
            if ext == extensions[i][extn]:
                _type = directories[i]

    if os.path.exists(path+"\\"+_type):
        shutil.move(path+'\\'+file, path+'\\'+_type+'\\'+file)
    elif _type == '.':
        os.makedirs(path+'\\'+ext)
        shutil.move(path+'\\'+file, path+'\\'+ext+'\\'+file)
    else:
        os.makedirs(path+'\\'+_type)
        shutil.move(path+'\\'+file, path+'\\'+_type+'\\'+file)

