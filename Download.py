from urllib.request import urlopen
html = urlopen('https://vietnamnet.vn/vn/the-thao/bong-da-viet-nam/doi-tuyen-viet-nam/lo-dieu-khoan-te-nhi-trong-ban-hop-dong-cua-hlv-park-hang-seo-585368').read()

filename = "1.txt"
file_ = open(filename, 'wb')
file_.write(html)
file_.close()