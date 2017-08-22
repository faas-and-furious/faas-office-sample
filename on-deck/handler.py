from pptx import Presentation
import sys

def handle(req):
    prs = Presentation()
    title_slide_layout = prs.slide_layouts[0]
    slide = prs.slides.add_slide(title_slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]

    title.text = "Hello " + req
    subtitle.text = "python-pptx was here!"

    prs.save("out.pptx")
    myfile = open('out.pptx', 'r')
    sys.stdout.write(myfile.read())
    myfile.close()
