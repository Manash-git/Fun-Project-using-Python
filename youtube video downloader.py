import pytube
from pprint import pprint

url = "https://www.youtube.com/watch?v=Xj49Lz1GPs0"

yt = pytube.YouTube(url)

# for seeing all the files resulation details
flies = yt.streams.all()
for i in flies:
    print(i)

# for downloading

vdo = yt.streams.get_by_itag(247)
vdo.download('F://git project//Fun-Project-using-Python')
# print(yt.get_videos())
print("Done")