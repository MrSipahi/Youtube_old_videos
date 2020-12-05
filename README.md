# What is it ?

  
This program analyzes the daily statistics of the YouTube channel in the database, sorts the old videos that attracting attention and shares them as an album on the Instagram page. 


![enter image description here](https://github.com/MrSipahi/Youtube_old_videos/blob/main/photo/post.PNG?raw=true)


# How does it work

For this application  to work, there must be a table named 'gunluk' in the database. The program obtains daily statistics data of youtube channels from the table named 'gunluk'.

 ![enter image description here](https://github.com/MrSipahi/Youtube_Top_List/blob/main/photo/gunluk_table.PNG?raw=true)


It determines the average number of views, likes, dislikes and comments per video by looking at the channel's total statistics throughout the day. It lists videos that are above this average by the date they were posted. The statistics data of these videos are written in a template, the video photo is placed and shared as an album on the Instagram page.




#  Technologies

 - [Mysql](https://www.mysql.com/)
 - [Python](https://www.python.org/)
 - [Pandas](https://pypi.org/project/pandas/)
 - [Matplotlib](https://pypi.org/project/matplotlib/)
 - [Pillow](https://pypi.org/project/Pillow/)
 - [Instabot](https://pypi.org/project/instabot/)
 - [Youtube Data API](https://developers.google.com/youtube/v3)
 - [Requests](https://pypi.org/project/requests/)


 

