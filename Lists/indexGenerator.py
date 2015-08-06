import markdown
import codecs

txt = """
# All Purpose Lists

* [All Cast](full-cast.html)
* [All Crew](all-crew.html)  

* [Leads]()
* [Leads + Welcoming Committees]()
* [Welcoming Committees + Ensemble]()
"""
html = markdown.markdown(txt, extensions=[]) 
print(html)