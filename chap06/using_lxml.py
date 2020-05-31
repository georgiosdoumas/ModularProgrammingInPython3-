from lxml import etree

movies = etree.Element("films")

movie = etree.SubElement(movies, "movie")
movie.text = "The Wizard of Oz"
movie.set("year", "1939")

movie = etree.SubElement(movies, "movie")
movie.text = "Mary Poppins"
movie.set("year", "1964")

movie = etree.SubElement(movies, "movie")
movie.text = "Chinatown"
movie.set("year", "1974")

print(etree.tostring(movies, pretty_print=True)) 


""" Output :
b'<films>\n  <movie year="1939">The Wizard of Oz</movie>\n  <movie year="1964">Mary Poppins</movie>\n  <movie year="1974">Chinatown</movie>\n</films>\n'
"""
