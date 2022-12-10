import os
level0 = [
	"           d       ",
	"           d       ",
	"           d       ",
	"           d       ",
	"           d       ",
	"           d       ",
	"           d       ",
	"           d                          m ",
	"  	        d     m                  gggg",
	"           d   ggg          M       dddd",
	"  	        d               ggm 2      dd            ",
	"           d    2       mggddgggm     dd            ",
	"        m  m  m   m  m mgdddddddgg  m     m    m    ",
	"ggggggggggggggggggggggggddddddddddgggggggggggggggggg",
	"dddddddddddddddddddddddddddddddddddddddddddddddddddd",
	"dddddddddddddddddddddddddddddddddddddddddddddddddddd",
	"dddddddddddddddddddddddddddddddddddddddddddddddddddd",
	"dddddddddddddddddddddddddddddddddddddddddddddddddddd",
	"dddddddddddddddddddddddddddddddddddddddddddddddddddd",
	"dddddddddddddddddddddddddddddddddddddddddddddddddddd",
	"dddddddddddddddddddddddddddddddddddddddddddddddddddd",
	"dddddddddddddddddddddddddddddddddddddddddddddddddddd",
	"dddddddddddddddddddddddddddddddddddddddddddddddddddd",
	"dddddddddddddddddddddddddddddddddddddddddddddddddddd",
	"dddddddddddddddddddddddddddddddddddddddddddddddddddd",
	"dddddddddddddddddddddddddddddddddddddddddddddddddddd"]
level1 = [
	".....................................................q.......",
	"...................................................qqQqq.....",
	"...ccc...........................................qqQQQQQqq...",
	"......cccc......................................qQQQQCQQQQq..",
	"................................................qqqqqqqqqqq..",
	".................................................pPpp.ppPp...",
	".................................................pPp...pPp...",
	".................................................pPpW.WpPp...",
	"...............................................mqqqqqqqqqqq..",
	"...............................................gdddddddddddg.",
	"............................................mggdddddddddddddgg",
	"...........................................ggddddddddddddddddd",
	"g...m....2...g...........M..m...m......m..gddddddddddddddddddd",
	"dggggggggggggdswwwwwwssgggggggggggggggggggdddddddddddddddddddd",
	"dddddddddddddddswwwwsddddddddddddddddddddddddddddddddddddddddd",
	"ddddddddddddddddssssdddddddddddddddddddddddddddddddddddddddddd",
	"dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd",
	"dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd",
	"dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd",
	"dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd",
	"dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd",
	"dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd",
	"dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd",
	"dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd",
	"dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd",
	"dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd",
	"dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd",
	"dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd",
	
	
	
	
	
]
path = os.path.dirname(os.getcwd())+"/plat.platformer/Assets/"
Backgrounds = {0:path+"Sky.png",1:path+"Sky.png"}
tilesize = 40
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

