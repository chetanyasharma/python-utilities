import pafy
y = raw_input("enter the url :")
video = pafy.new(y)
t = video.title
r = video.rating
print t
print r
best = video.getbest("mp4")
filename = best.download(quiet = False)
