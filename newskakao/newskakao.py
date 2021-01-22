import requests
from bs4 import BeautifulSoup
import bs4.element
import datetime

from gensim.summarization.summarizer import summarize

def get_soup_obj(url):
    headers = {'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15'}
    res = requests.get(url, headers = headers)
    soup = BeautifulSoup(res.text, 'lxml')

    return soup

# 뉴스 기본 정보 가져오기
def get_top3_news_info(sec, sid):
    # 임시 이미지
    default_img = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=naver#"

    # 해당 분야 상위 뉴스 목록 주소
    sec_url = "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=" + sid
    print("section URL =", sec_url)

    # 해당 분야 상위 뉴스 HTML 가져오기
    soup = get_soup_obj(sec_url)

    # 해당 분야 상위 뉴스 3개 가져오기
    news_list3 = []
    lis3 = soup.find('ul', class_='type06_headline').find_all('li', limit = 3)
    for li in lis3:
        # title : 뉴스 제목, news_url : 뉴스 URL, image_url : 이미지 URL
        news_info = {
            "title" : li.img.attrs.get('alt') if li.img else li.a.text.replace("\n", "").replace("\t", "").replace("\r", ""),
            "date" : li.find(class_="date").text,
            "news_url" : li.a.attrs.get('href'),
            "image_url" : li.img.attrs.get('src') if li.img else default_img
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

# '경제', '사회', '생활/문화' 분야의 상위 3개 뉴스 크롤링
def get_naver_news_top3():
    # 뉴스 결과를 담아낼 딕셔너리
    news_dic = dict()

    sections = ["eco", "soc", "lif"]
    section_ids = ["101", "102", "103"]

    for sec, sid in zip(sections, section_ids):
        news_info = get_top3_news_info(sec, sid)
        # print(news_info)
        for news in news_info:
            news_url = news["news_url"]
            news_contents = get_news_contents(news_url)

            # 뉴스 정보를 저장하는 dictionary를 구성
            news['news_contents'] = news_contents
        
        news_dic[sec] = news_info
    
    return news_dic

# 함수를 호출 - '경제', '사회', 생홀/문화' 분야의 상위 3개 뉴스 크롤링
news_dic = get_naver_news_top3()
# 경제의 첫번째 결과 확인하기
# news_dic["eco"][0])

# -------------------- 요약문 작성 ------------------------ 

# 섹션 지정
my_section = 'eco'    # 추후 반목문을 통해 모든 섹션으로 변경 예정
news_list3 = news_dic[my_section]
# 뉴스 요약하기
for news_info in news_list3:
    # 뉴스 본문이 10문장 이하일 경우 결과가 반환되지 않음
    # 이때는 요약하지 않고 앞문장 3문장을 사용함
    try:
        snews_contents = summarize(news_info['news_contents'], word_count=20)
    except:
        snews_contents = None

    if not snews_contents:
        news_sentences = news_info['news_contents'].split('.')

        if len(news_sentences) > 3:
            snews_contents = '.'.join(news_sentences[:3])
        else:
            snews_contents = '.'.join(news_sentences)
        
    news_info['snews_contents'] = snews_contents

# 요약 결과 - 첫번째 뉴스
print("===== 첫번째 뉴스 원문 =====")
print(news_list3[0]['news_contents'])
print("\n===== 첫번째 뉴스 요약문 =====")
print(news_list3[0]['snews_contents'])

# 요약 결과 - 두번째 뉴스
print("===== 두번째 뉴스 원문 =====")
print(news_list3[1]['news_contents'])
print("\n===== 두번째 뉴스 요약문 =====")
print(news_list3[1]['snews_contents'])