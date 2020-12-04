from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import PIL 
import urllib #importing to use its urlencode function
import urllib3 #for making http requests
import requests
import json #for decoding a JSON response
import pandas as pd
from datetime import datetime
import locale
import pymysql as MySQLdb
from io import BytesIO
from datetime import datetime, timedelta
from urllib.request import urlopen
import os
from collections import OrderedDict
from instabot import Bot

db = MySQLdb.connect("ip","user","password","db_names" )
cursor = db.cursor()

query="Select * from kanal"
df = pd.read_sql(query, con=db)

dun = datetime.today() - timedelta(days=1)
gun_ad = dun.strftime("%A")
dun = dun.strftime("%Y-%m-%d")


try:
    bot = Bot()
    bot.login(username="",password="")
except:
    pass

kanalID_list = df["ID"].unique()

gun_ad='Monday'

kanalID_list_son=[]
if gun_ad=='Monday':
    kanalID_list_son.append(kanalID_list[0])
    kanalID_list_son.append(kanalID_list[1])
elif gun_ad=='Tuesday':
    kanalID_list_son.append(kanalID_list[2])
    kanalID_list_son.append(kanalID_list[3])
elif gun_ad=='Wednesday':
    kanalID_list_son.append(kanalID_list[4])
    kanalID_list_son.append(kanalID_list[5])
elif gun_ad=='Thursday':
    kanalID_list_son.append(kanalID_list[6])
    kanalID_list_son.append(kanalID_list[7])
elif gun_ad=='Friday':
    kanalID_list_son.append(kanalID_list[8])
    kanalID_list_son.append(kanalID_list[9])
elif gun_ad=='Saturday':
    kanalID_list_son.append(kanalID_list[10])
    kanalID_list_son.append(kanalID_list[11])
elif gun_ad=='Sunday':
    kanalID_list_son.append(kanalID_list[12])
    kanalID_list_son.append(kanalID_list[13])



def watermark_photo(input_image_path,
                    output_image_path,
                    watermark_image_path,
                    position):
        base_image = Image.open(input_image_path)
        watermark = Image.open(watermark_image_path)
        base_image.paste(watermark, position)
        base_image.save(output_image_path)



font = ImageFont.truetype("/home/yonetici/font/arial.ttf", 45)
numara = ImageFont.truetype("/home/yonetici/font/arial.ttf", 150)
istatistik_font = ImageFont.truetype("/home/yonetici/font/arial.ttf", 45)


strip_width = 1700
strip_height = 520

def center_text(img, font, text, color=(255, 255, 255)):
    draw = ImageDraw.Draw(img)
    text_width, text_height = draw.textsize(text, font)
    position = ((strip_width-text_width)/2,(strip_height-text_height)/2)
    draw.text(position, text, color, font=font)
    return img

def center_text2(img, font, text, color=(255, 255, 255)):
    draw = ImageDraw.Draw(img)
    text_width, text_height = draw.textsize(text, font)
    position = ((1700-text_width)/2,(620-text_height)/2)
    draw.text(position, text, color, font=font)
    return img

def center_text3(img, font, text, color=(255, 255, 255)):
    draw = ImageDraw.Draw(img)
    text_width, text_height = draw.textsize(text, font)
    position = ((1700-text_width)/2,(200-text_height)/2)
    draw.text(position, text, color, font=font)
    return img






