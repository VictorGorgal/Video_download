from os import system, getcwd

url = str(input("insert URL: "))
file_name = str(input("file name: "))

path = f"{getcwd()}/{file_name}.%(ext)s"
system(f'youtube-dl -o "{path}" --extract-audio -x --audio-format mp3 {url}')
print("done")
