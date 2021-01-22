import json
import kakao_utils

KAKAO_TOKEN_FILENAME = "res/kakao_message/kakao_token.json" #"<kakao_token.json 파일이 있는 경로를 입력하세요.>"
KAKAO_APP_KEY = ce8a23a70d9d9a88ac0844fc111116f4
kakao_utils.update_tokens(KAKAO_APP_KEY, KAKAO_TOKEN_FILENAME)