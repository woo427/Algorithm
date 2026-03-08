function solution(s){
    s = s.toLowerCase();
    let num_p = num_y = 0
    
    for(let i of s) {
        if(i=="p")
            num_p += 1
        else if(i=="y")
            num_y += 1
    }
    
    if (num_p == num_y) {
        return true
    }
    else
        return false
    
}