#이용자의 ID가 담긴 문자열 배열 id_list
id_list = []
print("추가할 id가 없는 경우, end를 입력하시오.")
print("id의 개수가 10개 이상인 경우, 자동으로 넘어갑니다.")
while True:
    if len(id_list) >= 10:
        break
    id = input("이용자 id : ")
    if id == 'end':
        break
    id_list.append(id)
id_list = set(id_list)
id_list = list(id_list) #중복 제거
print("이용자 :", id_list, "\n")

#정지 기준이 되는 신고 횟수 k
print("정지를 위한 신고 횟수를 설정하십시오.(횟수는 최대 200회입니다.)")
while True:
    k = input("신고 횟수 : ")
    if int(k) < 200:
        break
    else:
        print("신고 횟수 오류")
print("설정하신 신고 횟수는 " + k + "회입니다.\n")

#각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 report
report = []
print("추가 신고가 없는 경우, end를 입력하시오.")
print("신고 개수는 3개와 21개 사이여야 합니다.")
while True:
    if len(report) >= 21 and len(report) <= 3:
        break
    report_str = input("신고 내용 : ")
    if  report_str == 'end':
        if len(report) < 3:
            print("신고 횟수가 너무 적습니다. 신고를 추가하세요.")
            continue
        else : break
    report.append(report_str)
report = set(report)
report = list(report) #중복 제거
print("신고 :", report, "\n")

report_id = []
reported_id = []
for i in range(len(report)):
    split_rpt = report[i].split()
    if split_rpt[0] == split_rpt[1]:
        print("자기 자신을 신고할 수 없습니다.")
        continue
    report_id.append(split_rpt[0])
    reported_id.append(split_rpt[1])
print("이용자 id :", report_id)
print("신고한 id :", reported_id)

# for i in range(len(report_id)):
#     print(report_id[i] + "가 신고한 id는 " + reported_id[i] + "입니다.")

#신고된 id 개수 카운트
reported_cnt = []
result_dictionary = dict.fromkeys(id_list,0)
for i in range(len(id_list)):
    cnt = reported_id.count(id_list[i])
    reported_cnt.append(cnt)
    if int(reported_cnt[i]) >= int(k):
        print(id_list[i] + "는 설정한 신고 횟수만큼 신고되었습니다.")
        cnt_two = id_list[i]
        for j in range(len(report_id)):
            if cnt_two == reported_id[j]:
                result_dictionary[report_id[j]] += 1

print("")
print(result_dictionary)




