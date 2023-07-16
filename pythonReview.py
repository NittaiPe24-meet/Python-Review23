


def create_youtube_video(title = input("title: "), description = input("description: ")):
	video = {"title": title, "description": description, "likes": 0, "dislikes": 0, "comments": {}}
	return video

def like(videoA = input()):
	if videoA["likes"]:
		videoA["likes"] += 1
		return (videoA["likes"])

def dislike(videoB = input()):
	if videoB["dislikes"]:
		videoB["dislikes"] += 1
		return (videoB["dislikes"])
