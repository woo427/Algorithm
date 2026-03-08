function solution(array, commands) {
    
    const answer = [];
    
    for (let i=0; i<commands.length; i++) {
        newArray = array.slice(commands[i][0]-1,commands[i][1])
        newArray.sort((a,b)=>a-b);
        answer.push(newArray[commands[i][2]-1]);
        console.log(newArray)
    }
    
    return answer
}