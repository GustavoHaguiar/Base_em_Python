from pytube import YouTube

link = str(input("Enter link: "))
name = str(input("Enter file name[Null = default]: "))
name = name+".mp4"
yt = YouTube(link)
stream = yt.streams.get_by_itag(22)
if name == '':
    stream.download()
else:
    stream.download(filename=name)
