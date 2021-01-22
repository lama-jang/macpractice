from gensim.summarization.summarizer import summarize

# 섹션 지정
my_section = 'eco'
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