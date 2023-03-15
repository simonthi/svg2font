install:
    chmod +x `pwd`/svg2font.sh
	ln -s `pwd`/svg2font.sh /usr/local/bin/svg2font.sh

uninstall:
	rm /usr/local/bin/svg2font.sh