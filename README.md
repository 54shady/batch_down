# batch_down
batch download pictures form a url with python

Usage:
	假设需要批量下载的图片URL如下所示:  
	http://example_target_url/01.jp  
	http://example_target_url/02.jpg  
	...  
	http://example_target_url/50.jpg  
	批量下载这50张图片:  

	保存图片在当前目录  
	python batch_down.py 1 50 http://example_target_url/  
	保存图片在指定目录  
	python batch_down.py 1 50 http://example_target_url/ /home/pic  
