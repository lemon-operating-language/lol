design notes:
    ??????? either you pile up object definitions
    next to the statements of your program, then
    the interpreter must go and actually instantiate
    them in some other space, or you just have a special
    area for them..simplifying interpreter?????????


class Interpreter(object):
    def set_program(self, program):
        self.program = program
    def prepare(self):
        for i in self.program.statements.items:
            if isinstance(i, Object
            
        


object_definitions=
Object(

database = [
	{"config":
		["delay", "sdl key first repeat delay"],
		["repeat", "sdl key repeat rate"]
	]
	,
	["snippets",
		[
"""
pyyaml syntax for object:
!!python/object:lemon.defun
"""
			,
			"source": "http://pyyaml.org/wiki/PyYAMLDocumentation",
			"note": "watch out for your module name, main is a bad name"
		}
	]
	"code snippets":
	{
		"value":"\"abc\"[::-1]",
		"notes":"reverse text"
	}
	,
	"notes":
	[
		{
			"date":"7. 7. 2013 20:10:36",
			"values"=
			[
				"SO integration status":
"""
kook@kook:~/Py-StackExchange/demo$ ./object_explorer.py 
Select a site (0 exits):
1) Stack Overflow
2) Server Fault
3) Super User
4) Meta Stack Overflow
5) Android Enthusiasts
6) Android Enthusiasts Meta
7) Answers OnStartups
8) Seasoned Advice Meta
9) Game Development
10) Game Development Meta
11) Mathematics
12) Mathematics Meta
13) Home Improvement
14) Home Improvement Meta
15) Meta Super User
16) Meta Server Fault
17) TeX - LaTeX Meta
18) Ask Ubuntu
19) Ask Ubuntu Meta
20) Personal Finance & Money
21) Stack Apps
22) User Experience
23) User Experience Meta
24) WordPress Answers Meta
25) Theoretical Computer Science
26) Theoretical Computer Science Meta
27) Role-playing Games Meta
28) Bicycles
29) Programmers Meta
30) Electrical Engineering
31) Electrical Engineering Meta
32) Arqade
33) Arqade Meta
34) Webmasters
35) Webmasters Meta
36) Seasoned Advice
37) Geographic Information Systems
38) Geographic Information Systems Meta
39) TeX - LaTeX
40) Unix & Linux
41) Unix & Linux Meta
42) WordPress Answers
43) Personal Finance & Money Meta
44) English Language & Usage
45) English Language & Usage Meta
46) Answers OnStartups Meta
47) Board & Card Games
48) Code Review Meta
49) Programming Puzzles & Code Golf
50) Programming Puzzles & Code Golf Meta
51) Board & Card Games Meta
52) Physics
53) Physics Meta
54) IT Security Meta
55) Writers
56) Writers Meta
57) Graphic Design Meta
58) Code Review
59) Parenting
60) Parenting Meta
61) SharePoint
62) SharePoint Meta
63) Musical Practice & Performance
64) Musical Practice & Performance Meta
65) Software Quality Assurance & Testing
66) Software Quality Assurance & Testing Meta
67) Mi Yodeya
68) Mi Yodeya Meta
69) German Language & Usage
70) German Language & Usage Meta
71) Philosophy
72) Philosophy Meta
73) Gardening & Landscaping
74) Database Administrators
75) Database Administrators Meta
76) Science Fiction & Fantasy
77) Science Fiction & Fantasy Meta
78) Japanese Language & Usage
79) Japanese Language & Usage Meta
80) Photography
81) Photography Meta
82) Cross Validated
83) Cross Validated Meta
84) Ask Different
85) Ask Different Meta
86) Role-playing Games
87) Bicycles Meta
88) Programmers
89) Homebrewing
90) Homebrewing Meta
91) IT Security
92) Audio-Video Production
93) Audio-Video Production Meta
94) Graphic Design
95) Quantitative Finance
96) Quantitative Finance Meta
97) Project Management
98) Project Management Meta
99) Skeptics
100) Skeptics Meta
101) Physical Fitness
102) Physical Fitness Meta
103) Drupal Answers
104) Drupal Answers Meta
105) Motor Vehicle Maintenance & Repair
106) Motor Vehicle Maintenance & Repair Meta
107) Signal Processing
108) Signal Processing Meta
109) Christianity Meta
110) Bitcoin
111) Bitcoin Meta
112) Biblical Hermeneutics
113) Biblical Hermeneutics Meta
114) History
115) LEGO® Answers
116) LEGO® Answers Meta
117) Cognitive Sciences Meta
118) The Great Outdoors
119) The Great Outdoors Meta
120) Chinese Language & Usage
121) Chinese Language & Usage Meta
122) Biology
123) Biology Meta
124) Personal Productivity Meta
125) Cryptography
126) Cryptography Meta
127) Computer Science
128) Computer Science Meta
129) The Workplace
130) Chemistry Meta
131) Chess
132) Chess Meta
133) Russian Language & Usage Meta
134) Islam
135) Islam Meta
136) History Meta
137) Martial Arts
138) Martial Arts Meta
139) Sports Meta
140) Academia
141) Academia Meta
142) Gardening & Landscaping Meta
143) Travel
144) Travel Meta
145) Personal Productivity
146) Spanish Language & Usage
147) Spanish Language & Usage Meta
148) Computational Science
149) Computational Science Meta
150) Movies & TV
151) Movies & TV Meta
152) Poker
153) Poker Meta
154) Linguistics
155) Linguistics Meta
156) Salesforce
157) Salesforce Meta
158) Sports
159) Mathematica
160) Mathematica Meta
161) Cognitive Sciences
162) Raspberry Pi
163) Raspberry Pi Meta
164) Russian Language & Usage
165) French Language & Usage
166) French Language & Usage Meta
167) Christianity
168) The Workplace Meta
169) Windows Phone
170) Windows Phone Meta
171) Chemistry
172) Web Applications
173) Web Applications Meta

Site ID: 4
Use function names you would when using the Site, etc. objects.
return:	Move back up an object.
exit:	Quits.
dir:		Shows meaningful methods and properties on the current object.
dir*:	Same as dir, but includes *all* methods and properties.
code:	Show the code you'd need to get to where you are now.
! before a non-function means "explore anyway."
a prompt ending in []> means the current item is a list.
Meta Stack Overflow> search
Traceback (most recent call last):
  File "./object_explorer.py", line 154, in <module>
    explore(site, site_def.name, 'site')
  File "./object_explorer.py", line 126, in explore
    rval = rval(*args)
  File "../stackexchange/__init__.py", line 748, in search
    return self.build('search', Question, 'questions', kw)
  File "../stackexchange/__init__.py", line 604, in build
    json = self._request(url, kw)
  File "../stackexchange/__init__.py", line 576, in _request
    json, info = request_mgr.json_request(url, new_params)
  File "../stackexchange/web.py", line 119, in json_request
    req = self.request(to, params)
  File "../stackexchange/web.py", line 92, in request
    conn = req_open.open(request)
  File "/usr/lib/python2.7/urllib2.py", line 410, in open
    response = meth(req, response)
  File "/usr/lib/python2.7/urllib2.py", line 523, in http_response
    'http', request, response, code, msg, hdrs)
  File "/usr/lib/python2.7/urllib2.py", line 448, in error
    return self._call_chain(*args)
  File "/usr/lib/python2.7/urllib2.py", line 382, in _call_chain
    result = func(*args)
  File "/usr/lib/python2.7/urllib2.py", line 531, in http_error_default
    raise HTTPError(req.get_full_url(), code, msg, hdrs, fp)
urllib2.HTTPError: HTTP Error 400: Bad Request
kook@kook:~/Py-StackExchange/demo$ 
"""
			,
			"database dumps are available at http://www.clearbits.net/creators/146-stack-exchange-data-dump, downloading..."
			,
			[
			"https://github.com/antoviaque/stack-overflow-command-line",
"""
kook@kook:~$ sudo gem install stackoverflow
[sudo] password for kook: 
Fetching: json-1.8.0.gem (100%)
Building native extensions.  This could take a while...
ERROR:  Error installing stackoverflow:
ERROR: Failed to build gem native extension.

        /usr/bin/ruby1.9.1 extconf.rb
/usr/lib/ruby/1.9.1/rubygems/custom_require.rb:36:in `require': cannot load such file -- mkmf (LoadError)
from /usr/lib/ruby/1.9.1/rubygems/custom_require.rb:36:in `require'
from extconf.rb:1:in `<main>'


Gem files will remain installed in /var/lib/gems/1.9.1/gems/json-1.8.0 for inspection.
Results logged to /var/lib/gems/1.9.1/gems/json-1.8.0/ext/json/ext/generator/gem_make.out
kook@kook:~$ 
"""
				]
			]
		}
	]#notes
}#whole database




---outlining / semantic / ? editor--
	leo
		sounds like a great IDE / outliner / thing
		once it starts supporting white on black qt themes :D

		try in kubuntu usb stick



funky unicode:

	😼oo~😈 ␀_␀⏣_⏣⍤⍊_⍊⍘⍚⍛⍢⍣




openblocks data structure:
....








