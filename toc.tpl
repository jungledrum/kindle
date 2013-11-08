<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8">
<title>TOC</title>
</head>
<body>

<h1 id="toc">Table of Contents</h1>

<ul>
	{% for article in articles %}
	<li><a href="{{article}}.html">{{article}}</a></li>
	{% endfor %}
</ul>
</body>
</html>
