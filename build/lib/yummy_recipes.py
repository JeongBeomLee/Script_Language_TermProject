import tkinter as tk
from PIL import ImageTk, Image
import json
from tkinter import font, ttk
import requests
from io import BytesIO
import random
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib
import telepot
from telepot.loop import MessageLoop
import spam
from distutils.core import setup

class MyApplication:
    def __init__(self, width, height, zoom=15):
        self.width = width
        self.height = height
        self.zoom = zoom
        self.window = tk.Tk()
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.title("termproject")
        self.TOKEN = '6176456356:AAFea3eqai6ryb6UECrlJUDvseRfkvbboWo'  # 여기에 Telegram 봇 토큰을 입력하세요
        self.bot = telepot.Bot(self.TOKEN)

        # 이미지 로드
        self.image1 = Image.open("Button1.png")
        self.image2 = Image.open("Button2.png")
        self.image3 = Image.open("Button3.png")
        self.image4 = Image.open("Button4.png")
        self.image5 = Image.open("bg.png")
        self.image6 = Image.open("bg2.png")
        self.image7 = Image.open("Page2.png")
        self.image8 = Image.open("Button5.png")
        self.image9 = Image.open("Button6.png")
        self.image10 = Image.open("Button7.png")
        self.image11 = Image.open("Page1.png")
        self.image12 = Image.open("Button8.png")
        self.image13 = Image.open("Button9.png")
        # 버튼 이미지 추가
        self.image14 = Image.open("Button10.png")
        self.image15 = Image.open("Button11.png")
        self.image16 = Image.open("Button12.png")
        self.image17 = Image.open("Button13.png")
        self.image18 = Image.open("Button14.png")
        self.image19 = Image.open("Button15.png")
        self.image20 = Image.open("Button16.png")
        self.image21 = Image.open("Button17.png")
        self.image22 = Image.open("Button18.png")
        self.image23 = Image.open("Button19.png")
        self.image24 = Image.open("Button20.png")
        self.image25 = Image.open("Page3.png")
        self.image26 = Image.open("Page4.png")
        self.image28 = Image.open("Button21.png")
        self.image29 = Image.open("Button22.png")

        # 이미지 크기 조정
        self.image1 = self.image1.resize((50, 50), Image.LANCZOS)
        self.image2 = self.image2.resize((50, 50), Image.LANCZOS)
        self.image3 = self.image3.resize((50, 50), Image.LANCZOS)
        self.image4 = self.image4.resize((50, 50), Image.LANCZOS)
        self.image6 = self.image6.resize((480, 440), Image.LANCZOS)
        self.image7 = self.image7.resize((160, 60), Image.LANCZOS)
        self.image8 = self.image8.resize((25, 25), Image.LANCZOS)
        self.image9 = self.image9.resize((25, 25), Image.LANCZOS)
        self.image10 = self.image10.resize((25, 25), Image.LANCZOS)
        self.image11 = self.image11.resize((160, 60), Image.LANCZOS)
        self.image12 = self.image12.resize((80, 30), Image.LANCZOS)
        self.image13 = self.image13.resize((80, 30), Image.LANCZOS)
        # 버튼 이미지 추가
        self.image14 = self.image14.resize((51, 25), Image.LANCZOS)
        self.image15 = self.image15.resize((51, 25), Image.LANCZOS)
        self.image16 = self.image16.resize((51, 25), Image.LANCZOS)
        self.image17 = self.image17.resize((51, 25), Image.LANCZOS)
        self.image18 = self.image18.resize((51, 25), Image.LANCZOS)
        self.image19 = self.image19.resize((51, 25), Image.LANCZOS)
        self.image20 = self.image20.resize((51, 25), Image.LANCZOS)
        self.image21 = self.image21.resize((51, 25), Image.LANCZOS)
        self.image22 = self.image22.resize((51, 25), Image.LANCZOS)
        self.image23 = self.image23.resize((51, 25), Image.LANCZOS)
        self.image24 = self.image24.resize((25, 25), Image.LANCZOS)
        self.image25 = self.image25.resize((160, 60), Image.LANCZOS)
        self.image26 = self.image26.resize((160, 60), Image.LANCZOS)
        self.image27 = self.image6.resize((550, 425), Image.LANCZOS)
        self.image28 = self.image28.resize((30, 30), Image.LANCZOS)
        self.image29 = self.image29.resize((30, 30), Image.LANCZOS)

        # PhotoImage 객체 생성
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.photo3 = ImageTk.PhotoImage(self.image3)
        self.photo4 = ImageTk.PhotoImage(self.image4)
        self.photo5 = ImageTk.PhotoImage(self.image5)
        self.photo6 = ImageTk.PhotoImage(self.image6)
        self.photo7 = ImageTk.PhotoImage(self.image7)
        self.photo8 = ImageTk.PhotoImage(self.image8)
        self.photo9 = ImageTk.PhotoImage(self.image9)
        self.photo10 = ImageTk.PhotoImage(self.image10)
        self.photo11 = ImageTk.PhotoImage(self.image11)
        self.photo12 = ImageTk.PhotoImage(self.image12)
        self.photo13 = ImageTk.PhotoImage(self.image13)
        # 버튼 이미지 추가
        self.photo14 = ImageTk.PhotoImage(self.image14)
        self.photo15 = ImageTk.PhotoImage(self.image15)
        self.photo16 = ImageTk.PhotoImage(self.image16)
        self.photo17 = ImageTk.PhotoImage(self.image17)
        self.photo18 = ImageTk.PhotoImage(self.image18)
        self.photo19 = ImageTk.PhotoImage(self.image19)
        self.photo20 = ImageTk.PhotoImage(self.image20)
        self.photo21 = ImageTk.PhotoImage(self.image21)
        self.photo22 = ImageTk.PhotoImage(self.image22)
        self.photo23 = ImageTk.PhotoImage(self.image23)
        self.photo24 = ImageTk.PhotoImage(self.image24)
        self.photo25 = ImageTk.PhotoImage(self.image25)
        self.photo26 = ImageTk.PhotoImage(self.image26)
        self.photo27 = ImageTk.PhotoImage(self.image27)
        self.photo28 = ImageTk.PhotoImage(self.image28)
        self.photo29 = ImageTk.PhotoImage(self.image29)

        # 페이지 생성
        self.page1 = tk.Frame(self.window, width=800, height=600)
        self.page2 = tk.Frame(self.window, width=800, height=600)
        self.page3 = tk.Frame(self.window, width=800, height=600)
        self.page4 = tk.Frame(self.window, width=800, height=600)
        
        # 버튼 초기화
        self.button1 = None
        self.button2 = None
        self.button3 = None
        self.button4 = None
        self.button5 = None
        self.button6 = None
        self.button7 = None
        self.button8 = None
        self.button9 = None
        # 버튼 추가
        self.button10 = None
        self.button11 = None
        self.button12 = None
        self.button13 = None
        self.button14 = None
        self.button15 = None
        self.button16 = None
        self.button17 = None
        self.button18 = None
        self.button19 = None
        self.button20 = None
        self.button21 = None

        # 첫 번째 페이지
        label1 = tk.Label(self.page1, width=800, height=600, image=self.photo5)
        self.page2_image1 = tk.Label(self.page1, image=self.photo11, bg='white')
        self.page2_image1.place(x=10, y=10)
        
        # 페이지에 넣을 내용 추가
        # 레시피 레이블
        self.page1_recipe_label = tk.Label(self.page1, width=480, height=440, bg='#DEDBD2', image=self.photo6)
        self.page1_recipe_label.place(x=160, y=80)
        
        # 레시피 이름, 재료(여기에 메뉴얼도 표시), 이미지 레이블
        self.page1_recipe_name_label = tk.Label(self.page1, wraplength=425, bg='#F7F6F4')
        self.page1_recipe_dtls_label = tk.Label(self.page1, wraplength=425, bg='#F7F6F4')
        self.page1_recipe_image_label = tk.Label(self.page1, width=200, height=200, bg='#DEDBD2')
                
        # ####
        label1.pack()

        # 두 번째 페이지
        label2 = tk.Label(self.page2, width=800, height=600, image=self.photo5)
        self.page2_image1 = tk.Label(self.page2, image=self.photo7, bg='white')
        self.page2_image1.place(x=10, y=10)

        # 페이지에 넣을 내용 추가
        self.page2_listbox = tk.Listbox(self.page2, width=40, height=29)
        self.page2_listbox.place(x=10, y=120)

        self.scrollbar = tk.Scrollbar(self.page2)
        self.page2_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.page2_listbox.yview)
        self.scrollbar.place(x=280, y=120, height=468)

        # 선택된 레시피의 이미지와 재료 정보를 표시할 레이블
        self.page2_recipe_label = tk.Label(self.page2, width=480, height=440, bg='#DEDBD2', image=self.photo6)
        self.page2_recipe_label.place(x=308, y=80)
        self.page2_recipe_name_label = tk.Label(self.page2, wraplength=425, bg='#F7F6F4')
        self.page2_recipe_dtls_label = tk.Label(self.page2, wraplength=425, bg='#F7F6F4')
        self.page2_recipe_image_label = tk.Label(self.page2, width=200, height=200, bg='#DEDBD2')

        # 오름차순 내림차순 정렬 버튼들
        self.button10 = tk.Button(self.page2, image=self.photo14, command=self.sort_recipes_by_calories, bg='white')
        self.button12 = tk.Button(self.page2, image=self.photo16, command=self.sort_recipes_by_car, bg='white')
        self.button14 = tk.Button(self.page2, image=self.photo18, command=self.sort_recipes_by_pro, bg='white')
        self.button16 = tk.Button(self.page2, image=self.photo20, command=self.sort_recipes_by_fat, bg='white')
        self.button18 = tk.Button(self.page2, image=self.photo22, command=self.sort_recipes_by_na, bg='white')
        
        self.button10.place(x=10, y=82)
        self.button12.place(x=10 + 55, y=82)
        self.button14.place(x=10 + 110, y=82)
        self.button16.place(x=10 + 165, y=82)
        self.button18.place(x=10 + 220, y=82)
        
        # ####
        label2.pack()

        # 세 번째 페이지
        label3 = tk.Label(self.page3, width=800, height=600, image=self.photo5)
        # 페이지에 넣을 내용 추가
        self.page3_image1 = tk.Label(self.page3, image=self.photo25, bg='white')
        self.page3_image1.place(x=10, y=10)

        # 페이지에 넣을 내용 추가
        self.page3_listbox = tk.Listbox(self.page3, width=40, height=29)
        self.page3_listbox.place(x=10, y=120)

        self.scrollbar = tk.Scrollbar(self.page3)
        self.page3_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.page3_listbox.yview)
        self.scrollbar.place(x=280, y=120, height=468)

        # 선택된 레시피의 이미지와 재료 정보를 표시할 레이블
        self.page3_recipe_label = tk.Label(self.page3, width=480, height=440, bg='#DEDBD2', image=self.photo6)
        self.page3_recipe_label.place(x=308, y=80)
        self.page3_recipe_name_label = tk.Label(self.page3, wraplength=425, bg='#F7F6F4')
        self.page3_recipe_dtls_label = tk.Label(self.page3, wraplength=425, bg='#F7F6F4')
        self.page3_recipe_image_label = tk.Label(self.page3, width=200, height=200, bg='#DEDBD2')
        
        # 검색 기능을 위한 검색 박스와 검색 버튼 추가
        self.search_entry = tk.Entry(self.page3, width=23, font=('Arial', 14))
        self.search_entry.place(x=10, y=83)
        self.search_button = tk.Button(self.page3, bg='#F7F6F4', width=25, height=25, font=('Arial', 12), command=self.search_recipes, image=self.photo24)
        self.search_button.place(x=269, y=81)
        # ####
        label3.pack()

        # 네 번째 페이지
        label4 = tk.Label(self.page4, width=800, height=600, image=self.photo5)
        
        # 페이지에 넣을 내용 추가
        #네 번째 페이지 모양잡기 - 라벨 
        self.title = tk.Label(self.page4,image=self.photo26 ,bg='white',width=160,height=60)
        self.title.place(x=10,y=10)
       
        self.city_dict = {'경기도': ('수원시','성남시','의정부시','안양시','부천시','광명시','평택시','동두천시','안산시','고양시','과천시','구리시','남양주시'
                     ,'오산시','시흥시','군포시','의왕시','하남시','용인시','파주시','이천시','안성시','김포시','화성시','광주시','양주시,'
                     ,'포천시','여주시','연천군','가평군','양평군'),
            '충청북도': ('청주시', '충주시', '제천시','보은군','옥천군','영동군','증평군','진천군','괴산군','음성군','단양군'),
            '충청남도': ('천안시','공주시','보령시','아산시','서산시','논산시','계룡시','당진시','금산군','부여군','서천군','청양군','홍성군','예산군','태안군'),
            '서울특별시': ('종로구','중구','용산구','성동구','광진구','동대문구','중랑구','성북구','강북구','도봉구','노원구','은평구','서대문구','마포구','양천구','강서구','구로구'
                     ,'금천구','영등포구','동작구','관악구','서초구','강남구','송파구','강동구'),
            '강원도': ('춘천시','원주시','강릉시','동해시','태백시','속초시','삼척시','홍천군','횡성군','영월군','평창군','정선군','철원군','화천군',
                     '양구군','인제군','고성군','양양군'),
            '전라북도':('전주시','군산시','익산시','정읍시','남원시','김제시','완주군','진안군','무주군','장수군','임실군','순창군','고창군','부안군'),
            '전라남도':('목포시','여수시','순천시','나주시','광양시','담양군','곡성군','구례군','고흥군','보성군','화순군','장흥군','강진군','해남군',
                     '영암군','무안군','함평군','영광군','장성군','완도군','진도군','신안군'),
            '경상북도':('포항시','경주시','김천시','안동시','구미시','영주시','영천시','상주시','문경시','경산시','군위군''의성군','청송군','영양군','영덕군',
                     '청도군','고령군','성주군','칠곡군','예천군','봉화군','울진군','울릉군'),
            '경상남도':('창원시','진주시','통영시','사천시','김해시','밀양시','거제시','양산시','의령군','함안군','창녕군','고성군','남해군','하동군','산청군','함양군',
                     '거창군','합천군'),
            '전라북도':('전주시','군산시','익산시','정읍시','남원시','김제시','완주군','진안군','무주군','장수군','임실군','순창군','고창군','부안군'),
            '전라남도':('목포시','여수시','순천시','나주시','광양시','담양군','곡성군','구례군','고흥군','보성군','화순군','장흥군','강진군','해남군'
                    ,'영암군','무안군','함평군','영광군','장성군','완도군','진도군','신안군')}
        
        def update_combo(*args):
            self.city_combo['values'] = self.city_dict[self.province_var.get()]

        def on_listbox_select(event):
            index = self.supermarket_list.curselection()[0]
            self.place_id = self.place_ids[index]
            show_map(self.place_id)
        
        def get_location(city_name):
            geocoding_url = "https://maps.googleapis.com/maps/api/geocode/json"
            geocoding_params = {
                "address": city_name,
                "key": "AIzaSyBJR7j7Dimxije82k_joAteqrYt3czAvrk"
            }
            geocoding_response = requests.get(geocoding_url, params=geocoding_params)
            geocoding_data = geocoding_response.json()
            if geocoding_data['status'] != 'OK':
                print("Geocoding API Error: {}".format(geocoding_data['status']))
                return None
            location = geocoding_data['results'][0]['geometry']['location']
            return "{},{}".format(location['lat'], location['lng'])

        def find_supermarkets():
            selected_city = self.city_var.get()
            location = get_location(selected_city)
            if location is None:
                return
            url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
            params = {
                "location": location,
                "radius": 3000,
                "type": "supermarket",
                "key": "AIzaSyBJR7j7Dimxije82k_joAteqrYt3czAvrk"
            }
            response = requests.get(url, params=params)
            data = response.json()
            self.supermarket_list.delete(0, tk.END)
            self.place_ids = []
            for place in data['results']:
                self.supermarket_list.insert(tk.END, place['name'])
                self.place_ids.append(place['place_id'])
        
        def show_map(place_id):
            # Place Details API를 사용하여 place_id에 대한 상세 정보를 얻습니다.
            place_url = "https://maps.googleapis.com/maps/api/place/details/json"
            place_params = {
                "place_id": place_id,
                "key": "AIzaSyBJR7j7Dimxije82k_joAteqrYt3czAvrk"
            }
            place_response = requests.get(place_url, params=place_params)
            place_data = place_response.json()
            location = place_data['result']['geometry']['location']
            lat, lng = location['lat'], location['lng']

            # Static Maps API를 사용하여 해당 위치의 지도 이미지를 얻습니다.
            map_url = "https://maps.googleapis.com/maps/api/staticmap"
            map_params = {
                "center": "{},{}".format(lat, lng),
                "zoom": self.zoom,
                "size": "400x300",
                "markers": "{},{}".format(lat, lng),
                "key": "AIzaSyBJR7j7Dimxije82k_joAteqrYt3czAvrk"
            }
            map_response = requests.get(map_url, params=map_params)

            # 응답으로 받은 이미지를 표시합니다.
            map_image = Image.open(BytesIO(map_response.content))
            map_photo = ImageTk.PhotoImage(map_image)

            # 기존에 생성된 라벨이 있으면 삭제합니다.
            if hasattr(self, 'map_label'):
                self.map_label.destroy()

            # 새로운 라벨을 생성하고 지도 이미지를 표시합니다.
            self.map_label = tk.Label(self.page4, image= map_photo)
            self.map_label.image = map_photo  # 이 라인이 없으면 이미지가 표시되지 않을 수 있습니다.
            self.map_label.place(x=304, y=150)
            
        def zoom_in():
            self.zoom += 1
            show_map(self.place_id)
    
        def zoom_out():
            self.zoom -= 1
            show_map(self.place_id)
            
        self.province_var = tk.StringVar()
        self.city_var = tk.StringVar()
        
        # 지도 배경
        self.map_bg_label = tk.Label(self.page4, image= self.photo27, width=546, height=420)
        self.map_bg_label.place(x=234, y=90)
        
        #콤보박스 크기 더 크게 변경 핉요
        self.province_combo = ttk.Combobox(self.page4,textvariable=self.province_var, width=9, height=5)
        self.province_combo.place(x=10, y=90)
        self.province_combo['values'] = ('경기도', '충청북도', '충청남도', '서울특별시', '강원도','전라남도','전라북도')
        self.province_combo.bind("<<ComboboxSelected>>", update_combo)

        self.city_combo = ttk.Combobox(self.page4, textvariable=self.city_var, width=9, height=5)
        self.city_combo.place(x=100, y=90)

        #슈퍼마켓 리스트 
        self.supermarket_list = tk.Listbox(self.page4, bg = 'white',width=29,height=24)
        self.supermarket_list.place(x=10, y=125)
        self.supermarket_list.bind("<<ListboxSelect>>", on_listbox_select)

        #슈퍼마켓 선택 버튼
        self.search_button = tk.Button(self.page4, image=self.photo24, command=find_supermarkets)
        self.search_button.place(x=190, y=88)
        
        # 줌인 줌아웃
        self.button20 = tk.Button(self.page4, image=self.photo28, command=zoom_in)
        self.button20.place(x=680, y=460)
        self.button21 = tk.Button(self.page4, image=self.photo29, command=zoom_out)
        self.button21.place(x=720, y=460)
        
        # ####
        label4.pack()

        # JSON 파일 읽기
        file_path = "recipes.json"
        with open(file_path, "r", encoding="utf-8") as file:
            # JSON 데이터 로드
            self.data = json.load(file)

        # 'RCP_NM' 내용을 리스트박스에 추가
        self.recipes = self.data['COOKRCP01']['row']
        for item in self.recipes:
            recipe_name = item['RCP_NM']
            self.page2_listbox.insert(tk.END, recipe_name)

        self.page2_listbox.bind('<<ListboxSelect>>', self.show_page2_recipe_details)

        self.page3_listbox.bind('<<ListboxSelect>>', self.show_page3_recipe_details)
        
        self.current_page = self.page1  # 현재 표시되는 페이지
        self.current_page.pack()  # 첫 번째 페이지 표시
        self.show_button()
        self.show_random_recipe()
        self.telegram()
        self.window.mainloop()

    def show_button(self):
        # 버튼 생성과 배치
        self.button1 = tk.Button(self.window, image=self.photo1, command=self.show_page1, bg='white')
        self.button2 = tk.Button(self.window, image=self.photo2, command=self.show_page2, bg='white')
        self.button3 = tk.Button(self.window, image=self.photo3, command=self.show_page3, bg='white')
        self.button4 = tk.Button(self.window, image=self.photo4, command=self.show_page4, bg='white')

        self.button1.place(x=575, y=540)  # 첫 번째 버튼 위치
        self.button2.place(x=630, y=540)  # 두 번째 버튼 위치
        self.button3.place(x=685, y=540)  # 세 번째 버튼 위치
        self.button4.place(x=740, y=540)  # 네 번째 버튼 위치

    def show_page1(self):
        self.current_page.pack_forget()  # 현재 페이지 숨기기
        self.current_page = self.page1
        self.current_page.pack()  # 새로운 페이지 표시
        self.show_button()
        self.show_random_recipe()
        self.page1_recipe_dtls_label.config(text='')
        if self.button5:
            self.button5.destroy()
        if self.button6:
            self.button6.destroy()
        if self.button7:
            self.button7.destroy()
        self.manual_index = 0
        
        # 'RCP_NM' 내용을 리스트박스에 추가
        self.recipes = self.data['COOKRCP01']['row']
        for item in self.recipes:
            recipe_name = item['RCP_NM']
            self.page2_listbox.insert(tk.END, recipe_name)

    def show_page2(self):
        self.current_page.pack_forget()
        self.current_page = self.page2
        self.current_page.pack()
        self.show_button()
        self.manual_index = 0
        
        # 'RCP_NM' 내용을 리스트박스에 추가
        self.recipes = self.data['COOKRCP01']['row']
        for item in self.recipes:
            recipe_name = item['RCP_NM']
            self.page2_listbox.insert(tk.END, recipe_name)

    def show_page3(self):
        self.current_page.pack_forget()
        self.current_page = self.page3
        self.current_page.pack()
        self.show_button()

    def show_page4(self):
        self.current_page.pack_forget()
        self.current_page = self.page4
        self.current_page.pack()
        self.show_button()
        
    def show_page1_recipe_details(self):
        if self.button8:
            self.button8.destroy()
        if self.button9:
            self.button9.destroy()
        
        # 레시피 재료 표시
        recipe_dtls = self.recipe['RCP_PARTS_DTLS']
        recipe_dtls_padded = '          ' * 900 + recipe_dtls  # 패딩 적용
        self.page1_recipe_dtls_label.config(font=font.Font(family='BM HANNA Pro', size=10, weight='normal'), fg='#574413')
        self.page1_recipe_dtls_label.config(text=recipe_dtls_padded)
        self.page1_recipe_dtls_label.place(x=185, y=370)

        # 레시피 이름 표시
        recipe_name = self.recipe['RCP_NM']
        recipe_name_padded = '          ' * 900 + recipe_name  # 패딩 적용
        self.page1_recipe_name_label.config(font=font.Font(family='BM HANNA Pro', size=21, weight='bold'), fg='#574413')
        self.page1_recipe_name_label.config(text=recipe_name_padded)
        self.page1_recipe_name_label.place(x=185, y=310)
        
        # 레시피 이미지 로드
        recipe_image_url = self.recipe['ATT_FILE_NO_MAIN']
        try:
            # 레시피 이미지 표시
            response = requests.get(recipe_image_url)
            recipe_image = Image.open(BytesIO(response.content))
            recipe_image = recipe_image.resize((200, 200), Image.LANCZOS)
            self.recipe_image_tk = ImageTk.PhotoImage(recipe_image)
            self.page1_recipe_image_label.config(image=self.recipe_image_tk)
            self.page1_recipe_image_label.place(x=300, y=120)
        except Exception as e:
            print(f"Failed to load recipe image: {e}")
        
        # 버튼 표시
        self.button5 = tk.Button(self.page1, image=self.photo8, command=self.show_previous_manual, bg='white')
        self.button6 = tk.Button(self.page1, image=self.photo9, command=self.show_next_manual, bg='white')
        self.button7 = tk.Button(self.page1, image=self.photo10, command=self.show_nutrition_chart, bg='white')

        self.button7.place(x=665 - 150, y=105)
        self.button5.place(x=700 - 150, y=105)
        self.button6.place(x=735 - 150, y=105)

        # MANUAL_IMG 및 MANUAL 표시
        self.manual_index = 0

    def show_page2_recipe_details(self, event):
        selection = self.page2_listbox.curselection()
        if selection:
            index = selection[0]
            self.recipe = self.recipes[index]

            # 레시피 재료 표시
            recipe_dtls = self.recipe['RCP_PARTS_DTLS']
            recipe_dtls_padded = '          ' * 900 + recipe_dtls  # 패딩 적용
            self.page2_recipe_dtls_label.config(font=font.Font(family='BM HANNA Pro', size=10, weight='normal'), fg='#574413')
            self.page2_recipe_dtls_label.config(text=recipe_dtls_padded)
            self.page2_recipe_dtls_label.place(x=335, y=370)

            # 레시피 이름 표시
            recipe_name = self.recipe['RCP_NM']
            recipe_name_padded = '          ' * 900 + recipe_name  # 패딩 적용
            self.page2_recipe_name_label.config(font=font.Font(family='BM HANNA Pro', size=21, weight='bold'), fg='#574413')
            self.page2_recipe_name_label.config(text=recipe_name_padded)
            self.page2_recipe_name_label.place(x=335, y=280)
            
            # 레시피 이미지 로드
            recipe_image_url = self.recipe['ATT_FILE_NO_MAIN']
            try:
                # 레시피 이미지 표시
                response = requests.get(recipe_image_url)
                recipe_image = Image.open(BytesIO(response.content))
                recipe_image = recipe_image.resize((200, 200), Image.LANCZOS)
                self.recipe_image_tk = ImageTk.PhotoImage(recipe_image)
                self.page2_recipe_image_label.config(image=self.recipe_image_tk)
                self.page2_recipe_image_label.place(x=445, y=105)
            except Exception as e:
                print(f"Failed to load recipe image: {e}")

            # 버튼 표시
            self.button5 = tk.Button(self.page2, image=self.photo8, command=self.show_previous_manual, bg='white')
            self.button6 = tk.Button(self.page2, image=self.photo9, command=self.show_next_manual, bg='white')
            self.button7 = tk.Button(self.page2, image=self.photo10, command=self.show_nutrition_chart, bg='white')

            self.button7.place(x=665, y=105)
            self.button5.place(x=700, y=105)
            self.button6.place(x=735, y=105)

            # MANUAL_IMG 및 MANUAL 표시
            self.manual_index = 0
            
    def show_page3_recipe_details(self, event):
        selection = self.page3_listbox.curselection()
        if selection:
            index = selection[0]
            self.recipe = self.search_recipes[index]

            # 레시피 재료 표시
            recipe_dtls = self.recipe['RCP_PARTS_DTLS']
            recipe_dtls_padded = '          ' * 900 + recipe_dtls  # 패딩 적용
            self.page3_recipe_dtls_label.config(font=font.Font(family='BM HANNA Pro', size=10, weight='normal'), fg='#574413')
            self.page3_recipe_dtls_label.config(text=recipe_dtls_padded)
            self.page3_recipe_dtls_label.place(x=335, y=370)

            # 레시피 이름 표시
            recipe_name = self.recipe['RCP_NM']
            recipe_name_padded = '          ' * 900 + recipe_name  # 패딩 적용
            self.page3_recipe_name_label.config(font=font.Font(family='BM HANNA Pro', size=21, weight='bold'), fg='#574413')
            self.page3_recipe_name_label.config(text=recipe_name_padded)
            self.page3_recipe_name_label.place(x=335, y=280)
            
            # 레시피 이미지 로드
            recipe_image_url = self.recipe['ATT_FILE_NO_MAIN']
            try:
                # 레시피 이미지 표시
                response = requests.get(recipe_image_url)
                recipe_image = Image.open(BytesIO(response.content))
                recipe_image = recipe_image.resize((200, 200), Image.LANCZOS)
                self.recipe_image_tk = ImageTk.PhotoImage(recipe_image)
                self.page3_recipe_image_label.config(image=self.recipe_image_tk)
                self.page3_recipe_image_label.place(x=445, y=105)
            except Exception as e:
                print(f"Failed to load recipe image: {e}")

            # 버튼 표시
            self.button5 = tk.Button(self.page3, image=self.photo8, command=self.show_previous_manual, bg='white')
            self.button6 = tk.Button(self.page3, image=self.photo9, command=self.show_next_manual, bg='white')
            self.button7 = tk.Button(self.page3, image=self.photo10, command=self.show_nutrition_chart, bg='white')

            self.button7.place(x=665, y=105)
            self.button5.place(x=700, y=105)
            self.button6.place(x=735, y=105)

            # MANUAL_IMG 및 MANUAL 표시
            self.manual_index = 0
            
    def show_previous_manual(self):
        self.manual_index -= 1
        if self.manual_index < 1:
            self.manual_index = 1
        self.show_manual()

    def show_next_manual(self):
        self.manual_index += 1
        if self.manual_index > 20:
            self.manual_index = 20
        self.show_manual()

    def show_manual(self):
        manual_img_key = f"MANUAL_IMG{str(self.manual_index).zfill(2)}"
        manual_key = f"MANUAL{str(self.manual_index).zfill(2)}"

        if manual_img_key in self.recipe and self.recipe[manual_img_key]:
            manual_img_url = self.recipe[manual_img_key]
            try:
                response = requests.get(manual_img_url)
                manual_img = Image.open(BytesIO(response.content))
                manual_img = manual_img.resize((200, 200), Image.LANCZOS)
                manual_img_tk = ImageTk.PhotoImage(manual_img)
                if self.current_page == self.page1:
                    self.page1_recipe_image_label.config(image=manual_img_tk)
                    self.page1_recipe_image_label.image = manual_img_tk
                elif self.current_page == self.page2:
                    self.page2_recipe_image_label.config(image=manual_img_tk)
                    self.page2_recipe_image_label.image = manual_img_tk
                elif self.current_page == self.page3:
                    self.page3_recipe_image_label.config(image=manual_img_tk)
                    self.page3_recipe_image_label.image = manual_img_tk
            except Exception as e:
                print(f"Failed to load manual image: {e}")
        else:
            if self.current_page == self.page1:
                self.page1_recipe_image_label.config(image=self.recipe_image_tk)
            elif self.current_page == self.page2:
                self.page2_recipe_image_label.config(image=self.recipe_image_tk)
            elif self.current_page == self.page3:
                self.page3_recipe_image_label.config(image=self.recipe_image_tk)

        if manual_key in self.recipe and self.recipe[manual_key]:
            manual_text = self.recipe[manual_key]
            manual_text_padded = '          ' * 900 + manual_text # 패딩 적용
            if self.current_page == self.page1:
                self.page1_recipe_dtls_label.config(font=font.Font(family='BM HANNA Pro', size=15, weight='bold'), fg='#574413')
                self.page1_recipe_dtls_label.config(text=manual_text_padded)
                self.page1_recipe_dtls_label.place(x=185, y=370)
            elif self.current_page == self.page2:
                self.page2_recipe_dtls_label.config(font=font.Font(family='BM HANNA Pro', size=15, weight='bold'), fg='#574413')
                self.page2_recipe_dtls_label.config(text=manual_text_padded)
                self.page2_recipe_dtls_label.place(x=335, y=345)
            elif self.current_page == self.page3:
                self.page3_recipe_dtls_label.config(font=font.Font(family='BM HANNA Pro', size=15, weight='bold'), fg='#574413')
                self.page3_recipe_dtls_label.config(text=manual_text_padded)
                self.page3_recipe_dtls_label.place(x=335, y=345)
        else:
            self.manual_index -= 1
            
    def show_random_recipe(self):
        random_seq = random.randint(1, 1115)  # 1부터 1114 사이의 랜덤한 숫자 생성
        recipe = None
        
        # 좋아요, 싫어요 버튼이 있다면 없애기
        if self.button8:
            self.button8.destroy()
        if self.button9:
            self.button9.destroy()
            
        # 랜덤한 RCP_SEQ 값을 가지고 있는 레시피 검색
        for item in self.recipes:
            if int(item['RCP_SEQ']) == random_seq:
                recipe = item
                self.recipe = recipe
                break

        if recipe:
            recipe_image_url = recipe['ATT_FILE_NO_MK']
            recipe_name = recipe['RCP_NM']

            # 레시피 이미지 로드
            try:
                # 레시피 이미지 표시
                response = requests.get(recipe_image_url)
                recipe_image = Image.open(BytesIO(response.content))
                recipe_image = recipe_image.resize((200, 200), Image.LANCZOS)
                self.recipe_image_tk = ImageTk.PhotoImage(recipe_image)
                self.page1_recipe_image_label.config(image=self.recipe_image_tk)
                self.page1_recipe_image_label.place(x=300, y=120)
            except Exception as e:
                print(f"Failed to load recipe image: {e}")
            
            # 레시피 이름 표시
            recipe_name_padded = '          ' * 900 + '오늘은 ' + recipe_name + ' 어떠세요?'  # 패딩 적용
            self.page1_recipe_name_label.config(font=font.Font(family='BM HANNA Pro', size=21, weight='bold'), fg='#574413')
            self.page1_recipe_name_label.config(text=recipe_name_padded)
            self.page1_recipe_name_label.place(x=185, y=310)
                
            # 버튼 표시
            # 좋아요
            self.button8 = tk.Button(self.page1, image=self.photo12, command=self.show_page1_recipe_details, bg='white')
            # 싫어요
            self.button9 = tk.Button(self.page1, image=self.photo13, command=self.show_random_recipe, bg='white')

            self.button8.place(x=265, y=430)
            self.button9.place(x=445, y=430)
                    
            self.manual_index = 0
        else:
            self.show_random_recipe()
    

    def show_nutrition_chart(self):
        # 한글 폰트 설정
        font_path = 'BMHANNAPro.ttf'  # 한글 폰트 파일 경로를 입력해주세요
        fontprop = fm.FontProperties(fname=font_path)
        
        # matplotlib 폰트 설정
        matplotlib.rcParams['font.family'] = fontprop.get_name()
        matplotlib.rcParams['font.size'] = 12

        # 칼로리 값 가져오기
        calories = str(self.recipe['INFO_ENG'])
        
        # 데이터 준비
        labels = ['나트륨', '단백질', '지방', '탄수화물']
        values = [float(self.recipe['INFO_NA']), float(self.recipe['INFO_PRO']), float(self.recipe['INFO_FAT']), float(self.recipe['INFO_CAR'])]

        # 색상 설정
        colors = ['red', 'orange', 'yellow', 'green']

        # 바차트 그리기
        fig, ax = plt.subplots()
        ax.bar(labels, values, color=colors)

        # 값 텍스트 표시
        for i, v in enumerate(values):
            ax.text(i, v, f'{v}g', ha='center', va='bottom')

        # 차트 타이틀 설정
        title = f'칼로리: {calories} kcal'
        ax.set_title(title, fontproperties=fontprop)  # 한글 폰트 적용
        
        # 바차트 윈도우 이름 설정
        fig.canvas.manager.set_window_title(self.recipe['RCP_NM'])

        # 차트 표
        plt.show()
    
    def sort_recipes_by_calories(self):
        # 현재 리스트 박스에 있는 레시피들을 열량 순으로 정렬
        self.recipes.sort(key=lambda x: float(x['INFO_ENG']))
        self.page2_listbox.delete(0, tk.END)  # 기존 리스트 박스 내용 삭제
        for item in self.recipes:
            recipe_name = item['RCP_NM']
            self.page2_listbox.insert(tk.END, recipe_name)
        
        self.button10.destroy()
        self.button11 = tk.Button(self.page2, image=self.photo15, command=self.sort_recipes_by_calories_reverse, bg='white')

        self.button11.place(x=10, y=82)
    
    def sort_recipes_by_calories_reverse(self):
        # 현재 리스트 박스에 있는 레시피들을 열량 역순으로 정렬
        self.recipes.sort(key=lambda x: float(x['INFO_ENG']), reverse=True)
        self.page2_listbox.delete(0, tk.END)  # 기존 리스트 박스 내용 삭제
        for item in self.recipes:
            recipe_name = item['RCP_NM']
            self.page2_listbox.insert(tk.END, recipe_name)
            
        self.button11.destroy()
        self.button10 = tk.Button(self.page2, image=self.photo14, command=self.sort_recipes_by_calories, bg='white')

        self.button10.place(x=10, y=82)
    
    def sort_recipes_by_car(self):
        # 현재 리스트 박스에 있는 레시피들을 탄수화물 순으로 정렬
        self.recipes.sort(key=lambda x: float(x['INFO_CAR']))
        self.page2_listbox.delete(0, tk.END)  # 기존 리스트 박스 내용 삭제
        for item in self.recipes:
            recipe_name = item['RCP_NM']
            self.page2_listbox.insert(tk.END, recipe_name)
            
        self.button12.destroy()
        self.button13 = tk.Button(self.page2, image=self.photo17, command=self.sort_recipes_by_car_reverse, bg='white')

        self.button13.place(x=10 + 55, y=82)
    
    def sort_recipes_by_car_reverse(self):
        # 현재 리스트 박스에 있는 레시피들을 탄수화물 순으로 정렬
        self.recipes.sort(key=lambda x: float(x['INFO_CAR']), reverse=True)
        self.page2_listbox.delete(0, tk.END)  # 기존 리스트 박스 내용 삭제
        for item in self.recipes:
            recipe_name = item['RCP_NM']
            self.page2_listbox.insert(tk.END, recipe_name)
            
        self.button13.destroy()
        self.button12 = tk.Button(self.page2, image=self.photo16, command=self.sort_recipes_by_car, bg='white')

        self.button12.place(x=10 + 55, y=82)
            
    def sort_recipes_by_pro(self):
        # 현재 리스트 박스에 있는 레시피들을 단백질 순으로 정렬
        self.recipes.sort(key=lambda x: float(x['INFO_PRO']))
        self.page2_listbox.delete(0, tk.END)  # 기존 리스트 박스 내용 삭제
        for item in self.recipes:
            recipe_name = item['RCP_NM']
            self.page2_listbox.insert(tk.END, recipe_name)
        
        self.button14.destroy()
        self.button15 = tk.Button(self.page2, image=self.photo19, command=self.sort_recipes_by_pro_reverse, bg='white')

        self.button15.place(x=10 + 110, y=82)
            
    def sort_recipes_by_pro_reverse(self):
        # 현재 리스트 박스에 있는 레시피들을 단백질 순으로 정렬
        self.recipes.sort(key=lambda x: float(x['INFO_PRO']), reverse=True)
        self.page2_listbox.delete(0, tk.END)  # 기존 리스트 박스 내용 삭제
        for item in self.recipes:
            recipe_name = item['RCP_NM']
            self.page2_listbox.insert(tk.END, recipe_name)
        
        self.button15.destroy()
        self.button14 = tk.Button(self.page2, image=self.photo18, command=self.sort_recipes_by_pro, bg='white')

        self.button14.place(x=10 + 110, y=82)
            
    def sort_recipes_by_fat(self):
        # 현재 리스트 박스에 있는 레시피들을 지방 순으로 정렬
        self.recipes.sort(key=lambda x: float(x['INFO_FAT']))
        self.page2_listbox.delete(0, tk.END)  # 기존 리스트 박스 내용 삭제
        for item in self.recipes:
            recipe_name = item['RCP_NM']
            self.page2_listbox.insert(tk.END, recipe_name)
        
        self.button16.destroy()
        self.button17 = tk.Button(self.page2, image=self.photo21, command=self.sort_recipes_by_fat_reverse, bg='white')

        self.button17.place(x=10 + 165, y=82)
            
    def sort_recipes_by_fat_reverse(self):
        # 현재 리스트 박스에 있는 레시피들을 지방 순으로 정렬
        self.recipes.sort(key=lambda x: float(x['INFO_FAT']), reverse=True)
        self.page2_listbox.delete(0, tk.END)  # 기존 리스트 박스 내용 삭제
        for item in self.recipes:
            recipe_name = item['RCP_NM']
            self.page2_listbox.insert(tk.END, recipe_name)
        
        self.button17.destroy()
        self.button16 = tk.Button(self.page2, image=self.photo20, command=self.sort_recipes_by_fat, bg='white')

        self.button16.place(x=10 + 165, y=82)
            
    def sort_recipes_by_na(self):
        # 현재 리스트 박스에 있는 레시피들을 나트륨 순으로 정렬
        self.recipes.sort(key=lambda x: float(x['INFO_NA']))
        self.page2_listbox.delete(0, tk.END)  # 기존 리스트 박스 내용 삭제
        
        for item in self.recipes:
            recipe_name = item['RCP_NM']
            self.page2_listbox.insert(tk.END, recipe_name)
        
        self.button18.destroy()
        self.button19 = tk.Button(self.page2, image=self.photo23, command=self.sort_recipes_by_na_reverse, bg='white')

        self.button19.place(x=10 + 220, y=82)
            
    def sort_recipes_by_na_reverse(self):
        # 현재 리스트 박스에 있는 레시피들을 나트륨 순으로 정렬
        self.recipes.sort(key=lambda x: float(x['INFO_NA']), reverse=True)
        self.page2_listbox.delete(0, tk.END)  # 기존 리스트 박스 내용 삭제
        for item in self.recipes:
            recipe_name = item['RCP_NM']
            self.page2_listbox.insert(tk.END, recipe_name)
        
        self.button19.destroy()
        self.button18 = tk.Button(self.page2, image=self.photo22, command=self.sort_recipes_by_na, bg='white')

        self.button18.place(x=10 + 220, y=82)
        
    def search_recipes(self):
        search_query = self.search_entry.get().lower()
        self.page3_listbox.delete(0, tk.END)  # 리스트박스 초기화

        # 검색된 레시피들을 담을 리스트
        self.search_recipes = []
        
        for item in self.recipes:
            recipe_name = item['RCP_NM'].lower()    
            if search_query in recipe_name:
                self.page3_listbox.insert(tk.END, item['RCP_NM'])
                self.search_recipes.append(item)
    
    def telegram(self):
        def handle(msg):        
            content_type, chat_type, chat_id = telepot.glance(msg)

            if content_type == 'text':
                if msg['text'] == '/start':
                    self.bot.sendMessage(chat_id, '안녕하세요! 맛있는 이야기 입니다! "오늘의 레시피를 추천해줘"라고 하시면 레시피를 추천해드릴게요!')
                elif msg['text'].lower() == '오늘의 레시피를 추천해줘':
                    selected_recipe = random.choice(self.recipes)
                    
                    message = f"★요리 이름: {selected_recipe['RCP_NM']}\n"
                    message += "★준비 재료: " + ''.join(selected_recipe['RCP_PARTS_DTLS']) + '\n'
                    message += f"★만드는 법: "
                    
                    for i in range(1, 20):
                        manual_key = f"MANUAL{str(i).zfill(2)}"
                        if manual_key in selected_recipe:
                            message += f"{selected_recipe[manual_key]}\n"

                    self.bot.sendMessage(chat_id, message)
                else:
                    self.bot.sendMessage(chat_id, '저는 "/start" 또는 "오늘의 레시피를 추천해줘" 라는 명령에 밖에 대답할 수 없어요. :<')
        MessageLoop(self.bot, handle).run_as_thread()

app = MyApplication(800, 600)