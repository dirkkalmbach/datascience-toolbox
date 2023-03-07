# `Pytube`  
> `pip install pytube`  
- works amazingly good 😀
- speedy: 90MB in 2,5 min (14h video in 70 min)
- works also with Youtube shorts
- tricky part: a lot of streams -> for high resolution I need to combine audio and video by myself OR I USE `progressive=True` (<- downloads <720pix)
- installed in conda environments: `base`, `media36`


## Example Code
```Python
from pytube import YouTube 
yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
yt.streams.filter(progressive=True)
stream = yt.streams.get_by_itag(22)#seems: 22=always 720p
stream.download(SAVE_PATH)
```
## MORE STUFF
- `yt.thumbnail_url`: link to download image
- `yt.title` 👈🏻 print title
###  ONLY AUDIO 🎧🥁🎤🎶 
```Python
t = yt.streams.filter(only_audio=True)`
t[0].download("/Users/dirkkalmbach/Downloads")
# dann einfach .mp4 -> .mp3 umbenennen (oder so lassen)
```   
## Reference 📚
https://pytube.io/en/latest/user/quickstart.html