import os
files = os.listdir()
# files.remove("FileCleaner.py")


def createfolder(foldername):
    if not os.path.exists(foldername):
        os.makedirs(foldername)


def sortfiles(fileslist, ext):
    for file in files:
        if os.path.splitext(file)[1].lower() in ext:
            fileslist.append(file)


def move(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")


imgext = [".png", ".jpg", ".jpeg", ".gif"]
medext = [".mpg", ".mp4", ".mpeg", ".mp3", ".mkv", ".avi"]
rarext = [".rar", ".zip", ".7z"]
codext = [".py", ".js", ".css", ".html", ".c", ".cpp", ".java", ".r"]
docsext = [".docs", ".ppt", ".pdf", ".md", ".doc", ".docx", ".txt"]
softext = [".exe", ".msi"]

createfolder("Images")
createfolder("Media")
createfolder("RAR/ZIP")
createfolder("Code")
createfolder("Docs")
createfolder("Softwares")
createfolder("Others")

image = []
media = []
rar = []
code = []
docs = []
soft = []
other = []

sortfiles(image, imgext)
sortfiles(media, medext)
sortfiles(rar, rarext)
sortfiles(docs, docsext)
sortfiles(code, codext)
sortfiles(soft, softext)

for file in files:
    ext = os.path.splitext(file)[1].lower()
    if(ext not in imgext) and (ext not in medext) and (ext not in rarext) and (ext not in codext) and (ext not in docsext) and (ext not in softext) and (os.path.isfile(file)):
        other.append(file)
move("Images", image)
move("Media", media)
move("RAR/ZIP", rar)
move("Softwares", soft)
move("Code", code)
move("Docs", docs)
move("Others", other)
