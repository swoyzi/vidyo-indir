from pytube import YouTube

link = input("linki yapıştırınız >")

yt =  YouTube(link)

ys = yt.streams.get_highest_resolution()

print("indiriliyor....")

ys.download()

print("indirildi kardeşim...")