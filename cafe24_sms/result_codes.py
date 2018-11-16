# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _


RESULT_CODES = {
    'success': _('전송성공'),
    'reserved': _('예약성공'),
    '-100': _('서버 에러'),
    '-101': _('변수부족 에러'),
    '-102': _('인증 에러'),
    '-105': _('예약시간 에러'),
    '-110': _('1000건 이상 발송 불가'),
    '-114': _('등록/인증되지 않은 발신번호'),
    '-201': _('SMS 건수 부족 에러'),
    '-202': _('문자 "됬"은 사용불가능한 문자입니다.'),
    '-203': _('SMS 대량 발송 에러'),
    '0001': _('서비스 번호 오류'),
    '0002': _('메시지 구성 결여'),
    '0003': _('메시지 포맷 오류'),
    '0004': _('메시지 제목(50Byte)/내용(SMS:90Byte,LMS:2000Byte) 초과'),
    '0005': _('Connect 필요'),
    '0099': _('기타 오류(DB 오류시스템장애)'),
    '0044': _('스팸메시지 차단(배팅, 바카라, 도박, 섹스, liveno1 ,카지노 등을 포함한 스팸메시지는 발송이 실패됩니다.)'),
    '3201': _('발송시각 오류'),
    '3202': _('폰넘버 오류'),
    '3203': _('SMS 메시지 Base64 Encoding 오류'),
    '3204': _('CallBack 메시지 Base64 Encoding 오류'),
    '3205': _('번호형식 오류'),
    '3206': _('전송 성공'),
    '3207': _('비가입자 결번 서비스정지'),
    '3208': _('단말기 Power-off 상태'),
    '3209': _('음영 지역'),
    '3210': _('단말기 메시지 FULL'),
    '3211': _('기타에러(이통사)'),
    '3214': _('기타에러(무선망)'),
    '3213': _('번호이동관련'),
    '3217': _('조합메시지 형식오류'),
    '3218': _('메시지 중복 오류'),
    '3219': _('월 송신건수 초과'),
    '3220': _('알 수 없는 에러'),
    '3221': _('착신번호 에러(자리수 에러)'),
    '3222': _('착신번호 에러(없는 국번)'),
    '3223': _('수신거부 메시지 부분 없음'),
    '3224': _('21시 이후 광고'),
    '-2': _('결과 수신 대기중'),
    '0': _('전송성공'),
    '1': _('시스템 장애'),
    '41': _('MMS Content 생성 실패'),
    '42': _('MMS 결과코드 에러'),
    '112': _('레포트 수신 시간 만료'),
    '114': _('번호도용/변작방지 차단'),
    '116': _('번호 세칙 위반'),
    '202': _('착신가입자없음'),
    '203': _('비가입자, 결번, 서비스정지 등 수신자 오류'),
    '204': _('단말기 전원 꺼짐'),
    '205': _('음영 지역'),
    '206': _('단말기 메시지 FULL'),
    '207': _('단말기 오류'),
    '209': _('번호이동된 가입자'),
    '210': _('SMS 착신전환회수초과'),
    '211': _('기간만료'),
    '212': _('기타에러(이통사)'),
    '216': _('수신번호 오류'),
    '245': _('메시지 전송불가(단말기에서 착신 거부)'),
    '253': _('전송 실패(무선망), 단말기 일시정지'),
    '254': _('전송 실패(무선망 -> 단말기단), 가입자 VLR 없음'),
    '2003': _('미지원 단말'),
    '4005': _('이통사 서비스 에러'),
    '4007': _('클라이언트 오류'),
    '4008': _('통신사 서버 과부하'),
    '4301': _('미 가입자 에러 오류(KTF), 결번'),
    '4305': _('단말기 오류'),
    '4307': _('일시정지 가입자 오류'),
    '6072': _('MMS 미지원단말기'),
    '8012': _('SKT MMS 오류'),
    '8200': _('단말기 오류'),
    '9999': _('알 수 없는 에러'),
}


def get_result_message(code):
    try:
        return RESULT_CODES[code]
    except KeyError:
        return _('Not registered code')
