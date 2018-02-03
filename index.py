#!/usr/bin/python
import cgi
print "Content-type:text/html\r\n\r\n"

print """

<html>
	<head>
		<title>LNCT Progect</title>
	</head>
		<style>
		textarea.foo
		{
		border: 3px solid;
		padding: 5px;
		resize:none;
		align-self: center;
		justify-self: center;
		border-radius: 5px;
		}
		.main_container{
		width: auto;
		height: auto;
		background: #f1ddf9;
		padding: 20px;
		}
		.areatitle{
		width: auto;
    		height: 90px;
    		padding: 1px;
		background-color: cadetblue;
		border-radius: 5px;
		color: snow;
		}
		.arealang{
		width: auto;
    		height: 25px;
    		padding: 10px;
		background-color: #fb4620;
		text-align: center;
		border-radius: 5px;

		}
		.areaname{
		display: grid;
		width: auto;
    		height: auto;
    		padding: 2px;
		background-color:  #aff94b;
		border-radius: 5px;
		grid-template-columns: 1fr 1fr;
		grid-gap: 1px;
		}
		.areaname > div:1{
		display: grid;
		text-align: center;
		background: #f1ddf9
		grid-row-gap: 1px;
		border-radius: 5px;
		}
		.areaname > div:2{
		display: grid;
		text-align: center;
		background: #f1ddf5
		grid-row-gap: 1px;
		border-radius: 5px;
		}
		.areaio{
		display: grid;
		text-align: center;
		background-color:  #f9e68f;
		grid-template-columns: 50% 50%;
		grid-gap: 1px;
		padding: 23px;
		}
		.areaio > div:1{
		display: grid;
		background: #f1ddf9
		grid-row-gap: 1px;
		border-radius: 5px;
		}
		.areaio > div:2{
		display: grid;
		background: #f1ddf5
		grid-row-gap: 1px;
		border-radius: 5px;
		}
		.arearun{
		text-align: center;
		background:  #0400fb;
		padding: 15px;
		border-radius: 5px;
		}
		.output{
		background: white;
		padding: 15px;
		border-radius: 5px;
		width: 428px;
		height: 416px;
		border-width: 19px;
		border-color: black;
		border: 3px solid;
		text-align: center;
		}
		</style>
<body>
	<div class="main_container">
		<div class="areatitle">
			<h1><center>Online Programming Plateform</center></h1>
		</div>
		<div class="arealang">
			<input type="checkbox" name="c" value="c" /><b> C
			<input type="checkbox" name="c++" /> C++
			<input type="checkbox" name="java" value="java" /> Java</b>
		</div>
		<div class="areaname">
			<div>
			<p style="margin-left: 20px;">Program Name: <input type="text" name="name"/></p>
			</div>
			<div>
			<p>             Output: </p>
			</div>
		</div>
		<div class="areaio">
			<div>
			<textarea class="foo" rows="30	" cols="60">Write your code here</textarea>
			</div>
			<div>
			<div class="output"></div>
			</div>
		</div>
		<div class="arearun">
		<input type="submit" value="          Run         " height="30" />
		</div>

<br>



</body>
</html>
"""
