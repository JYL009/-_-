from tkinter import *

window = Tk()
window.geometry("970x520")

def final():#여행지 정보에서 원하는 정보가 뜨도록 하게 하는 코드
    if continent.get()=='유럽' and country.get()=="스페인 마요르카" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1100x250")

        나라이름 = Label(travel, text="스페인 마요르카", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0,column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="자동차 운전\n"
                            "거주증이 없는 여행객의 경우에는 국제운전면허증을 한국에서 사전 발급(발급일로부터 6개월까지만 인정) 받은 후 한국면허증을 함께 소지하여야 운전이 가능합니다.\n"
                            "2006년부터 벌점 제도를 시행하고 있으며 과속(고속도로 80km 초과, 도심 지역 60km 초과) 및 음주운전에 대하여 형사처벌을 가하고 있습니다.\n"
                            "횡단보도에서는 보행자에 대한 절대적인 우선권이 인정되므로 반드시 정차하여야 하며, 앞차의 급정차에 따른 접촉 사고에 유의하시기 바랍니다.\n"
                            "횡단보도에 신호등이 여러 개 부착되어 있어 혼란이 생길 수 있으나 차량 대기선 옆에 설치된 신호등 및 운전자 눈높이에 설치된 보조 신호등이 운전자가 준수해야 할 주행 방향 신호등입니다.\n"
                            "교통사고가 발생하거나 차량 고장 등으로 고속도로 상에서 비상 정차한 경우에는 반드시 삼각대를 설치하고 노란색 형광 조끼를 착용하여야 합니다.\n"
                            "유의사항\n"
                            "스페인은 대부분의 고속도로와 일반도로가 잘 정비되어 있으며 과속으로 인한 사고 및 과속 단속 카메라에 따른 벌금 부과에 주의가 필요합니다.\n"
                            "주행 중 차에 이상이 있다며 도와주는 척 접근하는 사람들은 절도범일 가능성이 매우 높으므로 반드시 거절하고, 따로 차를 세운 뒤 확인이 필요합니다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="스페인 마요르카" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x150")

        나라이름 = Label(travel, text="스페인 마요르카", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="언어 : 스페인어(카스티야어); 지역별 카탈루냐어, 바스크어, 갈리시아어를 공용어로 사용",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="스페인 마요르카" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1100x1000")
        global img_스페인_마요르카2, img_스페인_마요르카3, img_스페인_마요르카4

        나라이름 = Label(travel, text="스페인 마요르카", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟 : 관광", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=5,column=0, sticky='W')
        Label(travel, text="추천스팟 : 관광", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=5,column=1, sticky='W')
        Label(travel, text="추천스팟 : 관광", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=8,column=0, sticky='W')
        
        Label(travel, text="발데모사\n"
                            "스페인 마요르카에서 가장 예쁜 동네, 발데모사\n"
                            "스페인 하면 떠오느는 색감과 분위기를 모두 가지고 있는 곳\n"
                            "쇼팽이 머물렀던 수도원이 있는 동네로 산책만으로도 충분히 그 아름다움을 느낄 수 있는 곳이다.",bg='lightsteelblue', justify='left').grid(row=6, column=0)
        Label(travel, text="소예르\n"
                            "지중해 서부 에스파냐령 마요르카 섬에 있는 작은 도시\n"
                            "특별히 유명한 곳은 없으나 15세기에 지어진 건물들이 많아 옛스러움이 가득하며,\n"
                            "그중에서도 1912년부터 달려온 소예르 철도가 가장 유명하다.\n"
                            "나무로 만들어진 열차가 조용하고 옛스러운 도시와 잘 어울린다.",bg='lightsteelblue', justify='left').grid(row=6, column=1)
        Label(travel, text="팔마\n"
                            "고대 아람 왕조의 거성과 중세에 세워진 건축물이 남아있어서\n"
                            "사진 찍으면 과거로 돌아가는 기분을 느낄 수 있다.",bg='lightsteelblue', justify='left').grid(row=9, column=0)

        
        img_스페인_마요르카2 = PhotoImage(file='스페인 마요르카_추천스팟_발데모사.gif').subsample(2)
        label_스페인_마요르카2 = Label(travel, image=img_스페인_마요르카2)
        label_스페인_마요르카2.grid(row=7, column=0, sticky='W')
        img_스페인_마요르카3 = PhotoImage(file='스페인 마요르카_추천스팟_소예르.gif').subsample(2)
        label_스페인_마요르카3 = Label(travel, image=img_스페인_마요르카3)
        label_스페인_마요르카3.grid(row=7, column=1)
        img_스페인_마요르카4 = PhotoImage(file='스페인 마요르카_추천스팟_팔마.gif').subsample(2)
        label_스페인_마요르카4 = Label(travel, image=img_스페인_마요르카4)
        label_스페인_마요르카4.grid(row=10, column=0)


    if continent.get()=='유럽' and country.get()=="스페인 마요르카" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x200")

        나라이름 = Label(travel, text="스페인 마요르카", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="안녕하세요 : 올라\n"
                            "안녕히 계세요 : 아디오\n"
                            "감사합니다 : 그라시아스\n"
                            "얼마에요 : 꾸안또 꾸에스타\n"
                            "화장실은 어디인가요 : 돈데 에스따 엘 세르비시오\n"
                            "계산서 주세요 : 라 꾸엔타",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="스페인 마요르카" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x200")

        나라이름 = Label(travel, text="스페인 마요르카", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="마요르카 섬(스페인어: Mallorca, 카탈루냐어: Mallorca)은 지중해 발레아레스 제도에 있는 스페인에서 가장 큰 섬이다.\n"
                            "면적은 3,640.11 km2이고, 인구는 2011년 기준으로 87만 3,414 명이다. 중심 도시인 팔마데마요르카는 발레아레스 제도 자치 지역의 중심지이다.\n"
                            "1952년 5월 영국과 독일에서 최초로 마요르카 여행 상품이 판매되기 시작한 이후 이곳은 유럽의 주요 관광지로 발돋움하여\n"
                            "섬의 이름은 '더 큰 섬'이라는 뜻의 라틴어 insula maior에서 유래하였다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="스페인 마요르카" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x200")

        나라이름 = Label(travel, text="스페인 마요르카", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text= "휴양/관광\n"
                            "발데모사 - 예쁜 동네\n"
                            "소예르 - 예쁜 거리\n"
                            "팔마 - 사진 찍기 좋은 스팟",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="스페인 마요르카" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("750x300")

        나라이름 = Label(travel, text="스페인 마요르카", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="일반 문화\n"
                            "스페인 사람들은 초면에도 서로 볼을 2번 맞대고 인사를 나누는 관습이 있으나 악수로 대신하는 경우도 많습니다.\n"
                            "어린이에 대한 신체 접촉은 아동성범죄로 오인될 수 있으니 주의를 요합니다.\n\n"
                            "종교 관련\n"
                            "스페인은 가톨릭 전통의 국가로 도시마다 대성당이 있습니다. 입장 시에는 복장에 유의를 요합니다.\n"
                            "아주 짧은 반바지, 치마, 민소매 T셔츠 등을 착용한 경우에는 입장 제한을 받을 수 있습니다.\n\n"
                            "팁 문화\n"
                            "보통은 팁을 주지 않거나 거스름돈 정도를 놓아둡니다. 고급 식당의 경우 식사비의 5~10% 정도의 팁을 주기도 합니다.\n"
                            "택시의 경우 팁은 없으나 1유로 미만의 거스름돈을 팁으로 주기도 합니다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="스페인 마요르카" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x200")

        나라이름 = Label(travel, text="스페인 마요르카", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="기후\n"
                            "대부분의 지역에서 4계절이 뚜렷하고 동남부 해안 지역은 지중해성 기후, 북서부 해안 지역은 해양성 기후, 내륙고원 지역은 대륙성 기후를 보이며,\n"
                            "카나리아 군도는 아열대성 기후로 연중 온난건조\n"
                            "봄·가을 : 8~21℃, 여름 : 25~45℃, 겨울 : 0~12℃ / 카나리아 군도 : 22℃(연평균)\n"
                            "강수량 : 300mm 이하(알메리아주, 무르시아주)~800mm 이상(바스크주, 갈리시아주)",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')



    if continent.get()=='유럽' and country.get()=="몰타" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1150x400")

        나라이름 = Label(travel, text="몰타", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="주요 교통 법규 및 문화\n"
                            "운전면허증 관련\n"
                            "우리나라 운전면허는 몰타 운전면허와 교환되지 않는다.\n"
                            "몰타는 유럽연합 회원국, 스위스, 호주의 운전면허만 교환해주고 있음\n"
                            "한국에서 발행한 국제운전면허증과 원본 한국면허증을 같이 휴대하여야 운전이 가능하다.\n"
                            "몰타는 1949년 제네바 협약의 국제운전면허증 인정 국가이므로 체류한 지 1년 동안은 국제운전면허증으로 운전이 가능하다. 하지만, 1년 경과 후에는 몰타 면허증을 취득하여야 한다.\n\n"
                            "교통 법규\n"
                            "몰타는 영국과 같이 차량이 좌측 통행을 하며, 세계적으로 일반적인 교통법규를 따르면 되며 특히 영국과 거의 유사하다.\n"
                            "고속도로는 없으며, 국도와 같은 도로의 속도제한은 시속 80킬로미터, 시내 도로는 시속 50킬로미터이며, 도로안전 상황에 따라 속도제한이 바뀔 수 있으므로 속도제한 표지판에 주의하여야 한다.\n"
                            "시골지역에서 속도제한 표지판이 없더라도 마을이나 민가 지역이 나타나면 50km/h 이하로 감속하는 것이 좋다. 속도위반으로 단속될 수 있기 때문이다.\n\n"
                            "대중교통\n"
                            "대중교통 수단으로 버스와 택시를 이용할 수 있습니다.\n"
                            "2014년부터 몰타대중교통사(Malta Public Transport) 운영개시, 5:30 ~ 23:00까지 운영되는 버스망이 잘 발달되어 있으며, 버스를 이용하는 것이 일반화되어 있습니다.\n"
                            "티켓은 티켓 판매기, 버스 운전수로부터 구입이 가능합니다.\n"
                            "버스는 A~D zone으로 나누어 운행되며 각 구역별로 요금이 차등 적용(0.40 유로~1유로) 됩니다.\n"
                            "택시는 미터제가 아님. 승객이 행선지를 말하면 택시 운전수가 거리에 따라 행선지까지의 요금을 제시하고 탑승객이 이에 동의하면 탑승하게 됩니다.\n"
                            "단, Malta International Airport(Luqa 소재)에서 택시를 탑승하는 경우, 입국장에서 선지불티켓(pre-paid ticket)을 구입하여, 고정된 가격으로 이용할 수 있습니다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="몰타" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("300x100")

        나라이름 = Label(travel, text="몰타", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="언어 : 몰타어(아랍어와 유사) 및 영어, 이탈리아어도 통용",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="몰타" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1100x500")
        global img_몰타2, img_몰타3, img_몰타4

        나라이름 = Label(travel, text="몰타", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟 : 관광/휴양", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=5,column=0, sticky='W')
        Label(travel, text="추천스팟 : 관광/휴양", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=5,column=1, sticky='W')
        Label(travel, text="추천스팟 : 관광휴양", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=8,column=0, sticky='W')
        
        Label(travel, text="블루 라군\n"
                            "몰타에서 가장 예쁜 해변, 블루 라군\n"
                            "배를 타고 바다 위에서 즐길 수 있는 휴양\n"
                            "신혼여행으로 많이 가는 곳",bg='lightsteelblue', justify='left').grid(row=6, column=0)
        Label(travel, text="고조섬\n"
                            "몰타 섬보다 유명하다는 말이 있을 정도로 예쁜 섬\n"
                            "석양이 아름다워 예전부터 사진 찍는 곳으로 유명한 곳\n"
                            "주변에 바로 호텔이 있어서 호텔에서 보는 야경도 멋있다.",bg='lightsteelblue', justify='left').grid(row=6, column=1)
        Label(travel, text="임디나 & 라밧\n"
                            "역사를 담은 교회가 있는 곳으로 \n"
                            "교회 안으로 들어가는 순간 이 세상 기분이 아니다.",bg='lightsteelblue', justify='left').grid(row=9, column=0)

        
        img_몰타2 = PhotoImage(file='몰타_추천스팟_블루 라군.gif').subsample(7)
        label_몰타2 = Label(travel, image=img_몰타2)
        label_몰타2.grid(row=7, column=0, sticky='W')
        img_몰타3 = PhotoImage(file='몰타_추천스팟_고조섬.gif').subsample(3)
        label_몰타3 = Label(travel, image=img_몰타3)
        label_몰타3.grid(row=7, column=1)
        img_몰타4 = PhotoImage(file='몰타_추천스팟_임디나 & 라밧.gif').subsample(3)
        label_몰타4 = Label(travel, image=img_몰타4)
        label_몰타4.grid(row=10, column=0)


    if continent.get()=='유럽' and country.get()=="몰타" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("300x200")

        나라이름 = Label(travel, text="몰타", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="안녕하세요 : 부온 죠르노/부오나 세라\n"
                            "잘자요 : 부오나 노떼\n"
                            "안녕 또 봐요 : 아리베데르치\n"
                            "죄송합니다 : 미 스꾸지\n"
                            "만나서 반갑습니다 : 삐아체레\n"
                            "나는 한국입니다 : 소노 꼬레아노/나",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="몰타" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("900x400")

        나라이름 = Label(travel, text="몰타", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="이탈리아의 시칠리아 섬에서 남쪽으로 93킬로미터 떨어져 있으며 지중해의 한가운데에 있다.\n"
                            "튀니지의 동쪽이고 리비아의 북쪽에 있다. 몰타 내에서는 오직 세 곳의 섬(몰타 섬, 고조 섬, 코미노 섬)에만 사람이 살고 그보다 작은 나머지 섬들은 무인도다.\n"
                            "해안선을 따라 만이 형성되어 있어 항구가 생기기 좋은 환경을 갖고 있다.\n"
                            "비가 많이 내릴 때 강이 생기기도 하지만 강이나 호수라고 부를 만한 것들은 몰타에 없다.\n"
                            "그러나 작은 물줄기가 가끔씩 섬 전역에서 발견되기도 한다.\n"
                            "보통 몰타의 남쪽 속령제도가 유럽의 가장 남쪽이라고 여겨지지만 사실은 그리스의 가브도스 섬이 유럽에서 최남단에 있다.\n"
                            "면적은 316km²로 302km²인 대한민국의 강화도보다 조금 더 큰 면적이다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="몰타" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x600")

        나라이름 = Label(travel, text="몰타", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동 : 관광/ 휴양", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="블루 라군 - 세상에서 예쁜 해변\n"
                            "고조섬 - 오랜 역사를 가진 섬\n"
                            "세인트 줄리안스 - 해변에 있는 맛집",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="몰타" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("850x400")

        나라이름 = Label(travel, text="몰타", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="팁 문화\n"
                            "일반적으로 서비스 분야(택시 포함)에서 총 비용의 5~10%의 팁을 지불하는 관행이 있습니다.\n"
                            "호텔과 식당(Restaurant)의 경우 봉사료(Service charge)가 포함되지 않는 경우에 총 가격의 약 10%를 팁으로 지불합니다.\n\n"
                            "조심해야 할 것\n"
                            "사회 전체적으로 치안이 안정되어 있는 가운데, 경범죄에 대해서는 관대하게 처벌하는 경향이 있으나,\n"
                            "마약사범(마약류의 반입, 거래, 소지)에 대해서는 외국인이라 할지라도 구속 기소 및 실형 선고, 고액의 벌금 부과 등을 통하여 강력하게 처벌하고 있습니다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="몰타" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("850x400")

        나라이름 = Label(travel, text="몰타", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="날씨\n"
                            "전형적인 지중해성 기후로서 여름에는 고온 건조하고 겨울에는 습도가 높은 편입니다.\n"
                            "연평균 강우량은 약 600mm 이며 대부분의 비는 10월~3월 사이에 내립니다.\n"
                            "여름철 낮기온은 30도~35도, 일조시간은 평균 12시간에 이르며, 겨울철의 경우 낮기온은 15도~20도, 일조시간은 평균 5~6시간에 이르는 온화한 날씨를 보입니다.\n"
                            "눈과 서리는 내리지 않으며 안개를 거의 찾아볼 수 없습니다.\n"
                            "겨울철에 가끔 중부 유럽으로부터 찬 공기를 동반한 바람이 불어옵니다.\n"
                            "가끔 우박이 떨어지기도 합니다.\n"
                            "전형적인 지중해성 기후로서 여름에는 고온 건조하고 겨울에는 습도가 높은 편입니다.\n"
                            "연평균 강우량은 약 600mm 이며 대부분의 비는 10월~3월 사이에 내립니다.\n"
                            "여름철 낮기온은 30도~35도, 일조시간은 평균 12시간에 이르며, 겨울철의 경우 낮기온은 15도~20도, 일조시간은 평균 5~6시간에 이르는 온화한 날씨를 보입니다.\n"
                            "눈과 서리는 내리지 않으며 안개를 거의 찾아볼 수 없습니다.\n"
                            "겨울철에 가끔 중부 유럽으로부터 찬 공기를 동반한 바람이 불어옵니다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')



    if continent.get()=='유럽' and country.get()=="영국 런던" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("900x600")
        global img_런던1

        나라이름 = Label(travel, text="영국 런던", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="지하철(Tube)은 노선이 굉장히 헷갈리고, 객차 내부가 좁고, 스마트폰이 아예 먹통이 된다.\n"
                            "Zone마다 요금이 다른데 가장 짧은 구간인 Zone1도 4.9 파운드로 요금이 비싼 편이다\n"
                            "그 대신 오이스터 카드를 pay as you go(원하는 만큼 이용하고 충전) 혹은 정기권으로 구매하여 사용하는게 합리적!\n"
                            "각 역에 설치된 티켓판매기나 인포메이션에서 티켓을 구매할 수 있다.\n"
                            "영국의 택시 기본 요금은 5800원에 50분 거리를 가야한다면 12만원이 나올 정도로 비싼 편이다.\n"
                            "버스는 현금으로 승차가 불가능하기 때문에 지하철역 혹은 상점에서 오이스터 카드나 트래블 카드를 미리 구매해야한다. \n"
                            "피크 타임에는 대중교통 이용료가 더 비싸진다",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')
        img_런던1 = PhotoImage(file='영국런던_교통정보.gif').subsample(1)
        label_런던1 = Label(travel, image=img_런던1)
        label_런던1.grid(row=4, column=0, sticky='W')

    if continent.get()=='유럽' and country.get()=="영국 런던" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x100")
        

        나라이름 = Label(travel, text="영국 런던", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="영어를 사용하지만 미국식 영어와 다른 표현들이 많기 때문에 주의해야한다",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="영국 런던" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")
        global img_런던2, img_런던3, img_런던4

        나라이름 = Label(travel, text="영국 런던", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="템즈강변, 타워브리지, 런던탑",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')
        img_런던2 = PhotoImage(file='영국런던_추천스팟_템즈강변.gif').subsample(2)
        label_런던2 = Label(travel, image=img_런던2)
        label_런던2.grid(row=4, column=0, sticky='W')
        img_런던3 = PhotoImage(file='영국런던_추천스팟_타워브릿지.gif').subsample(2)
        label_런던3 = Label(travel, image=img_런던3)
        label_런던3.grid(row=4, column=1)
        img_런던4 = PhotoImage(file='영국런던_추천스팟_런던탑.gif').subsample(2)
        label_런던4 = Label(travel, image=img_런던4)
        label_런던4.grid(row=4, column=2)

    if continent.get()=='유럽' and country.get()=="영국 런던" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x300")

        나라이름 = Label(travel, text="영국 런던", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="Can I have a cup of tea please?( 차 한 잔 주세요)\n"
                            "Tap water(수돗물), Still water(일반 생수), Sparkling water(탄산수)\n"
                            "Flat(아파트) Lift(엘리베이터) Trousers(바지) Booking(예약) Ring(전화하다)",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="영국 런던" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("300x100")

        나라이름 = Label(travel, text="영국 런던", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="유럽 전체 대도시권중 가장 큰 권역을 자랑한다",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="영국 런던" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1200x800")
        global img_런던5, img_런던6, img_런던7

        나라이름 = Label(travel, text="영국 런던", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="((관광))\n"
                            "빅벤: 영국의 수도 런던에 있는 웨스트 민스터 궁전(영국 국회 의사당)에 부속된 시계탑의 큰 종에 대한 애칭이다. \n"
                            "1859년에 완성된 빅 벤은 세계에서 두번째로 큰 4면의 차임벨 시계를 보유하고 있다.\n"
                            "영국에서 가장 눈에 띄는 상징이 된 시계탑은 많은 영화에서 런던을 상징하는 장소로 등장하였다.\n"
                            "런던아이: 런던 아이는 영국 런던 템즈 강변에 위치한 대형 대관람차로, 높이가 135m에 달하고, 유럽에서 가장 높은 대관람차이다.\n"
                            "또한 영국의 관광지에서 가장 유명한 장소 중 하나로 꼽히며, 매년 350만 여명의 관광객이 방문한다.\n\n"
                            "((쇼핑))\n"
                            "1.빈티지 앤티크 마켓(브릭레인 마켓, 버로우 마켓, 그리니치 마켓 등) :\n"
                            "런던에서 차 문화가 발달해 있기 때문에 유명한 티웨어 용품이 많다\n"
                            "2. 러쉬 : 영국에서 설립한 핸드메이드 자연성분 화장품 브랜드로, 현지에서 더욱 저렴하게 구매 가능.\n"
                            "3. 차 가게(포트넘앤메이슨, 트와이닝, 립톤 등)\n"
                            "차 문화로 유명한 영국에서는 수많은 홍차 브랜드와 제품들을 만날 수 있다.\n"
                            "4. 옥스포드 거리: 하루 평균 50만명의 쇼핑객들이 찾아오고, 300개 넘는 가게들이 자리잡고 있는 쇼핑 거리\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')
        img_런던5 = PhotoImage(file='영국런던_테마별추천활동_관광_빅벤.gif').subsample(1)
        label_런던5 = Label(travel, image=img_런던5)
        label_런던5.grid(row=3, column=1)
        img_런던6 = PhotoImage(file='영국런던_테마별추천활동_관광_런던아이.gif').subsample(2)
        label_런던6 = Label(travel, image=img_런던6)
        label_런던6.grid(row=4, column=0, sticky='W')
        img_런던7 = PhotoImage(file='영국런던_테마별추천활동_쇼핑_옥스포드거리.gif').subsample(2)
        label_런던7 = Label(travel, image=img_런던7)
        label_런던7.grid(row=5, column=0, sticky='W')

    if continent.get()=='유럽' and country.get()=="영국 런던" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")

        나라이름 = Label(travel, text="영국 런던", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="1.오이스터 카드에서 pay as you go 로 구매할 시 현금가의 절반 가격으로 사용 가능하다\n"
                            "2. 매년 6월 셋쨋주 토요일 엘리자베스 2세여행 생일 축하 퍼레이드, 8월 말 2-3이에 걸쳐 열리는 대규모 축제인 노팅힐 카니발 등\n"
                            "특정 시기에 열리는 축제가 있어 시기를 맞춰 여행을 가는 것을 추천\n"
                            "3. 영국의 대부분의 상점들은 공휴일에 거의 영업을 하지 않는다. \n"
                            "특히 부활절이나 크리스마스 기간에는 대부분의 상점, 회사들이 휴일 전후로 일주일 가량 쉬기 때문에 여행 기간에 공휴일이 겹치는가 확인 중요.", bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="영국 런던" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x200")

        나라이름 = Label(travel, text="영국 런던", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="일년 내내 비가 많이 옴, 11-2월 짙은 안개. 한겨울과 여름에도 선선한 날씨",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')



    if continent.get()=='유럽' and country.get()=="프랑스 파리" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")

        나라이름 = Label(travel, text="프랑스 파리", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="지하철은 14개의 노선들이 거미줄처럼 파리 곳곳을 연결하고 있다. 각각의 노선도 한국의 노선도처럼 색깔이 존재하여 구분이 편리하다.\n"
                            "파리 외곽까지 갈 수 있는 수도권 고속 전철인 RER은 노선이 다섯개가 있고, \n"
                            "보통 A노선은 디디즈니랜드 갈 때, B노선은 공항으로 이동할 때, C노선은 베르사유 궁전을 갈 때 주로 이용한다.\n"
                            "트램은 9개의 노선이 있고, 도시의 외곽까지 이동할 수 있다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="프랑스 파리" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x130")

        나라이름 = Label(travel, text="프랑스 파리", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="공용어는 프랑스어이지만, 생각보다 많은 사람들이 영어를 잘 한다고 한다. \n"
              "하지만 변두리로 가면 노년층은 영어를 모르는 경우가 허다하다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="프랑스 파리" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1000x700")
        global img_파리1, img_파리2, img_파리3

        나라이름 = Label(travel, text="프랑스 파리", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="에펠탑, 노트르담 대성당, 샹젤리제 거리",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')
        img_파리1 = PhotoImage(file='프랑스파리_추천스팟_에펠탑.gif').subsample(3)
        label_파리1 = Label(travel, image=img_파리1)
        label_파리1.grid(row=4, column=0, sticky='W')
        img_파리2 = PhotoImage(file='프랑스파리_추천스팟_노트르담대성당.gif').subsample(2)
        label_파리2 = Label(travel, image=img_파리2)
        label_파리2.grid(row=4, column=1)
        img_파리3 = PhotoImage(file='프랑스파리_추천스팟_샹젤리제거리.gif').subsample(2)
        label_파리3 = Label(travel, image=img_파리3)
        label_파리3.grid(row=4, column=2)


    if continent.get()=='유럽' and country.get()=="프랑스 파리" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x600")
        global img_파리4

        나라이름 = Label(travel, text="프랑스 파리", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_파리4 = PhotoImage(file='프랑스파리_필수어휘.gif')
        label_파리4 = Label(travel, image=img_파리4)
        label_파리4.grid(row=4, column=1)

    if continent.get()=='유럽' and country.get()=="프랑스 파리" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("700x400")

        나라이름 = Label(travel, text="프랑스 파리", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="유럽에서 러시아와 우크라이나 다음으로 세 번째로 큰 규모를 자랑한다. \n"
                            "프랑스는 북해, 영불 해협, 대서양, 지중해 네 곳의 해안선을 아우른다. \n"
                            "북-동부 지역을 제외하고 영토는 바다로 둘러 쌓여 있으며, 고루 형성된 산맥은 자연적인 국경지대를 이룬다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')
        

    if continent.get()=='유럽' and country.get()=="프랑스 파리" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1500x1200")
        global img_파리5, img_파리6, img_파리7, img_파리8, img_파리9

        나라이름 = Label(travel, text="프랑스 파리", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="((관광))\n"
                            "베르사유 궁전: 베르사유 궁전은 단순히 궁전 한 채로만 이루어져있는 것이 아니다. \n"
                            "베르사유 궁전 뿐만 아니라 정원, 공원(운하), 트리아농궁, 프티트리아농궁, 마리-앙투아네트 농가 등으로 이루어져 있다. \n"
                            "분수쇼, 무도회, 불꽃놀이 등의 이벤트도 자주 진행하는 편이니 미리 찾아보고 가는 것이 좋다.\n"
                            "루브르 박물관: 세계에서 제일 크고, 가장 많은 사람들이 방문하며, 유리 피라미드로도 유명한 루브르 박물관은 파리에서 절대 놓치지 말아야 할 관광 명소다. \n"
                          "총 35,000여점의 작품이 전시되어 있어 한 작품당 10초씩만 머무른다고 해도, 모든 작품을 보기 위해서는 4일 내내 단 한 순간도 쉬지 않고 감상에 전념해야 할 정도다.\n"
                            "에투알 개선문:높이 51미터, 너비 45미터의 파리 개선문은 세계에서 두번째로 큰 개선문이다. \n"
                            "개선문 주위로 12개의 큰 에비뉴가 뻗어있고, ‘별’이라는 뜻의 에투알 광장의 중심에 자리잡고 있다.\n\n"
                            "((식도락))\n"
                            "1.Au Bougnat(26 Rue Chanoinesse, 75004, Paris) : 25유로 정도의 저렴한 가격에 코스 요리를 즐길 수 있는 식당. \n"
                            "2.Chez Le Libanais(traiteur) (35 Rue Saint-Andre des Arts, 7500g Paris): 사람이 많은 관광지 근처에 있는 크레페/케밥 맛집. \n"
                            "3. Boulangerie Raphaelle(1 Rue Feutrier, 75018 Paris): 빵으로 유명한 파리에서도 인기가 많은 디저트 카페. \n"
                            "케이크, 타르트, 에끌레어 등 다양한 빵이 있으며, 모두 맛이 굉장히 좋다고 한다. 접근성이 떨어지지만 인기가 좋아 사람들의 발길이 끊이지 않는 빵집.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')
        img_파리5 = PhotoImage(file='프랑스파리_테마별추천활동_관광_베르사유궁전.gif').subsample(2)
        label_파리5 = Label(travel, image=img_파리5)
        label_파리5.grid(row=4, column=0, sticky='W')
        img_파리6 = PhotoImage(file='프랑스파리_테마별추천활동_관광_루브르.gif').subsample(2)
        label_파리6 = Label(travel, image=img_파리6)
        label_파리6.grid(row=4, column=1, sticky='W')
        img_파리7 = PhotoImage(file='프랑스파리_테마별추천활동_관광_개선문.gif').subsample(2)
        label_파리7 = Label(travel, image=img_파리7)
        label_파리7.grid(row=4, column=2, sticky='W')
        img_파리8 = PhotoImage(file='프랑스파리_테마별추천활동_식도락_코스요리.gif').subsample(3)
        label_파리8 = Label(travel, image=img_파리8)
        label_파리8.grid(row=5, column=0, sticky='W')
        img_파리9 = PhotoImage(file='프랑스파리_테마별추천활동_식도락_빵집.gif').subsample(3)
        label_파리9 = Label(travel, image=img_파리9)
        label_파리9.grid(row=5, column=1, sticky='W')

    if continent.get()=='유럽' and country.get()=="프랑스 파리" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")

        나라이름 = Label(travel, text="프랑스 파리", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="1. 매달 첫 주 일요일은 대부분의 박물괸을 무료로 입장할 수 있다.\n"
                            "2. 몽쥬 약국에서 훨씬 저렴한 가격에 좋은 품질의 화장품이 많기 때문에 현지에서 사서 이용하는 것이 더 합리적이다.\n"
                            "3.입장권, 뮤지엄 패스 등을 미리 한국에서 대행사를 통해서 구입하는 것이 훨씬 저렴하다,",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="프랑스 파리" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x100")

        나라이름 = Label(travel, text="프랑스 파리", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="일년 내내 온화한 날씨. 3월 소나기, 6월 햇볕이 가장 좋은 시기",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')



    if continent.get()=='유럽' and country.get()=="이탈리아 로마" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("300x100")

        나라이름 = Label(travel, text="이탈리아 로마", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="지하철, 버스\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')
        
    if continent.get()=='유럽' and country.get()=="이탈리아 로마" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("300x100")

        나라이름 = Label(travel, text="이탈리아 로마", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="이탈리아어\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="이탈리아 로마" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x400")
        global img_바티칸박물관, img_콜로세움, img_트레비분수

        나라이름 = Label(travel, text="이탈리아 로마", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="바티칸박물관\n",bg='lightsteelblue', justify='left').grid(row=3, column=0, sticky='W')
        Label(travel, text="콜로세움\n",bg='lightsteelblue', justify='left').grid(row=3, column=1)

        img_바티칸박물관 = PhotoImage(file='이탈리아로마_추천스팟_바티칸박물관.gif')
        label_바티칸박물관 = Label(travel, image=img_바티칸박물관)
        label_바티칸박물관.grid(row=4, column=0, sticky='W')

        img_콜로세움 = PhotoImage(file='이탈리아로마_추천스팟_콜로세움.gif')
        label_콜로세움 = Label(travel, image=img_콜로세움)
        label_콜로세움.grid(row=4, column=1)

    if continent.get()=='유럽' and country.get()=="이탈리아 로마" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x200")

        나라이름 = Label(travel, text="이탈리아 로마", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="Grazie mille. 그라찌에 밀레.:매우 감사합니다\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="이탈리아 로마" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x200")

        나라이름 = Label(travel, text="이탈리아 로마", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="펜니노산맥에서 발원하는 테베레강 하류에 면하며 주로 홍적대지로 이루어진 구릉지대\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="이탈리아 로마" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x500")
        global img_피자, img_카스텔로마노아울렛

        나라이름 = Label(travel, text="이탈리아 로마", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="피자\n",bg='lightsteelblue', justify='left').grid(row=3, column=0, sticky='W')
        Label(travel, text="카스텔로마노아울렛\n",bg='lightsteelblue', justify='left').grid(row=3, column=1, sticky='W')

        img_피자 = PhotoImage(file='이탈리아로마_테마별추천활동_피자.gif').subsample(2)
        label_피자 = Label(travel, image=img_피자)
        label_피자.grid(row=4, column=0, sticky='W')
        
        img_카스텔로마노아울렛 = PhotoImage(file='이탈리아로마_테마별추천활동_카스텔로마노아울렛.gif').subsample(2)
        label_카스텔로마노아울렛 = Label(travel, image=img_카스텔로마노아울렛)
        label_카스텔로마노아울렛.grid(row=4, column=1)
        
    if continent.get()=='유럽' and country.get()=="이탈리아 로마" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("700x300")

        나라이름 = Label(travel, text="이탈리아 로마", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="스탠드 문화 이해-카페에서 테이블에 앉아서 마시기보다 스탠딩 테이블에서 서서 음료를 즐김\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="이탈리아 로마" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x200")

        나라이름 = Label(travel, text="이탈리아 로마", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="여름은 덥고 건조하고 겨울은 춥지만 우리나라와 달리 혹한기는 없다. 여름 평균 최고 기온은 30℃, 겨울 평균 최저 기온은 5℃\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')


    if continent.get()=='유럽' and country.get()=="체코 프라하" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")

        나라이름 = Label(travel, text="체코 프라하", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="지하철 ABC선, 트램, 버스 04:30-12;00 사이 운행. 트램/지하철 티켓 상점, 지하철 자동판매기, 프라하 트램 자동 판매기 등 어디서나 구매 가능\n"
                         "1회권(30분 티켓. 지하철만 가능), 1회권(90분 티켓. 환승가능), 시간 내 환승 무한 번 가능(펀칭 시간을 기준으로 시간 측정). \n"
                          "30분 티켓 기준 어른(16-59) 24kc(1200원),어린이와 노인 12kc(600원) 정도\n"
                          "모든 대중교통 탑승전 교통티켓 ‘펀칭’ 필수! 안 하면 무임승차로 간주되어 800 kc 상당의 벌금.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="체코 프라하" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x200")

        나라이름 = Label(travel, text="체코 프라하", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="인구의 96%가 체코어 사용. 영어 상대적 잘 통하는 편. 러시아어, 독일어도 종종 쓰임",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="체코 프라하" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x900")
        global img_체코1, img_체코2, img_체코3

        나라이름 = Label(travel, text="체코 프라하", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟 : 관광", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="프라하성,  카를교,  구시가광장",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')
        img_체코1 = PhotoImage(file='체코프라하_추천스팟_프라하성.gif')
        label_체코1 = Label(travel, image=img_체코1)
        label_체코1.grid(row=4, column=0, sticky='W')
        img_체코2 = PhotoImage(file='체코프라하_추천스팟_카를교.gif').subsample(2)
        label_체코2 = Label(travel, image=img_체코2)
        label_체코2.grid(row=4, column=1)
        img_체코3 = PhotoImage(file='체코프라하_추천스팟_구시가광장.gif').subsample(2)
        label_체코3 = Label(travel, image=img_체코3)
        label_체코3.grid(row=5, column=0, sticky='W')



    if continent.get()=='유럽' and country.get()=="체코 프라하" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1100x500")
        global img_체코4

        나라이름 = Label(travel, text="체코 프라하", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_체코4 = PhotoImage(file='체코프라하_필수어휘.gif').subsample(1)
        label_체코4 = Label(travel, image=img_체코4)
        label_체코4.grid(row=3, column=1)

    if continent.get()=='유럽' and country.get()=="체코 프라하" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("700x200")

        나라이름 = Label(travel, text="체코 프라하", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="오스트리아, 독일, 폴란드, 슬로바키아 공화국과 인접. 국토의 서부는 보헤미아 지방, 동부는 모라비아 지방으로 불림.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="체코 프라하" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("2000x1300")
        global img_체코5, img_체코6, img_체코7

        나라이름 = Label(travel, text="체코 프라하", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="((관광))\n"
                            "구시가 광장 구시청사 시계탑: 1410년에 처음 만들어진 매시 정각에"
                            "종소리와 함께 인형들이 나와 움직이는 천문 시계\n"
                            "구시가 광장 틴 성모교회: 구시가 광장의 여러 건물들 중"
                            "야경이 가장 아름답다고 꼽히는 성모 교회:"
                            "전망대에서 프라하의 시내를 한 눈에 볼 수 있음\n\n"
                            "((휴양))"
                            "프라하온천마을 까를로비바리: 카를의 온천이라는 뜻의 카를로비바리 마을.\n"
                            "괴테가 서른 번 넘게 방문했고, 그 외에도 베토벤, 쇼팽, 표트르 대제 등 많은 유명인들도"
                            "즐겨 찾은 오래 휴양지. \n"
                            "온천수를 원없이 마시고 온천을 즐길 수 있는 곳\n\n"
                            "((식도락))\n"
                            "1. 꼴레뇨 : 돼지 무릎부위를 구워낸 체코식 족발\n"
                            "2. 굴라쉬 : 동유럽에서 즐겨먹는 속을 파낸 빵 속에 고기와 야채로 만든 전통 스튜\n"
                            "3.스비치코바 : 스프에 익힌 소고기와 빵을 생크림과 크랜베리잼과 곁들어 먹는 체코식 스테이크\n"
                            "4. 팔라친키 : 체코식 얇은 팬케이크로 크레페와 비슷",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')
        img_체코5 = PhotoImage(file='체코프라하_테마별추천활동_관광_시계탑.gif').subsample(2)
        label_체코5 = Label(travel, image=img_체코5)
        label_체코5.grid(row=3, column=1)
        img_체코6 = PhotoImage(file='체코프라하_테마별추천활동_관광_성모교회.gif').subsample(2)
        label_체코6 = Label(travel, image=img_체코6)
        label_체코6.grid(row=4, column=0, sticky='W')
        img_체코7 = PhotoImage(file='체코프라하_테마별추천활동_휴양_온천마을.gif').subsample(2)
        label_체코7 = Label(travel, image=img_체코7)
        label_체코7.grid(row=4, column=1)

    if continent.get()=='유럽' and country.get()=="체코 프라하" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1000x600")
        global img_체코8

        나라이름 = Label(travel, text="체코 프라하", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="많은 관광지 방문 예정이라면 프라하 카드 구매할 것! 해당기간 동안 교통수단(공항 익스프레스 포함) 무료 + 프라하의 관광지 무료입장/할인.\n"
                        "2일 : 성인 1550kc, 학생 1150 kc , 3일 : 성인 1810 kc, 학생: 1330 kc\n"
                        "여권과 여행자보험증서(영문) 항시 휴대 필요. 불심검문시 없으면 상당한 벌금 부과되기에 주의할 것!!",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')
        img_체코8 = PhotoImage(file='체코프라하_개인적꿀팁.gif').subsample(1)
        label_체코8 = Label(travel, image=img_체코8)
        label_체코8.grid(row=4, column=0, sticky='W')

    if continent.get()=='유럽' and country.get()=="체코 프라하" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")

        나라이름 = Label(travel, text="체코 프라하", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="-1,2월 한겨울 날씨 평균기온 -2도, 3,4월 적은비 평균기온 4도, 5,6월 평균기온 15도 적은비,\n"
                           "7,8월 평균기온 19도 선선한 날씨, 9,10월 평균기온 11도 서늘 11,12월 평균기온 1도 약간의 비",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')
    


    if continent.get()=='유럽' and country.get()=="오스트리아 빈" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x100")

        나라이름 = Label(travel, text="오스트리아 빈", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="지하철, 경전철, 버스, 근거리 열차, 트램\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="오스트리아 빈" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x100")

        나라이름 = Label(travel, text="오스트리아 빈", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="독일어\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="오스트리아 빈" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")

        나라이름 = Label(travel, text="오스트리아 빈", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        travel.geometry("800x600")
        global img_슈테판대성당, img_빈국립오페라하우스

        나라이름 = Label(travel, text="오스트리아 빈", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="슈테판대성당\n",bg='lightsteelblue', justify='left').grid(row=3, column=0, sticky='W')
        Label(travel, text="빈국립오페라하우스\n",bg='lightsteelblue', justify='left').grid(row=3, column=1)

        img_슈테판대성당 = PhotoImage(file='오스트리아빈_추천스팟_슈테판대성당.gif')
        label_슈테판대성당 = Label(travel, image=img_슈테판대성당)
        label_슈테판대성당.grid(row=4, column=0, sticky='W')

        img_빈국립오페라하우스 = PhotoImage(file='오스트리아빈_추천스팟_빈국립오페라하우스.gif')
        label_빈국립오페라하우스 = Label(travel, image=img_빈국립오페라하우스)
        label_빈국립오페라하우스.grid(row=4, column=1)

    if continent.get()=='유럽' and country.get()=="오스트리아 빈" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x100")

        나라이름 = Label(travel, text="오스트리아 빈", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="Vielen Dank.필-렌 당크: 감사합니다\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="오스트리아 빈" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x100")

        나라이름 = Label(travel, text="오스트리아 빈", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="오스트리아 북서부\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="오스트리아 빈" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x400")

        나라이름 = Label(travel, text="오스트리아 빈", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="빈국립오페라하우스",bg='lightsteelblue', justify='left').grid(row=3, column=0, sticky='W')
        Label(travel, text="니슈마르크트시장",bg='lightsteelblue', justify='left').grid(row=3, column=1, sticky='W')
        global img_빈국립오페라하우스2, img_니슈마르크트시장

        img_빈국립오페라하우스2 = PhotoImage(file='오스트리아빈_추천스팟_빈국립오페라하우스.gif')
        label_빈국립오페라하우스2 = Label(travel, image=img_빈국립오페라하우스2)
        label_빈국립오페라하우스2.grid(row=4, column=0, sticky='W')
        
        img_니슈마르크트시장 = PhotoImage(file='오스트리아빈_테마별추천활동_니슈마르크트시장.gif')
        label_니슈마르크트시장 = Label(travel, image=img_니슈마르크트시장)
        label_니슈마르크트시장.grid(row=4, column=1)


    if continent.get()=='유럽' and country.get()=="오스트리아 빈" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x200")

        나라이름 = Label(travel, text="오스트리아 빈", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="비엔나 왕궁 예배당 매주 일요일 빈 소년 합창단의 공연 \n 여름에도 10도까지 내려갈 수 있어 겉옷 챙기는 것이 좋음\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="오스트리아 빈" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x200")

        나라이름 = Label(travel, text="오스트리아 빈", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="여름철 평균 온도는 약 27도, 겨울철 평균온도는 약 6도\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')


    if continent.get()=='유럽' and country.get()=="스웨덴 스톡홀롬" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x400")

        나라이름 = Label(travel, text="스웨덴 스톡홀롬", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=3,column=0, sticky='W')
        Label(travel, text="버스와 지하철, 배가 스톡홀롬의 구석구석을 연결해준다.\n외국인들이 가장 편리하게 이용할 수 있는 교통수단은 Tunnelban이라 부르는 지하철이다.\n그러나 교통비가 비싸서 많은 사람들이 자전거를 탄다.\n유럽여행하면 자주 볼 수 있는 트램도 있다.\n트램은 일반적인 도로 위에 깔린 레일 위를 주행하는 노면전차이다.",bg='lightsteelblue', justify='left').grid(row=4,column=0, sticky='W')

    if continent.get()=='유럽' and country.get()=="스웨덴 스톡홀롬" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x100")

        나라이름 = Label(travel, text="스웨덴 스톡홀롬", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=51,column=0, sticky='W')
        Label(travel, text="스웨덴어",bg='lightsteelblue', justify='left').grid(row=52,column=0, sticky='W')

    if continent.get()=='유럽' and country.get()=="스웨덴 스톡홀롬" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x400")

        나라이름 = Label(travel, text="스웨덴 스톡홀롬", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=5,column=0, sticky='W')
        Label(travel, text="바사박물관\n시티 홀\n포토그라피스카 박물관\n드류르 가르텐\n스칸센 야외 박물관\n드로트닝홀름 궁전 및 극장\n스톡홀롬 중세 박물관\n스톡홀롬 대성당\n쇠데르말름",bg='lightsteelblue', justify='left').grid(row=6,column=0, sticky='W')

    if continent.get()=='유럽' and country.get()=="스웨덴 스톡홀롬" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x500")

        나라이름 = Label(travel, text="스웨덴 스톡홀롬", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=53,column=0, sticky='W')
        Label(travel, text="안녕하세요(hej, god eftermiddag)\n실례합니다(Ursäkta, förlåt)\n감사합니다(tack)\n반갑습니다(Trevligt att träffas)\n죄송합니다(Jag är ledsen, Ursäkta, förlåt)\n아주 감사드립니다(Tack så mycket)\n뭐라고요?(Ursäkta, vad sa du?)\n영어를 할 줄 아세요?(Talar du engelska?)\n만나서 반가워요.(Trevligt att träffas.)\n이거 얼마예요?(Hur mycket kostar den här?)\n카드로 계산할 수 있어요?(Kan jag betala med kort?)\n어디서 계산하면 되죠?(Var betalar jag?)\n...는(은) 어디서 찾을 수 있나요?(Var kan jag hitta...)\n실례지만 현지인이신가요?(Ursäkta mig, bor du här?)\n저 좀 도와주시겠어요?(Kan du hjälpa mig?)\n도와주셔서 감사합니다(Tack för hjälpen!)\n얼마예요?(Vad är jag skyldig?)\n메뉴 좀 주시겠어요?(Kan vi få titta på menyn, tack?)\n이거 포장해 주실 수 있나요?(Kan vi beställa det här att ta med?)\n",bg='lightsteelblue', justify='left').grid(row=54,column=0, sticky='W')

    if continent.get()=='유럽' and country.get()=="스웨덴 스톡홀롬" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")

        나라이름 = Label(travel, text="스웨덴 스톡홀롬", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=7,column=0, sticky='W')
        Label(travel, text="스톡홀름이라는 이름의 유래는 통나무(Stock)와 작은 섬(Holm)이라는 설이 있다.\n이 지역을 처음 발견한 사람들이 통나무를 띄워 도시를 만들면서 이름을 이렇게 지었다고 한다.\n많은 반도와 작은 섬 위에 자리잡고 있다.\n13개의 하중도가 연결되어 이루어진 도시여서 별명도 '북유럽의 베네치아'이다.",bg='lightsteelblue', justify='left').grid(row=8,column=0, sticky='W')

    if continent.get()=='유럽' and country.get()=="스웨덴 스톡홀롬" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1100x800")
        global img_스3,img_스4,img_스6,img_스7

        나라이름 = Label(travel, text="스웨덴 스톡홀롬", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동(휴양)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=10,column=0, sticky='W')
        Label(travel, text="쇠데르말름: 시내에서 조금 떨어진 동네인데 조용하고 건물들도 시내보다는 유럽양식이라 예쁘다.\n평화로운 분위기가 좋다. 언덕에 올라가면 스톡홀롬 시내 전경을 볼 수 있다.\n아기자기한 카페와 상점이 많다.",bg='lightsteelblue', justify='left').grid(row=11,column=0, sticky='W')
        img_스3 = PhotoImage(file='스톡홀롬 쇠데르말름.gif').subsample(3)
        label_스3 = Label(travel, image=img_스3)
        label_스3.grid(row=12, column=0, sticky='W')

        Label(travel, text="테마별추천활동(휴양)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=13,column=0, sticky='W')
        Label(travel, text="드류르 가르텐: 시내와는 거리가 좀 떨어져 있어서 교통수단을 이용하면 편하게 다녀올 수 있다.\n공간 구성이 잘 되어있어서 아무 생각없이 가볍게 산책하기 좋고, 힐링이 되는 공원이다.",bg='lightsteelblue', justify='left').grid(row=14,column=0, sticky='W')
        img_스4 = PhotoImage(file='스톡홀롬 드류르 가르텐.gif').subsample(4)
        label_스4 = Label(travel, image=img_스4)
        label_스4.grid(row=15, column=0, sticky='W')


        Label(travel, text="테마별추천활동(관광)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=10,column=1)
        Label(travel, text="스톡홀롬 대성당: 감라스탄 중심부 노벨뮤지엄, 스톡홀름 왕궁 바로 옆에 위치한다.\n다른 유럽의 대성당들과 비교하자면 그렇게 크고 화려한 외관은 아니지만 아름답다.\n북유럽풍보다는 전형적인 가톨릭 성당 느낌이 많이 난다. 입장료가 있다.",bg='lightsteelblue', justify='left').grid(row=11,column=1)
        img_스6 = PhotoImage(file='스톡홀롬 대성당.gif').subsample(2)
        label_스6 = Label(travel, image=img_스6)
        label_스6.grid(row=12, column=1)


        Label(travel, text="테마별추천활동(식도락)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=13,column=1)
        Label(travel, text="순록 스테이크: 스웨덴 전통 요리이다. 고기는 부드럽지만 처음에 먹을 때 가죽향이 조금 심하다.\n동물향이 심하다고 보면 된다. 가죽을 먹는 듯한 착각이 들 수도 있다.\n그런데 먹다보면 맛있어진다. 샐러리와 같이 먹으면 환상적이다.",bg='lightsteelblue', justify='left').grid(row=14,column=1)
        img_스7 = PhotoImage(file='스톡홀롬 순록 스테이크.gif').subsample(4)
        label_스7 = Label(travel, image=img_스7)
        label_스7.grid(row=15, column=1)

    if continent.get()=='유럽' and country.get()=="스웨덴 스톡홀롬" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x400")

        나라이름 = Label(travel, text="스웨덴 스톡홀롬", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=55,column=0, sticky='W')
        Label(travel, text="1. 유럽은 도시락 문화가 잘 발달되어 있어서\n스웨덴 버스 안에서는 음식 먹는 게 일반적이다.\n\n2. 물가가 정말 살벌하다.\n\n3. 보편적인 유럽 음식이 다 그렇듯이, 음식이 조금 짜다.\n\n4. 스웨덴은 예약 문화가 활성화 돼있어서\n레스토랑 같은 곳은 예약을 안 하면 안 좋은 자리를 내어준다.\n가능하면 예약을 하고 가는 것이 좋다.",bg='lightsteelblue', justify='left').grid(row=56,column=0, sticky='W')

    if continent.get()=='유럽' and country.get()=="스웨덴 스톡홀롬" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x600")
        global img_스2

        나라이름 = Label(travel, text="스웨덴 스톡홀롬", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=1,column=0, sticky='W')
        Label(travel, text="스톡홀롬의 여름은 쾌적하지만 부분적으로 흐리며, 겨울은 매우 춥고 건조하며 대부분 흐리다.\n기온은 전형적으로 영하 6도~22도이며, 드물게 영하 14도 이하거나 27도 이상이다.\n따뜻한 활동을 위해서는 6월말~8월 중순에 여행가는 것이 가장 적합하다.",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_스2 = PhotoImage(file='스톡홀롬의 날씨.gif').subsample(2)
        label_스2 = Label(travel, image=img_스2)
        label_스2.grid(row=3, column=0, sticky='W')


    if continent.get()=='유럽' and country.get()=="스페인 바르셀로나" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("700x350")

        나라이름 = Label(travel, text="스페인 바르셀로나", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=3,column=0, sticky='W')
        Label(travel, text="오직 바르셀로나 도심 여행을 위해서는 렌트차를 쓰는 것은 추천하지 않는다.\n주차나 치안의 문제도 있지만 무엇보다 바르셀로나는 대중교통이 잘 발달되어 있다.\n바르셀로나 교통수단의 꽃으로 T-10을 꼽아볼 수 있다.\n이 카드를 구매하면 1년 동안 사용이 가능하며, 매년 금액이 인상된다.\n75분간 총 3번 환승이 가능하다. 다만, 같은 교통수단은 환승이 불가능하다.\n모든 지하철역과 담배 가게에서 판다.\n대중교통 종류와 상관없이 10번 사용할 수 있다.\nT-30은 30회, T-50은 50회 사용 가능하다. T-mes는 한 달 무제한권이다.\n마그네틱 인식 시스템이라 구겨지지 않게 조심한다. \n10회를 모두 사용했어도 마지막 목적지 출구를 통과하기 전까지 티켓을 소지한다.\n만 4세의 어린이는 무임승차가 가능하다.",bg='lightsteelblue', justify='left').grid(row=4,column=0, sticky='W')

    if continent.get()=='유럽' and country.get()=="스페인 바르셀로나" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x200")

        나라이름 = Label(travel, text="스페인 바르셀로나", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=51,column=0, sticky='W')
        Label(travel, text="에스파냐어(스페인어)가 공용어이나\n바르셀로나는 독립운동 중이어서 독자적인 까탈루냐어를 쓴다.",bg='lightsteelblue', justify='left').grid(row=52,column=0, sticky='W')

    if continent.get()=='유럽' and country.get()=="스페인 바르셀로나" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x400")

        나라이름 = Label(travel, text="스페인 바르셀로나", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=5,column=0, sticky='W')
        Label(travel, text="라 사그라다 파밀리아\n구엘 공원\n카사 밀라\n카사 바트요\n카탈라나 음악당\n몬세라트 절벽 도시\n람블라스 거리\n몬주익 언덕\n바르셀로나 올림픽 경기장",bg='lightsteelblue', justify='left').grid(row=6,column=0, sticky='W')

    if continent.get()=='유럽' and country.get()=="스페인 바르셀로나" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")

        나라이름 = Label(travel, text="스페인 바르셀로나", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=53,column=0, sticky='W')
        Label(travel, text="안녕(Hola: 올라/만났을 때)\n잘가(Adios: 아디오스/헤어질 때)\n감사해요(Gracias: 그라씨아스)\n정말 고맙습니다(Muchas gracias: 무챠스 그라씨아스)\n실례합니다.(Perdon: 뻬르돈/Permiso: 뻬르미쏘)\n미안합니다(Lo siento: 로 씨엔또)\n네(si: 씨)\n아니요(no: 노)\n얼마예요?(¿Cuanto cuesta?: 꾸안또 꾸에스따?)\n화장실이 어디에 있습니까?(¿Donde esta el aseo?: 돈데 에스따 엘 아쎄오?)\n~에 가려면 어떻게 갑니까?(Como se va a esta ~?: 꼬모 쎄 바 에쓰따 ~?)\n짐을 보관해 주실 수 있나요?(¿Puede guardar el equipaje, por favor?: 뿌에데 구알달 엘 에끼빠헤, 뽈 파볼?)",bg='lightsteelblue', justify='left').grid(row=54,column=0, sticky='W')

    if continent.get()=='유럽' and country.get()=="스페인 바르셀로나" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x300")

        나라이름 = Label(travel, text="스페인 바르셀로나", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=7,column=0, sticky='W')
        Label(travel, text="스페인의 북동쪽 지중해 해변에 위치한다.\n지중해 연안의 항구도시이며,\n항만규모와 상공업 활동에 있어서는 에스파냐 제1의 도시이다.\n교외지역을 포함한 바르셀로나는 비옥한 해안평야에 펼쳐져 있으며,\n천연의 양항과 더불어 에스파냐 최대의 산업도시를 이룬다.",bg='lightsteelblue', justify='left').grid(row=8,column=0, sticky='W')

    if continent.get()=='유럽' and country.get()=="스페인 바르셀로나" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1100x1100")
        global img_바3,img_바5,img_바6,img_바7

        나라이름 = Label(travel, text="스페인 바르셀로나", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동(쇼핑)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=10,column=0, sticky='W')
        Label(travel, text="B.d: 바르셀로나의 최첨단 건축가와 디자이너 그룹이 세운 B.d는\n가우디가 그의 상징적인 건물을 염두에 두고 착안한 가구와 세간살이를\n수작업으로 복제한 제품들을 선보인다.",bg='lightsteelblue', justify='left').grid(row=11,column=0, sticky='W')
        img_바3 = PhotoImage(file='바르셀로나 B.d.gif').subsample(3)
        label_바3 = Label(travel, image=img_바3)
        label_바3.grid(row=12, column=0, sticky='W')

        Label(travel, text="테마별추천활동(식도락)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=13,column=0, sticky='W')
        Label(travel, text="빠에야: 해산물을 주재료로 하는 볶음밥이다.\n스페인의 전통요리로 잘 알려져 있다.\n빠에야는 둥근 프라이팬을 가리키는 말이다. 보통 양쪽에 손잡이가 있다.\n야채와    육류가 어우러져 있는 것이 일품이다.",bg='lightsteelblue', justify='left').grid(row=14,column=0, sticky='W')
        img_바7 = PhotoImage(file='바르셀로나 빠에야.gif').subsample(3)
        label_바7 = Label(travel, image=img_바7)
        label_바7.grid(row=15, column=0, sticky='W')

        Label(travel, text="테마별추천활동(관광)", font=('양재참숯체B', 15), fg="blue",bg=    'lightsteelblue', justify='left').grid(row=10,column=1)
        Label(travel, text="라 사그라다 파밀리아: 기하학적인 네오고딕양식을 차용해서 성당 외관에 대한 고정관념을 깬 건축물이다.\n가우디는 세상을 떠나기 전 40년 동안 이 성 가족성당 건축에 심혈을 기울였다.\n이 건축물은 가우디 사망 100년이 되는 해인 2026년에 완공될 예정이다.",bg='lightsteelblue', justify='left').grid(row=11,column=1)
        img_바5 = PhotoImage(file='바르셀로나 라 사그라다 파밀리아.gif').subsample(4)
        label_바5 = Label(travel, image=img_바5)
        label_바5.grid(row=12, column=1)

        Label(travel, text="테마별추천활동(관광)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=13,column=1)
        Label(travel, text="구엘 공원: 지중해가 내려다보이는 전망 좋은 언덕 위에 자리잡고 있다.\n이 공원은 아기자기한 것들로 가득찬 곳이다.\n가우디는 이곳을 부유층의 전원주택 단지로 개발했으나\n바르셀로나 시가 소유권을 사들여 공원으로 탈바꿈시켰다.",bg='lightsteelblue', justify='left').grid(row=14,column=1)
        img_바6 = PhotoImage(file='바르셀로나 구엘공원.gif').subsample(3)
        label_바6 = Label(travel, image=img_바6)
        label_바6.grid(row=15, column=1)

        Label(travel, text="테마별추천활동(식도락)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=13,column=0, sticky='W')
        Label(travel, text="빠에야: 해산물을 주재료로 하는 볶음밥이다.\n스페인의 전통요리로 잘 알려져 있다.\n빠에야는 둥근 프라이팬을 가리키는 말이다. 보통 양쪽에 손잡이가 있다.\n야채와 육류가 어우러져 있는 것이 일품이다.",bg='lightsteelblue', justify='left').grid(row=14,column=0, sticky='W')
        img_바7 = PhotoImage(file='바르셀로나 빠에야.gif').subsample(3)
        label_바7 = Label(travel, image=img_바7)
        label_바7.grid(row=15, column=0, sticky='W')

    if continent.get()=='유럽' and country.get()=="스페인 바르셀로나" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x400")

        나라이름 = Label(travel, text="스페인 바르셀로나", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=55,column=0, sticky='W')
        Label(travel, text="1. 신용카드 하나만 들고 가지 말고\n반드시 스페인의 통화인 유로화를 환전해서 챙겨간다.\n\n2. 스페인 사람들은 영어로 대화가 잘 되지 않는다.\n간단한 대화는 가능하지만, 말이 길어지면 스페인어로 답변이 돌아온다.\n\n3. 버스는 크게 파란색의 심야 버스 2가지와\n일반 빨간색 버스가 있다.\n\n4. 지하철이 시내 중심부까지 잘 연결되어 있어서\n가장 편리하게 사용할 수 있는 교통수단이다.\n티켓을 찍는 방향이 왼쪽이라는 점만 참고하면 된다.",bg='lightsteelblue', justify='left').grid(row=56,column=0, sticky='W')

    if continent.get()=='유럽' and country.get()=="스페인 바르셀로나" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x500")
        global img_바2

        나라이름 = Label(travel, text="스페인 바르셀로나", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=1,column=0, sticky='W')
        Label(travel, text="바르셀로나는 지중해성 기후이다.\n따뜻하고 습도가 있는 겨울과 건조한 여름이 특징이다.\n이베리아 반도 동쪽에 있는 바르셀로나는 대서양에서 서풍이 불어와\n비가 내리지 않는 낮은 습도 상태에 도달하게 한다.\n대서양에 근접 위도와 지형이 다른 대부분의 지중해 분지 지역에 비해\n바르셀로나의 여름이 건조하지 않을 이유가 된다.",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_바2 = PhotoImage(file='바르셀로나 날씨.gif')
        label_바2 = Label(travel, image=img_바2)
        label_바2.grid(row=3, column=0, sticky='W')



    if continent.get()=='유럽' and country.get()=="아이슬란드 레이카비크" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("450x100")

        나라이름 = Label(travel, text="아이슬란드 레이카비크", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="버스\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="아이슬란드 레이카비크" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("450x100")

        나라이름 = Label(travel, text="아이슬란드 레이카비크", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="아이슬란드어\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="아이슬란드 레이카비크" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x450")

        나라이름 = Label(travel, text="아이슬란드 레이카비크", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        global img_오로라투어, img_블루라군온천

        나라이름 = Label(travel, text="아이슬란드 레이카비크", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="오로라투어\n",bg='lightsteelblue', justify='left').grid(row=3, column=0, sticky='W')
        Label(travel, text="블루라군온천\n",bg='lightsteelblue', justify='left').grid(row=3, column=1)

        img_오로라투어 = PhotoImage(file='아이슬란드레이카비크_추천스팟_오로라투어.gif')
        label_오로라투어 = Label(travel, image=img_오로라투어)
        label_오로라투어.grid(row=4, column=0, sticky='W')

        img_블루라군온천 = PhotoImage(file='아이슬란드레이카비크_추천스팟_블루라군온천.gif')
        label_블루라군온천 = Label(travel, image=img_블루라군온천)
        label_블루라군온천.grid(row=4, column=1)        

    if continent.get()=='유럽' and country.get()=="아이슬란드 레이카비크" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("450x100")

        나라이름 = Label(travel, text="아이슬란드 레이카비크", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="takk.탁: 감사합니다\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="아이슬란드 레이카비크" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("50x100")

        나라이름 = Label(travel, text="아이슬란드 레이카비크", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="아이슬란드 섬 남서부 팍사 만에 면한 도시\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="아이슬란드 레이카비크" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x400")

        나라이름 = Label(travel, text="아이슬란드레이카비크", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="오로라투어",bg='lightsteelblue', justify='left').grid(row=3, column=0, sticky='W')
        Label(travel, text="블루라군온천",bg='lightsteelblue', justify='left').grid(row=3, column=1, sticky='W')
        global img_오로라투어2, img_블루라군온천2

        img_오로라투어2 = PhotoImage(file='아이슬란드레이카비크_추천스팟_오로라투어.gif')
        label_오로라투어2 = Label(travel, image=img_오로라투어2)
        label_오로라투어2.grid(row=4, column=0, sticky='W')

        img_블루라군온천2 = PhotoImage(file='아이슬란드레이카비크_추천스팟_블루라군온천.gif')
        label_블루라군온천2 = Label(travel, image=img_블루라군온천2)
        label_블루라군온천2.grid(row=4, column=1)     

    if continent.get()=='유럽' and country.get()=="아이슬란드 레이카비크" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("450x200")

        나라이름 = Label(travel, text="아이슬란드 레이카비크", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="대중교통이 불편하여 시티투어 버스 추천\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='유럽' and country.get()=="아이슬란드 레이카비크" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("450x200")

        나라이름 = Label(travel, text="아이슬란드 레이카비크", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="여름철 평균기온은 약 10도, 겨울철 기온은 영하 10도에서 영상10도까지\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')


    if continent.get()=='북아메리카' and country.get()=="쿠바 하바나" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x200")

        나라이름 = Label(travel, text="쿠바 하바나", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="시내버스\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='북아메리카' and country.get()=="쿠바 하바나" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x200")

        나라이름 = Label(travel, text="쿠바 하바나", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="에스파냐어\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='북아메리카' and country.get()=="쿠바 하바나" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x500")

        나라이름 = Label(travel, text="쿠바 하바나", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        global img_까삐똘리오, img_비에하광장

        나라이름 = Label(travel, text="쿠바 하바나", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="까삐똘리오\n",bg='lightsteelblue', justify='left').grid(row=3, column=0, sticky='W')
        Label(travel, text="비에하 광장\n",bg='lightsteelblue', justify='left').grid(row=3, column=1)

        img_까삐똘리오 = PhotoImage(file='쿠바아바나_추천스팟_까삐똘리오.gif')
        label_까삐똘리오 = Label(travel, image=img_까삐똘리오)
        label_까삐똘리오.grid(row=4, column=0, sticky='W')

        img_비에하광장 = PhotoImage(file='쿠바아바나_추천스팟_비에하광장.gif')
        label_비에하광장 = Label(travel, image=img_비에하광장)
        label_비에하광장.grid(row=4, column=1)    
        

    if continent.get()=='북아메리카' and country.get()=="쿠바 하바나" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x200")

        나라이름 = Label(travel, text="쿠바 하바나", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="Me lo puede rebajar.멜 로 뿌에데 레바하르?: 좀 만 깎아주세요\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='북아메리카' and country.get()=="쿠바 하바나" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x200")

        나라이름 = Label(travel, text="쿠바 하바나", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="쿠바섬의 북서해안, 멕시코만에 면하는 항구도시\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='북아메리카' and country.get()=="쿠바 하바나" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x400")

        나라이름 = Label(travel, text="쿠바 하바나", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="올드카투어",bg='lightsteelblue', justify='left').grid(row=3, column=0, sticky='W')
        Label(travel, text="말레콘비치",bg='lightsteelblue', justify='left').grid(row=3, column=1, sticky='W')
        global img_올드카투어, img_말레콘비치
        
        img_올드카투어 = PhotoImage(file='쿠바아바나_테마별추천활동_올드카투어.gif')
        label_올드카투어 = Label(travel, image=img_올드카투어)
        label_올드카투어.grid(row=4, column=0, sticky='W')

        img_말레콘비치 = PhotoImage(file='쿠바아바나_테마별추천활동_말레콘비치.gif')
        label_말레콘비치 = Label(travel, image=img_말레콘비치)
        label_말레콘비치.grid(row=4, column=1)
        

    if continent.get()=='북아메리카' and country.get()=="쿠바 하바나" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x200")

        나라이름 = Label(travel, text="쿠바 하바나", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="미국달러보다 캐나다 유로 화폐 환전이 이득, 구글 사용할 수 없어 맵스미 어플 설치, 흥정 필수\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='북아메리카' and country.get()=="쿠바 하바나" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x200")

        나라이름 = Label(travel, text="쿠바 하바나", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="여름은 6월부터 9월 평균 기온은 24~32, 겨울은 12월부터 3월 평균 기온은 18~26\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')


    if continent.get()=='북아메리카' and country.get()=="미국 뉴욕" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x400")

        나라이름 = Label(travel, text="미국 뉴욕", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="교통정보: 버스, 지하철 편도 2.75$, express 버스 편도 6.5$(출퇴근시간과 일반 요금이 조절되어 바뀌기도 함)\n"
                            "메트로 카드로 티켓 구메 후 7일간 무제한 버스, 지하철 이용이 가능한 카드 32$. \n"
                            "모든 지하철 역의 티켓 자판기, 부스, 혹은 메트로카드 판매 점포라고 써있는 모든 가게에서 티켓 구입 가능\n\n"
                            "페리를 이용하여 스테이튼 아일랜드와 맨하튼 사이를 지나갈 수 있음 \n\n"
                            "택시 기본요금 3$내외, 안원수에 따라 차비가 더 붙고, 팁도 요금에 합산되어 나옴",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='북아메리카' and country.get()=="미국 뉴욕" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x200")

        나라이름 = Label(travel, text="미국 뉴욕", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="800개가 넘는 언어가 사용되며, 세계에서 가장 다양한 언어가 공존하는 도시. 하지만 영어가 주언어",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='북아메리카' and country.get()=="미국 뉴욕" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1200x1000")
        global img_뉴욕1, img_뉴욕2

        나라이름 = Label(travel, text="미국 뉴욕", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="타임스스퀘어, 자유의 여신상",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')
        img_뉴욕1 = PhotoImage(file='미국뉴욕_추천스팟_타임스스퀘어.gif').subsample(1)
        label_뉴욕1 = Label(travel, image=img_뉴욕1)
        label_뉴욕1.grid(row=4, column=0, sticky='W')
        img_뉴욕2 = PhotoImage(file='미국뉴욕_추천스팟_자유의여신상.gif').subsample(1)
        label_뉴욕2 = Label(travel, image=img_뉴욕2)
        label_뉴욕2.grid(row=4, column=1)

    if continent.get()=='북아메리카' and country.get()=="미국 뉴욕" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x400")

        나라이름 = Label(travel, text="미국 뉴욕", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="입국심사가 깐깐한 경우가 많으니 여행목적, 체류기간, 공간을 완벽히 대답할 수 있어야함.\n\n"
                            "I will stay in America for 2 weeks(미국에 2주동안 있을거에요)\n"
                            "My purpose of visit is for sightseeing(방문 목적은 관광이에요)\n"
                            "I will stay at Hilton Hotel in New York, but I don’t know the address\n"
                            "(뉴욕의 힐튼 호텔에서 지낼거지만 주소는 잘 모르겠네요)\n"
                            "I now have 1500$. 1000$ in traveler’s check and rest in cash. \n"
                            "(저는 지금 1500 달러를 갖고 있는 데, 1000 달러는 여행자 수표, 나머지는 현금으로 가지고 있어요.)",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='북아메리카' and country.get()=="미국 뉴욕" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x300")

        나라이름 = Label(travel, text="미국 뉴욕", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="맨하튼, 브루클린, 퀸즈, 브롱크스, 스테이튼 아일랜드 다섯개의 자치구로 이루어져 있음.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='북아메리카' and country.get()=="미국 뉴욕" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1500x1500")
        global img_뉴욕3, img_뉴욕4, img_뉴욕5, img_뉴욕6, img_뉴욕7

        나라이름 = Label(travel, text="미국 뉴욕", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="((관광))\n"
                            "맨하튼 타임스스퀘어 24시간 꺼지지 않는 화려한 전광판들과 수많은 사람들과 상점들로 북적거리는 곳\n"
                            "엠파이어 스테이트 빌딩 : 뉴욕의 상징으로 널리 알려져 있는 건물. 위의 전망대에서 뉴욕을 한 눈에 볼 수 있다\n"
                            "그랜드 센트럴 역: 뉴욕 도심에 위치한 기차역으로 외벽에서 뉴욕을 상징하는 독수리 등의 조각상을 구경할 수 있음\n\n"
                            "((쇼핑))\n"
                            "소호거리 : 사우스 어브 하우스턴의 약자인 소호 거리. 브랜드와 편집샵들이 한 곳에 모여있는 쇼핑 거리\n"
                            "블루밍 데일스: 뉴욕의 대표적인 백화점\n"
                            "세포라: 코덕(코스메틱 덕후)들의 성지인 세포라.\n\n" 
                            "((식도락))\n"
                            "1. 피터루거 스테이크.(178 Broadway, New York, NY 11211) 정통 미국식 스테이크를 맛 볼 수 있는 곳\n"
                            "2. 에사 베이글(831 3rd Avenue, New York, NY 10022) 크림치즈 베이글이 유명한 브런치 식당\n"
                            "3. 쉑쉑 버거(691 8th Avenue, NewYork, NY 10036), 파이브가이즈 버거(253 @ 42nd Street, New York 10036)\n"
                              "미국식 두툼한 버거가 유명한 식당",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')
        img_뉴욕3 = PhotoImage(file='미국뉴욕_테마별추천활동_관광_타임스스퀘어.gif').subsample(2)
        label_뉴욕3 = Label(travel, image=img_뉴욕3)
        label_뉴욕3.grid(row=4, column=0, sticky='W')
        img_뉴욕4 = PhotoImage(file='미국뉴욕_테마별추천활동_관광_엠파이어스테이트빌딩.gif').subsample(2)
        label_뉴욕4 = Label(travel, image=img_뉴욕4)
        label_뉴욕4.grid(row=4, column=1)
        img_뉴욕5 = PhotoImage(file='미국뉴욕_테마별추천활동_관광_그랜드센트럴역.gif').subsample(2)
        label_뉴욕5 = Label(travel, image=img_뉴욕5)
        label_뉴욕5.grid(row=4, column=2)
        img_뉴욕6 = PhotoImage(file='미국뉴욕_테마별추천활동_쇼핑_소호거리.gif').subsample(2)
        label_뉴욕6 = Label(travel, image=img_뉴욕6)
        label_뉴욕6.grid(row=3, column=1)
        img_뉴욕7 = PhotoImage(file='미국뉴욕_테마별추천활동_쇼핑_블루밍데일스.gif').subsample(2)
        label_뉴욕7 = Label(travel, image=img_뉴욕7)
        label_뉴욕7.grid(row=3, column=2)

    if continent.get()=='북아메리카' and country.get()=="미국 뉴욕" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x400")

        나라이름 = Label(travel, text="미국 뉴욕", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="1.교통수단 조심하기: 한갸의 선로에 여러 개의 노선이 함께하기 때문에 노선 이름을 꼭 확인해야한다. \n"
                            "또한 뉴욕의 버스는 안내방송이 나오지도 않고 간격이 일정하지 않기 때문에 지하철을 주로 이용하거나 가까운 거리는 도보로 이동하라.\n"
                            "뉴욕의 교통체증은 심각한 편이기에 택시 또한 급한 경우가 아니면 타는 것을 피하라\n"
                            "2.자전거를 이용하라. 따릉이 처럼 뉴욕에도 시티 바이크가 비치되어 있기에 이용하여 이동하라\n"
                            "3.여신상에 올라가기 위해서는 하루에 300명만 입장이 가능하기 때문에 아침 일찍 가야지만 가능하다\n"
                            "4.메트로폴리탄 미술관은 상시 기부금 입장이 가능하다. 25달러 전부를 내기 보다는 더 적은 액수의 기부금을 내고 더 싸게 입장하여라",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='북아메리카' and country.get()=="미국 뉴욕" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")

        나라이름 = Label(travel, text="미국 뉴욕", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="7,8월 무더운 날씨와 많은 비 12-2월 혹한기 매우 춥고 많은 눈 나머지는 선선",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')


    if continent.get()=='북아메리카' and country.get()=="캐나다 밴쿠버" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x500")

        나라이름 = Label(travel, text="캐나다 밴쿠버", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=3,column=0, sticky='W')
        Label(travel, text="버스보다 공중에서 다니는 지상 전철인\n스카이 트레인을 많이 이용한다.\n공중에서 바깥 구경도 할 수 있다.\n무인으로 운영된다는 점이\n우리나라의 지하철과 다르다.\n넓어서 개인 자동차도 많이 타고 다닌다.",bg='lightsteelblue', justify='left').grid(row=4, column=0, sticky='W')

    if continent.get()=='북아메리카' and country.get()=="캐나다 밴쿠버" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x200")

        나라이름 = Label(travel, text="캐나다 밴쿠버", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=51,column=0, sticky='W')
        Label(travel, text="영어",bg='lightsteelblue', justify='left').grid(row=52,column=0, sticky='W')

    if continent.get()=='북아메리카' and country.get()=="캐나다 밴쿠버" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x500")

        나라이름 = Label(travel, text="캐나다 밴쿠버", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=5,column=0, sticky='W')
        Label(travel, text="그라우스 마운틴\n그랜빌 아일랜드\n하버센터 타워 전망대\n밴쿠버 아트갤러리\n캐나다 플레이스\n해리슨 핫 스프링스\n민터 가든\n캐필라노 협곡\n스탠리 파크",bg='lightsteelblue', justify='left').grid(row=6,column=0, sticky='W')

    if continent.get()=='북아메리카' and country.get()=="캐나다 밴쿠버" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x500")

        나라이름 = Label(travel, text="캐나다 밴쿠버", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=53,column=0, sticky='W')
        Label(travel, text="안녕하세요(Hello, How are you?)\n이거 얼마에요(How much is this?)\n감사합니다(Thank you.)\n우리 호텔은 몇호인가요?(What is my room number?)\n짐 좀 맡길 수 있을까요?(Can I leave my luggage?)\n~까지 어떻게 가나요?(How can I get to ~?)\n네(Yes/Okay)\n화장실이 어딘가요?(Where is the toilet?)\n아니요(No/Nope)\n반갑습니다(Nice to meet you!)",bg='lightsteelblue', justify='left').grid(row=54,column=0, sticky='W')

    if continent.get()=='북아메리카' and country.get()=="캐나다 밴쿠버" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x500")

        나라이름 = Label(travel, text="캐나다 밴쿠버", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=7,column=0, sticky='W')
        Label(travel, text="일반적으로 밴쿠버라고 할 때는\n밴쿠버 도심지, 노스 밴쿠버, 웨스트 밴쿠버, 버내비, 리치먼드 등\n13개 위성도시를 포함해 일컫는다.\n밴쿠버는 태평양을 바라보는 항구도시로,\n서부 캐나다 최대의 상공업 도시이자\n태평양으로 통하는 주요 무역항이다.\n시가지는 남쪽에 프레이저강의 삼각주 지대,\n북쪽에 만년설이 있는 해안산지를 바라보며,\n완만한 구릉에 전개되어 있다.\n다양한 자연환경에 둘러싸인 밴쿠버는\n캐나다 제3의 대도시임에도 불구하고\n아름다운 주택이 많아 조용한 휴양도시 같은 인상을 준다.",bg='lightsteelblue', justify='left').grid(row=8,column=0, sticky='W')

    if continent.get()=='북아메리카' and country.get()=="캐나다 밴쿠버" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x800")
        global img_밴3,img_밴4,img_밴5,img_밴8

        나라이름 = Label(travel, text="캐나다 밴쿠버", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동(휴양)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=10,column=0, sticky='W')
        Label(travel, text="스탠리 파크: 밴쿠버 다운타운의 서쪽,\n버라드만으로 튀어나온 반도에 자리 잡은 도시공원이다.\n버라드만을 바라볼 수 있는 반도의 바깥쪽을 따라\n'시월'이라 불리는 자전거 도로가 정비되어 있으며\n자전거와 도보로 아름다운 밴쿠버의 바다와 숲을 만끽할 수 있다.\n",bg='lightsteelblue', justify='left').grid(row=11,column=0, sticky='W')
        img_밴3 = PhotoImage(file='밴쿠버 스탠리파크.gif').subsample(2)
        label_밴3 = Label(travel, image=img_밴3)
        label_밴3.grid(row=12, column=0, sticky='W')


        Label(travel, text="테마별추천활동(휴양)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=13,column=0, sticky='W')
        Label(travel, text="빅토리아 부차드 가든: 원래 석회암 채석장이였는데\n그 수명을 다해 거의 폐허가 된 곳을\n부차드 부인이 사들여 정원으로 조금씩 조금씩 가꾸다\n그 규모가 커져 지금의 모습으로 변했다.",bg='lightsteelblue', justify='left').grid(row=14,column=0, sticky='W')
        img_밴4 = PhotoImage(file='밴쿠버 부차드 정원.gif').subsample(3)
        label_밴4 = Label(travel, image=img_밴4)
        label_밴4.grid(row=15, column=0, sticky='W')


        Label(travel, text="테마별추천활동(관광)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=10,column=1)
        Label(travel, text="캐필라노 협곡: 밴쿠버의 스탠리 파크에서 연결되는\n라이온스 게이트 브리지를 건너서 북쪽으로 길게 이어지는 협곡이다.\n안쪽으로 조금 더 들어가면 나오는 캐필라노 서스펜션 다리는\n이곳의 명물이다. 걸을 때마다 흔들려 상당한 스릴을 느낄 수 있다.",bg='lightsteelblue', justify='left').grid(row=11,column=1)
        img_밴5 = PhotoImage(file='밴쿠버 캐필라노협곡.gif').subsample(2)
        label_밴5 = Label(travel, image=img_밴5)
        label_밴5.grid(row=12, column=1)

        Label(travel, text="테마별추천활동(식도락)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=13,column=1)
        Label(travel, text="수블라키: 그리스의 유명한 패스트푸드이다.\n주로 꼬치에 여러 조각의 고기와 채소를 꽂아서 구워먹는다.\n이 음식은 피타라는 그리스식 빵에 구운 감자와\n여러 고명과 소스를 곁들여 먹는다.",bg='lightsteelblue', justify='left').grid(row=14,column=1)
        img_밴8 = PhotoImage(file='밴쿠버 수블라키.gif').subsample(2)
        label_밴8 = Label(travel, image=img_밴8)
        label_밴8.grid(row=15, column=1)


    if continent.get()=='북아메리카' and country.get()=="캐나다 밴쿠버" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x400")

        나라이름 = Label(travel, text="캐나다 밴쿠버", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=55,column=0, sticky='W')
        Label(travel, text="1. 밴쿠버는 캐나다 제 2의 도시지만 우리나라 사람들의 눈에는\n느리게 흘러가는 유유자적한 도시로 느껴질 가능성이 크다.\n여행 중간중간에 근처 공원에 들러서 쉬어가듯 시간을 보내고 가는 것도 추천한다.\n\n2. 밴쿠버의 치안은 안전한 편이나 여행자를 노리는\n절도, 소매치기 사건 등이 증가하고 있으므로 주의해야 한다.\n\n3. 생각보다 물가가 비싸므로 주의한다.",bg='lightsteelblue', justify='left').grid(row=56,column=0, sticky='W')

    if continent.get()=='북아메리카' and country.get()=="캐나다 밴쿠버" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x600")
        global img_밴2

        나라이름 = Label(travel, text="캐나다 밴쿠버", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=1,column=0, sticky='W')
        Label(travel, text="겨울에 캐나다 전 지역을 뒤덮는 북극의 찬 공기가 로키 산맥에 가로막혀\n밴쿠버의 겨울은 영하로 내려가는 날 거의 없이 온난하며,\n여름도 무덥지 않고 쾌적한 편이다.\n10~3월은 우기인데, 특히 12~1월은 흐리고 비 오는 날이 많은 편이다.\n6~8월은 햇볕이 좋아 여행하기에 최적의 환경이다.\n밴쿠버의 봄과 가을은 매우 짧은 편이다.\n눈이 4월 중순을 전후로 녹기에 봄이 매우 짧고,\n가을에는 강풍이 부는 지역이 많아 체감 온도가 매우 낮아\n외출이 가능한 날이 그리 많지 않다.",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_밴2 = PhotoImage(file='밴쿠버 날씨.gif')
        label_밴2 = Label(travel, image=img_밴2)
        label_밴2.grid(row=3, column=0, sticky='W')



    if continent.get()=='북아메리카' and country.get()=="미국 LA" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x200")

        나라이름 = Label(travel, text="미국 LA", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="버스, 우버, 지하철\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='북아메리카' and country.get()=="미국 LA" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x200")

        나라이름 = Label(travel, text="미국 LA", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="영어\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='북아메리카' and country.get()=="미국 LA" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x500")

        나라이름 = Label(travel, text="미국 LA", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        global img_산타모니카해변, img_유니버셜스튜디오

        나라이름 = Label(travel, text="미국 LA", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="산타모니카해변\n",bg='lightsteelblue', justify='left').grid(row=3, column=0, sticky='W')
        Label(travel, text="유니버셜스튜디오\n",bg='lightsteelblue', justify='left').grid(row=3, column=1)

        img_산타모니카해변 = PhotoImage(file='미국LA_추천스팟_산타모니카해변.gif')
        label_산타모니카해변 = Label(travel, image=img_산타모니카해변)
        label_산타모니카해변.grid(row=4, column=0, sticky='W')

        img_유니버셜스튜디오 = PhotoImage(file='미국LA_추천스팟_유니버셜스튜디오.gif')
        label_유니버셜스튜디오 = Label(travel, image=img_유니버셜스튜디오)
        label_유니버셜스튜디오.grid(row=4, column=1)

    if continent.get()=='북아메리카' and country.get()=="미국 LA" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x300")

        나라이름 = Label(travel, text="미국 LA", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="For sightseeing.:관광입니다\n I'm here on vacation.:휴가때문에 왔습니다.\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='북아메리카' and country.get()=="미국 LA" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x200")

        나라이름 = Label(travel, text="미국 LA", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="미국 캘리포니아주 남부의 태평양에 면한 도시\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='북아메리카' and country.get()=="미국 LA" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x400")

        나라이름 = Label(travel, text="미국 LA", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="다저스스타디움",bg='lightsteelblue', justify='left').grid(row=3, column=0, sticky='W')
        Label(travel, text="디즈니랜드",bg='lightsteelblue', justify='left').grid(row=3, column=1, sticky='W')
        global img_다저스스타디움, img_디즈니랜드
        
        img_다저스스타디움 = PhotoImage(file='미국LA_테마별추천활동_다저스스타디움.gif')
        label_다저스스타디움 = Label(travel, image=img_다저스스타디움)
        label_다저스스타디움.grid(row=4, column=0, sticky='W')

        img_디즈니랜드 = PhotoImage(file='미국LA_추천스팟_디즈니랜드.gif')
        label_디즈니랜드 = Label(travel, image=img_디즈니랜드)
        label_디즈니랜드.grid(row=4, column=1)

    if continent.get()=='북아메리카' and country.get()=="미국 LA" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x300")

        나라이름 = Label(travel, text="미국 LA", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="유니버셜스튜디오 미리 예약하면 가격 이익\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='북아메리카' and country.get()=="미국 LA" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x400")

        나라이름 = Label(travel, text="미국 LA", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="평균기온은 약 18℃이다\n 연평균강수량은 356㎜인데 대부분은 겨울철에 내린다\n 연 최고 기온은 29℃이며 최저기온은 약 7℃\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')



    if continent.get()=='남아메리카' and country.get()=="브라질 상파울로" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1100x500")

        나라이름 = Label(travel, text="브라질 상파울로", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="주요 교통 법규 및 문화\n"
                            "브라질은 자동차 보험가입이 의무사항 아니어서 무보험 차량이 상당수 운행 중이므로 이에 대해 각별히 주의를 기울여야 함\n"
                            "일방통행 도로가 상당히 발달해 있기에 익숙하지 않은 도로 운전 시 역주행에 각별히 유의해야 함\n"
                            "관련 사건사고 사례\n"
                            "무보험 차량과 사고 시 보상을 받지 못할 확률이 높음\n"
                            "카니발 축제기간 중 음주운전으로 인한 사고가 빈번히 발생함\n"
                            "실수나 주의부족으로 차량이 주요 대도시 빈민가에 진입할 경우 차량강도를 당할 확률이 아주 높음\n"
                            "대도시 후미진 주차장 등에서 충분한 주의를 기울이지 않을 경우 차량 강도를 당할 확률이 높음\n"
                            "대중교통\n"
                            "버스 및 소형택시(흰색, Ponto de Taxi)가 있으나 버스 내에서 강도, 소매치기 등 피해가 많이 발생하므로 시내 이동 시에는 택시를 이용하시는 것이 바람직합니다.\n"
                            "거리에 돌아다니는 택시보다는 호텔에 정차하고 있는 택시나, 공항에서는 라디오 택시( Radio Taxi, 선불제)를 이용하시는 것이 사후 요금에 따른 시비를 방지하기 위해 바람직합니다.\n"
                            "도로교통\n"
                            "도로가 일반적으로 노면이 고르지 못하고 정비 상태가 불량합니다. 도심에서 운전하다 보면 차량 및 오토바이가 차선 변경 신호를 주지 않고 갑자기 끼어들기 때문에 안전거리를 확보하여 운행합니다.\n"
                            "브라질리아 시내에서는 신호가 없는 횡단보도를 건너는 보행자가 있으면 무조건 정지해야 한다. 보행자는 차량이 정지하는 것을 당연하게 생각하고 있습니다.\n"
                            "무보험 차량이 많고 사고가 발생해도 무책임하므로 접촉사고가 나지 않도록 주의해야 합니다.\n"
                            "교통법규를 위반하면 벌과금이 많습니다. 운전자석, 조수석 및 뒷좌석 동반자의 안전벨트 착용도 의무사항이다.\n"
                            "안전벨트 미착용시 벌금을 127.69 헤알(약 63불) 정도 내야 합니다",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='남아메리카' and country.get()=="브라질 상파울로" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")

        나라이름 = Label(travel, text="브라질 상파울로", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text=" 언어 : 스페인어(카스티야어); 지역별 카탈루냐어, 바스크어, 갈리시아어를 공용어로 사용",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='남아메리카' and country.get()=="브라질 상파울로" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1200x800")
        global img_상파울로2, img_상파울로3, img_상파울로4

        나라이름 = Label(travel, text="브라질 상파울로", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟 : 관광", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=5,column=0, sticky='W')
        Label(travel, text="추천스팟 : 관광", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=5,column=1, sticky='W')
        Label(travel, text="추천스팟 : 관광", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=8,column=0, sticky='W')
        
        Label(travel, text="봉헤찌로\n"
                            "한인타운이 있어 한국인이라면 한번 들리면 재밌는 곳\n"
                            "상파울로 사람이 한국어를 하며 맞이해준다.",bg='lightsteelblue', justify='left').grid(row=6, column=0)
        Label(travel, text="베트맨 골목\n"
                            "배트맨 골목이지만 다양한 그래비피가 있는 곳으로\n"
                            "미국의 뒷골목에 온 듯한 느낌을 주는 골목이다.\n"
                            "사진을 찍는 명소로 유명하다.",bg='lightsteelblue', justify='left').grid(row=6, column=1)
        Label(travel, text="쎄 광장\n"
                            "상파울로 대성당이 있는 곳으로 웅장한 광장과 대성당이 압도하는 분위기이다.",bg='lightsteelblue', justify='left').grid(row=9, column=0)

        
        img_상파울로2 = PhotoImage(file='상파울로_추천스팟_봉헤찌로.gif').subsample(2)
        label_상파울로2 = Label(travel, image=img_상파울로2)
        label_상파울로2.grid(row=7, column=0, sticky='W')
        img_상파울로3 = PhotoImage(file='상파울로_추천스팟_베트맨 골목.gif').subsample(2)
        label_상파울로3 = Label(travel, image=img_상파울로3)
        label_상파울로3.grid(row=7, column=1)
        img_상파울로4 = PhotoImage(file='상파울로_추천스팟_쎄 광장.gif').subsample(2)
        label_상파울로4 = Label(travel, image=img_상파울로4)
        label_상파울로4.grid(row=10, column=0)
        

    if continent.get()=='남아메리카' and country.get()=="브라질 상파울로" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x400")

        나라이름 = Label(travel, text="브라질 상파울로", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="일반 문화\n"
                            "인사\n"
                            "아침인사 Bom dia (봉 지아)\n"
                            "오후인사 Boa tarde (보아 따르지)\n"
                            "저녁인사 Boa noite (보아 노이찌)\n"
                            "헤어질 때 Tchau (짜우)\n"
                            "일반 안부 Tudo bem (뚜두 벵)\n"
                            "감사표시\n"
                            "남자는 Obrigado (오브리가두)\n"
                            "여자는 Obrigada (오브리가다)\n"
                            "의사 표시\n"
                            "OK Esta bom(따봉)\n"
                            "예 Sim (씽)\n"
                            "아니오 Nao (너웅)\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='남아메리카' and country.get()=="브라질 상파울로" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")

        나라이름 = Label(travel, text="브라질 상파울로", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text= "리우데자네이루 남서쪽 약 500km 지점, 해발고도 약 800m의 고원지대에 있으며,\n"
                            "부근의 20여 개 위성도시를 포함하여 인구 1천만이 넘는 남아메리카 최대의 도시이다.\n"
                            "여름은 서늘하고 쾌적한 기후로 연평균기온 18.2℃, 연강수량 1,247mm이다. 연중 기온의 변화가 적은 것이 특색이다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='남아메리카' and country.get()=="브라질 상파울로" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x300")

        나라이름 = Label(travel, text="브라질 상파울로", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동 : 관광", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="봉헤찌로 - 한인타운\n"
                            "배트맨 골목 - 다양한 그래비티 작품들\n"
                            "쎄 광장 - 거대한 고대 건물들이 있는 광장\n"
                            "루즈 역- 오래된 기차역으로 관광명소",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')
        
    if continent.get()=='남아메리카' and country.get()=="브라질 상파울로" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")

        나라이름 = Label(travel, text="브라질 상파울로", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="팁 문화\n"
                            "식당, 호텔 등의 요금 계산서에 10%의 봉사료가 포함되어 있으므로 별도의 팁은 필요치 않습니다.\n"
                            "그러나 호텔에서 짐을 운반하는 보이 또는 체크아웃 하기 위해 객실을 나올 때는 미화 1불(2헤알) 정도 팀을 주는 것이 예의입니다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='남아메리카' and country.get()=="브라질 상파울로" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1100x400")

        나라이름 = Label(travel, text="브라질 상파울로", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="날씨\n"
                            "국토가 광대하여 지역마다 기후가 상이하나, 브라질리아는 18∼30℃의 아열대성 기후로서,\n"
                            "건기인 4월 중순에서 9월 말까지는 비가 오지 않고 매우 건조 (습도 15% 이하로 사막 기후) 하며\n"
                            "특히 겨울철인 6월에서 8월 중순까지는 아침, 저녁으로 쌀쌀하고, 6월 중순에서 8월 중순까지는 감기에 걸리는 경우도 있습니다.\n"
                            "우기인 10월에서 익년 3월까지는 심한 번개를 동반한 소나기가 하루에 한두 차례 오며,\m"
                            "기온은 한국의 5월 말이나 6월 초 정도의 20℃에서 30℃ 정도이나 습기가 적기 때문에 실내는 서늘합니다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')


    if continent.get()=='남아메리카' and country.get()=="칠레 산티아고" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x600")

        나라이름 = Label(travel, text="칠레 산티아고", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="주요 교통 법규 및 문화\n"
                            "브라질은 자동차 보험가입이 의무사항 아니어서 무보험 차량이 상당수 운행 중이므로 이에 대해 각별히 주의를 기울여야 함\n"
                            "일방통행 도로가 상당히 발달해 있기에 익숙하지 않은 도로 운전 시 역주행에 각별히 유의해야 함\n"
                            "관련 사건사고 사례\n"
                            "무보험 차량과 사고 시 보상을 받지 못할 확률이 높음\n"
                            "카니발 축제기간 중 음주운전으로 인한 사고가 빈번히 발생함\n"
                            "실수나 주의부족으로 차량이 주요 대도시 빈민가에 진입할 경우 차량강도를 당할 확률이 아주 높음\n"
                            "대도시 후미진 주차장 등에서 충분한 주의를 기울이지 않을 경우 차량 강도를 당할 확률이 높음\n"
                            "대중교통\n"
                            "버스 및 소형택시(흰색, Ponto de Taxi)가 있으나 버스 내에서 강도, 소매치기 등 피해가 많이 발생하므로 시내 이동 시에는 택시를 이용하시는 것이 바람직합니다.\n"
                            "거리에 돌아다니는 택시보다는 호텔에 정차하고 있는 택시나, 공항에서는 라디오 택시( Radio Taxi, 선불제)를 이용하시는 것이 사후 요금에 따른 시비를 방지하기 위해 바람직합니다.\n"
                            "도로교통\n"
                            "도로가 일반적으로 노면이 고르지 못하고 정비 상태가 불량합니다. 도심에서 운전하다 보면 차량 및 오토바이가 차선 변경 신호를 주지 않고 갑자기 끼어들기 때문에 안전거리를 확보하여 운행합니다.\n"
                            "브라질리아 시내에서는 신호가 없는 횡단보도를 건너는 보행자가 있으면 무조건 정지해야 한다. 보행자는 차량이 정지하는 것을 당연하게 생각하고 있습니다.\n"
                            "무보험 차량이 많고 사고가 발생해도 무책임하므로 접촉사고가 나지 않도록 주의해야 합니다.\n"
                            "교통법규를 위반하면 벌과금이 많습니다. 운전자석, 조수석 및 뒷좌석 동반자의 안전벨트 착용도 의무사항이다.\n"
                            "안전벨트 미착용시 벌금을 127.69 헤알(약 63불) 정도 내야 합니다",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='남아메리카' and country.get()=="칠레 산티아고" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x200")

        나라이름 = Label(travel, text="칠레 산티아고", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text=" 언어 : 스페인어(카스티야어); 지역별 카탈루냐어, 바스크어, 갈리시아어를 공용어로 사용",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='남아메리카' and country.get()=="칠레 산티아고" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x500")
        global img_산티아고2

        나라이름 = Label(travel, text="칠레 산티아고", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟 : 관광", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=5,column=0, sticky='W')

        Label(travel, text="산티아고 순례길\n"
                            "1993년 유네스코 세계문화유산으로 지정된 스페인과 프랑스 접경에 위치한 기독교 순례길이다.\n"
                            "종교의 발생지 또는 성인의 무덤이나 거주지와 같이 종교적인 의미가 있는 곳을 찾아다니며 방문하여 참배하는 순례자 길이다.",bg='lightsteelblue', justify='left').grid(row=6, column=0)

        img_산티아고2 = PhotoImage(file='산티아고_추천스팟_순례길.gif').subsample(2)
        label_산티아고2 = Label(travel, image=img_산티아고2)
        label_산티아고2.grid(row=7, column=0, sticky='W')



    if continent.get()=='남아메리카' and country.get()=="칠레 산티아고" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x400")

        나라이름 = Label(travel, text="칠레 산티아고", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="일반 문화\n"
                            "인사\n"
                            "아침인사 Bom dia (봉 지아)\n"
                            "오후인사 Boa tarde (보아 따르지)\n"
                            "저녁인사 Boa noite (보아 노이찌)\n"
                            "헤어질 때 Tchau (짜우)\n"
                            "일반 안부 Tudo bem (뚜두 벵)\n"
                            "감사표시\n"
                            "남자는 Obrigado (오브리가두)\n"
                            "여자는 Obrigada (오브리가다)\n"
                            "의사 표시\n"
                            "OK Esta bom(따봉)\n"
                            "예 Sim (씽)\n"
                            "아니오 Nao (너웅)\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='남아메리카' and country.get()=="칠레 산티아고" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")

        나라이름 = Label(travel, text="칠레 산티아고", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="칠레 중앙부 안데스산맥과 해안산맥 사이에 전개된 분지 위에 있으며, 높이 450~650m의 고지대에 위치한다.\n"
                            "1541년 에스파냐의 페드로 데 발디비아가 건설했으며, 최초의 요새가 산타 루시아 언덕에 구축되었다.\n"
                            "이후 지진 ·홍수 ·대화재 등 여러 차례의 재해로 파괴되었으나 기후가 양호하고 경치가 아름다워 관광객이 많다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='남아메리카' and country.get()=="칠레 산티아고" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")

        나라이름 = Label(travel, text="칠레 산티아고", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="산티아고 순례길 - 유네스코 세계문화유산으로 지정된 기독교 순례길",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='남아메리카' and country.get()=="칠레 산티아고" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1100x300")

        나라이름 = Label(travel, text="칠레 산티아고", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text= "팁 문화\n"
                            "식당, 호텔 등의 요금 계산서에 10%의 봉사료가 포함되어 있으므로 별도의 팁은 필요치 않습니다.\n"
                            "그러나 호텔에서 짐을 운반하는 보이 또는 체크아웃 하기 위해 객실을 나올 때는 미화 1불(2헤알) 정도 팀을 주는 것이 예의입니다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='남아메리카' and country.get()=="칠레 산티아고" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1100x400")

        나라이름 = Label(travel, text="칠레 산티아고", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text= "날씨\n"
                            "국토가 광대하여 지역마다 기후가 상이하나, 브라질리아는 18∼30℃의 아열대성 기후로서,\n"
                            "건기인 4월 중순에서 9월 말까지는 비가 오지 않고 매우 건조 (습도 15% 이하로 사막 기후) 하며\n"
                            "특히 겨울철인 6월에서 8월 중순까지는 아침, 저녁으로 쌀쌀하고, 6월 중순에서 8월 중순까지는 감기에 걸리는 경우도 있습니다.\n"
                            "우기인 10월에서 익년 3월까지는 심한 번개를 동반한 소나기가 하루에 한두 차례 오며,\m"
                            "기온은 한국의 5월 말이나 6월 초 정도의 20℃에서 30℃ 정도이나 습기가 적기 때문에 실내는 서늘합니다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')



    if continent.get()=='아시아' and country.get()=="터키 안탈리아" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x400")

        나라이름 = Label(travel, text="터키 안탈리아", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=3,column=0, sticky='W')
        Label(travel, text="유럽여행을 하면 자주 볼 수 있는 트램을 터키에서도 볼 수 있다.\n트램은 일반적인 도로 위에 깔린 레일 위를 주행하는 노면전차이다.\n안탈리아 트램은 빈티지트램과 신식트램 모두를 볼 수 있다.\n트램길을 따라 주요 관광지와 예쁜 거리들이 연결되어 있어서\n이동하기도 편리하다. 요금도 저렴해서 부담없이 이용할 수 있다.\n우리나라 카드 시스템처럼 카드에 돈을 충전해서 사용하면 된다.",bg='lightsteelblue', justify='left').grid(row=4, column=0, sticky='W')

    if continent.get()=='아시아' and country.get()=="터키 안탈리아" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x200")

        나라이름 = Label(travel, text="터키 안탈리아", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=51,column=0, sticky='W')
        Label(travel, text="터키어",bg='lightsteelblue', justify='left').grid(row=52,column=0, sticky='W')

    if continent.get()=='아시아' and country.get()=="터키 안탈리아" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x400")

        나라이름 = Label(travel, text="터키 안탈리아", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=5,column=0, sticky='W')
        Label(travel, text="카푸타스 해변\n욀뤼데니즈\n페르게 유적\n뎀레 마을\n울루보를루\n칼레이치 구시가지\n뒤덴 폭포\n안탈리아 고고학 박물관\n안탈리아 아쿠아리움",bg='lightsteelblue', justify='left').grid(row=6,column=0, sticky='W')

    if continent.get()=='아시아' and country.get()=="터키 안탈리아" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x400")

        나라이름 = Label(travel, text="터키 안탈리아", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=53,column=0, sticky='W')
        Label(travel, text="안녕하세요(메르하바)\n좋은 하루 되세요(이이균렐)\n감사합니다(테쉐큘렐)\n죄송합니다(오줄 딜레림)\n반갑습니다(멤눈 올둠)\n얼마에요?(네 카달?)\n너무 비싸요(촉 파할르)\n안녕(귤레귤레/헤어질 때 인사)\n네(Evet)\n아니요(Hayir)\n~에 어떻게 갈 수 있어요?(~'e nasil gidebilirim?)",bg='lightsteelblue', justify='left').grid(row=54,column=0, sticky='W')

    if continent.get()=='아시아' and country.get()=="터키 안탈리아" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x300")

        나라이름 = Label(travel, text="터키 안탈리아", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=7,column=0, sticky='W')
        Label(travel, text="안탈리아 만에 동서로 길게 면한 항구도시이다.\n해안 평야지대, 중앙 아나톨리아 고원, 동부 산악지대로\n구분되는 터키 지형 중에 해안 평야지대이다.",bg='lightsteelblue', justify='left').grid(row=8,column=0, sticky='W')

    if continent.get()=='아시아' and country.get()=="터키 안탈리아" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x1200")
        global img_안3,img_안4,img_안5,img_안8

        나라이름 = Label(travel, text="터키 안탈리아", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동(관광)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=10,column=0, sticky='W')
        Label(travel, text="카푸타스 해변: 일명 클레오파트라 해변이라고 불리는데,\n클레오파트라가 여기서 해수욕을 즐겼다고 전해진다.\n하얗게 부서지는 파도와 푸른 하늘을 배경으로\n여유롭게 수영을 즐겨볼 수 있다.",bg='lightsteelblue', justify='left').grid(row=11,column=0, sticky='W')
        img_안3 = PhotoImage(file='안탈리아 카푸타스 해변.gif').subsample(2)
        label_안3 = Label(travel, image=img_안3)
        label_안3.grid(row=12, column=0, sticky='W')


        Label(travel, text="테마별추천활동(관광)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=13,column=0, sticky='W')
        Label(travel, text="페르게 유적: 페르게 고대도시 유적이다.\n약 3000년 전 로마제국에 편입되어 황금기를 구가했던\n페르게의 생활상을 볼 수 있다.\n밑의 그림은 당시 스타디움의 유적이다.",bg='lightsteelblue', justify='left').grid(row=14,column=0, sticky='W')
        img_안4 = PhotoImage(file='안탈리아 페르게 유적.gif').subsample(3)
        label_안4 = Label(travel, image=img_안4)
        label_안4.grid(row=15, column=0, sticky='W')


        Label(travel, text="테마별추천활동(식도락)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=10,column=1)
        Label(travel, text="케밥: 케밥 중에 아다나케밥과 우르파케밥이 있는데\n모양이 비슷하게 생겼지만 우르파케밥이 약간 더 맵다.\n밑의 사진은 아다나 케밥이다.\n다른 종류로는 빵 위에 고기를 올리고\n토마토 소스랑 같이 먹는 이스켄데르 케밥,\n가지 케밥, 그리고 자으 케밥 등이 있다.",bg='lightsteelblue', justify='left').grid(row=11,column=1)
        img_안5 = PhotoImage(file='안탈리아 케밥.gif').subsample(2)
        label_안5 = Label(travel, image=img_안5)
        label_안5.grid(row=12, column=1)

        Label(travel, text="테마별추천활동(활동)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=13,column=1)
        Label(travel, text="보트 투어: 안탈리아에서 경험할 수 있는 활동 중에\n가성비 좋은 게 보트 투어이다.\n다른 지중해 도시들보다 저렴하게\n지중해 바다를 느낄 수 있다.\n배들도 제각각 재미있는 모양을 하고 있다.",bg='lightsteelblue', justify='left').grid(row=14,column=1)
        img_안8 = PhotoImage(file='안탈리아 보트 투어.gif').subsample(3)
        label_안8 = Label(travel, image=img_안8)
        label_안8.grid(row=15, column=1)


    if continent.get()=='아시아' and country.get()=="터키 안탈리아" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x500")

        나라이름 = Label(travel, text="터키 안탈리아", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=55,column=0, sticky='W')
        Label(travel, text="1. 옷차림: 봄에는 한국의 봄 복장을 입으면 되고,\n여름에는 여름철 복장을 입되,\n물을 많이 섭취해야 한다.\n가을에는 긴 팔과 자켓을 입어서 따뜻한 복장을 유지하고,\n겨울에는 한국과 동일한 겨울철 복장을 입으면 된다.\n\n2. 안탈리아 사람들은 남들에게 정말 관심이 없다.\n흔한 호객행위를 하는 사람이 없어\n자유롭다는 느낌을 만끽할 수 있다.\n휴양지 느낌이 물씬난다.\n\n3. 지하철과 공항을 제외한 대부분의 공중화장실에서는\n돈을 내야 한다.",bg='lightsteelblue', justify='left').grid(row=56,column=0, sticky='W')

    if continent.get()=='아시아' and country.get()=="터키 안탈리아" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x600")
        global img_안2

        나라이름 = Label(travel, text="터키 안탈리아", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=1,column=0, sticky='W')
        Label(travel, text="12, 1, 2월에는 매우 추운 날씨이고,\n3, 4, 10, 11월은 약간 춥고 선선한 날씨이다.\n5, 6, 10월에는 쾌적하며 따뜻한 날씨이며,\n7, 8월에는 더운 날씨가 지속된다.",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_안2 = PhotoImage(file='안탈리아 날씨.gif').subsample(1)
        label_안2 = Label(travel, image=img_안2)
        label_안2.grid(row=3, column=0, sticky='W')


    if continent.get()=='아시아' and country.get()=="몰디브" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("900x400")

        나라이름 = Label(travel, text="몰디브", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="*교통 법규와 문화\n"
                            "자동차 운전석 위치가 한국과 반대(오른쪽 핸들)이며, 신호체계가 상이함\n"
                            "국제운전면허 인정하지 않음\n"
                            "도로가 좁아서 일방통행이 많으며, 차보다는 오토바이가 많으니 도로나 골목을 보행 시 좌우를 잘 살피고 건너기 바라며\n"
                            "운전석은 오른쪽이므로 택시에서 타고 내릴 때에 꼭 왼쪽으로 내려야합니다.\n"
                            "*대중교통\n"
                            "공항과 수도 '말레'섬 간 이동은 공항 페리(Airport Ferry 또는 Dhoni,도니라고 부름)를 이용하거나\n"
                            "18.10월 개통된 시나말레 다리를 건너는 버스를 이용하실 수 있습니다.\n"
                            "버스요금은 10 MVR(몰디브 루피야)입니다.\n"
                            "말레와 공항섬인 훌훌레에서는 택시를 이용할 수 있습니다. 택시요금은 거리와 탑승 인원 수에 상관없이 한번 세워서 내려주는데 25루피야 정도를 받습니다.\n"
                            "말레와 공항섬인 훌훌레에서는 버스도 운행합니다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="몰디브" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x400")

        나라이름 = Label(travel, text="몰디브", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text= "몰디브의 고유어이자 공용어인 디베히어는 인도-유럽어군에 속한다.\n"
                            "디베히어는 사용 인구가 30만 명에 불과해 소멸 위기에 처한 언어로 분류되고 있다.\n"
                            "영어 역시 관광을 비롯하여 상업 활동에 두루 쓰이고 있다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="몰디브" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1200x800")
        global img_몰디브2, img_몰디브3, img_몰디브4

        나라이름 = Label(travel, text="몰디브", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟 : 관광", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=5,column=0, sticky='W')
        Label(travel, text="추천스팟 : 관광", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=5,column=1, sticky='W')
        Label(travel, text="추천스팟 : 관광", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=8,column=0, sticky='W')
        
        Label(travel, text="대통령 궁\n"
                            "말레의 관광 명소 중 하나로,\n"
                            "관광객이라면 꼭 한번쯤 들르는 곳이다.\n"
                            "몰디브 전통의 건축 양식에 현대적인 예술미가 가미된 아름다운 건물이다.",bg='lightsteelblue', justify='left').grid(row=6, column=0)
        Label(travel, text="국립박물관\n"
                            "몰디브의 역사를 보여주는 박물관으로 몰디브에 대해 알고 싶다면 와야하는 곳",bg='lightsteelblue', justify='left').grid(row=6, column=1)
        Label(travel, text="말레 수산시장 & 재래시장\n"
                            "현지인들이 자주 가는 곳으로 생선 가격이 매우 싸다.\n"
                            "예를 들어 우리나라에서 몇백만원하는 참치 한마리가 7만원이다.",bg='lightsteelblue', justify='left').grid(row=9, column=0)

        
        img_몰디브2 = PhotoImage(file='몰디브_추천스팟_대통령궁.gif').subsample(2)
        label_몰디브2 = Label(travel, image=img_몰디브2)
        label_몰디브2.grid(row=7, column=0, sticky='W')
        img_몰디브3 = PhotoImage(file='몰디브_추천스팟_국립박물관.gif').subsample(2)
        label_몰디브3 = Label(travel, image=img_몰디브3)
        label_몰디브3.grid(row=7, column=1)
        img_몰디브4 = PhotoImage(file='몰디브_추천스팟_말레 수산시장 & 재래시장.gif').subsample(2)
        label_몰디브4 = Label(travel, image=img_몰디브4)
        label_몰디브4.grid(row=10, column=0)


    if continent.get()=='아시아' and country.get()=="몰디브" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x500")

        나라이름 = Label(travel, text="몰디브", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="기본 회화\n"
                            "만났을 때 인사말 : 앗쌀람 알라이쿰\n"
                            "상대방이 앗쌀람 알라이쿰이라고 하면 : 알라이쿰 쌀람\n"
                            "환영합니다 : 마루하바\n"
                            "감사합니다 : 쑤쿠란\n"
                            "네 : 아~\n"
                            "아니요 : 눈~",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="몰디브" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("900x500")

        나라이름 = Label(travel, text="몰디브", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text= "정식명칭은 몰디브공화국(Republic of Maldives)이다. 스리랑카의 남서 약 650km에 있으며,\n"
                            "8°선 해협(Eight Degree Channel)에서 동경 73°선을 따라 적도 남쪽까지 남북으로 약 760km, 동서 128km의 해역에 흩어져 있는 1,190여 개의 작은 산호섬과\n"
                            "26개 환초(環礁)로 이루어져 있는데, 그 가운데 200개 섬에서만 사람이 산다. 국토 면적은 300㎢이고, 해안선 총 연장은 644km이다.\n"
                            "독립 직후 국제연합(UN)에, 1985년 영국연방에 정식 가맹하였다. 조용하고 깨끗한 환경과 다양한 해양 생태계를 지녀 해마다 관광객이 늘고 있다.\n"
                            "행정구역은 19개 환초(atolls)와 1개 수도 시(capital city:말레)로 이루어져 있다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="몰디브" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x400")

        나라이름 = Label(travel, text="몰디브", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동 : 관광", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text= "몰디브 대통령궁\n"
                            "몰디브 국립박물관\n"
                            "말레 수산시장 & 재래시\n"
                            "주변의 원주민 섬 & 무인도 방문",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="몰디브" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")

        나라이름 = Label(travel, text="몰디브", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="일반문화\n" 
                            "영어로 인사하면서 악수하는 것이 일반적입니다.\n"
                            "종교관련\n"
                            "왼손으로 악수를 하지 않습니다.(무슬림들은 악수를 하거나 식사를 할 때는 반드시 오른손을 사용합니다.)\n"
                            "팁 문화\n"
                            "리조트나 식당에서 성의를 표시하는 정도의 팁 문화가 보편화되어 있습니다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="몰디브" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")

        나라이름 = Label(travel, text="몰디브", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="기후는 고온 다습한 열대성기후로 1년은 남서몬순계(5~10월)와 북동몬순계(11~4월)로 나뉜다.\n"
                            "남서몬순계에는 강한 바람이 불고 강우량이 많으나, 북동몬순계에는 공기가 건조하고 바람이 잔잔하여 비교적 견디기가 쉽다.\n"
                            "우계의 변절기에 해당하는 3~5월은 1년을 통해서 가장 더운 시기이다. 연평균 기온은 24~30℃이고. 연평균강우량은 1,869mm이다.\n"
                            "북태평양의 팔라우와 더불어 연교차가 가장 적은 지역(1℃)이기도 하다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')



    if continent.get()=='아시아' and country.get()=="아랍에미리트 두바이" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x400")

        나라이름 = Label(travel, text="아랍에미리트 두바이", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="택시: 대부분의 호텔이나 쇼핑몰, 공항에는 택시 승강장이 설치되어 있다. \n"
                            "시내 택시가 공항 택시보다 더 비싼 편이고, 공항에서 30분거리의 목적지까지 대략 15000-20000원 정도의 요금이 나온다.\n "
                            "우버 택시 또한 활발히 운영 중이며, 일반 택시보다 30%가량 더 비싸다.\n"
                            "버스: 현재 60-70개의 노선 버스가 운행중이며 요금은 1000-1500원 정도로 저렴한 편이다. \n"
                            "지하철: 레드라인(두바이공항-제벨알리)와 그린라인(두바이 크릭 수로 주변 22km)로 구성되어 있으며 \n"
                            "전부 무인 자동시스템으로 운행되고 있음. \n"
                            "1등칸인 골드클래스(3000-6000)와 일반칸(1000-2000) 2개 종류로 나뉜다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="아랍에미리트 두바이" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("900x300")

        나라이름 = Label(travel, text="아랍에미리트 두바이", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="아랍어는 아랍에미리트의 공식 공용어이다. 아랍어의 걸프지역 방언은 두바이 사람들 사이에서 흔한 언어이다. 영어는 두 번째로 많이 사용되는 언어이다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="아랍에미리트 두바이" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x500")
        global img_아랍1

        나라이름 = Label(travel, text="아랍에미리트 두바이", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="버즈 알아랍 주메이라",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')
        img_아랍1 = PhotoImage(file='아랍두바이_추천스팟.gif').subsample(2)
        label_아랍1 = Label(travel, image=img_아랍1)
        label_아랍1.grid(row=4, column=0, sticky='W')

    if continent.get()=='아시아' and country.get()=="아랍에미리트 두바이" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x300")

        나라이름 = Label(travel, text="아랍에미리트 두바이", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="'Na’am'  – 네\n"
                            "‘La' – 아니요\n"
                            "'Marhaba'– 안녕하세요\n"
                            "‘Maasalaamah' - 안녕히 가세요\n"
                            "'Affwaan' – 미안합니다, 실례합니다\n"
                            "'In sh'Allah' – 알라신의 뜻대로",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="아랍에미리트 두바이" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("700x400")

        나라이름 = Label(travel, text="아랍에미리트 두바이", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="두바이는 아랍에미리트의 페르시아 만 연안 해수면 16m에 위치해 있다. \n"
                            "남쪽으로는 아부다비, 북동쪽으로는 샤르자, 남동쪽으로는 오만과 국경을 맞대고 있다. \n"
                            "해안은 페르시아 만과 맞닿아 있다. 두바이는 아라비아 사막 바로 위에 펼쳐져 있다.\n"
                            "두바이의 지형은 아랍에미리트의 남쪽 일부 모습과는 상당히 다르다.\n"
                            "남쪽 대부분 풍경은 자갈 사막인데 반해 두바이는 모래 사막이 주를 이룬다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="아랍에미리트 두바이" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1500x1500")
        global img_아랍2, img_아랍3, img_아랍4, img_아랍5, img_아랍6

        나라이름 = Label(travel, text="아랍에미리트 두바이", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="((관광)\n"
                            "부르즈 할리파: 아랍에미리트 두바이의 신도심 지역에 있는 높이 829.8미터의 마천루. \n"
                            "주메이라 모스크: 인상적인 구조를 가진 모스크. \n"
                            "두바이에서 가장 많은 관광객들이 모이는 모스크로, 비 무슬림과 관광객의 출입이 허용된 몇 모스크 중 하나이다.\n\n"
                            "((쇼핑)\n"
                            "두바이 몰: 세계에서 가장 큰 쇼핑몰이며, 세계 각지에서 가장 많은 사람들이 즐겨 찾는 쇼핑몰이다. \n"
                            "200개 의 가게들이 입점해 있고, 쇼핑몰 안에 세계에서 가장 큰 아쿠아리움, 언더워터 동물원, 아이스링크 또한 입점해 있다. \n"
                            "두바이 마리나: 모든 것들이 인공적으로 조성된 곳으로, 세계에서 가장 큰 사람이 만든 정박지라는 타이틀을 가지고 있다. \n"
                            "수많은 카페와 공예품 팝업 마켓이 주위 해변 산책로인 두바이 마리나 워크에 위치하고 있으며, \n"
                            "두바이 마리나 몰 내부에는 체인 및 고급 패션 브랜드가 입점해 있다.\n\n"
                            "((휴양)\n"
                            "두바이 사막 사파리: 두바이의 사막을 걸어보며 부드러운 모래를 발가락 사이로 느껴볼 수 있다.\n"
                            "혹은 밤을 사막 위에서 텐트를 치고 지내며 수많은 별을 보고 사막을 완벽하게 경험할 수 있다",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')
        img_아랍2 = PhotoImage(file='아랍두바이_테마별추천활동_관광_부르즈할리파.gif').subsample(2)
        label_아랍2 = Label(travel, image=img_아랍2)
        label_아랍2.grid(row=3, column=1)
        img_아랍3 = PhotoImage(file='아랍두바이_테마별추천활동_관광_주메이라모스크.gif').subsample(2)
        label_아랍3 = Label(travel, image=img_아랍3)
        label_아랍3.grid(row=4, column=0, sticky='W')
        img_아랍4 = PhotoImage(file='아랍두바이_테마별추천활동_쇼핑_두바이몰.gif').subsample(1)
        label_아랍4 = Label(travel, image=img_아랍4)
        label_아랍4.grid(row=4, column=1)
        img_아랍5 = PhotoImage(file='아랍두바이_테마별추천활동_쇼핑_두바이마리나.gif').subsample(2)
        label_아랍5 = Label(travel, image=img_아랍5)
        label_아랍5.grid(row=3, column=2)
        img_아랍6 = PhotoImage(file='아랍두바이_테마별추천활동_액티비티_사막사파리.gif').subsample(2)
        label_아랍6 = Label(travel, image=img_아랍6)
        label_아랍6.grid(row=4, column=2)
                            

    if continent.get()=='아시아' and country.get()=="아랍에미리트 두바이" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x400")

        나라이름 = Label(travel, text="아랍에미리트 두바이", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="1.여성전용 : 버스를 이용할 때 제일 앞 두 줄은 여자 전용석이기 때문에 남자는 앉는 것이 금지된다.\n"
                            "지하철에서도 여성 유아 전용 칸이 있는 데 성인 남자가 그의 경계인 핑크색 라인을 침범하면 100디르함(3만원)의 벌금이 부과된다.\n"
                            "2.두바이의 날씨는 매우 덥고 주차시설은 매우 잘 정비되어 있고, 기름값이 저렴해 렌터카로 이동하는 것이 가장 합리적이다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="아랍에미리트 두바이" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x400")

        나라이름 = Label(travel, text="아랍에미리트 두바이", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="1,2월 평균기온 19도 선선 3,4월 평균기온 23도 5-10월 무더운 날씨 8월에는 40도 임박 11,12월 선선한 가을 날씨. \n"
                            "두바이의 여행 최고 적기는 겨울",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

        

    if continent.get()=='아시아' and country.get()=="라오스 루앙프라방" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("700x600")
        global img_루3

        나라이름 = Label(travel, text="라오스 루앙프라방", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=3,column=0, sticky='W')
        Label(travel, text="유네스코 세계문화유산인 루앙프라방의 중심지에는\n버스가 다니지 못한다. 주로 걷거나 자전거를 탄다.\n뚝뚝이라는 현지 택시가 있는데,\n창문이 열려있는 버스를 타고 이동하는 느낌이라\n춥고 먼지가 날리므로 마스크랑 겉옷이 필요하다.\n저렴한 뚝뚝이는 오토바이 뒤에 앉을 칸이 연결되어 있고,\n고급진 뚝뚝이는 자동차 뒤에 앉을 칸이 연결되어 있다.",bg='lightsteelblue', justify='left').grid(row=4, column=0, sticky='W')
        img_루3 = PhotoImage(file='루앙프라방 뚝뚝이.gif').subsample(2)
        label_루3 = Label(travel, image=img_루3)
        label_루3.grid(row=5, column=0, sticky='W')


    if continent.get()=='아시아' and country.get()=="라오스 루앙프라방" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x200")

        나라이름 = Label(travel, text="라오스 루앙프라방", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=51,column=0, sticky='W')
        Label(travel, text="라오스어",bg='lightsteelblue', justify='left').grid(row=52,column=0, sticky='W')

    if continent.get()=='아시아' and country.get()=="라오스 루앙프라방" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x400")

        나라이름 = Label(travel, text="라오스 루앙프라방", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=5,column=0, sticky='W')
        Label(travel, text="꽝시폭포\n빡우동굴\n위스키마을\n곰 보호센터\n푸시산\n황금 도시의 사원(왓 시엥 통)\n탁발 의식\n루앙프라방 도서관\n루앙프라방 야시장",bg='lightsteelblue', justify='left').grid(row=6,column=0, sticky='W')

    if continent.get()=='아시아' and country.get()=="라오스 루앙프라방" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x500")

        나라이름 = Label(travel, text="라오스 루앙프라방", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=53,column=0, sticky='W')
        Label(travel, text="안녕하세요(ສະບາຍດີ: 싸바이디/헤어질 때 인사로 사용해도 된다)\n감사합니다(ຂອບໃຈ: 컵짜이)\n죄송합니다, 실례합니다(ຂໍໂທດ: 커톳/질문 하기 전에 커톳이라고 하면 더욱 정중하게 느껴진다)\n괜찮습니다(ບໍ່ເປັນຫຍັງ: 버뻰냥)\n네(ແມ່ນແລ້ວ: 맨래우)\n아니오(ບໍ່ແມ່ນ: 버맨)\n~주세요(ຂໍ~: 커~)\n고수 빼주세요(ບໍ່ໄສຜັກຫອມປ້ອມ: 버싸이팍험뻠)\n얼마에요?(ເທົ່າໃດ: 타오다이?)\n계산서 좀 주세요(ຂໍບິນແດ່: 커빈대)\n계산 해주세요(ແຊັກບິນແດ່: 쌕빈대)\n너무 비싸요(ແພງເກີນໄປ: 팽끈빠이)\n더 싼 물건으로 보여주세요(ຂໍເບິ່ງຂອວຖືກກວ່ານີ້ແນ່ໄດ້ບໍ: 커븡컹특꽈니내다이버)",bg='lightsteelblue', justify='left').grid(row=54,column=0, sticky='W')

    if continent.get()=='아시아' and country.get()=="라오스 루앙프라방" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x500")

        나라이름 = Label(travel, text="라오스 루앙프라방", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=7,column=0, sticky='W')
        Label(travel, text="라오스는 동남아시아에서 생태환경이 가장 잘 보존된 곳이다.\n국토의 75퍼센트가 푸른 숲으로 덮여 있고,\n북부의 산과 남부의 평원을 넉넉히 적시며 메콩강이 흘러간다.\n특히 라오스 북부지역은 오염되지 않은 자연환경과\n다양한 소수부족들의 삶이 매력적인 곳이다.\n루앙프라방은 라오스 북서부 메콩강 유역에 있는 도시로\n여행자들에게 '영혼의 강장제'로 불린다.\n칸강과 메콩강이 합류하는 지점에 걸터앉은 루앙프라방은\n황금 지붕을 인 오래된 사원들과 프랑스풍의 저택들이 독특한 조화를 이루는 옛 도시다.",bg='lightsteelblue', justify='left').grid(row=8,column=0, sticky='W')

    if continent.get()=='아시아' and country.get()=="라오스 루앙프라방" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x1000")
        global img_루5,img_루6,img_루7,img_루8
        나라이름 = Label(travel, text="라오스 루앙프라방", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')

        Label(travel, text="테마별추천활동(휴양)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=13,column=0, sticky='W')
        Label(travel, text="부라사리 스파: 매우 유명한 곳이라 예약을 하는 것이 좋다.\n호텔인 부라사리 헤리티지의 옆에 위치하고 있다.\n호텔에서 운영하고 있어 일반 마사지샵보다 비싸다\n이 마사지샵은 프라이빗 마사지만 진행한다.\n2인 기준이어서 한 방에서 2명이서만 마사지를 받는다.\n성인 2명과 소아 2명까지 동반 입실이 가능하다.",bg='lightsteelblue', justify='left').grid(row=14,column=0, sticky='W')
        img_루5 = PhotoImage(file='루앙프라방 스파.gif').subsample(4)
        label_루5 = Label(travel, image=img_루5)
        label_루5.grid(row=15, column=0, sticky='W')


        Label(travel, text="테마별추천활동(관광)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=16,column=0, sticky='W')
        Label(travel, text="꽝시폭포: 루앙프라방 남쪽으로 약 45km 떨어진 관광명소이다.\n석회암 지대를 흐르는 폭포라서 맑고 청명하며,\n주변의 자연과 어우러진 풍경이 매우 아름다운 곳이다.\n에메랄드 빛의 푸른 물이 고인 웅덩이는 수영장 역할을 하고 있다.\n수영은 안전을 고려해 정해진 곳에서만 한다.",bg='lightsteelblue', justify='left').grid(row=17,column=0, sticky='W')
        img_루6 = PhotoImage(file='루앙프라방 꽝시폭포.gif').subsample(3)
        label_루6 = Label(travel, image=img_루6)
        label_루6.grid(row=18, column=0, sticky='W')


        Label(travel, text="테마별추천활동(관광)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=13,column=1)
        Label(travel, text="황금 도시의 사원(왓 시엥 퉁): 메콩강과 남칸강의 합류점 인근에 건설되었고,\n1975년 왕정이 무너질 때까지 대관식을 비롯한\n수많은 왕실 행사의 장소로 쓰여 왔던 곳이다.\n지붕의 장식들과 벽면의 모자이크들까지\n섬세하고 예술적인 모습이 드러나 있으며\n수많은 침략에서도 훼손되지 않아\n지금까지 원형을 지켜오고 있다.",bg='lightsteelblue', justify='left').grid(row=14,column=1)
        img_루7 = PhotoImage(file='루앙프라방 황금 도시의 사원.gif').subsample(3)
        label_루7 = Label(travel, image=img_루7)
        label_루7.grid(row=15, column=1)


        Label(travel, text="테마별추천활동(식도락)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=16,column=1)
        Label(travel, text="신닷: 끝이 말려 올라간 투구 모양의 팟 위에\n고기를 굽고 밑에서는 샤브샤브처럼\n고기와 야채를 익혀먹는 음식이다.",bg='lightsteelblue', justify='left').grid(row=17,column=1)
        img_루8 = PhotoImage(file='루앙프라방 신닷.gif').subsample(4)
        label_루8 = Label(travel, image=img_루8)
        label_루8.grid(row=18, column=1)

    if continent.get()=='아시아' and country.get()=="라오스 루앙프라방" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x500")

        나라이름 = Label(travel, text="라오스 루앙프라방", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=55,column=0, sticky='W')
        Label(travel, text="1. 루앙프라방의 한낮은 매우 덥기 때문에,\n이 더위를 피해 이른 오전과 늦은 오후로 나누어\n도시를 걷는 일을 권장한다.\n\n2. 4월 중순에 여행한다면 송칸이라 불리는\n라오스의 새해맞이 물 축제를 즐길 수 있다.\n\n3. 통금으로 인해 떠들썩한 밤 문화가 없다.\n\n4. 느긋하고 순박한 성품의 도시이므로 그 여유로움을 한껏 누린다.",bg='lightsteelblue', justify='left').grid(row=56,column=0, sticky='W')

    if continent.get()=='아시아' and country.get()=="라오스 루앙프라방" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x500")
        global img_루2

        나라이름 = Label(travel, text="라오스 루앙프라방", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=1,column=0, sticky='W')
        Label(travel, text="루앙프라방의 날씨는 사계절 동안\n여름 날씨를 유지한다.\n여름철 최고기온은 5월에 약 34도 정도이며,\n겨울철 최저기온은 1~2월에 약 14도까지 내려간다.\n제일 더운 시기는 7~8월의 여름인데,\n이때 우기이기 때문에 비가 많이 내려\n실제 기온은 5월이 제일 덥다\n루앙프라방은 매우 더운 밀림으로,\n비도 많고 햇빛도 따갑다.\n여행을 갈 때는 겨울철이 그나마 선선해서 제격이다.",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_루2 = PhotoImage(file='루앙프라방 날씨.gif').subsample(2)
        label_루2 = Label(travel, image=img_루2)
        label_루2.grid(row=3, column=0, sticky='W')



    if continent.get()=='아시아' and country.get()=="인도네시아 발리" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x300")
        

        나라이름 = Label(travel, text="인도네시아 발리", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="""발리의 대중교통은 다소 불편한 편.
지하철은 없고 버스 시스템은 열악함.
But 저렴한 미터택시와 가이드 차량 존재""",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="인도네시아 발리" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x300")

        나라이름 = Label(travel, text="인도네시아 발리", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="인도네시아어, 발리어 사",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="인도네시아 발리" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x300")

        나라이름 = Label(travel, text="인도네시아 발리", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="몽키 모레스트, Mount Agung, Ulun Danu Bratan Tample 등이 존재함\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="인도네시아 발리" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x500")
        global img_발리어휘

        나라이름 = Label(travel, text="인도네시아 발리", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_발리어휘 = PhotoImage(file='발리_언어.gif')
        label_발리어휘 = Label(travel, image=img_발리어휘)
        label_발리어휘.grid(row=4)

    if continent.get()=='아시아' and country.get()=="인도네시아 발리" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x600")

        나라이름 = Label(travel, text="인도네시아 발리", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        global img_발리지리

        나라이름 = Label(travel, text="인도네시아 발리", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_발리지리 = PhotoImage(file='발리_지리.gif').subsample(2)
        label_발리지리 = Label(travel, image=img_발리지리)
        label_발리지리.grid(row=4)

    if continent.get()=='아시아' and country.get()=="인도네시아 발리" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x1000")
        global img_발리추천1,img_발리추천2

        나라이름 = Label(travel, text="인도네시아 발리", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="몽키 모레스트",bg='lightsteelblue', justify='left').grid(row=3)
        img_발리추천1 = PhotoImage(file='발리_추천1.gif').subsample(2)
        label_발리추천1 = Label(travel, image=img_발리추천1)
        label_발리추천1.grid(row=4)

        Label(travel, text="Mount Agung",bg='lightsteelblue', justify='left').grid(row=6)
        img_발리추천2 = PhotoImage(file='발리_추천2.gif').subsample(2)
        label_발리추천2 = Label(travel, image=img_발리추천2)
        label_발리추천2.grid(row=7)

        Label(travel, text="""\n\n\n발리음식추천
1.나시 짬뿌르:서너 가지 반찬이 밥과 함께 한 그릇에 같이 나온다. 식당마다 반찬 종류는 천차만별.
2.나시 고렝:잘게 썬 야채와 고기, 해산물을 기름에 볶고 밥과 양념을 넣은 요리
3.미 고렝:인도네시아식 볶음국수.
4.바비 굴링:어린 돼지를 통째로 바싹 굽는 바비큐 요리""",bg='lightsteelblue', justify='left').grid(row=10, sticky='W')


    if continent.get()=='아시아' and country.get()=="인도네시아 발리" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x400")

        나라이름 = Label(travel, text="인도네시아 발리", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="""1.택시비가 매우 쌈
2. 발리 까프푸에 가면 다양한 식자재가 있음
3. 발리 환전소 중 가끔 눈속임으로 사기치는 환전소가 있으니 길 가 밝은 곳에
위치한 환전소에서 환전하는 것을 추천
4.발리 3월은 비가 많이 옴.""",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="인도네시아 발리" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")

        나라이름 = Label(travel, text="인도네시아 발리", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="날씨 : 1년 내내 더운 날씨",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')


    if continent.get()=='아시아' and country.get()=="싱가포르공화국" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x300")

        나라이름 = Label(travel, text="싱가포르공화국", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=3,column=0, sticky='W')
        Label(travel, text="MRT(지하철), 버스\n-가격이 저렴하면서 시설이 좋다.\n\n택시\n-가장 흔한 교통수단으로 요금이 저렴하다.\n어디서든 아무 때나 탈 수 있어 편리하다.",bg='lightsteelblue', justify='left').grid(row=4,column=0, sticky='W')

    if continent.get()=='아시아' and country.get()=="싱가포르공화국" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x400")

        나라이름 = Label(travel, text="싱가포르공화국", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=51,column=0, sticky='W')
        Label(travel, text="영어, 중국어, 말레이어, 타밀어\n\n싱글리쉬\n-공식적인 언어는 아니고,\n영어를 기반으로 중국어, 각종 중국방언, 말레이어 등이 혼합된 언어이다.\n우리나라의 콩글리쉬와 비슷한 느낌이다.)",bg='lightsteelblue', justify='left').grid(row=52,column=0, sticky='W')

    if continent.get()=='아시아' and country.get()=="싱가포르공화국" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x500")

        나라이름 = Label(travel, text="싱가포르공화국", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=5,column=0, sticky='W')
        Label(travel, text="가든스바이더베이\n마리나베이샌즈\n머라이언파크\n센토사섬\n유니버설 스튜디오\n실로소비치\n팔라완비치\n주롱 새 공원\n에스플라네이드 도서관",bg='lightsteelblue', justify='left').grid(row=6,column=0, sticky='W')

    if continent.get()=='아시아' and country.get()=="싱가포르공화국" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x500")

        나라이름 = Label(travel, text="싱가포르공화국", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=53,column=0, sticky='W')
        Label(travel, text="안녕하세요(Hello, How are you?)\n이거 얼마에요(How much is this?)\n감사합니다(Thank you.)\n우리 호텔은 몇호인가요?(What is my room number?)\n짐 좀 맡길 수 있을까요?(Can I leave my luggage?)\n~까지 어떻게 가나요?(How can I get to ~?)\n네(Yes/Okay)\n화장실이 어딘가요?(Where is the toilet?)\n아니요(No/Nope)\n반갑습니다(Nice to meet you!)\n\n싱가포르만의 표현\nTa Pao(따빠오): 주로 테이크아웃 음식, 포장음식을 말할 때 쓴다.\nChio(치오): 예쁘다, 귀엽다\nBlur(블러): 잘 모르겠다, 헷갈린다\nYah: 네\nNo lah: 아니요\nOk lah, Okie: 알았어",bg='lightsteelblue', justify='left').grid(row=54,column=0, sticky='W')

    if continent.get()=='아시아' and country.get()=="싱가포르공화국" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x300")

        나라이름 = Label(travel, text="싱가포르공화국", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=7,column=0, sticky='W')
        Label(travel, text="동남아시아 말레이반도 최남단에 위치한다.\n총 63개 섬으로 구성된다.\n항구 도시로 이루어진 도시 국가이다.\n북쪽의 조호르 해협과 남쪽의 싱가포르 해협을 두고\n각각 말레이시아, 인도네시아와 약간 분리되어 있다.",bg='lightsteelblue', justify='left').grid(row=8,column=0, sticky='W')

    if continent.get()=='아시아' and country.get()=="싱가포르공화국" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1100x800")
        global img_싱3,img_싱5,img_싱8,img_싱10,img_싱12

        나라이름 = Label(travel, text="싱가포르공화국", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동(쇼핑)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=10,column=0, sticky='W')
        Label(travel, text="부기스 정션 몰: 현지 10대들에게 인기가 높다.\n아기자기한 물건들이 많고,\n문구와 완구 같은 것을 좋아하는 사람들에게 추천한다.\n기념품 가게와 옷 가게 등\n다양하게 둘러볼 수 있다.",bg='lightsteelblue', justify='left').grid(row=11,column=0, sticky='W')
        img_싱3 = PhotoImage(file='싱가포르 부기스 정션 몰.gif').subsample(4)
        label_싱3 = Label(travel, image=img_싱3)
        label_싱3.grid(row=12, column=0, sticky='W')

        Label(travel, text="테마별추천활동(휴양)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=13,column=0, sticky='W')
        Label(travel, text="헬릭스 브리지: 야경도 예쁘고 앞에 야자수들이 줄지어 서있어서\n사진이 예쁘게 나온다.\n브리지의 난간 디자인도 매우 유니크하다.\n다리 위에 테라스도 설치되어 있는데\n사람이 없으면 앉아서 시간을 보내는 것도 추천한다.",bg='lightsteelblue', justify='left').grid(row=14,column=0, sticky='W')
        img_싱5 = PhotoImage(file='싱가포르 헬릭스 브리지.gif').subsample(3)
        label_싱5 = Label(travel, image=img_싱5)
        label_싱5.grid(row=15, column=0, sticky='W')

        Label(travel, text="테마별추천활동(관광)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=10,column=1)
        Label(travel, text="마리나베이샌즈호텔: 싱가포르의 랜드마크 호텔이다.\n밤마다 분수쇼와 레이저쇼, 야경 감상 및 쇼핑 즐기기가 가능하다.\n인피니티풀과 전망이 멋지고 편의시설이 매우 좋다.\n주변이 다 관광지라 접근성이 매우 좋다.\n가든스바이더베이가 바로 옆에 위치한다.",bg='lightsteelblue', justify='left').grid(row=11,column=1)
        img_싱8 = PhotoImage(file='싱가포르 마리나베이샌즈호텔.gif').subsample(2)
        label_싱8 = Label(travel, image=img_싱8)
        label_싱8.grid(row=12, column=1)

        Label(travel, text="테마별추천활동(식도락)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=13,column=1)
        Label(travel, text="칠리 크랩: 싱가포르식 게 요리다.\n걸쭉한 토마토 칠리소스가 칠리 크랩의 핵심이다.\n새콤달콤하면서도 매운맛이 특징이다.\n소스의 맛이 묘하게 중독적이다.\n싱가포르 식당에서 제공하는 물티슈는 대부분 유료이므로\n물티슈 또는 비닐장갑을 직접 챙겨가면 좋다.",bg='lightsteelblue', justify='left').grid(row=14,column=1)
        img_싱10 = PhotoImage(file='싱가포르 칠리크랩.gif').subsample(3)
        label_싱10 = Label(travel, image=img_싱10)
        label_싱10.grid(row=15, column=1)

        Label(travel, text="테마별추천활동(활동)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=10,column=2)
        Label(travel, text="어드벤처 코브 워터파크: 싱가포르를 대표하는 워터파크이다.\n스릴 넘치는 워터 슬라이드 등 놀이기구 뿐만 아니라\n열대어 스노클링과 파도 풀 서핑, 수영도 즐길 수 있다.\n스릴 넘치는 놀이기구들도 많지만, 어린이를 위한 시설도 있다.\n특히 튜브를 타고 떠다니며\n다양한 물고기를 감상하는 어트랙션인 어드벤처 리버를 추천한다.",bg='lightsteelblue', justify='left').grid(row=11,column=2)
        img_싱12 = PhotoImage(file='싱가포르 워터파크.gif').subsample(2)
        label_싱12 = Label(travel, image=img_싱12)
        label_싱12.grid(row=12, column=2)


    if continent.get()=='아시아' and country.get()=="싱가포르공화국" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x600")

        나라이름 = Label(travel, text="싱가포르공화국", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=55,column=0, sticky='W')
        Label(travel, text="1. 지하철인 MRT를 많이 타고 다니는 경우,\n관광객을 위한 투어리스트 티켓을 구입하면 돈을 절약할 수 있다.\n\n2. 버스를 탈 때 현금을 내도 되지만 잔돈이 없음을 주의해야 한다.\n선불 교통카드인 이지링크 티켓을 써서 환승해도 된다.\n\n3.벌금 제도가 엄격하다.\n\n\n껌 반입: 벌금 1만 달러\n미신고 담배 반입: 200달러(초범)~최대 5000달러(재범 및 악성)\n-반입신고하면 세금 부과(담배 1개비당 35.2센트에 소비세 7% 가산)\n-담배값이 우리나라 돈으로 따지면 1갑에 만원이 넘고 매장에서 이제 담배 진열이 금지되어서 담배의 이름을 모르면 구입할 수 없다.\nMRT를 탈 때 음식: 500달러의 벌금, 흡연: 1000달러, 애완동물 반입: 500달러, 두리안 반입: 500달러, 가연성 액체 반입: 500달러\n횡단보도 및 육교를 이용하지 않고 50m 이내의 거리에서 도로를 횡단: 50달러\n조류의 먹이주기: 최대 1000달러\n공중화장실에서 사용 후 물을 내리지 않을 경우: 최대 1000달러\n쓰레기 투기: 최대 1000달러(초범)~최대 2000달러 및 청소 작업(재범)\n흡연 장소 이외에서의 흡연: 최대 1000달러\n침이나 가래를 뱉은 경우: 최대 1000달러\n\n\n4.공공장소에서 심야 10시 30분~아침 7시까지 음주 금지\n(술집, 바, 레스토랑 등의 허가된 상점과 호텔 등의 객실 내에서는 음주 가능)\n\n5.심야 10시~아침 7시까지 주류 판매 금지\n(공항 면세점 제외)\n\n6.오차드 로드, 리틀인디아, 차이나타운, 겔랑, 그리고 발레스티어 등을 조심\n-치안이 상대적으로 좋지 않은 곳들",bg='lightsteelblue', justify='left').grid(row=56,column=0, sticky='W')

    if continent.get()=='아시아' and country.get()=="싱가포르공화국" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x600")
        global img_싱2

        나라이름 = Label(travel, text="싱가포르공화국", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=1,column=0, sticky='W')
        Label(travel, text="전형적인 열대기후로 무덥고 습하며\n우기와 건기의 구별이 뚜렷해\n6~9월에 비가 자주 내린다.\n계절이 바뀌는 시기에는 대기가 불안정해\n주로 저녁에 천둥번개를 동반한 폭우가 쏟아진다.\n1년 내내 우리나라 8월의 기온이라고 생각하면 되어서\n여행할 때 반팔, 반바지 등 시원한 옷을 준비해 가는 게 좋다.\n근데 실내는 냉방이 잘 되어있기 때문에\n겉옷 하나씩 준비해가면 좋다.",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_싱2 = PhotoImage(file='싱가포르의 기후.gif')
        label_싱2 = Label(travel, image=img_싱2)
        label_싱2.grid(row=3, column=0, sticky='W')



    if continent.get()=='아시아' and country.get()=="태국 방콕" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("700x400")

        나라이름 = Label(travel, text="태국 방콕", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="교통이 편리한 편. 지하철, 버스 등이 있으며 택시나 작은 트럭으로도 이동 가능",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="태국 방콕" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x200")

        나라이름 = Label(travel, text="태국 방콕", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="언어 : 태국어\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="태국 방콕" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x300")

        나라이름 = Label(travel, text="태국 방콕", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="석가모니 열반상, 새벽 사원 등",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="태국 방콕" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("700x900")
        global img_어휘

        나라이름 = Label(travel, text="태국 방콕", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_어휘 = PhotoImage(file='어휘.gif').subsample(1)
        label_어휘 = Label(travel, image=img_어휘)
        label_어휘.grid(row=3)

    if continent.get()=='아시아' and country.get()=="태국 방콕" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x800")
        global img_지리정보

        나라이름 = Label(travel, text="태국 방콕", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_지리정보 = PhotoImage(file='지리정보.gif').subsample(1)
        label_지리정보 = Label(travel, image=img_지리정보)
        label_지리정보.grid(row=5)

    if continent.get()=='아시아' and country.get()=="태국 방콕" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("700x900")
        global img_태국추천1,img_태국추천2

        나라이름 = Label(travel, text="태국 방콕", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')

        Label(travel, text="관광 : 새벽사원",bg='lightsteelblue', justify='left').grid(row=4)
        img_태국추천1 = PhotoImage(file='태국추천1.gif').subsample(2)
        label_태국추천1 = Label(travel, image=img_태국추천1)
        label_태국추천1.grid(row=5)

        Label(travel, text="쇼핑 : 센트럴 월드 플라자",bg='lightsteelblue', justify='left').grid(row=9)
        img_태국추천2 = PhotoImage(file='태국추천2.gif').subsample(2)
        label_태국추천2 = Label(travel, image=img_태국추천2)
        label_태국추천2.grid(row=10)
        

    if continent.get()=='아시아' and country.get()=="태국 방콕" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x100")

        나라이름 = Label(travel, text="태국 방콕", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="없음\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="태국 방콕" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x200")

        나라이름 = Label(travel, text="태국 방콕", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="날씨 : 고온 다습",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')



    if continent.get()=='아시아' and country.get()=="베트남 다낭" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x300")

        나라이름 = Label(travel, text="베트남 다낭", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="택시 - 편하고 빠르게 이동할 수 있는 교통수단\n시내버스 - 요금은 저렴하지만, 속도는 느려요!\n오토바이 택시 '쎄옴' - 베트남 현지인들의 대중교통수단",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="베트남 다낭" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x200")

        나라이름 = Label(travel, text="베트남 다낭", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="언어 : 베트남어",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="베트남 다낭" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x300")

        나라이름 = Label(travel, text="베트남 다낭", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="The Marble Mountains, Lady Buddha, Ba Na Hills, Dragon Bridge \n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="베트남 다낭" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("700x800")
        global img_다낭어휘

        나라이름 = Label(travel, text="베트남 다낭", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_다낭어휘 = PhotoImage(file='다낭어휘.gif')
        label_다낭어휘 = Label(travel, image=img_다낭어휘)
        label_다낭어휘.grid(row=10)

    if continent.get()=='아시아' and country.get()=="베트남 다낭" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1000x500")
        global img_다낭지리

        나라이름 = Label(travel, text="베트남 다낭", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_다낭지리 = PhotoImage(file='다낭지리.gif')
        label_다낭지리 = Label(travel, image=img_다낭지리)
        label_다낭지리.grid(row=10)

    if continent.get()=='아시아' and country.get()=="베트남 다낭" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x600")
        global img_다낭추천1,img_다낭추천2

        나라이름 = Label(travel, text="베트남 다낭", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_다낭추천1 = PhotoImage(file='다낭추천1.gif').subsample(3)
        label_다낭추천1 = Label(travel, image=img_다낭추천1)
        label_다낭추천1.grid(row=4)
        Label(travel, text="My Khe Beach(해변)",bg='lightsteelblue', justify='left').grid(row=5)

        img_다낭추천2 = PhotoImage(file='다낭추천2.gif').subsample(3)
        label_다낭추천2 = Label(travel, image=img_다낭추천2)
        label_다낭추천2.grid(row=7)
        Label(travel, text="My Khe Beach(해변)",bg='lightsteelblue', justify='left').grid(row=8)

        Label(travel, text="""다낭 음식추천
1.퍼 보 Pho Bo - 대표적인 베트남 쌀국수
2.미 꽝 Mi Quang - 중부 지방의 명물 비빔 쌀국수
3.반쎄오 Ban Xeo - 취향대로 고를 수 있는 베트남식 빈대떡
4.껌가 Com Ga - 저렴한 가격이 매력, 담백한 닭고기덮밥
5.반미 Banh Mi - 파리만큼 맛있는 베트남식 바게트 샌드위치
""",bg='lightsteelblue', justify='left').grid(row=4,column=1)


    if continent.get()=='아시아' and country.get()=="베트남 다낭" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")
        global img_다낭꿀팁

        나라이름 = Label(travel, text="베트남 다낭", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_다낭꿀팁 = PhotoImage(file='다낭꿀팁.gif')
        label_다낭꿀팁 = Label(travel, image=img_다낭꿀팁)
        label_다낭꿀팁.grid(row=10)

    if continent.get()=='아시아' and country.get()=="베트남 다낭" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x300")

        나라이름 = Label(travel, text="베트남 다낭", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="날씨 : 보통 따뜻, 10~11: 비 많이 옴, 12~1: 폭우성 비+기온이 내려감(약 20도)\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

        

    if continent.get()=='아시아' and country.get()=="중국 마카오" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x500")

        나라이름 = Label(travel, text="중국 마카오", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=3,column=0, sticky='W')
        Label(travel, text="지하철이 없다. 지역 내 관광은 도보를 추천한다.\n마카오 반도 내 먼 거리를 이동할 때,\n외곽 지역은 버스를 이용한다.\n일행이 여러 명이면 택시로 움직이는 것이\n저렴하고 빠르고 편리하다.\n주요 호텔은 무료 셔틀 버스를 운영한다.\n삼륜 자전거인 페디캡은\n옛 정취가 남아 있는 마카오의 역사적인 거리를\n느긋하게 돌아볼 수 있는 낭만적인 교통수단이다.\n페디캡은 외항 페리 터미널이나 리스보아 호텔 주변에\n많이 모여 있는데, 바가지를 쓰는 일이 없도록\n타기 전에 운전사와 미리 가격 흥정을 하는 것이 좋다.",bg='lightsteelblue', justify='left').grid(row=4, column=0, sticky='W')

    if continent.get()=='아시아' and country.get()=="중국 마카오" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x300")

        나라이름 = Label(travel, text="중국 마카오", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=51,column=0, sticky='W')
        Label(travel, text="중국어(광둥어를 주로 쓴다), 포르투갈어",bg='lightsteelblue', justify='left').grid(row=52,column=0, sticky='W')

    if continent.get()=='아시아' and country.get()=="중국 마카오" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x500")

        나라이름 = Label(travel, text="중국 마카오", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=5,column=0, sticky='W')
        Label(travel, text="세나도 광장\n코타이 스트립\n타이파 빌리지\n몽콕야시장\n아마 사원\n마카오 타워\n성 라자루스 성당\n피크트램\n브로드웨이 푸드스트릿",bg='lightsteelblue', justify='left').grid(row=6,column=0, sticky='W')

    if continent.get()=='아시아' and country.get()=="중국 마카오" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x500")

        나라이름 = Label(travel, text="중국 마카오", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=53,column=0, sticky='W')
        Label(travel, text="안녕하세요(你好嗎?: nǐhǎo ma?)\n이거 얼마에요?(幾多錢?: jǐduō qián?)\n감사합니다(我好感激。: wǒhǎo gǎnjī)\n우리 호텔은 몇호인가요?(我哋有幾多間酒店?: wŏdì yǒu jǐduō jiàn jiǔdiàn?)\n짐을 맡길 수 있을까요?(我可唔可以留低行李呀?: wǒ kĕwú kěyǐ liú dī xíngli ya?)\n~까지 어떻게 가나요?(我如何到達~?: wǒhǎo hé dàodá~?)\n네(係。: xì)\n화장실이 어딘가요?(廁所喺邊?: cèsuǒ xìbiān)\n아니요(唔係。: mú xì)\n반갑습니다(我好高興識得你。: nǐ hǎo gāoxìng shídé nǐ)",bg='lightsteelblue', justify='left').grid(row=54,column=0, sticky='W')

    if continent.get()=='아시아' and country.get()=="중국 마카오" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x500")

        나라이름 = Label(travel, text="중국 마카오", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=7,column=0, sticky='W')
        Label(travel, text="중국 난하이 유역 주장강에 위치한다.\n남중국해에 접하는 마카오는 중심지가 되는 반도부와\n타이파 섬과 콜로아느 섬 사이를 매립해 연결한 섬으로 되어 있다.\n중화인민공화국 본토의 주하이 경제특구와 다리로 연결되어 있다.\n1970년대 이후에 대규모 매립을 했기 때문에\n마카오의 지형은 대체로 평탄하지만,\n많은 언덕이 지형의 근본을 이루고 있다.\n마카오 반도는 원래 섬이었지만\n서서히 사주가 성장해 좁은 지협이 되었다.\n마카오는 고도로 밀집된 도시이며,\n경작지, 목장, 삼림이나 숲은 없고,\n실질적으로 농사를 짓기 힘들다.",bg='lightsteelblue', justify='left').grid(row=8,column=0, sticky='W')

    if continent.get()=='아시아' and country.get()=="중국 마카오" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1000x900")
        global img_마3,img_마6,img_마7,img_마9

        나라이름 = Label(travel, text="중국 마카오", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동(관광)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=10,column=0, sticky='W')
        Label(travel, text="세나도 광장: 세나도는 포르투갈어로 의회를 뜻한다.\n동양과 서양의 문화가 공존하는 거리 풍경을 지니고 있다.\n유럽의 광장에 비하면 그리 크지 않은 규모이지만\n광장을 둘러싼 유럽풍 건물과 물결무늬가 새겨진 타일 바닥이\n이국적인 아름다움을 연출한다.",bg='lightsteelblue', justify='left').grid(row=11,column=0, sticky='W')
        img_마3 = PhotoImage(file='마카오 세나도 광장.gif').subsample(4)
        label_마3 = Label(travel, image=img_마3)
        label_마3.grid(row=12, column=0, sticky='W')

        Label(travel, text="테마별추천활동(관광)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=13,column=0, sticky='W')
        Label(travel, text="피크트램: 마카오의 야경을 가장 잘 볼 수 있다.\n아래 사진이 피크트램에서 찍은 마카오의 야경이다.",bg='lightsteelblue', justify='left').grid(row=14,column=0, sticky='W')
        img_마6 = PhotoImage(file='마카오 피크트램 전경.gif').subsample(4)
        label_마6 = Label(travel, image=img_마6)
        label_마6.grid(row=15, column=0, sticky='W')


        Label(travel, text="테마별추천활동(식도락)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=10,column=1)
        Label(travel, text="쭈빠빠오: 마카오 대표 음식인 돼지고기 번이다.\n빵 속에 튀긴 돼지고기를 넣은 이 빵은\n마카오 현지인들이 가볍게 즐겨먹는 한끼 식사이다.\n별다른 소스 없이 고기와 빵만 있는데 맛있다.",bg='lightsteelblue', justify='left').grid(row=11,column=1)
        img_마7 = PhotoImage(file='마카오 쭈빠빠오.gif').subsample(3)
        label_마7 = Label(travel, image=img_마7)
        label_마7.grid(row=12, column=1)

        Label(travel, text="테마별추천활동(활동)", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=13,column=1)
        Label(travel, text="마카오 타워: 전망대로써의 역할도 하지만,\n그 높이를 이용한 다양한 체험을 할 수 있다.\n타워 클라이밍, 스카이워크 X, 스카이 점프 등\n200m 높이에서 번지점프에 도전할 수 있다.",bg='lightsteelblue', justify='left').grid(row=14,column=1)
        img_마9 = PhotoImage(file='마카오 타워.gif').subsample(4)
        label_마9 = Label(travel, image=img_마9)
        label_마9.grid(row=15, column=1)

    if continent.get()=='아시아' and country.get()=="중국 마카오" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x550")

        나라이름 = Label(travel, text="중국 마카오", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=55,column=0, sticky='W')
        Label(travel, text="1. 옷차림: 1~2월, 12월 옷차림은 긴팔과 점퍼가 좋다.\n3, 4, 10, 11월 옷차림은 긴팔과 반팔이 좋다.\n5~9월 옷차림은 반팔이 좋다.\n겨울일 때 가면 약간 쌀쌀하니 가디건이 필요할 수 있고,\n여름에는 실내로 들어가면 에어컨 때문에 추울 수 있으니\n가디건이 필요할 수 있다.\n\n2. 마카오 24시간 긴급 핫라인: (853)110, 112\n경찰: (853)999\n여권분실: (852)9155-7204\n\n3. 전압: 220V\n플러그 타입: 타입 G\n\n4. 마카오에서는 1층이 Ground Floor,\n2층이 First Floor(1st Floor)이다.\n즉, 엘리베이터에서 2F 버튼을 누르면 3층으로 간다.\n\n5. 버스 탈 때, 목적지를 정확히 알기 위해\n지도를 들고 타는 것을 추천한다.\n\n6. 구시가지 도로는 일방통행이 많고\n차선이 좌측통행이므로 안전에 주의한다.",bg='lightsteelblue', justify='left').grid(row=56,column=0, sticky='W')

    if continent.get()=='아시아' and country.get()=="중국 마카오" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("700x500")
        global img_마2

        나라이름 = Label(travel, text="중국 마카오", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=1,column=0, sticky='W')
        Label(travel, text="마카오에는 봄/가을 날씨와 여름 날씨가 있다.\n봄/가을 날씨는 1~4월, 10~12월이고,\n그중에 1월과 12월에는 11~20도로 약간 춥다고 느껴질 수 있다.\n여름 날씨는 5~9월로 30~40도로 정말 더운 날씨이다.\n체감온도로는 2~4월, 10~11월에 일교차가 크지 않으며\n1월, 5~9월, 12월에는 일교차가 크다.\n우리나라 겨울에 여행을 가면 약간 쌀쌀한 날씨이고,\n우리나라 여름에 여행을 가면\n높은 기온과 습도로 인해서\n체감온도가 굉장히 높다.",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_마2 = PhotoImage(file='마카오 날씨.gif').subsample(2)
        label_마2 = Label(travel, image=img_마2)
        label_마2.grid(row=3, column=0, sticky='W')


    if continent.get()=='아시아' and country.get()=="홍콩" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x200")

        나라이름 = Label(travel, text="홍콩", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="버스, 지하철, 트램\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="홍콩" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x200")

        나라이름 = Label(travel, text="홍콩", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="광동어, 영어\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="홍콩" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x500")
        global img_심포니오브라이트, img_미드레벨에스컬레이터

        나라이름 = Label(travel, text="홍콩", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="심포니오브라이트\n",bg='lightsteelblue', justify='left').grid(row=3, column=0, sticky='W')
        Label(travel, text="미드레벨에스컬레이터\n",bg='lightsteelblue', justify='left').grid(row=3, column=1)

        img_심포니오브라이트 = PhotoImage(file='홍콩_추천스팟_심포니오브라이트.gif')
        label_심포니오브라이트 = Label(travel, image=img_심포니오브라이트)
        label_심포니오브라이트.grid(row=4, column=0, sticky='W')

        img_미드레벨에스컬레이터 = PhotoImage(file='홍콩_테마별추천활동_미드레벨에스컬레이터.gif')
        label_미드레벨에스컬레이터 = Label(travel, image=img_미드레벨에스컬레이터)
        label_미드레벨에스컬레이터.grid(row=4, column=1)

    if continent.get()=='아시아' and country.get()=="홍콩" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x200")

        나라이름 = Label(travel, text="홍콩", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="多谢! 뚸~째:감사합니다!\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="홍콩" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x250")

        나라이름 = Label(travel, text="홍콩", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="지질학적으로 3개의 영토로 구분된다-가우룽, 홍콩섬, 신제\n 60개의 섬들이 홍콩 주변을 아우르고 있다\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="홍콩" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("700x500")
        global img_딤섬, img_하버시티
        
        나라이름 = Label(travel, text="홍콩", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="딤섬",bg='lightsteelblue', justify='left').grid(row=3, column=0, sticky='W')
        Label(travel, text="하버시티",bg='lightsteelblue', justify='left').grid(row=3, column=1, sticky='W')
        
        img_딤섬 = PhotoImage(file='홍콩_테마별추천활동_딤섬.gif')
        label_딤섬 = Label(travel, image=img_딤섬)
        label_딤섬.grid(row=4, column=0, sticky='W')

        img_하버시티 = PhotoImage(file='홍콩_테마별추천활동_하버시티.gif')
        label_하버시티 = Label(travel, image=img_하버시티)
        label_하버시티.grid(row=4, column=1)


    if continent.get()=='아시아' and country.get()=="홍콩" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x200")

        나라이름 = Label(travel, text="홍콩", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="옥토퍼스 카드 사용(교통 식사 쇼핑 가능)\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="홍콩" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")

        나라이름 = Label(travel, text="홍콩", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="홍콩의 여름은 따뜻한 남서풍과 가끔씩 오는 소나기와 뇌우 등의 영향으로 대체로 덥고 습하다.\n 겨울은 온화하며 초반에는 화창하나 대체로 2월부터 흐려지며, 가끔 발생되는 한랭전선은 북쪽에서 강하고 차가운 바람을 가져온다.\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')


    if continent.get()=='아시아' and country.get()=="중국 상하이" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")

        나라이름 = Label(travel, text="중국 상하이", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="지하철: 상해의 지하철은 17개의 노선으로 이루어져있다. 기본요금 3위안부터 시작하여 거리에 비례해서 요금이 늘어난다. \n"
                            "보통 운행시간은 05:00-23:30까지이며, 지하철 티켓은 역마다 판매 기계에서 쉽게 구매할 수 있다.\n\n"
                            "버스: 기본요금 2위안이며, 환승이 불가능하다. 거스름돈을 주지 않고, 보통 운행시간은 05;30-23;00이지만 정확하게 지켜지지 않는 편이다.\n\n"
                            "택시: 기본요금은 14엔이고 3km까지는 기본요금에 해당하고, 그 이후로는 거리에 비례하여 요금이 올라간다. \n"
                            "23시부터 새벽 5시까지는 야간 할증이 적용되며 기본요금이 18위안부터 시작한다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="중국 상하이" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x200")

        나라이름 = Label(travel, text="중국 상하이", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="공용어는 중국어이고, 중국에서 상하이는 영어 숙련도 지수가 가장 높은 것으로 평가받았다. 즉, 어느정도 영어로 의사소통이 가능하다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="중국 상하이" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x550")
        global img_상하이1, img_상하이2

        나라이름 = Label(travel, text="중국 상하이", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="디즈니랜드, 예원",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')
        img_상하이1 = PhotoImage(file='중국상하이_추천스팟_디즈니랜드.gif')
        label_상하이1 = Label(travel, image=img_상하이1)
        label_상하이1.grid(row=4, column=0, sticky='W')
        img_상하이2 = PhotoImage(file='중국상하이_추천스팟_예원.gif')
        label_상하이2 = Label(travel, image=img_상하이2)
        label_상하이2.grid(row=5, column=0, sticky='W')

    if continent.get()=='아시아' and country.get()=="중국 상하이" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("700x500")

        나라이름 = Label(travel, text="중국 상하이", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="안녕하세요. 您好 [닌하오](Nín hǎo)\n"
                            "안녕히 계세요. 再见 [짜이 지엔](Zàijiàn)\n"
                            "고맙습니다. 谢谢 [씨에씨에](Xièxiè)\n"
                            "별말씀을요. 不客气 [부크어치](Bù kèqì)\n"
                            "죄송합니다. 不好意思 [뿌하오이쓰](Bù hǎoyìsi)\n"
                            "괜찮아요. 不用不用 [부용부용](Bùyòng bùyòng)\n"
                            "어느 나라 사람입니까? 你是哪国人 [니 시 나 꾸어 런](Nǐ shì nǎ guórén)\n"
                            "저는 한국사람입니다. 我是韩国人 [워 시 한 꾸어 런](Wǒ shì hánguó rén)\n"
                            "이름이 뭐예요? 你叫什么名字 [니 쟈오 션머 밍 쯔](Nǐ jiào shénme míngzì)\n"
                            "내 이름은 XXX입니다. 我叫XXX [워 지아오 XXX](Wǒ jiào XXX)\n"
                            "만나서 반가워요. 见到您很高兴 [지엔 따오 닌헌 가오싕](Jiàn dào nín hěn gāoxìng)\n"
                            "나는 이것이 좋다. 我喜欢这个 [워 씨 후완 쩌 거](Wǒ xǐhuān zhège.)\n"
                            "나는 저것이 싫다. 我不喜欢那个 [워 뿌 씨 후완 나 거](Wǒ Bù xǐhuān Nàgè)\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="중국 상하이" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")

        나라이름 = Label(travel, text="중국 상하이", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="상하이는 면적은 서울의 약 열배 이상이다. 상하이의 지리는 크게 황푸강을 경계로 푸동과 푸시로 나뉜다. \n"
                            "푸동은 동방명주를 비롯한 현대적이고 세련된 고층빌딩들을 많이 볼 수 있고, 푸시는 반대로 구시가지로 상하이만의 독특한 정취를 느낄 수 있다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="중국 상하이" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1500x1500")
        global img_상하이3, img_상하이4, img_상하이5

        나라이름 = Label(travel, text="중국 상하이", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="((관광)\n"
                            "동방명주: 건설 당시 '아시아에서 두 번째 높은 건물'이라는 타이틀을 달 정도로 최고 높이 468m를 자랑한다. \n"
                            "350m 높이의 전망대에서 초고층 건물이 선사하는 화려한 스카이라인과저녁에 방문하면 환상적인 야경을 한눈에 감상할 수 있다. \n"
                            "입장료는 26000원 정도이고, 더 높이 올라가면 올라갈수록 입장료가 더 비싸진다고 한다.\n"
                            "대한민국임시정부청사: 대한민국 임시정부의 터가 그대로 남아 있는 자리로, 그 시절의 한민족의 정서를 그대로 느낄 수 있다. \n"
                            "3500원 정도로 입장료 또한 싼편이며, 한국인들만이 즐겨찾는 관광지로, 여유롭게 관광을 즐길 수 있다.\n\n"
                            "((휴양)\n"
                            "드래곤플라이&그린 마사지샵: 상해에서 유명한 마사지샵 체인으로 총 5개가 있다고 한다. \n"
                            "1시간 20분짜리 마사지(발 + 전신 마사지)가 190위안, 즉 32000원일 정도로 저렴하기 때문에 힐링이 필요하다면 여행 중 틈틈이 방문하는 것을 추천한다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')
        img_상
하이3 = PhotoImage(file='중국상하이_테마별추천활동_동방명주.gif').subsample(2)
        label_상하이3 = Label(travel, image=img_상하이3)
        label_상하이3.grid(row=4, column=0, sticky='W')
        img_상하이4 = PhotoImage(file='중국상하이_테마별추천활동_임시청사.gif').subsample(2)
        label_상하이4 = Label(travel, image=img_상하이4)
        label_상하이4.grid(row=4, column=1)
        img_상하이5 = PhotoImage(file='중국상하이_테마별추천활동_마사지.gif').subsample(2)
        label_상하이5 = Label(travel, image=img_상하이5)
        label_상하이5.grid(row=3, column=1)


    if continent.get()=='아시아' and country.get()=="중국 상하이" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1300x300")

        나라이름 = Label(travel, text="중국 상하이", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="1. 상하이에서는 지하철을 타기 전 개찰구 앞에서 수하물 검사를 한다. 그러기에 많은 짐을 싸다니고 여행을 하면 검사 시간도 늦어지니 짐을 가볍게 들고 여행하는 것을 추천한다.\n"
                            "2. 상하이는 회사별로 택시 색이 다르다. 그 중 보통 빨간색 택시는 미터기가 올라가는 속도가 더욱 빠르고 난폭운전을 할 가능성이 더 높아 피하는 것이 좋다. \n"
                            "그래서 짙은 하늘색, 짙은 연두색, 흰색, 노란색, 파란색, 빨간색, 남색, 팥죽색 순서대로의 택시를 추천한다. \n"
                            "또한 보조좌속 쪽 붙어있는 택시 면허증의 별 개수를 보고 친절도와 능력을 알 수 있다. 5점 만점으로 별의 개수가 많을수록 더욱 편리한 여정이 될 것이다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="중국 상하이" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")

        나라이름 = Label(travel, text="중국 상하이", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="12-2월 평균기온 3도, 3-4월 비, 선선한 날씨, 더운 여름 5-9월 많은 비. 소나기, 10,11월 비가 가장 적게 오는 기간",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')



    if continent.get()=='아시아' and country.get()=="일본 오사카" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x600")

        나라이름 = Label(travel, text="일본 오사카", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="우리나라랑 유사함",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="일본 오사카" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x200")

        나라이름 = Label(travel, text="일본 오사카", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="언어 : 일본어",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="일본 오사카" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x200")

        나라이름 = Label(travel, text="일본 오사카", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="나가지 공원, 미도 스지(산책로), 텐노지 공원 등",bg='lightsteelblue', justify='left').grid(row=3,column=0, sticky='W')


    if continent.get()=='아시아' and country.get()=="일본 오사카" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x1000")
        global img_오사카회화

        나라이름 = Label(travel, text="일본 오사카", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_오사카회화 = PhotoImage(file='오사카회화.gif').subsample(1)
        label_오사카회화 = Label(travel, image=img_오사카회화)
        label_오사카회화.grid(row=10)

    if continent.get()=='아시아' and country.get()=="일본 오사카" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x600")
        global img_오사카지리

        나라이름 = Label(travel, text="일본 오사카", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_오사카지리 = PhotoImage(file='오사카지리.gif')
        label_오사카지리 = Label(travel, image=img_오사카지리)
        label_오사카지리.grid(row=4)

    if continent.get()=='아시아' and country.get()=="일본 오사카" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x600")
        global img_오사카추천1,img_오사카추천2

        나라이름 = Label(travel, text="일본 오사카", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_오사카추천1 = PhotoImage(file='오사카추천1.gif').subsample(2)
        label_오사카추천1 = Label(travel, image=img_오사카추천1)
        label_오사카추천1.grid(row=4)
        Label(travel, text="나가이공원",bg='lightsteelblue', justify='left').grid(row=5,column=0, sticky='W')
        

        img_오사카추천2 = PhotoImage(file='오사카추천2.gif').subsample(2)
        label_오사카추천2 = Label(travel, image=img_오사카추천2)
        label_오사카추천2.grid(row=7)
        Label(travel, text="street Kart Osaka",bg='lightsteelblue', justify='left').grid(row=9,column=0, sticky='W')


    if continent.get()=='아시아' and country.get()=="일본 오사카" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x300")

        나라이름 = Label(travel, text="일본 오사카", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="""1. 오사카 교통패스는 사는 게 이득!
2. 오사카의 밤을 그냥 보내지 말고, 숙소 근처에서 이자카야를 누려라
3. 동전 지갑은 지갑과 별개로 따로 꼭 챙기자""",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="일본 오사카" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x200")

        나라이름 = Label(travel, text="일본 오사카", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="날씨 : 우리나라랑 같음\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')


    if continent.get()=='아시아' and country.get()=="일본 도쿄" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x200")

        나라이름 = Label(travel, text="일본 도쿄", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="일본의 전역에서는 일본어가 사용되며, 영어는 잘 안 통하는 편이다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="일본 도쿄" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x400")

        나라이름 = Label(travel, text="일본 도쿄", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="전철 : JR은 일본 철도청 Japan Railway에서 운영하는 전철로, 주오선, 소부선 등이 있다.\n"
                            "기본 요금은 ¥140부터 시작하며 목적지에 따라 요금이 추가된다. \n"
                            "지하철과 JR선에 속하지 않는 다른 전철인 사철은 노선 이름에 따라 운영하는 회사가 다르며, 서로 환승이 불가능하다. \n\n" 
                            "지하철: 지하로 다니는 열차를 지하철이라 하며 도쿄의 지하철은 크게 도쿄 메트로와 도에이로 나뉜다. \n"
                            "도쿄 메트로는 도쿄 지하철 주식회사에서 운영하는 지하철로 총 9개 노선이고, 환승이 가능하며 요금은 ¥170부터이다. \n"
                            "도쿄도 교통국에서 운영하는 노선을 도영선, 즉 도에이선이라고 하며 총 4개의 노선이 있다. \n"
                            "도쿄 메트로와 마찬가지로 도에이선끼리의 환승은 추가 요금을 내지 않는다. 기본 요금은 ¥180부터이다.\n\n"
                            "택시: 일본의 택시는 요금이 많이 비싼 편이다. 기본요금은 ¥410이며 2km 이후부터는 237m마다 ¥80씩 올라간다. \n"
                            "일본 택시의 또 다른 특징은 바로 자동문이다. 손님이 직접 문을 열 필요 없이 택시 기사의 조종으로 뒷문을 여닫을 수 있다. \n\n"
                            "버스: 대부분 주택가와 지하철 역을 연결하는 노선으로 운영된다. 도영 시내버스의 기본 요금은 ¥210이다. \n"
                            "도쿄 외곽이나 시외로 넘어가는 버스는 거리에 따라 할증이 붙는다. 시간표에 맞춰 정확한 시간에 버스가 도착하는 편이다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="일본 도쿄" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x600")
        global img_도쿄1, img_도쿄2

        나라이름 = Label(travel, text="일본 도쿄", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="도쿄타워, 메이지 신궁.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')
        img_도쿄1 = PhotoImage(file='일본도쿄_추천스팟_도쿄타워.gif')
        label_도쿄1 = Label(travel, image=img_도쿄1)
        label_도쿄1.grid(row=4, column=0, sticky='W')
        img_도쿄2 = PhotoImage(file='일본도쿄_추천스팟_메이지신사.gif')
        label_도쿄2 = Label(travel, image=img_도쿄2)
        label_도쿄2.grid(row=5, column=0, sticky='W')


    if continent.get()=='아시아' and country.get()=="일본 도쿄" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x400")

        나라이름 = Label(travel, text="일본 도쿄", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="예/아니요　　　　　はい　하이/ いいえ　이이에\n"
                            "실례합니다(죄송합니다) 　　　　　 すみません　스미마센\n"
                            "감사합니다  　　　　　ありがとうございます　아리가토고자이마스 \n"
                            "에 가고 싶어요.   —–に行きたいです　 —–니 이키타이 데스\n"
                            "—-가(은/는) 있습니까?  —–が（は）ありますか　　—–가(와) 아리마스까\n"
                            "—-는 어디입니까?  —–はどこですか　　—–와 도꼬데스까\n"
                            "—-를 주세요   —–をください　　　—-오 쿠다사이",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="일본 도쿄" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")

        나라이름 = Label(travel, text="일본 도쿄", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="도쿄는 일본 열도의 중심부, 간토 지방의 남부에 위치한다. \n"
                            "동쪽은 에도가와를 경계로 지바현, 서쪽은 산지를 경계로 야마나시현, 남쪽은 다마가와를 경계로 가나가와현, 북쪽은 사이타마현과 각각 접해 있다.\n"
                            "일본 전체 인구의 약 30%를 차지하는 도쿄권은 도쿄와 인접한 3현(사이타마현, 지바현, 가나가와현)으로 구성되며, \n"
                            "수도권은 도쿄와 주변 7현(사이타마현, 지바현, 가나가와현, 이바라키현, 도치기현, 군마현, 야마나시현)으로 구성된다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="일본 도쿄" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1000x400")

        나라이름 = Label(travel, text="일본 도쿄", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="1. 도쿄 시내를 편하게 관광할 수 있는 스카이 버스 도쿄는 버스 2층에 앉아 도쿄 주요 여행지를 돌아보는 ‘스카이 버스 도쿄’\n"
                            "원하는 정류장에서 자유롭게 승하차할 수 있는 ‘스카이 홉 버스’, 강과 육지를 모두 이동할 수 있는 수륙 양용 ‘스카이덕’까지 \n"
                            "세가지로 크게 나뉜다. 중국어, 영어, 한국어로 음성 안내가 지원되기 때문에 편안한 여행을 원한다면 이용하는 것이 합리적이다. \n"
                            "2. 일본은 모든 상품에 8%의 소비세를 부과한다(2019년 10월부터 10%로 인상 예정). \n"
                            "하지만 외국인 관광객의 소비 장려를 위해 특별히 세금을 면제하고 있으니 잘 활용해보자. \n"
                            "여권만 있다면 세금이 제외된 가격에 물건을 살 수 있으니 쇼핑 전 해당 상점의 면세 대상 상품을 꼭 확인하고 계산할 때도 금액을 잘 확인하자. \n"
                            "또한 면세 혜택을 받을 수 있는 최소 구매 금액 기준을 미리 알아두도록 하자. \n"
                            "식료품, 화장품, 의약품 등 소모품은 5,001엔(약 51,000원), 의류나 액세서리, 신발, 전자제품과 같은 일반 품목은 10,001엔(약 102,000원) 이상을 구매해야 세금이 면제된다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아시아' and country.get()=="일본 도쿄" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1500x1500")
        global img_도쿄3, img_도쿄4, img_도쿄5, img_도쿄6

        나라이름 = Label(travel, text="일본 도쿄", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="((쇼핑)\n"
                            "도쿄 신주쿠 다카시마야: 일본의 최고급 브랜드들을 비롯해 고급 제품을 두루 갖추고 있는 백화점이다.\n"
                            "일본산 화장품 가게들과 패션 브랜드들도 입점 되어있기 때문에 다양한 쇼핑을 즐길 수 있다.\n" 
                            "긴자거리: 세계에서 가장 고급스러운 쇼핑 지역 중 하나인 긴자. 주말 오후에는 차량 통행을 억제하여 보행자들이 더욱 편하게 쇼핑을 할 수 있다.\n"
                            "화려한 부티크 상점들에 더불어 문구 전문점이나 할인 잡화점, 장난감 가게, 기념품 가게 또한 입점해 있기 때문에 즐거운 쇼핑을 즐길 수 있다.\n\n" 
                            "((식도락)\n"
                            "1. 스시노 미도리(일본 〒107-6901 東京都Minato-ku, 港区赤坂5−3−1) \n"
                            "도쿄에서 스시라고 하면 딱 2곳이 손에 꼽히는 데, 그 중 한 곳이 미도리 스시라고 불리는 스시노 미도리이다. \n"
                            "줄서서 먹어야 할 정도로 인기가 많은 곳인데, 회가 정말 부드러워 식감이 매우 좋아 기다림의 가치가 충분히 있는 초밥이라고 한다.\n" 
                            "2. 긴자 사가야 레스토랑: \n"
                            "최고급 와규를 즐길 수 있는 긴자 최고의 맛집으로 유명한 사가야 레스토랑도 도쿄 방문시 꼭 가봐야 하는 맛집 중 하나이다. \n"
                            "입에서 살살 녹는 일본 최고급 와규가 가장 잘 나가는 메뉴이고, 음식도 맛있지만 아늑한 분위기 그리고 계절감까지 완벽한 공간을 갖추고 있어 꾸준한 인기를 끈다.\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')
        img_도쿄3 = PhotoImage(file='일본도쿄_테마별추천활동_쇼핑_백화점.gif').subsample(3)
        label_도쿄3 = Label(travel, image=img_도쿄3)
        label_도쿄3.grid(row=4, column=0, sticky='W')
        img_도쿄4 = PhotoImage(file='일본도쿄_테마별추천활동_쇼핑_긴자거리.gif').subsample(3)
        label_도쿄4 = Label(travel, image=img_도쿄4)
        label_도쿄4.grid(row=4, column=1)
        img_도쿄5 = PhotoImage(file='일본도쿄_테마별추천활동_식도락_스시.gif').subsample(3)
        label_도쿄5 = Label(travel, image=img_도쿄5)
        label_도쿄5.grid(row=5, column=0, sticky='W')
        img_도쿄6 = PhotoImage(file='일본도쿄_테마별추천활동_식도락_와규.gif').subsample(3)
        label_도쿄6 = Label(travel, image=img_도쿄6)
        label_도쿄6.grid(row=5, column=1)


    if continent.get()=='아시아' and country.get()=="일본 도쿄" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")

        나라이름 = Label(travel, text="일본 도쿄", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="1,2월 평균기온 7도 눈 옴, 3,4월 평균기온 14도 최적기 5,6월 장마촌 평균기온 22도 \n"
                            "7,8월 한여름 날씨와 장마,태풍 평균기온 30도 9,10월 비, 태풍, 선선한 날씨 평균기온 24도, \n"
                            "11,12월 단풍시즌 평균기온 13도",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')



    if continent.get()=='오세아니아' and country.get()=="호주 호바트" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x400")

        나라이름 = Label(travel, text="호주 호바트", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text= "대중 교통\n"
                            "광대한 지역의 호주는 도시마다 각기 다른 교통시스템을 갖고 있습니다.호주의 대중교통은 버스, 기차, 페리, 트램, 택시라고 할 수 있다.\n"
                            "주요 교통 법규 및 문화\n"
                            "운전석위치 및 자동차 진행 방향이 반대\n"
                            "자동차 운전석 위치가 우측에 위치하며 차선 방향도 한국과 반대\n"
                            "방향지시등 설치 위치 반대\n"
                            "대부분 조향장치(핸들) 오른쪽에 방향지시등 장치가 있어, 한국운전자들의 경우 방향지시등 대신 와이퍼를 켜는 경우 다수 발생하여,\n"
                            "안전거리가 충분하지 않을 경우 접촉사고 발생가능성 상존\n"
                            "일부 외제차는 한국과 같으므로 운전하기 전에 반드시 확인 요망\n"
                            "회전교차로(Round About) \n"
                            "회전교차로에서는 먼저 진입한 차량에게 양보하는 것이 우선임",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='오세아니아' and country.get()=="호주 호바트" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x200")

        나라이름 = Label(travel, text="호주 호바트", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="언어 : 영어",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='오세아니아' and country.get()=="호주 호바트" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1300x600")
        global img_호주_호바트2, img_호주_호바트3

        나라이름 = Label(travel, text="호주호바트", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟 : 관광", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=5,column=0, sticky='W')
        Label(travel, text="추천스팟 : 관광", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=5,column=1, sticky='W')
        
        Label(travel, text="호바트 비어\n"
                            "바다를 보면서 맛있는 음식을 먹는 곳으로 유명한 식당",bg='lightsteelblue', justify='left').grid(row=6, column=0)
        Label(travel, text="MONA\n"
                            "Museum of Old and New Art\n"
                            "세계에서 꼽히는 박물관으로 화제를 모은 예술 박물관",bg='lightsteelblue', justify='left').grid(row=6, column=1)

        
        img_호주_호바트2 = PhotoImage(file='호주 호바트_추천스팟_호바트 비어.gif').subsample(7)
        label_호주_호바트2 = Label(travel, image=img_호주_호바트2)
        label_호주_호바트2.grid(row=7, column=0, sticky='W')
        img_호주_호바트3 = PhotoImage(file='호주 호바트_추천스팟_MONA.gif').subsample(2)
        label_호주_호바트3 = Label(travel, image=img_호주_호바트3)
        label_호주_호바트3.grid(row=7, column=1)


    if continent.get()=='오세아니아' and country.get()=="호주 호바트" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x300")

        나라이름 = Label(travel, text="호주 호바트", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text= "안녕하세요, 만나서 반가워요 : 헬로우, 나이스 투 미츄\n"
                            "어떻게 지내세요 : 하우 아 유 두잉\n"
                            "얼마에요? : 하우 머치 이스 잇\n"
                            "계산서 주세요 : 빌 플리즈\n"
                            "화장실이 어디에요? : 웨어 이즈 토일렛?",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='오세아니아' and country.get()=="호주 호바트" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x400")

        나라이름 = Label(travel, text="호주 호바트", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text= "국가 남동 더웬트 강 하구에 위치한다. 도심은 더웬트 강 서안 설리반 만에 인접하고 있다.\n"
                            "시역은 더웬트 강가에서 웰링턴 산(해발 1,270m)의 구릉까지 펼쳐져 있다.\n"
                            "설리반 만 전체가 호바트 항구가 되고 있다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='오세아니아' and country.get()=="호주 호바트" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("700x400")

        나라이름 = Label(travel, text="호주 호바트", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="휴양/관광\n"
                            "호바트 비어- 바다를 보면서 맛있는 음식을 먹는 곳으로 유명한 식당\n"
                            "Museum of Old and New Art - 세계에서 꼽히는 박물관으로 화제를 모은 예술 박물관",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='오세아니아' and country.get()=="호주 호바트" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1000x500")

        나라이름 = Label(travel, text="호주 호바트", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text= "팁 문화\n"
                            "미국과는 달리 호주에서는 팁이 생활화되어 있지 않습니다.\n"
                            "다만, 호텔이나 식당 등에서 아주 만족할 만한 음식과 서비스를 받았을 때는 간혹 식당 종업원에게 약간의 팁을 주어 고마움을 표시하는 경우는 있습니다.\n"
                            "일반적 관행은 없으나, 호텔의 경우 AU $2-3, 레스토랑도 대부분 음식값의 3% 정도면 무난하다고 합니다.\n"
                            "일반문화\n" 
                            "호주인들은 약한 편을 돕는 메이트쉽(mateship)이 강하다고 합니다. 호주인들은 모든 사람들이 평등한 사회적, 종교적, 정치적, 법적 권리를 가져야 한다고 믿고 있습니다.\n"
                            "차별 금지법은 어느 누구라도 인종, 성별, 결혼 여부, 종교, 신체적 결함 때문에 차별받는 것을 방지하는 기능을 하고 있습니다.\n"
                            "일상적으로 전혀 모르는 사람이라도 지나가며 Good Day Mate! 하거나 눈인사 정도는 합니다.\n"
                            "호주인들은 전반적으로 친절한 편이라고 할 수 있으며, 낙천적인 사고와 여행을 즐기고 여유를 갖고 생활하는 자세를 갖고 있습니다.\n"
                            "호주는 비교적 직업에 귀천을 두지 않는 평등한 사회로 자신과 다른 분야에 종사하는 사람들을 인정하고 존중한다고 생각합니다.\n"
                            "따라서 부모의 직업이나 사회적 신분에 관한 질문은 삼가하는 것이 좋습니다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='오세아니아' and country.get()=="호주 호바트" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1000x500")

        나라이름 = Label(travel, text="호주 호바트", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="날씨\n"
                            "천혜의 자연 환경과 온난한 기후\n"
                            "호주는 국토가 넓기 때문에 열대기후부터 온대기후까지 지역에따라 기후 차이가 난다.\n"
                            "하지만 호주는 세계에서 가장 건조한 대륙으로 대륙 중앙부는 사막지대입니다.\n"
                            "여름은 기온이 높아도 다윈 등 노던테러토리 지역외에는 습도가 낮기 때문에 지낼만 하며, 자외선이 매우 강하여 선글래스, 선텐로션(Sun block)과 모자는 필수입니다.\n"
                            "겨울은 대부분의 지역이 낮동안에는 영상의 기온으로 일상생활에는 지장이 없으며 산간지역이나 캔버라와 같은 고지대 도시는 일교차가 심해 상대적으로 추위를 느낄 수 있습니다.\n"
                            "시드니를 비롯한 NSW지역은 생활하기 적합한 기후입니다. 다만 일 교차가 심하고 하루중에 기상 변화가 심하여 ‘하루에 사계절이 다있다’라고 표현하기도 합니다.\n"
                            "여름은 기온이 높아도 대체적으로 습도가 낮아서 지내기 좋으나 최근 습도가 높으며 기온이 올라가는 경우도 간혹 있고\n"
                            "열풍이 불면 매우 건조하고 더운 날씨가 되기도 합니다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')





    if continent.get()=='오세아니아' and country.get()=="호주 시드니" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1100x800")
        global img_시드니교통

        나라이름 = Label(travel, text="호주 시드니", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_시드니교통 = PhotoImage(file='시드니교통.gif').subsample(1)
        label_시드니교통 = Label(travel, image=img_시드니교통)
        label_시드니교통.grid(row=8)

    if continent.get()=='오세아니아' and country.get()=="호주 시드니" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x200")

        나라이름 = Label(travel, text="호주 시드니", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="언어 : 영어사용\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='오세아니아' and country.get()=="호주 시드니" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x250")

        나라이름 = Label(travel, text="호주 시드니", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="오페라 하우스, 하버 브리지, Bondi to Coogee Beach Coastal Walk 등",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='오세아니아' and country.get()=="호주 시드니" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x200")

        나라이름 = Label(travel, text="호주 시드니", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="대부분 영어를 잘 알고 있으므로 생략",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='오세아니아' and country.get()=="호주 시드니" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("950x500")
        global img_시드니지리

        나라이름 = Label(travel, text="호주 시드니", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_시드니지리 = PhotoImage(file='시드니지리.gif')
        label_시드니지리 = Label(travel, image=img_시드니지리)
        label_시드니지리.grid(row=5)


    if continent.get()=='오세아니아' and country.get()=="호주 시드니" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x600")
        global img_시드니추천1,img_시드니추천2

        나라이름 = Label(travel, text="호주 시드니", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_시드니추천1 = PhotoImage(file='시드니추천1.gif').subsample(2)
        label_시드니추천1 = Label(travel, image=img_시드니추천1)
        label_시드니추천1.grid(row=5)
        Label(travel, text="Barangaroo Foreshore Walk(산책로)",bg='lightsteelblue', justify='left').grid(row=7)

        img_시드니추천2 = PhotoImage(file='시드니추천2.gif').subsample(2)
        label_시드니추천2 = Label(travel, image=img_시드니추천2)
        label_시드니추천2.grid(row=8)
        Label(travel, text="오페라 하우스",bg='lightsteelblue', justify='left').grid(row=9)



    if continent.get()=='오세아니아' and country.get()=="호주 시드니" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("400x300")

        나라이름 = Label(travel, text="호주 시드니", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="""1. 무료 가이드북 받기
2.로밍대신 심카드 이용하기
3.택시대신 우버 이용하기
4. 팁 주지 않기""",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='오세아니아' and country.get()=="호주 시드니" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x300")

        나라이름 = Label(travel, text="호주 시드니", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="날씨 : 우리나라랑 정 반대\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')




    if continent.get()=='오세아니아' and country.get()=="뉴질랜드 웰링턴" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x200")

        나라이름 = Label(travel, text="뉴질랜드 웰링턴", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="버스\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='오세아니아' and country.get()=="뉴질랜드 웰링턴" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x200")

        나라이름 = Label(travel, text="뉴질랜드 웰링턴", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="영어, 마오리어\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='오세아니아' and country.get()=="뉴질랜드 웰링턴" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("700x400")

        나라이름 = Label(travel, text="뉴질랜드 웰링턴", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        
        나라이름 = Label(travel, text="뉴질랜드 웰링턴", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="웰링턴케이블카\n",bg='lightsteelblue', justify='left').grid(row=3, column=0, sticky='W')
        Label(travel, text="마운트빅토리아전망대\n",bg='lightsteelblue', justify='left').grid(row=3, column=1)
        global img_마운트빅토리아전망대, img_웰링턴케이블카

        img_웰링턴케이블카 = PhotoImage(file='뉴질랜드웰링턴_추천스팟_웰링턴케이블카.gif')
        label_웰링턴케이블카 = Label(travel, image=img_웰링턴케이블카)
        label_웰링턴케이블카.grid(row=4, column=0, sticky='W')

        img_마운트빅토리아전망대 = PhotoImage(file='뉴질랜드웰링턴_추천스팟_마운트빅토리아전망대.gif')
        label_마운트빅토리아전망대 = Label(travel, image=img_마운트빅토리아전망대)
        label_마운트빅토리아전망대.grid(row=4, column=1)


    if continent.get()=='오세아니아' and country.get()=="뉴질랜드 웰링턴" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x200")

        나라이름 = Label(travel, text="뉴질랜드 웰링턴", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="ka pai.카 파이:감사합니다\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='오세아니아' and country.get()=="뉴질랜드 웰링턴" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x200")

        나라이름 = Label(travel, text="뉴질랜드 웰링턴", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="뉴질랜드 북섬의 남쪽 끝\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='오세아니아' and country.get()=="뉴질랜드 웰링턴" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("700x400")

        나라이름 = Label(travel, text="뉴질랜드 웰링턴", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="웰링턴케이블카",bg='lightsteelblue', justify='left').grid(row=3, column=0, sticky='W')
        Label(travel, text="보타닉가든",bg='lightsteelblue', justify='left').grid(row=3, column=1, sticky='W')
        global img_웰링턴케이블카2, img_보타닉가든
        
        img_웰링턴케이블카2 = PhotoImage(file='뉴질랜드웰링턴_추천스팟_웰링턴케이블카.gif')
        label_웰링턴케이블카2 = Label(travel, image=img_웰링턴케이블카2)
        label_웰링턴케이블카2.grid(row=4, column=0, sticky='W')

        img_보타닉가든 = PhotoImage(file='뉴질랜드웰링턴_테마별추천활동_보타닉가든.gif')
        label_보타닉가든 = Label(travel, image=img_보타닉가든)
        label_보타닉가든.grid(row=4, column=1)

    if continent.get()=='오세아니아' and country.get()=="뉴질랜드 웰링턴" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x200")

        나라이름 = Label(travel, text="뉴질랜드 웰링턴", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="2년마다 한 번(홀수해) 열리는 쿠바스트리트카니발\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='오세아니아' and country.get()=="뉴질랜드 웰링턴" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")

        나라이름 = Label(travel, text="뉴질랜드 웰링턴", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="따뜻한 2월 평균기온이 15.7℃, 가장 추운 7월 평균기온이 7.8℃이며, 연평균기온 11.8℃, 연강수량이 1,224mm\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='오세아니아' and country.get()=="미국 괌" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("700x200")

        나라이름 = Label(travel, text="미국 괌", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="택시, 픽업서비스, 랜터카, 트롤리 버스(괌 시내만 돌아다님) 등이 존재함",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='오세아니아' and country.get()=="미국 괌" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x200")

        나라이름 = Label(travel, text="미국 괌", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="언어 : 영어",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='오세아니아' and country.get()=="미국 괌" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x200")

        나라이름 = Label(travel, text="미국 괌", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="차모로 빌리지, 스페인 광장, 파세오 공원 등\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='오세아니아' and country.get()=="미국 괌" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x200")

        나라이름 = Label(travel, text="미국 괌", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="영어는 대부분 잘 알고 있으므로 생략\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='오세아니아' and country.get()=="미국 괌" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x600")
        global img_괌지리

        나라이름 = Label(travel, text="미국 괌", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')

        img_괌지리 = PhotoImage(file='괌지리.gif')
        label_괌지리 = Label(travel, image=img_괌지리)
        label_괌지리.grid(row=8)
    if continent.get()=='오세아니아' and country.get()=="미국 괌" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1100x800")
        global img_괌추천1,img_괌추천2

        나라이름 = Label(travel, text="미국 괌", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_괌추천1 = PhotoImage(file='괌추천1.gif').subsample(2)
        label_괌추천1 = Label(travel, image=img_괌추천1)
        label_괌추천1.grid(row=4)
        Label(travel, text="스페인 광장",bg='lightsteelblue', justify='left').grid(row=5)


        img_괌추천2 = PhotoImage(file='괌추천2.gif').subsample(2)
        label_괌추천2 = Label(travel, image=img_괌추천2)
        label_괌추천2.grid(row=9)
        Label(travel, text="리티디안 비치",bg='lightsteelblue', justify='left').grid(row=10)

        Label(travel, text="""괌 음식추천""",bg='lightsteelblue', justify='left', font=11).grid(row=3,column=1)

        Label(travel, text="""괌 음식추천
1. Beachin' Shrimp (비치인쉬림프)
괌 맛집하면 1순위로 생각나는 비치인쉬림프는 투몬 시내와 PIC 건너편까지
모두 2개의 지점을 보유하고 있는 인기만점 맛집입니다!
코코넛에 샤워한 코코넛 새우튀김과 스페인 타파스 요리인 감바스가 이 곳의 최고 메뉴라고 하는데요~
한국인 관광객들에게는 밥과 함께 먹을 수 있는 엔젤 헤어 파스타도 유명하다고 하니,
뜨끈한 국물이 생각나시는 분들께 안성맞춤입니다!
2. Pika's Cafe (피카스카페)
투몬샌즈 근처에 위치하고 있는 피카스 카페는 관광객들보다, 괌 현지인들의 맛집으로 유명합니다.
친절하고 유머감각이 뛰어난 직원분들 덕분에 바로 기분이 좋아지는 이 곳!
크림리조또랑 비슷한 느낌의 로코모코가 인기메뉴이며,
자극적이지 않아 괌의 100%를 입 안에 가득 느끼실 수 있습니다.
3. Jamaican Grill (자메이칸 그릴)
색다른 자메이카 분위기를 100% 느낄 수 있는 자메이칸 그릴은
PIC호텔 건너편 건물 2층에 위치하고 있는 접근성 최강인 맛집입니다.
괌 현지인 맛집인 이 곳은 단짠단짠 양념이 가득 베인 립으로 유명한 곳입니다. """,bg='lightsteelblue', justify='left').grid(row=4,column=1)
        

    if continent.get()=='오세아니아' and country.get()=="미국 괌" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x200")

        나라이름 = Label(travel, text="미국 괌", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="없음",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='오세아니아' and country.get()=="미국 괌" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("700x200")

        나라이름 = Label(travel, text="미국 괌", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="날씨 :  연평균 25~ 30, 고온 다습\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')


    if continent.get()=='아프리카' and country.get()=="모리셔스" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x400")

        나라이름 = Label(travel, text="모리셔스", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="주요 교통 법규 및 문화\n"
                            "자동차 운전석 위치가 오른쪽이며, 신호체계는 한국과 같으나, 원형 로터리에서 진입 된 차량이 우선권을 가집니다.\n"
                            "모터웨이(high way) 운행 시에는 좌측 차로로 운행해야 합니다. 추월시에만 우측 차선을 이용 합니다.\n"
                            "면허증은 국제면허증이 인정 되며, 꼭 운전을 해야 할 경우면 여행객에는 관대한 편이라 한국 운전 면허증만으로도 운전이 가능 할 수 있습니다.\n"
                            "모리셔스 현지인들의 운전이 약간 거친 편입니다. 양보 운전을 권고드립니다.\n"
                            "한국에서는 전조등을 밝게 깜박거리는 신호가 본인이 우선 진입 하겠다는 신호이지만, 모리셔스는 이와 반대입니다.\n"
                            "상대방에게 먼저 가라고 할 때 전조등을 밝게 깜박거리기 때문에 사고 가 날수 있습니다.\n"
                            "교통경찰은 아주 드물게 금전을 요구하는 경우도 있지만 관광객에게는 대체적으로 친절 합니다.\n"
                            "렌트 차량은 차량 앞 번호판 색깔 이 노란색으로 구분이 됩니다. 현지 교통경찰들은 관광객이 운전하는 렌트카에는 호의를 베풀어 주는 편입니다.\n"
                            "차량 랜트 업체는 관광 국가답게 많습니다. 한국 면허증으로 렌트가 가능하고 현지의 지인을 통하거나 관광 안내원에게 소개를 받는 편이 좋습니다.\n"
                            "현지 ABC 같은 업체는 규모가 큰 렌트 업체이지만, 계약 취소가 불가한 점이 있습니다.\n"
                            "과속 카메라가 곳곳에 설치되어 있습니다. 구간에 따라 60km, 80km, 110km 단위로 단속을 합니다.\n"
                            "속도위반시 과태료는 2,000루피(약 7만원) 정도가 부과 됩니다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아프리카' and country.get()=="모리셔스" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x200")

        나라이름 = Label(travel, text="모리셔스", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="언어 : 영어(공식어), 불어, 크레올어, 힌디어",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아프리카' and country.get()=="모리셔스" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1200x500")
        global img_모리셔스2, img_모리셔스3, img_모리셔스4

        나라이름 = Label(travel, text="모리셔스", font=('양재참숯체B',30),bg='lightsteelblue', justify='left',fg="darkblue").grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟 : 관광/휴양", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=5,column=0, sticky='W')
        Label(travel, text="추천스팟 : 관광/휴양", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=5,column=1, sticky='W')
        Label(travel, text="추천스팟 : 관광/휴양", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=8,column=0, sticky='W')
        
        Label(travel, text="카젤라 파크\n"
                            "한국의 사파리와 같은 곳\n"
                            "다양한 테마가 있으며 사자와 손을 잡을 수 있는 기회도 있다. \n"
                            "흔치 않은 동물들과의 기념사진은 덤",bg='lightsteelblue', justify='left').grid(row=6, column=0)
        Label(travel, text="팜플무스 식물원\n"
                            "모리셔스의 국립 식물원으로 과거 대영제국의 통치를 받을 때 조성된 곳이다.\n"
                            "전 세계에 있는 다양한 식물들을 모아 야외 식물원을 만든 것이다.",bg='lightsteelblue', justify='left').grid(row=6, column=1)
        Label(travel, text="일로셰프 섬\n"
                            "신혼여행의 순위안에 드는 곳으로 다양한 활동을 할 수 있다.\n"
                            "짚라인을 통해 섬에 들어가고 카누, 요트를 타며 낭만을 누릴 수 있다. ",bg='lightsteelblue', justify='left').grid(row=9, column=0)

        
        img_모리셔스2 = PhotoImage(file='모리셔스_추천스팟_카젤라 파크.gif').subsample(14)
        label_모리셔스2 = Label(travel, image=img_모리셔스2)
        label_모리셔스2.grid(row=7, column=0, sticky='W')
        img_모리셔스3 = PhotoImage(file='모리셔스_추천스팟_팜플무스 식물원.gif').subsample(14)
        label_모리셔스3 = Label(travel, image=img_모리셔스3)
        label_모리셔스3.grid(row=7, column=1)
        img_모리셔스4 = PhotoImage(file='모리셔스_추천스팟_일로셰프 섬.gif').subsample(2)
        label_모리셔스4 = Label(travel, image=img_모리셔스4)
        label_모리셔스4.grid(row=10, column=0)


    if continent.get()=='아프리카' and country.get()=="모리셔스" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x300")

        나라이름 = Label(travel, text="모리셔스", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text= "안녕: 잠보\n"
                            "어떻게 지냈어? : 하바리 간\n"
                            "아무 문제 없어~ : 하쿠나마 타타\n"
                            "감사합니다 : 아산티 사나\n"
                            "안녕(헤어질 때) : 카와히리",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아프리카' and country.get()=="모리셔스" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x400")

        나라이름 = Label(travel, text="모리셔스", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="모리셔스는 과거 화산 폭발로 인해 생성된 섬으로 추정되며 대략 800~1,000만 년 정도에 생긴 것으로 보인다.\n"
                            "그러나 지금에 와서는 화산 활동이 전혀 나타나지 않고 있다.\n"
                            "모리셔스 섬은 중앙 평원으로 이뤄져 있고 남서쪽에 가장 높은 봉우리인 Piton de la Petite Rivière Noire가 828 m로 솟아 있다.\n"
                            "수도인 포트 루이스는 북서쪽에 있으며 다른 주요 거점들도 다 이 부근에 있다.\n"
                            "자연 경관으로 유명한 모리셔스는 작가 마크 트웨인이 여행을 하면서 영감을 얻었다고 전해지기도 한다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아프리카' and country.get()=="모리셔스" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("500x400")

        나라이름 = Label(travel, text="모리셔스", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="휴양/관광\n"
                            "카젤라 파크\n"
                            "팜플무스 식물원 - 거대한 식물원으로 다양한 희귀 식물 존\n"
                            "일로셰프 섬 - 요트체험을 할 수 있는 \n"
                            "포트루이스",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아프리카' and country.get()=="모리셔스" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x500")

        나라이름 = Label(travel, text="모리셔스", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text= """일반 문화
인적 구성이 인도계(68%), Creole 27%, 중국계 3%, 프랑스계 2% 등 다양한 만큼 문화도 힌두, 이슬람, 중화 문화가 혼합되어 있습니다.
라마단 축제는 2~10일간 계속되기도 합니다.
경찰관이 가끔 외국인들에게 신분증 제시를 요구하기도 합니다.
따라서 여권, 운전면허증 등 원본은 안전한 금고에 보관을 하더라도 복사본을 소지해야 합니다.
팁 문화
호텔이나 음식점에서 요금의 10%가 서비스료로 부과되므로 별도의 팁을 줄 필요는 없으나, 잔돈 등 작은 돈을 주기도 합니다.""",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아프리카' and country.get()=="모리셔스" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x300")

        나라이름 = Label(travel, text="모리셔스", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="대개 열대기후이며 남동 무역풍의 영향을 받는다. 덥고 건조한 겨울이 11월에서 5월까지 이어지고 무덥고 습한 여름이 나머지 기간에 해당된다.\n"
                            "사이클론의 영향이 4월에서 11월 전까지 나타나기도 한다.",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')



    if continent.get()=='아프리카' and country.get()=="이집트 카이로" and 교통1.get()==1:
        travel= Toplevel(window)
        travel.geometry("700x600")
        global img_카이로교통

        나라이름 = Label(travel, text="이집트 카이로", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="교통정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_카이로교통 = PhotoImage(file='카이로교통.gif').subsample(2)
        label_카이로교통 = Label(travel, image=img_카이로교통)
        label_카이로교통.grid(row=3)

    if continent.get()=='아프리카' and country.get()=="이집트 카이로" and 언어1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x200")

        나라이름 = Label(travel, text="이집트 카이로", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="언어정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="언어 : 아랍어",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아프리카' and country.get()=="이집트 카이로" and 추천스팟1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x200")

        나라이름 = Label(travel, text="이집트 카이로", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="추천스팟", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="이집트 유물 박물관\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    if continent.get()=='아프리카' and country.get()=="이집트 카이로" and 필수어휘1.get()==1:
        travel= Toplevel(window)
        travel.geometry("800x900")
        global img_카이로어휘

        나라이름 = Label(travel, text="이집트 카이로", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="필수어휘", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_카이로어휘 = PhotoImage(file='카이로어휘.gif').subsample(1)
        label_카이로어휘 = Label(travel, image=img_카이로어휘)
        label_카이로어휘.grid(row=3)

    if continent.get()=='아프리카' and country.get()=="이집트 카이로" and 지리정보1.get()==1:
        travel= Toplevel(window)
        travel.geometry("1100x500")
        global img_카이로지리

        나라이름 = Label(travel, text="이집트 카이로", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="지리정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_카이로지리 = PhotoImage(file='카이로지리.gif').subsample(1)
        label_카이로지리 = Label(travel, image=img_카이로지리)
        label_카이로지리.grid(row=9)

    if continent.get()=='아프리카' and country.get()=="이집트 카이로" and 테마별추천활동1.get()==1:
        travel= Toplevel(window)
        travel.geometry("700x900")
        global img_카이로추천,img_카이로추천2

        나라이름 = Label(travel, text="이집트 카이로", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="테마별추천활동", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="이집트 유물 박물관\n",bg='lightsteelblue', justify='left').grid(row=3)
        img_카이로추천 = PhotoImage(file='카이로추천.gif').subsample(2)
        label_카이로추천 = Label(travel, image=img_카이로추천)
        label_카이로추천.grid(row=4)

        img_카이로추천2 = PhotoImage(file='카이로추천2.gif').subsample(2)
        label_카이로추천2 = Label(travel, image=img_카이로추천2)
        label_카이로추천2.grid(row=6)
        Label(travel, text="쿠사리(추천음식)\n",bg='lightsteelblue', justify='left').grid(row=5,column=0)

    if continent.get()=='아프리카' and country.get()=="이집트 카이로" and 개인적꿀팁1.get()==1:
        travel= Toplevel(window)
        travel.geometry("700x500")
        global img_카이로꿀팁

        나라이름 = Label(travel, text="이집트 카이로", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="개인적꿀팁", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        img_카이로꿀팁 = PhotoImage(file='카이로꿀팁.gif').subsample(2)
        label_카이로꿀팁 = Label(travel, image=img_카이로꿀팁)
        label_카이로꿀팁.grid(row=3)

    if continent.get()=='아프리카' and country.get()=="이집트 카이로" and 날씨1.get()==1:
        travel= Toplevel(window)
        travel.geometry("600x300")

        나라이름 = Label(travel, text="이집트 카이로", font=('양재참숯체B',30),bg='lightsteelblue', justify='left').grid(row=0, column=0, sticky='W')
        Label(travel, text="날씨정보", font=('양재참숯체B', 15), fg="blue",bg='lightsteelblue', justify='left').grid(row=2,column=0, sticky='W')
        Label(travel, text="날씨 : 11~ 3월 : 봄가을 날씨, 4~10월 : 더움\n",bg='lightsteelblue', justify='left').grid(row=3, sticky='W')

    travel.config(bg="lightsteelblue")
    
def lists():#여행지 추천에서 추천여행지 목록이 뜨도록하는 코드
    lists_box=Toplevel(window)
    lists_box.geometry("400x300")
    Label(lists_box, text="추천여행지", font=('양재참숯체B',16), fg="blue", bg="cornflowerblue").grid(row=1)

    if (var1.get() ==1 or var1.get()==0) and var16.get()==1 and 경1.get()==1:
        해당없음=Label(lists_box, text="◎해당없음", bg="lightblue", font=("양재참숯체B",11))
        아프리카5시간=[]
        if var21.get()==1:
            아프리카5시간.extend([해당없음])
        if var22.get()==1:
            아프리카5시간.extend([해당없음])
        if var23.get()==1:
            아프리카5시간.extend([해당없음])
        if var24.get()==1:
            아프리카5시간.extend([해당없음])
        if var25.get()==1:
            아프리카5시간.extend([해당없음])
        tmp_set = set(아프리카5시간)
        아프리카5시간 = list(tmp_set)
        for i, country in enumerate(아프리카5시간):
            country.grid(row=i+612,sticky='W')

    if (var1.get() ==1 or var1.get()==0) and (var16.get()==1) and (경2.get()==1):
        해당없음=Label(lists_box, text="◎해당없음", bg="lightblue", font=("양재참숯체B",11))
        아프리카510시간=[]
        if var21.get()==1:
            아프리카510시간.extend([해당없음])
        if var22.get()==1:
            아프리카510시간.extend([해당없음])
        if var23.get()==1:
            아프리카510시간.extend([해당없음])
        if var24.get()==1:
            아프리카510시간.extend([해당없음])
        if var25.get()==1:
            아프리카510시간.extend([해당없음])
        tmp_set = set(아프리카510시간)
        아프리카510시간 = list(tmp_set)
        for i, country in enumerate(아프리카510시간):
            country.grid(row=i+602,sticky='W')

    if (var1.get() ==1 or var1.get()==0) and (var16.get()==1) and (경3.get()==1):
        해당없음=Label(lists_box, text="◎해당없음", bg="lightblue", font=("양재참숯체B",11))
        카이로=Label(lists_box, text="카이로", bg="lightblue", font=("양재참숯체B",11))
        아프리카1020시간=[]
        if var21.get()==1:
            아프리카1020시간.extend([해당없음])
        if var22.get()==1:
            아프리카1020시간.extend([해당없음])
        if var23.get()==1:
            아프리카1020시간.extend([카이로])
        if var24.get()==1:
            아프리카1020시간.extend([카이로])
        if var25.get()==1:
            아프리카1020시간.extend([해당없음])
        tmp_set = set(아프리카510시간)
        아프리카1020시간 = list(tmp_set)
        for i, country in enumerate(아프리카1020시간):
            country.grid(row=i+592,sticky='W')


    if (var1.get() ==1 or var1.get()==0) and (var16.get()==1) and (경4.get()==1):
        해당없음=Label(lists_box, text="◎해당없음", bg="lightblue", font=("양재참숯체B",11))
        모리셔스=Lable(lists_box, text="모리셔스", bg="lightblue", font=("양재참숯체B",11))
        아프리카20시간=[]
        if var21.get()==1:
            아프리카20시간.extend([해당없음])
        if var22.get()==1:
            아프리카20시간.extend([모리셔스])
        if var23.get()==1:
            아프리카20시간.extend([모리셔스])
        if var24.get()==1:
            아프리카20시간.extend([모리셔스])
        if var25.get()==1:
            아프리카20시간.extend([해당없음])
        tmp_set = set(아프리카20시간)
        아프리카510시간 = list(tmp_set)
        for i, country in enumerate(아프리카20시간):
            country.grid(row=i+582,sticky='W')


    if (var1.get() ==1 or var1.get()==0) and (var17.get()==1) and (경1.get()==1):
        해당없음=Label(lists_box, text="◎해당없음", bg="lightblue", font=("양재참숯체B",11))
        북아메리카5시간=[]
        if var21.get()==1:
            북아메리카5시간.extend([해당없음])
        if var22.get()==1:
            북아메리카5시간.extend([해당없음])
        if var23.get()==1:
            북아메리카5시간.extend([해당없음])
        if var24.get()==1:
            북아메리카5시간.extend([해당없음])
        if var25.get()==1:
            북아메리카5시간.extend([해당없음])
        tmp_set = set(북아메리카5시간)
        북아메리카5시간 = list(tmp_set)
        for i, country in enumerate(북아메리카5시간):
            country.grid(row=i+572,sticky='W')

    if (var1.get() ==1 or var1.get()==0) and (var17.get()==1) and (경2.get()==1):
        해당없음=Label(lists_box, text="◎해당없음", bg="lightblue", font=("양재참숯체B",11))
        북아메리카510시간=[]
        if var21.get()==1:
            북아메리카510시간.extend([해당없음])
        if var22.get()==1:
            북아메리카510시간.extend([해당없음])
        if var23.get()==1:
            북아메리카510시간.extend([해당없음])
        if var24.get()==1:
            북아메리카510시간.extend([해당없음])
        if var25.get()==1:
            북아메리카510시간.extend([해당없음])
        tmp_set = set(북아메리카510시간)
        북아메리카510시간 = list(tmp_set)
        for i, country in enumerate(북아메리카510시간):
            country.grid(row=i+562,sticky='W')


    if (var1.get() ==1 or var1.get()==0) and (var17.get()==1) and (경3.get()==1):
        해당없음=Label(lists_box, text="◎해당없음", bg="lightblue", font=("양재참숯체B",11))
        아바나=Label(lists_box, text="◎아바나", bg="lightblue", font=("양재참숯체B",11))
        로스엔젤로스=Label(lists_box, text="◎로스엔젤로스", bg="lightblue", font=("양재참숯체B",11))
        뉴욕=Label(lists_box, text="◎뉴욕", bg="lightblue", font=("양재참숯체B",11))
        벤쿠버=Label(lists_box, text="◎벤쿠버", bg="lightblue", font=("양재참숯체B",11))
        북아메리카1020시간=[]
        if var21.get()==1:
            북아메리카1020시간.extend([뉴욕, 로스엔젤로스])
        if var22.get()==1:
            북아메리카1020시간.extend([아바나, 벤쿠버])
        if var23.get()==1:
            북아메리카1020시간.extend([뉴욕, 로스엔젤로스, 아바나, 벤쿠버])
        if var24.get()==1:
            북아메리카1020시간.extend([뉴욕, 벤쿠버])
        if var25.get()==1:
            북아메리카1020시간.extend([해당없음])
        tmp_set = set(북아메리카1020시간)
        북아메리카1020시간 = list(tmp_set)
        for i, country in enumerate(북아메리카1020시간):
            country.grid(row=i+552,sticky='W')

    if (var1.get() ==1 or var1.get()==0) and (var17.get()==1) and (경4.get()==1):
        해당없음=Label(lists_box, text="◎해당없음", bg="lightblue", font=("양재참숯체B",11))
        상파울로=Label(lists_box, text="상파울로", bg="lightblue", font=("양재참숯체B",11))
        산티아고=Label(lists_box, text="산티아고", bg="lightblue", font=("양재참숯체B",11))
        북아메리카20시간=[]
        if var21.get()==1:
            북아메리카20시간.extend([해당없음])
        if var22.get()==1:
            북아메리카20시간.extend([상파울로])
        if var23.get()==1:
            북아메리카20시간.extend([상파울로, 산티아고])
        if var24.get()==1:
            북아메리카20시간.extend([산티아고])
        if var25.get()==1:
            북아메리카20시간.extend([해당없음])
        tmp_set = set(북아메리카20시간)
        북아메리카20시간 = list(tmp_set)
        for i, country in enumerate(북아메리카20시간):
            country.grid(row=i+542,sticky='W')


    if (var1.get() ==1 or var1.get()==0) and (var18.get()==1) and (경1.get()==1):
        해당없음=Label(lists_box, text="◎해당없음", bg="lightblue", font=("양재참숯체B",11))
        남아메리카5시간=[]
        if var21.get()==1:
            남아메리카5시간.extend([해당없음])
        if var22.get()==1:
            남아메리카5시간.extend([해당없음])
        if var23.get()==1:
            남아메리카5시간.extend([해당없음])
        if var24.get()==1:
            남아메리카5시간.extend([해당없음])
        if var25.get()==1:
            남아메리카5시간.extend([해당없음])
        tmp_set = set(남아메리카5시간)
        남아메리카5시간 = list(tmp_set)
        for i, country in enumerate(남아메리카5시간):
            country.grid(row=i+532,sticky='W')

    if (var1.get() ==1 or var1.get()==0) and (var18.get()==1) and (경2.get()==1):
        해당없음=Label(lists_box, text="◎해당없음", bg="lightblue", font=("양재참숯체B",11))
        남아메리카510시간=[]
        if var21.get()==1:
            남아메리카510시간.extend([해당없음])
        if var22.get()==1:
            남아메리카510시간.extend([해당없음])
        if var23.get()==1:
            남아메리카510시간.extend([해당없음])
        if var24.get()==1:
            남아메리카510시간.extend([해당없음])
        if var25.get()==1:
            남아메리카510시간.extend([해당없음])
        tmp_set = set(남아메리카510시간)
        남아메리카510시간 = list(tmp_set)
        for i, country in enumerate(남아메리카510시간):
            country.grid(row=i+522,sticky='W')

    if (var1.get() ==1 or var1.get()==0) and (var18.get()==1) and (경3.get()==1):
        해당없음=Label(lists_box, text="◎해당없음", bg="lightblue", font=("양재참숯체B",11))
        남아메리카1020시간=[]
        if var21.get()==1:
            남아메리카1020시간.extend([해당없음])
        if var22.get()==1:
            남아메리카1020시간.extend([해당없음])
        if var23.get()==1:
            남아메리카1020시간.extend([해당없음])
        if var24.get()==1:
            남아메리카1020시간.extend([해당없음])
        if var25.get()==1:
            남아메리카1020시간.extend([해당없음])
        tmp_set = set(남아메리카1020시간)
        남아메리카1020시간 = list(tmp_set)
        for i, country in enumerate(남아메리카1020시간):
            country.grid(row=i+512,sticky='W')


    if (var1.get() ==1 or var1.get()==0) and (var18.get()==1) and (경4.get()==1):
        해당없음=Label(lists_box, text="◎해당없음", bg="lightblue", font=("양재참숯체B",11))
        남아메리카20시간=[]
        if var21.get()==1:
            남아메리카20시간.extend([해당없음])
        if var22.get()==1:
            남아메리카20시간.extend([해당없음])
        if var23.get()==1:
            남아메리카20시간.extend([해당없음])
        if var24.get()==1:
            남아메리카20시간.extend([해당없음])
        if var25.get()==1:
            남아메리카20시간.extend([해당없음])
        tmp_set = set(남아메리카20시간)
        남아메리카20시간 = list(tmp_set)
        for i, country in enumerate(남아메리카20시간):
            country.grid(row=i+502,sticky='W')
    

    if (var1.get() ==1 or var1.get()==0) and (var17.get()==1) and (경3.get()==1):
        아바나=Label(lists_box, text="◎쿠바 하바나(북아메리카)", bg="lightblue", font=("양재참숯체B",11))
        뉴욕=Label(lists_box, text="◎미국 뉴욕(북아메리카)", bg="lightblue", font=("양재참숯체B",11))
        밴쿠버=Label(lists_box, text="◎캐나다 밴쿠버(북아메리카)", bg="lightblue", font=("양재참숯체B",11))
        로스엔젤로스=Label(lists_box, text="◎미국 로스엔젤로스(LA/북아메리카)", bg="lightblue", font=("양재참숯체B",11))
        북아메리카1020시간=[]
        if var21.get()==1:
            북아메리카1020시간.extend([뉴욕, 로스엔젤로스])
        if var22.get()==1:
            북아메리카1020시간.extend([아바나, 밴쿠버])
        if var23.get()==1:
            북아메리카1020시간.extend([아바나, 뉴욕, 밴쿠버, 로스엔젤로스])
        if var24.get()==1:
            북아메리카1020시간.extend([뉴욕, 밴쿠버])
        if var25.get()==1:
            북아메리카1020시간.extend([])
        tmp_set = set(북아메리카1020시간)
        북아메리카1020시간 = list(tmp_set)
        for i, country in enumerate(북아메리카1020시간):
            country.grid(row=i+4, sticky='W')

    


    if (var1.get() ==1 or var1.get()==0) and (var17.get()==1) and (경4.get()==1):
        상파울로=Label(lists_box, text="◎브라질 상파울로(남아메리카)", bg="lightblue", font=("양재참숯체B",11))
        산티아고=Label(lists_box, text="◎칠레 산티아고(남아메리카)", bg="lightblue", font=("양재참숯체B",11))
        남아메리카20시간=[]
        if var21.get()==1:
            남아메리카20시간.extend([])
        if var22.get()==1:
            남아메리카20시간.extend([상파울로])
        if var23.get()==1:
            남아메리카20시간.extend([상파울로, 산티아고])
        if var24.get()==1:
            남아메리카20시간.extend([산티아고])
        if var25.get()==1:
            남아메리카20시간.extend([])
        tmp_set = set(남아메리카20시간)
        남아메리카20시간 = list(tmp_set)
        for i, country in enumerate(남아메리카20시간):
            country.grid(row=i+14, sticky='W')


    if (var1.get() ==1 or var1.get()==0) and (var14.get()==1) and (경1.get()==1):
        마카오=Label(lists_box, text="◎중국 마카오(아시아)", bg="lightblue", font=("양재참숯체B",11))
        홍콩=Label(lists_box, text="◎홍콩(아시아)", bg="lightblue", font=("양재참숯체B",11))
        상하이=Label(lists_box, text="◎중국 상하이(아시아)", bg="lightblue", font=("양재참숯체B",11))
        도쿄=Label(lists_box, text="◎일본 도쿄(아시아)", bg="lightblue", font=("양재참숯체B",11))
        오사카=Label(lists_box, text="◎일본 오사카(아시아)", bg="lightblue", font=("양재참숯체B",11))
        아시아5시간=[]
        if var21.get()==1:
            아시아5시간.extend([홍콩, 도쿄])
        if var22.get()==1:
            아시아5시간.extend([상하이, 오사카])
        if var23.get()==1:
            아시아5시간.extend([마카오, 홍콩, 상하이, 오사카])
        if var24.get()==1:
            아시아5시간.extend([마카오, 홍콩, 상하이, 도쿄, 오사카])
        if var25.get()==1:
            아시아5시간.extend([마카오, 오사카])
        tmp_set = set(아시아5시간)
        아시아5시간 = list(tmp_set)
        for i, country in enumerate(아시아5시간):
            country.grid(row=i+22, sticky='W')

    if (var1.get() ==1 or var1.get()==0) and (var14.get()==1) and (경2.get()==1):
        루앙프라방=Label(lists_box, text="◎라오스 루앙프라방(아시아)", bg="lightblue", font=("양재참숯체B",11))
        발리=Label(lists_box, text="◎인도네시아 발리(아시아)", bg="lightblue", font=("양재참숯체B",11))
        싱가포르=Label(lists_box, text="◎싱가포르공화국(아시아)", bg="lightblue", font=("양재참숯체B",11))
        방콕=Label(lists_box, text="◎태국 방콕(아시아)", bg="lightblue", font=("양재참숯체B",11))
        다낭=Label(lists_box, text="◎베트남 다낭(아시아)", bg="lightblue", font=("양재참숯체B",11))
        아시아510시간=[]
        if var21.get()==1:
            아시아510시간.extend([방콕, 싱가포르])
        if var22.get()==1:
            아시아510시간.extend([루앙프라방, 싱가포르])
        if var23.get()==1:
            아시아510시간.extend([루앙프라방, 발리, 싱가포르, 방콕, 다낭])
        if var24.get()==1:
            아시아510시간.extend([루앙프라방, 발리, 싱가포르, 방콕, 다낭])
        if var25.get()==1:
            아시아510시간.extend([다낭, 발리, 싱가포르])
        tmp_set = set(아시아510시간)
        아시아510시간 = list(tmp_set)
        for i, country in enumerate(아시아510시간):
            country.grid(row=i+262, sticky='W')


    if (var1.get() ==1 or var1.get()==0) and (var14.get()==1) and (경3.get()==1):
        몰디브=Label(lists_box, text="◎몰디브(아시아)", bg="lightblue", font=("양재참숯체B",11))
        두바이=Label(lists_box, text="◎아랍에미리트 두바이(아시아)", bg="lightblue", font=("양재참숯체B",11))
        안탈리아=Label(lists_box, text="◎터키 안탈리아(아시아)", bg="lightblue", font=("양재참숯체B",11))
        아시아1020시간=[]
        if var21.get()==1:
            아시아1020시간.extend([두바이])
        if var22.get()==1:
            아시아1020시간.extend([두바이, 몰디브])
        if var23.get()==1:
            아시아1020시간.extend([두바이, 안탈리아])
        if var24.get()==1:
            아시아1020시간.extend([두바이, 몰디브, 안탈리아])
        if var25.get()==1:
            아시아1020시간.extend([몰디브, 안탈리아])
        tmp_set = set(아시아1020시간)
        아시아1020시간 = list(tmp_set)
        for i, country in enumerate(아시아1020시간):
            country.grid(row=i+52, sticky='W')

    if (var1.get() ==1 or var1.get()==0) and (var14.get()==1) and (경4.get()==1):
        해당없음=Label(lists_box, text="◎해당없음", bg="lightblue", font=("양재참숯체B",11))
        아시아20시간=[]
        if var21.get()==1:
            아시아20시간.extend([해당없음])
        if var22.get()==1:
            아시아20시간.extend([해당없음])
        if var23.get()==1:
            아시아20시간.extend([해당없음])
        if var24.get()==1:
            아시아20시간.extend([해당없음])
        if var25.get()==1:
            아시아20시간.extend([해당없음])
        tmp_set = set(아시아20시간)
        아시아20시간 = list(tmp_set)
        for i, country in enumerate(아시아20시간):
            country.grid(row=i+252, sticky='W')
            
    if (var1.get() ==1 or var1.get()==0) and (var15.get()==1) and (경1.get()==1):
        괌=Label(lists_box, text="◎미국 괌(오세아니아)", bg="lightblue", font=("양재참숯체B",11))
        코로르=Label(lists_box, text="◎팔라우 코로르(오세아니아)", bg="lightblue", font=("양재참숯체B",11))
        오세아니아5시간=[]
        if var21.get()==1:
            오세아니아5시간.extend([코로르])
        if var22.get()==1:
            오세아니아5시간.extend([괌, 코로르])
        if var23.get()==1:
            오세아니아5시간.extend([괌, 코로르])
        if var24.get()==1:
            오세아니아5시간.extend([괌, 코로르])
        if var25.get()==1:
            오세아니아5시간.extend([괌, 코로르])
        tmp_set = set(오세아니아5시간)
        오세아니아5시간 = list(tmp_set)
        for i, country in enumerate(오세아니아5시간):
            country.grid(row=i+32, sticky='W')

    if (var1.get() ==1 or var1.get()==0) and (var15.get()==1) and (경2.get()==1):
        브리즈번=Label(lists_box, text="◎호주 브리즈번(오세아니아)", bg="lightblue", font=("양재참숯체B",11))
        오세아니아510시간=[]
        if var21.get()==1:
            오세아니아510시간.extend([브리즈번])
        if var22.get()==1:
            오세아니아510시간.extend([브리즈번])
        if var23.get()==1:
            오세아니아510시간.extend([브리즈번])
        if var24.get()==1:
            오세아니아510시간.extend([브리즈번])
        if var25.get()==1:
            오세아니아510시간.extend([브리즈번])
        tmp_set = set(오세아니아510시간)
        오세아니아510시간 = list(tmp_set)
        for i, country in enumerate(오세아니아510시간):
            country.grid(row=i+242, sticky='W')


    if (var1.get() ==1 or var1.get()==0) and (var15.get()==1) and (경3.get()==1):
        시드니=Label(lists_box, text="◎호주 시드니(오세아니아)", bg="lightblue", font=("양재참숯체B",11))
        웰링턴=Label(lists_box, text="◎뉴질랜드 웰링턴(오세아니아)", bg="lightblue", font=("양재참숯체B",11))
        호바트=Label(lists_box, text="◎호주 호바트(오세아니아)", bg="lightblue", font=("양재참숯체B",11))
        애들레이드=Label(lists_box, text="◎호주 애들레이드(오세아니아)", bg="lightblue", font=("양재참숯체B",11))
        오세아니아1020시간=[]
        if var21.get()==1:
            오세아니아1020시간.extend([애들레이드])
        if var22.get()==1:
            오세아니아1020시간.extend([시드니, 웰링턴, 호바트, 애들레이드])
        if var23.get()==1:
            오세아니아1020시간.extend([시드니, 웰링턴, 호바트, 애들레이드])
        if var24.get()==1:
            오세아니아1020시간.extend([시드니, 웰링턴, 호바트, 애들레이드])
        if var25.get()==1:
            오세아니아1020시간.extend([애들레이드])
        tmp_set = set(오세아니아1020시간)
        오세아니아1020시간 = list(tmp_set)
        for i, country in enumerate(오세아니아1020시간):
            country.grid(row=i+42, sticky='W')

    if (var1.get() ==1 or var1.get()==0) and (var15.get()==1) and (경4.get()==1):
        해당없음=Label(lists_box, text="◎해당없음", bg="lightblue", font=("양재참숯체B",11))
        오세아니아20시간=[]
        if var21.get()==1:
            오세아니아20시간.extend([해당없음])
        if var22.get()==1:
            오세아니아20시간.extend([해당없음])
        if var23.get()==1:
            오세아니아20시간.extend([해당없음])
        if var24.get()==1:
            오세아니아20시간.extend([해당없음])
        if var25.get()==1:
            오세아니아20시간.extend([해당없음])
        tmp_set = set(오세아니아20시간)
        오세아니아20시간 = list(tmp_set)
        for i, country in enumerate(오세아니아20시간):
            country.grid(row=i+52, sticky='W')

    if (var1.get() ==1 or var1.get()==0) and (var13.get()==1) and (경1.get()==1):
        해당없음=Label(lists_box, text="◎해당없음", bg="lightblue", font=("양재참숯체B",11))
        유럽5시간=[]
        if var21.get()==1:
            유럽5시간.extend([해당없음])
        if var22.get()==1:
            유럽5시간.extend([해당없음])
        if var23.get()==1:
            유럽5시간.extend([해당없음])
        if var24.get()==1:
            유럽5시간.extend([해당없음])
        if var25.get()==1:
            유럽5시간.extend([해당없음])
        tmp_set = set(유럽5시간)
        유럽5시간 = list(tmp_set)
        for i, country in enumerate(유럽5시간):
            country.grid(row=i+162, sticky='W')

    if (var1.get() ==1 or var1.get()==0) and (var13.get()==1) and (경2.get()==1):
        헬싱키=Label(lists_box, text="◎핀란드 헬싱키(유럽)", bg="lightblue", font=("양재참숯체B",11))
        유럽510시간=[]
        if var21.get()==1:
            유럽510시간.extend([헬싱키])
        if var22.get()==1:
            유럽510시간.extend([헬싱키])
        if var23.get()==1:
            유럽510시간.extend([헬싱키])
        if var24.get()==1:
            유럽510시간.extend([헬싱키])
        if var25.get()==1:
            유럽510시간.extend([헬싱키])
        tmp_set = set(유럽510시간)
        유럽510시간 = list(tmp_set)
        for i, country in enumerate(유럽510시간):
            country.grid(row=i+102, sticky='W')

    if (var1.get() ==1 or var1.get()==0) and (var13.get()==1) and (경3.get()==1):
        마요르카=Label(lists_box, text="◎스페인 마요르카(유럽)", bg="lightblue", font=("양재참숯체B",11))
        몰타=Label(lists_box, text="◎몰타(유럽) ", bg="lightblue", font=("양재참숯체B",11))
        런던=Label(lists_box, text="◎영국 런던(유럽)", bg="lightblue", font=("양재참숯체B",11))
        파리=Label(lists_box, text="◎프랑스 파리(유럽)", bg="lightblue", font=("양재참숯체B",11))
        로마=Label(lists_box, text="◎이탈리아 로마(유럽)", bg="lightblue", font=("양재참숯체B",11))
        프라하=Label(lists_box, text="◎체코 프라하(유럽)", bg="lightblue", font=("양재참숯체B",11))
        빈=Label(lists_box, text="◎오스트리아 빈(유럽)", bg="lightblue", font=("양재참숯체B",11))
        코펜하겐=Label(lists_box, text="◎덴마크 코펜하겐(유럽)", bg="lightblue", font=("양재참숯체B",11))
        유럽1020시간=[]
        if var21.get()==1:
            유럽1020시간.extend([런던, 로마, 코펜하겐])
        if var22.get()==1:
            유럽1020시간.extend([마요르카, 몰타, 프라하, 코펜하겐])
        if var23.get()==1:
            유럽1020시간.extend([마요르카, 몰타, 런던, 파리, 로마, 프라하, 빈, 코펜하겐])
        if var24.get()==1:
            유럽1020시간.extend([마요르카, 몰타, 런던, 파리, 로마, 프라하, 빈, 코펜하겐])
        if var25.get()==1:
            유럽1020시간.extend([코펜하겐])
        tmp_set = set(유럽1020시간)
        유럽1020시간 = list(tmp_set)
        for i, country in enumerate(유럽1020시간):
            country.grid(row=i+72, sticky='W')

    if (var1.get() ==1 or var1.get()==0) and (var13.get()==1) and (경4.get()==1):
        스톡홀롬=Label(lists_box, text="◎스웨덴 스톡홀롬(유럽)", bg="lightblue", font=("양재참숯체B",11))
        바르셀로나=Label(lists_box, text="◎스페인 바르셀로나(유럽)", bg="lightblue", font=("양재참숯체B",11))
        포드고리차=Label(lists_box, text="◎몬테네그로 포드고리차(유럽)", bg="lightblue", font=("양재참숯체B",11))
        유럽20시간=[]
        if var21.get()==1:
            유럽20시간.extend([바르셀로나])
        if var22.get()==1:
            유럽20시간.extend([스톡홀롬, 포드고리차])
        if var23.get()==1:
            유럽20시간.extend([바르셀로나, 스톡홀롬, 포드고리차])
        if var24.get()==1:
            유럽20시간.extend([바르셀로나, 스톡홀롬, 포드고리차])
        if var25.get()==1:
            유럽20시간.extend([포드고리차])
        tmp_set = set(유럽20시간)
        유럽20시간 = list(tmp_set)
        for i, country in enumerate(유럽20시간):
            country.grid(row=i+172, sticky='W')


    if (var1.get() ==1 or var1.get()==0) and (var16.get()==1) and (경4.get()==1):
        모리셔스=Label(lists_box, text="◎모리셔스(아프리카)", bg="lightblue", font=("양재참숯체B",11))
        아프리카20시간=[]
        if var21.get()==1:
            아프리카20시간.extend([])
        if var22.get()==1:
            아프리카20시간.extend([모리셔스])
        if var23.get()==1:
            아프리카20시간.extend([모리셔스])
        if var24.get()==1:
            아프리카20시간.extend([모리셔스])
        if var25.get()==1:
            아프리카20시간.extend([])
        tmp_set = set(아프리카20시간)
        아프리카20시간 = list(tmp_set)
        for i, country in enumerate(아프리카20시간):
            country.grid(row=i+82, sticky='W')

    if (var1.get() ==1 or var1.get()==0) and (var16.get()==1) and (경3.get()==1):
        카이로=Label(lists_box, text="◎이집트 카이로(아프리카)", bg="lightblue", font=("양재참숯체B",11))
        아프리카1020시간=[]
        if var21.get()==1:
            아프리카1020시간.extend([])
        if var22.get()==1:
            아프리카1020시간.extend([])
        if var23.get()==1:
            아프리카1020시간.extend([카이로])
        if var24.get()==1:
            아프리카1020시간.extend([카이로])
        if var25.get()==1:
            아프리카1020시간.extend([])
        tmp_set = set(아프리카1020시간)
        아프리카1020시간 = list(tmp_set)
        for i, country in enumerate(아프리카1020시간):
            country.grid(row=i+92, sticky='W')

    lists_box.configure(background='cornflowerblue')

        


def recommand():#여행지 추천에서 자신이 원하는 여행지에 대한 정보를 클릭할 수 있도록 하는 창
    global var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18,var19,var20,var21,var22,var23,var24,var25
    global 경1, 경2, 경3, 경4, 경5


    recommandation=Toplevel(window)
    recommandation.geometry("500x430")
    
    여행가는달 = Label(recommandation, text="여행가는 달", font='양재참숯체B',bg='lightsteelblue', justify='left').grid(row=1, column=1)
    var1 = IntVar()
    월1 = Checkbutton(recommandation, text=" 1월 ", variable=var1, bg='lightblue').grid(row=2, column=0, sticky='W')
    var2 = IntVar()
    월2 = Checkbutton(recommandation, text=" 2월 ", variable=var2, bg='lightblue').grid(row=2, column=1)
    var3 = IntVar()
    월3 = Checkbutton(recommandation, text=" 3월 ", variable=var3, bg='lightblue').grid(row=2, column=2)
    var4 = IntVar()
    월4 = Checkbutton(recommandation, text=" 4월 ", variable=var4, bg='lightblue').grid(row=3, column=0, sticky='W')
    var5 = IntVar()
    월5 = Checkbutton(recommandation, text=" 5월 ", variable=var5, bg='lightblue').grid(row=3, column=1)
    var6 = IntVar()
    월6 = Checkbutton(recommandation, text=" 6월 ", variable=var6, bg='lightblue').grid(row=3, column=2)
    var7 = IntVar()
    월7 = Checkbutton(recommandation, text=" 7월 ", variable=var7, bg='lightblue').grid(row=4, column=0, sticky='W')
    var8 = IntVar()
    월8 = Checkbutton(recommandation, text=" 8월 ", variable=var8, bg='lightblue').grid(row=4, column=1)
    var9 = IntVar()
    월9 = Checkbutton(recommandation, text=" 9월 ", variable=var9, bg='lightblue').grid(row=4, column=2)
    var10 = IntVar()
    월10 = Checkbutton(recommandation, text="10월", variable=var10, bg='lightblue').grid(row=5, column=0, sticky='W')
    var11 = IntVar()
    월11 = Checkbutton(recommandation, text="11월", variable=var11, bg='lightblue').grid(row=5, column=1)
    var12 = IntVar()
    월12 = Checkbutton(recommandation, text="12월", variable=var12, bg='lightblue').grid(row=5, column=2)

    
    대륙 = Label(recommandation, text="대륙", font='양재참숯체B',bg='lightsteelblue', justify='left').grid(row=6, column=1)
    var13 = IntVar()
    대륙1 = Checkbutton(recommandation, text="   유럽   ", variable=var13, bg='lightblue').grid(row=7, column=0, sticky='W')
    var14= IntVar()
    대륙2 = Checkbutton(recommandation, text="   아시아   ", variable=var14, bg='lightblue').grid(row=7, column=1)
    var15 = IntVar()
    대륙3 = Checkbutton(recommandation, text="오세아니아", variable=var15, bg='lightblue').grid(row=7, column=2)
    var16 = IntVar()
    대륙4 = Checkbutton(recommandation, text="아프리카", variable=var16, bg='lightblue').grid(row=8, column=0, sticky='W')
    var17 = IntVar()
    대륙5 = Checkbutton(recommandation, text="북아메리카", variable=var17, bg='lightblue').grid(row=8, column=1)
    var18 = IntVar()
    대륙6 = Checkbutton(recommandation, text="남아메리카",variable=var18, bg='lightblue').grid(row=8, column=2)

    비행시간 = Label(recommandation, text="비행시간", font='양재참숯체B',bg='lightsteelblue', justify='left').grid(row=17, column=1)
    경1 = IntVar()
    경비1 = Checkbutton(recommandation, text="          5시간 미만          ", variable=경1, bg='lightblue').grid(row=18, column=0, sticky='W')
    경2 = IntVar()
    경비2 = Checkbutton(recommandation, text=" 5시간 이상, 10시간 미만 ", variable=경2, bg='lightblue').grid(row=18, column=2)
    경3 = IntVar()
    경비3 = Checkbutton(recommandation, text="10시간 이상, 20시간 미만", variable=경3, bg='lightblue').grid(row=20, column=0, sticky='W')
    경4 = IntVar()
    경비4 = Checkbutton(recommandation, text="         20시간 이상         ", variable=경4, bg='lightblue').grid(row=20, column=2)

    테마 = Label(recommandation, text="테마", font='양재참숯체B',bg='lightsteelblue', justify='left').grid(row=21, column=1)
    var21 = IntVar()
    테마1 = Checkbutton(recommandation, text=" 쇼핑 ", variable=var21, bg='lightblue').grid(row=22, column=0, sticky='W')
    var22 = IntVar()
    테마2 = Checkbutton(recommandation, text="휴양", variable=var22, bg='lightblue').grid(row=22, column=1)
    var23 = IntVar()
    테마3 = Checkbutton(recommandation, text="관광", variable=var23, bg='lightblue').grid(row=22, column=2)
    var24 = IntVar()
    테마4 = Checkbutton(recommandation, text="식도락", variable=var24, bg='lightblue').grid(row=23, column=0, sticky='W')
    var25 = IntVar()
    테마5 = Checkbutton(recommandation, text="활동", variable=var25, bg='lightblue').grid(row=23, column=1)

    Label(recommandation, text="", font='양재참숯체B',bg='lightsteelblue', justify='left').grid(column=1)




    버튼 = Button(recommandation, text='추천여행지 검색', command=lists, bg='orange').grid(column = 1)

    recommandation.configure(background='lightsteelblue')

    recommandation.mainloop()

def country_1(a):#여행지 정보창에서 첫번째 옵션메뉴인 대륙을 누르면 뜨도록하는 옵션메뉴
    global info, tmp, country, country_menu
    tmp = [None]

    try:
        country_menu.destroy()
        country.destroy()
    except:
        pass
    
    if a == '유럽':
        country = StringVar()
        country.set("나라 선택")
        
        country_menu = OptionMenu(info, country, "스웨덴 스톡홀롬", "스페인 바르셀로나", "아이슬란드 레이카비크", "스페인 마요르카", "몰타", "영국 런던", "프랑스 파리", "이탈리아 로마", "체코 프라하", "오스트리아 빈")
        country_menu.config(bg="lightblue")
        
    elif a=='아시아':
        country = StringVar()
        country.set("나라 선택")

        country_menu = OptionMenu(info, country, "터키 안탈리아", "몰디브", "아랍에미리트 두바이", "라오스 루앙프라방", "인도네시아 발리", "싱가포르공화국", "태국 방콕", "베트남 다낭", "중국 마카오", "홍콩", "중국 상하이", "일본 도쿄", "일본 오사카")
        country_menu.config(bg="lightblue")
        
    elif a=='오세아니아':
        country = StringVar()
        country.set("나라 선택")

        country_menu = OptionMenu(info, country, "호주 호바트", "호주 시드니", "뉴질랜드 웰링턴", "미국 괌")
        country_menu.config(bg="lightblue")

    elif a=='아프리카':
        country = StringVar()
        country.set("나라 선택")

        country_menu = OptionMenu(info, country, "모리셔스", "이집트 카이로")
        country_menu.config(bg="lightblue")

    elif a=='북아메리카':
        country = StringVar()
        country.set("나라 선택")

        country_menu = OptionMenu(info, country, "쿠바 하바나", "미국 뉴욕", "미국 LA", "캐나다 밴쿠버")
        country_menu.config(bg="lightblue")

    elif a=='남아메리카':
        country = StringVar()
        country.set("나라 선택")

        country_menu = OptionMenu(info, country, "브라질 상파울로", "칠레 산티아고")
        country_menu.config(bg="lightblue")    

    tmp[0] = country_menu
    tmp[0].grid(row=2, column=2)


def information():#여행지정보에서 첫번째로 누르는 옵션메뉴
    global info, continent
    info = Toplevel(window)
    info.geometry("900x300")

    continent = StringVar()
    continent.set("대륙 선택")

    continent_menu = OptionMenu(info, continent, "유럽", "아시아", "오세아니아", "아프리카", "북아메리카", "남아메리카", command=country_1)
    continent_menu.config(bg="lightblue")
    continent_menu.grid(row=2, column=1)

    
    global 교통1, 언어1, 추천스팟1, 필수어휘1, 지리정보1, 테마별추천활동1, 개인적꿀팁1, 날씨1
    

    Label(info, text="▶", font=('양재참숯체B',30), bg="lightsteelblue").grid(row=0, sticky='W')
    Label(info, text="원하시는", font=('양재참숯체B',30), bg="lightsteelblue").grid(row=0, column=1)
    Label(info, text="정보를", font=('양재참숯체B',30), bg="lightsteelblue").grid(row=0, column=2)
    Label(info, text="클릭해주세요", font=('양재참숯체B',30), bg="lightsteelblue").grid(row=0, column=3)
    Label(info, text="순서:대륙선택->", font=('양재참숯체B',14), bg="lightblue").grid(row=1, column=1)
    Label(info, text="나라선택->", font=('양재참숯체B',14), bg="lightblue").grid(row=1, column=2)
    Label(info, text="원하는정보 하나선택", font=('양재참숯체B',14), bg="lightblue").grid(row=1, column=3)

    
    교통1=IntVar()
    교통정보 = Checkbutton(info, text="교통정보", font=(12), variable=교통1, bg="lightblue").grid(row=5,column=3)
        
    언어1=IntVar()
    언어정보 = Checkbutton(info, text="언어정보",font=(12), variable=언어1, bg="lightblue").grid(row=5,column=4)
        
    추천스팟1=IntVar()
    추천스팟 = Checkbutton(info, text="추천스팟",font=(12), variable=추천스팟1, bg="lightblue").grid(row=7,column=3)
        
    필수어휘1=IntVar()
    필수어휘 = Checkbutton(info, text="필수어휘",font=(12), variable=필수어휘1, bg="lightblue").grid(row=7,column=4)
        
    지리정보1=IntVar()
    지리정보 = Checkbutton(info, text="지리정보",font=(12), variable=지리정보1, bg="lightblue").grid(row=10,column=3)
        
    테마별추천활동1=IntVar()
    태마별추천활동 = Checkbutton(info, text="테마별추천활동",font=(12), variable=테마별추천활동1, bg="lightblue").grid(row=10,column=4)
        
    개인적꿀팁1=IntVar()
    개인적꿀팁 = Checkbutton(info, text="개인적 꿀팁",font=(12), variable=개인적꿀팁1, bg="lightblue").grid(row=11,column=3)

    날씨1=IntVar()
    날씨 = Checkbutton(info, text="날씨정보",font=(12), variable=날씨1, bg="lightblue").grid(row=11,column=4)


    Label(info, text="", font='양재참숯체B',bg='lightsteelblue', justify='left').grid(column=1)

    버튼 = Button(info, text='검색',font=('양재참숯체B',15), command=final, bg="orange").grid(column = 3)

    info.configure(background='lightsteelblue')


    info.mainloop()








#맨 처음에 뜨는 화면
title = Label(window, text="당신의 완벽한 \n\n 여행을 \n\n위하여", font=('양재참숯체B',20)).grid(row=1, column=4)
img = PhotoImage(file='여행.gif')
label = Label(window, image=img)
label.grid(row=1, column=1)

여행지추천 = Button(window, text='여행지추천',font=('양재참숯체B',12), bg="orange", command=recommand).grid(row =2, column = 1)
여행지정보 = Button(window, text='여행지정보',font=('양재참숯체B',12), bg="orange", command=information).grid(row=3, column = 1)


window.mainloop()
