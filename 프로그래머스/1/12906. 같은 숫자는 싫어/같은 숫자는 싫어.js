function solution(arr)
{
    const len = arr.length
    let answer = []
    let std = arr[0]
    
    answer.push(arr[0])
    for (let i=1; i<len; i++) {
        if (std != arr[i]) {
            answer.push(arr[i])
        }
        std = arr[i]
    }
    
    
    return answer;
}