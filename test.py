import tkinter as tk
from PIL import ImageTk, Image
import json
from tkinter import font
import requests
from io import BytesIO
import random

class MyApplication:
    def __init__(self, width, height, zoom=15):
        self.width = width
        self.height = height
        self.zoom = zoom
        self.window = tk.Tk()
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.title("termproject")

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

        # 첫 번째 페이지
        label1 = tk.Label(self.page1, width=800, height=600, image=self.photo5)
        self.page2_image1 = tk.Label(self.page1, image=self.photo11, bg='white')
        self.page2_image1.place(x=10, y=10)
        
        # 페이지에 넣을 내용 추가
        self.page1_recipe_label = tk.Label(self.page1, width=480, height=440, bg='#DEDBD2', image=self.photo6)
        self.page1_recipe_label.place(x=160, y=80)
        
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
        self.page2_listbox = tk.Listbox(self.page2, width=40, height=32)
        self.page2_listbox.place(x=10, y=80)

        self.scrollbar = tk.Scrollbar(self.page2)
        self.page2_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.page2_listbox.yview)
        self.scrollbar.place(x=280, y=80, height=515)

        # 선택된 레시피의 이미지와 재료 정보를 표시할 레이블
        self.page2_recipe_label = tk.Label(self.page2, width=480, height=440, bg='#DEDBD2', image=self.photo6)
        self.page2_recipe_label.place(x=308, y=80)
        self.page2_recipe_name_label = tk.Label(self.page2, wraplength=425, bg='#F7F6F4')
        self.page2_recipe_dtls_label = tk.Label(self.page2, wraplength=425, bg='#F7F6F4')
        self.page2_recipe_image_label = tk.Label(self.page2, width=200, height=200, bg='#DEDBD2')

        # ####
        label2.pack()

        # 세 번째 페이지
        label3 = tk.Label(self.page3, width=800, height=600, image=self.photo5)
        # 페이지에 넣을 내용 추가

        # ####
        label3.pack()

        # 네 번째 페이지
        label4 = tk.Label(self.page4, width=800, height=600, image=self.photo5)
        # 페이지에 넣을 내용 추가
         # Google Cloud API Key
        api_key = 'AIzaSyDM1VdP71cSPp6yINofwpNXZdssDMKPceI'

        def search_supermarkets():
            #초기값 설정
            self.results_listbox.delete(0, tk.END)

            #위치(주소)
            address = self.address_entry.get()  # Get the input from the Entry widget

            #주소를 위도 경도로 변환 
            geocode_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'
            geocode_res = requests.get(geocode_url)
            geocode_data = geocode_res.json()

            if geocode_data['results']:
                location = geocode_data['results'][0]['geometry']['location']
                lat, lon = location['lat'], location['lng']

                #마트 검색 , radius은 거리 m단위로 
                place_type = 'supermarket'
                radius = 1000

                # 위도 경도를 이용해서 장소 추적 
                place_url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lon}&radius={radius}&type={place_type}&key={api_key}'

                #장소를 전송 
                place_res = requests.get(place_url)
                place_data = place_res.json()

                if place_data['results']:
                    for result in place_data['results']:
                        # 마트의 이름과 주소 
                        name = result['name']
                        address = result['vicinity']
                        #리스트 박스안에 넣기 
                        self.results_listbox.insert(tk.END, f'{name}, {address}\n')
                else:
                    self.results_listbox.insert(tk.END, '입력하신 지역 근처에 마트가 없습니다.\n')
            else:
                self.results_listbox.insert(tk.END, '잘못된 주소 입력입니다.\n')

        #지도 보여주는 함수 
        def show_map(lat, lon, zoom=15):
            map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lon}&zoom={zoom}&size=400x400&markers=color:red|{lat},{lon}&key={api_key}"
            map_image = Image.open(BytesIO(requests.get(map_url).content)) #핀까지 이미지에 뜨도록 설정 
            map_photo = ImageTk.PhotoImage(map_image)

            self.map_label.config(image=map_photo)
            self.map_label.image = map_photo  

        def zoom_in(): #확대
            self.zoom = min(21, self.zoom + 1)  #확대/축소 0~21 
            show_map(lat, lon, self.zoom)

        def zoom_out(): #축소 
            self.zoom  = max(0, self.zoom - 1)  
            show_map(lat, lon, self.zoom)

        #리스트 박스에서 주소 선택하기 
        def on_result_selected(evt):
            global lat, lon
            selected_result = evt.widget.get(evt.widget.curselection()) #선택한 결과를 항목 텍스트에 가져오기 
            selected_address = selected_result.split(", ", 1)[1]  # 선택한 주소부분만 가져오기 

            geocode_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={selected_address}&key={api_key}'
            geocode_res = requests.get(geocode_url)
            geocode_data = geocode_res.json()

            if geocode_data['results']:
                location = geocode_data['results'][0]['geometry']['location']
                lat, lon = location['lat'], location['lng']
                show_map(lat, lon, self.zoom)

       
        self.address_entry = tk.Entry(self.page4, width=40)
        self.address_entry.pack()

        # Create a Button widget to trigger the search
        self.search_button = tk.Button(self.page4, text="Search", command=search_supermarkets)
        self.search_button.pack()

        # Create a Listbox widget to display the results
        self.results_frame = tk.Frame(self.page4)
        self.results_frame.pack()

        self.scrollbar = tk.Scrollbar(self.results_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.results_listbox = tk.Listbox(self.results_frame, width=50, height=10)
        self.results_listbox.pack(side=tk.LEFT, fill=tk.Y)
        self.results_listbox.bind('<<ListboxSelect>>', on_result_selected)

        self.scrollbar.config(command=self.results_listbox.yview)
        self.results_listbox.config(yscrollcommand=self.scrollbar.set)

        # Initialize global variables for map
      

        # Create a Label widget to display the map
        self.map_label = tk.Label(self.page4,image=self.photo5)
        self.map_label.pack()

        # Create Buttons to zoom in and out
        self.zoom_in_button = tk.Button(self.page4, text="Zoom In", command=zoom_in)
        self.zoom_in_button.place(x = 600, y= 30)

        self.zoom_out_button = tk.Button(self.page4, text="Zoom Out", command=zoom_out)
        self.zoom_out_button.place(x = 600 ,y = 65)
        # ####
        label4.pack()

        # JSON 파일 읽기
        file_path = "recipes.json"
        with open(file_path, "r", encoding="utf-8") as file:
            # JSON 데이터 로드
            data = json.load(file)

        # 'RCP_NM' 내용을 리스트박스에 추가
        self.recipes = data['COOKRCP01']['row']
        for item in self.recipes:
            recipe_name = item['RCP_NM']
            self.page2_listbox.insert(tk.END, recipe_name)

        self.page2_listbox.bind('<<ListboxSelect>>', self.show_page2_recipe_details)
        
        self.current_page = self.page1  # 현재 표시되는 페이지
        self.current_page.pack()  # 첫 번째 페이지 표시
        self.show_button()
        self.show_random_recipe()

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

    def show_page2(self):
        self.current_page.pack_forget()
        self.current_page = self.page2
        self.current_page.pack()
        self.show_button()
        self.manual_index = 0

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
        
        # 레시피 이미지 로드
        recipe_image_url = self.recipe['ATT_FILE_NO_MAIN']
        try:
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

            # 레시피 이미지 표시
            response = requests.get(recipe_image_url)
            recipe_image = Image.open(BytesIO(response.content))
            recipe_image = recipe_image.resize((200, 200), Image.LANCZOS)
            self.recipe_image_tk = ImageTk.PhotoImage(recipe_image)
            self.page1_recipe_image_label.config(image=self.recipe_image_tk)
            self.page1_recipe_image_label.place(x=300, y=120)

            # 버튼 표시
            self.button5 = tk.Button(self.page1, image=self.photo8, command=self.show_previous_manual, bg='white')
            self.button6 = tk.Button(self.page1, image=self.photo9, command=self.show_next_manual, bg='white')
            self.button7 = tk.Button(self.page1, image=self.photo10, command=None, bg='white')

            self.button7.place(x=665 - 150, y=105)
            self.button5.place(x=700 - 150, y=105)
            self.button6.place(x=735 - 150, y=105)

            # MANUAL_IMG 및 MANUAL 표시
            self.manual_index = 0
            # self.show_manual()

        except Exception as e:
            print(f"Failed to load recipe image: {e}")

    def show_page2_recipe_details(self, event):
        selection = self.page2_listbox.curselection()
        if selection:
            index = selection[0]
            self.recipe = self.recipes[index]

            # 레시피 이미지 로드
            recipe_image_url = self.recipe['ATT_FILE_NO_MAIN']
            try:
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

                # 레시피 이미지 표시
                response = requests.get(recipe_image_url)
                recipe_image = Image.open(BytesIO(response.content))
                recipe_image = recipe_image.resize((200, 200), Image.LANCZOS)
                self.recipe_image_tk = ImageTk.PhotoImage(recipe_image)
                self.page2_recipe_image_label.config(image=self.recipe_image_tk)
                self.page2_recipe_image_label.place(x=445, y=105)

                # 버튼 표시
                self.button5 = tk.Button(self.page2, image=self.photo8, command=self.show_previous_manual, bg='white')
                self.button6 = tk.Button(self.page2, image=self.photo9, command=self.show_next_manual, bg='white')
                self.button7 = tk.Button(self.page2, image=self.photo10, command=None, bg='white')

                self.button7.place(x=665, y=105)
                self.button5.place(x=700, y=105)
                self.button6.place(x=735, y=105)

                # MANUAL_IMG 및 MANUAL 표시
                self.manual_index = 0
                # self.show_manual()

            except Exception as e:
                print(f"Failed to load recipe image: {e}")

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
            except Exception as e:
                print(f"Failed to load manual image: {e}")
        else:
            if self.current_page == self.page1:
                self.page1_recipe_image_label.config(image=self.recipe_image_tk)
            elif self.current_page == self.page2:
                self.page2_recipe_image_label.config(image=self.recipe_image_tk)

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
        else:
            self.manual_index -= 1
            
    def show_random_recipe(self):
        random_seq = random.randint(1, 1115)  # 1부터 1114 사이의 랜덤한 숫자 생성
        recipe = None

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
                
                # 레시피 이름 표시
                recipe_name_padded = '          ' * 900 + '오늘은 ' + recipe_name + ' 어떠세요?'  # 패딩 적용
                self.page1_recipe_name_label.config(font=font.Font(family='BM HANNA Pro', size=21, weight='bold'), fg='#574413')
                self.page1_recipe_name_label.config(text=recipe_name_padded)
                self.page1_recipe_name_label.place(x=185, y=310)
                
                # 버튼 표시
                self.button8 = tk.Button(self.page1, image=self.photo12, command=self.show_page1_recipe_details, bg='white')
                self.button9 = tk.Button(self.page1, image=self.photo13, command=self.show_random_recipe, bg='white')

                self.button8.place(x=265, y=430)
                self.button9.place(x=445, y=430)
                    
                self.manual_index = 0
                    

            except Exception as e:
                print(f"Failed to load recipe image: {e}")
        else:
            self.show_random_recipe()

app = MyApplication(800, 600)
#...