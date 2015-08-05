import markdown
import codecs

txt = """
# Welcome to Week 2

## Monday
* Morning
	* [Work Act 1 Numbers](../Lists/act-1.html)
* Afternoon
	* [Blocking](blocking-8-3.html)
	* [Choreography](choreo-8-3.html)
	* [Vocals](vocals-8-3.html)

## Tuesday
* [Blocking](blocking-8-4.html)
* [Vocals](../Lists/act-1.html)

## Wednesday
* [Watta Man](8-4-m.html)
* [Turn the Beat Around](TTBA-8-4.html)
* [Parent's Meeting](../Lists/act-1.html)

## Thrusday
* [Act 1 Scene 3]()
* [Act 2 Scene 4]()
* [All Leads w/ Russ]()

## Friday
* [Run Act 1]()
* [Run Act 2]()
"""
html = markdown.markdown(txt, extensions=[]) #'markdown_checklist.extension'
print("<div class=\"weekList\">\n" + html + "\n</div>")
# output_file = codecs.open("index.html", "w", 
#                           encoding="utf-8", 
#                           errors="xmlcharrefreplace"
# )
# output_file.write(html)