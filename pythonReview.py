


def create_youtube_video(title = input("title: "), description = input("description: ")):
	youtube_video = {"title": title, "description": description, "likes": 0, "dislikes": 0, "comments": {}}
	return youtube_video

def like(videoA = input("gimmie da dictionary: ")):
	if ("likes" in videoA):
		videoA["likes"] += 1
		print(videoA["likes"])
		return (videoA["likes"])

def dislike(videoB = input("gimmie da dictionary; ")):
	if videoB["dislikes"]:
		videoB["dislikes"] += 1
		print(videoB["dislikes"])
		return (videoB["dislikes"])

def add_comment(video, user, text):
	video["comments"][user] = text
	return video


viral_video = {"title": "how to breath", "description": "very useful!!!", "likes": 0, "dislikes": 0}
for num in range(495):
	like(viral_video)
print("likes: ", viral_video["likes"])