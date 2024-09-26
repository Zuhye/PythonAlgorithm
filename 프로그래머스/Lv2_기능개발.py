def solution(progresses, speeds):
    answer = []
    result = []
    count = 0

    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] != 0:
            value = (100 - progresses[i]) // speeds[i] + 1
        else:
            value = (100 - progresses[i]) // speeds[i]
        answer.append(value)

    for i in range(len(answer)):
        if count < answer[i]:
            result.append(1)
            count = answer[i]
        else:
            result[len(result) - 1] += 1

    return result


print(solution([93, 30, 55], [1, 30, 5]))
# [2, 1] 출력
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
# [1, 3, 2] 출력


"""
Java 풀이

import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answer = new ArrayList<>();
        ArrayList<Integer> result = new ArrayList<>();
        int count = 0;
        
        for(int i = 0 ; i<progresses.length; i++){
            int remaining = 100-progresses[i];
            int daysRequired = remaining/speeds[i];
            
            if(remaining % speeds[i] != 0){
                daysRequired += 1;
            }
            answer.add(daysRequired);
        }
        
        for(int i = 0; i< answer.size(); i++){
            if(count < answer.get(i)) {
                result.add(1);
                count = answer.get(i);
            } else {
                int lastIdx = result.size() - 1;
                result.set(lastIdx, result.get(lastIdx) + 1);
            }
        }
        
        int [] finalResult = new int[result.size()];
        for(int i = 0; i<result.size(); i++) {
            finalResult[i] = result.get(i);
        }
        
        return finalResult;
    }
}

"""
