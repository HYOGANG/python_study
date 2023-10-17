#마라톤 불합격자 출력

def solution(participant, completion):
    answer = []
    for i in range(len(completion)):
        if (completion[i] in participant):
            participant.remove(completion[i]) 
    for j in range(len(participant)):
        answer = participant[j]
    return answer
#정확성은 만점인데 효율성 0