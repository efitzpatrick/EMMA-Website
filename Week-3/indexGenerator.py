import markdown
import codecs

txt = """
* Tuesday
	* [Choreo: Straight Up + Brave](choreo-8-11.html)
	* [Choreo: Unwritten](../Lists/full-cast.html)
"""
html = markdown.markdown(txt, extensions=[]) 
print(html)