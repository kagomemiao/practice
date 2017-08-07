import webbrowser

class Movie():
    def __init__(self, title, story_line, image, trailer):
        self.title = title
        self.storyline = story_line
        self.image = image
        self.trailer = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
