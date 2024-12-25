from fasthtml.common import *

app = FastHTML()

@app.get("/")
def home():
    page = Html(
        Head(Title('Some page')),
        Body(Div('Some text, ', 
	     A('A link', href='https://example.com'), 
             Img(src="https://placehold.co/200"), cls='myclass')
             ),
        Div(A("2024336408", href="https://beian.miit.gov.cn/", target="_blank"))
        )
    return page

serve()