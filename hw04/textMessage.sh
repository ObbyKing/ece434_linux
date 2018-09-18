SIZE=320x240
TMP_FILE=/tmp/frame.png

convert $BORIS -fill red -font Times-Roman -pointsize 16 \
	label:'Andrew Lund\nECE434\nfor class' \
	-draw "text 0,200 'Bottom Text'" \
	-append $TMP_FILE

sudo fbi -noverbose -T 1 $TMP_FILE
sudo fbi -noverbose -T 1 boris.png
