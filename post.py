"""Defines the Post object, which represents a blog post"""


class Post:

    def __init__(self, title, date):
        self.title = title
        self.subtitle = False
        self.endnotes = False
        self.date = date
        self.photos = []
        self.paragraphs = []

    def set_subtitle(self, str):
        self.subtitle = str

    def set_endnotes(self, str):
        self.endnotes = str

    def add_image(self, image):
        self.photos.append(image)

    def add_paragraph(self, str):
        self.paragraphs.append(str)
