<?xml version="1.0" encoding="utf-8"?>
<package unique-identifier="uid" xmlns:opf="http://www.idpf.org/2007/opf" xmlns:asd="http://www.idpf.org/asdfaf">
	<metadata>
		<dc-metadata  xmlns:dc="http://purl.org/metadata/dublin_core" xmlns:oebpackage="http://openebook.org/namespaces/oeb-package/1.0/">
			<dc:Title>Blog</dc:Title>
			<dc:Language>zh</dc:Language>
			<dc:Creator>Amazon.com</dc:Creator>
			<dc:Copyrights>Amazon.com</dc:Copyrights>
			<dc:Publisher>Amazon.com</dc:Publisher>
			<x-metadata>
				<EmbeddedCover>images/cover.jpg</EmbeddedCover>
			</x-metadata>
		</dc-metadata>
	</metadata>
	<manifest>
		<item id="content" media-type="text/x-oeb1-document" href="toc.html"></item>
		{% for article in articles %}
		<item id="{{forloop.counter}}" media-type="text/x-oeb1-document" href="{{article}}.html"></item>
		{% endfor %}
	</manifest>
  <spine toc="ncx">
  	<itemref idref="content"/>
  	{% for article in articles %}
  	<itemref idref="{{forloop.counter}}"/>
  	{% endfor %}
  </spine>
	<guide>
		<reference type="toc" title="Table of Contents" href="toc.html"/>
	</guide>
</package>
