# About this Project
This project is for our class ece 434 embedded linux course for Rose-Hulman Institute of Technology. Our project and more about it is located here: [https://elinux.org/ECE497_Project_-_LED_Matrix_Graduation_Cap](https://elinux.org/ECE497_Project_-_LED_Matrix_Graduation_Cap)

# Installation

## Setting up Falcon and xLights

Go to [this](https://markayoder.github.io/PRUCookbook/01case/case.html#case_rgb_matrix) link and go to section 1.4. This will describe how to properly install Falcon and xLights. For the already completed image that you can burn to the sd card right away is found here [SD Card](https://github.com/ObbyKing/ece434_linux/tree/master/finalProject/Install). The default image starts up the demo sequence we have automatically but might take awhile to start. Give it about 2-3 minutes to start displaying.

Some specific settings for the 32x32 are here that are different from the instructions above.

Settings:

* Single Panel Size (WxH): `32x32 1\16 Scan`
* End Channel: 3072

xLights is used to make the sequences that are displayed on the graduation cap. Follow [this](https://www.youtube.com/watch?v=9BYLIGVjxrI) guide to set up a matrix in xLights and use a sequence.

Wifi and how to configure can be found here: [Wifi](https://github.com/ObbyKing/ece434_linux/tree/master/finalProject/Internet).

## Adding a GIF
To use a GIF you find online you need to convert it to the correct format which is mp4 and this can be done using [this](https://ezgif.com/gif-to-mp4) website.

Next you can import this video into xLights to add to the sequence that you are making. 

## Making a Sequence

Making a sequence is a fairly simple task. Open up xLights and navigate to the sequencer tab. You can then simply drag and drop premade blocks into your timeline and make your sequence!

## Uploading Sequence to Falcon

To upload a .fseq file to Falcon, simply navigate to Content Setup -> File Manager -> Sequences. At the bottom of the page, click on select files and navigate to your sequence file. Upload it.

## Creating a Playlist in Falcon

Once your sequence is uploaded to Falcon, navigate to Content Setup -> Playlists. Name your playlist then add your sequence file to the playlist. Save your playlist.

## Setting up Scripts

In order to have the sequence play on startup, you need to download the UserCallbackHooks.sh script from the script repository. Get internet on your pocketbeagle by using the ipMasquerade script as well as the pocketssh script.
SSH into your beagle and run a ping google.com command to verify that you have internet on your pocketbeagle. Once you do, open a browser and log into Falcon. go to 192.168.7.2 and navigate to content setup -> Script Repository. If you have internet on your Pocketbeagle, you should see a bunch of scripts in which you can download.

Download UserCallbackHooks.sh.

## Editing UserCallbackHooks.sh

Navigate to Content Setup -> File Manager -> Scripts. Click on UserCallbackHooks.sh and click edit. Add the line `fpp -p <PLAYLIST_NAME>` to the post-start section above the `;;`. This command runs a playlist repeatedly and will execute on startup.

# Wikipedia
The wikipedia for this project can be found [here](https://elinux.org/ECE497_Project_-_LED_Matrix_Graduation_Cap#Executive_Summary).


