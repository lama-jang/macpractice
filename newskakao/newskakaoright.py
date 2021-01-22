import requests
from bs4 import BeautifulSoup
import bs4.element
import datetime

# BeautifulSoup 객체 생성
def get_soup_obj(url):
    headers = {'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15'}
    res = requests.get(url, headers = headers)
    soup = BeautifulSoup(res.text, 'lxml')
    
    return soup

# 뉴스의 기본 정보 가져오기
# 뉴스의 기본 정보 가져오기
def get_top3_news_info(sec, sid):
    # 임시 이미지
    default_img = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=naver#"
    
     # 해당 분야 상위 뉴스 목록 주소
    sec_url = "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec" \
                + "&sid1=" \
                + sid
    print("section url : ", sec_url)
    
    # 해당 분야 상위 뉴스 HTML 가져오기
    soup = get_soup_obj(sec_url)
  
    # 해당 분야 상위 뉴스 3개 가져오기
    news_list3 = []
    lis3 = soup.find('ul', class_='type06_headline').find_all("li", limit=3)
    for li in lis3:
        # title : 뉴스 제목, news_url : 뉴스 URL, image_url : 이미지 URL
        news_info = {
            "title" : li.img.attrs.get('alt') if li.img else li.a.text.replace("\n", "").replace("\t","").replace("\r","") , 
            "date" : li.find(class_="date").text,
            "news_url" : li.a.attrs.get('href'),
            "image_url" :  li.img.attrs.get('src') if li.img else default_img
        }
        news_list3.append(news_info)
        
    return news_list3

# 뉴스 본문 가져오기
def get_news_contents(url):
    soup = get_soup_obj(url)
    body = soup.find('div', class_="_article_body_contents")

    news_contents = ''
    for content in body:
        if type(content) is bs4.element.NavigableString and len(content) > 50:
            # content.strip() : whitepace 제거 (참고 : https://www.tutorialspoint.com/python3/string_strip.htm)
            # 뉴스 요약을 위하여 '.' 마침표 뒤에 한칸을 띄워 문장을 구분하도록 함
            news_contents += content.strip() + ' '
         
    return news_contents
        
    
# '정치', '경제', '사회' 분야의 상위 3개 뉴스 크롤링
def get_naver_news_top3():
    # 뉴스 결과를 담아낼 dictionary
    news_dic = dict()
    
    # sections : '정치', '경제', '사회'
    sections = ["pol", "eco","soc"]
    # section_ids :  URL에 사용될 뉴스  각 부문 ID
    section_ids = ["100", "101","102"]
    
    for sec, sid in zip(sections, section_ids):   
        # 뉴스의 기본 정보 가져오기
        news_info = get_top3_news_info(sec, sid)
        #print(news_info)
        for news in news_info:
            # 뉴스 본문 가져오기
            news_url = news['news_url']
            news_contents = get_news_contents(news_url)
            
            # 뉴스 정보를 저장하는 dictionary를 구성
            news['news_contents'] = news_contents

        news_dic[sec] = news_info
    
    return news_dic
    
# 함수 호출 - '정치', '경제', '사회' 분야의 상위 3개 뉴스 크롤링
news_dic = get_naver_news_top3()
# 경제의 첫번째 결과 확인하기 
news_dic['eco'][0]