for kanalID in kanalID_list_son:
    try:
        query=f"Select distinct data.ad,kanal.ad as kanalad,kanal.tag,kanal.user_id,gunluk.data_videoID,gunluk.goruntulenme,gunluk.begenme,gunluk.begenmeme,gunluk.yorum,data.yuklenme_tarihi from gunluk,data,kanal where gunluk.kanal_ID='{kanalID}' AND gunluk.tarih='{dun}' AND data_videoID=data.videoID and kanal.ID='{kanalID}'"
        df = pd.read_sql(query, con=db)
        df2 = df.sort_values('yuklenme_tarihi',ascending=True)
        tag = df["tag"][0]
        
        user_id = df["user_id"][0]
        goruntulenme_ortalama= df2['goruntulenme'].mean()
        begenme_ortalama= df2['begenme'].mean()
        begenmeme_ortalama= df2['begenmeme'].mean()
        yorum_ortalama= df2['yorum'].mean()


        print(goruntulenme_ortalama)
        print(goruntulenme_ortalama*0.50)
        df2 = df2.drop(df2[df2.goruntulenme < goruntulenme_ortalama].index)
        df2 = df2.drop(df2[df2.begenme < begenme_ortalama].index)
        df2 = df2.drop('tag',1)
        df2 = df2.drop('user_id',1)
        df3 = df2.head(10)
        df3 = df3.sort_values('goruntulenme',ascending=False)
        print(df3)

        goruntulenmeler=[]
        begenmeler=[]
        begenmemeler=[]
        yorumlar=[]
        videoidler=[]
        yuklenme_tarihleri=[]
        adlar = []
        kanal=[]

        goruntulenme= df3['goruntulenme']
        begenme = df3['begenme']
        begenmeme = df3['begenmeme']
        yorum = df3['yorum']
        kanalad = df3['kanalad']
        video_liste = df3['data_videoID']
        yuklenme_tarih = df3['yuklenme_tarihi']
        ad = df3['ad']


        for i in goruntulenme:
            goruntulenmeler.append(i)
        for i in begenme:
            begenmeler.append(i)
        for i in begenmeme:
            begenmemeler.append(i)
        for i in yorum:
            yorumlar.append(i)
        for i in video_liste:
            videoidler.append(i)
        for i in yuklenme_tarih:
            yuklenme_tarihleri.append(i)
        for i in ad:
            Tr2Eng = str.maketrans("çğöşü", "cgosu")
            videoad = i
            videoad2 = videoad.translate(Tr2Eng)
            print(videoad2)
            adlar.append(videoad2)
        for i in kanalad:
            kanal.append(i)
        fotolar =[]

        for i in range(0,10):
            img = Image.open("arkaplaneski.jpg") #!
            draw = ImageDraw.Draw(img)

            draw.text((747, 135),dun,(255,255,255),font=font) #! tarih
            #draw.text((747, 100),kanal[i],(255,255,255),font=font) #! kanalad
            center_text3(img,font,kanal[i]) 

            url = f"https://img.youtube.com/vi/{videoidler[i]}/maxresdefault.jpg"
            videofoto = Image.open(urlopen(url))
            resim=videofoto.resize((960,540),PIL.Image.ANTIALIAS)
            resim.save("videofoto.jpg")

            draw.text((1280, 392),str(goruntulenmeler[i]),(255,255,255),font=istatistik_font) #! goruntulenme
            draw.text((1280, 558),str(begenmeler[i]),(255,255,255),font=istatistik_font) #! begenme
            draw.text((1280, 726),str(begenmemeler[i]),(255,255,255),font=istatistik_font) #! begenmeme
            draw.text((1280, 870),str(yorumlar[i]),(255,255,255),font=istatistik_font) #! yorum
            videoad= adlar[i]
            center_text(img,font,videoad[:80])    
            center_text2(img,font,yuklenme_tarihleri[i].strftime("%Y-%m-%d"))
            img.save('eskivideo2.jpg')
            img = 'eskivideo2.jpg'

            watermark_photo(img, f'{i}.jpg',"videofoto.jpg", position=(60,390))
            fotolar.append(f"{i}.jpg")

        users_to_tag = []
        x = 0.5
        y = 0.1

        if len(user_id.split(","))!=1:
            user = user_id.split(",")
            for j in user:
                print(j)
                s = {'user_id': j, 'x': x, 'y': y}
                users_to_tag.append(s)
                x += 0.1
                y += 0.1
        else:
            s = {'user_id': user_id, 'x': x, 'y': y}
            users_to_tag.append(s)    

        try:
            bot.upload_album(fotolar,user_tags= users_to_tag,caption=f"{kanal[i]} Kanalının {dun} tarihinde ki günlük izlenmesi baz alınmıştır.\n\n{kanal[i]} Kanalının Eski Videolarından İstatistik Verileri Dikkat Çeken Videoları\n\nBu videolar günlük video başına düşen izlenme ortalaması baz alınarak listelenmiştir.\n\n\n\n#youtube #youtubetürkiye #enesbatur #basakkarahan #delimine #reynmen #orkunışıtmak #twitchturkiye #wtcnn #hazretiyasuo #hzyasuo #evonmoss #twitch #kafalar #alibicim #mesutcantomay #babala #oguzhanugur #magazin #youtubemagazin")
        except Exception as e:
            print(e)
        os.remove("0.jpg.REMOVE_ME")
        os.remove("1.jpg.REMOVE_ME")
        os.remove("2.jpg.REMOVE_ME")
        os.remove("3.jpg.REMOVE_ME")
        os.remove("4.jpg.REMOVE_ME")
        os.remove("5.jpg.REMOVE_ME")
        os.remove("6.jpg.REMOVE_ME")
        os.remove("7.jpg.REMOVE_ME")
        os.remove("8.jpg.REMOVE_ME")
        os.remove("9.jpg.REMOVE_ME")
    except Exception as e:
        print(e)