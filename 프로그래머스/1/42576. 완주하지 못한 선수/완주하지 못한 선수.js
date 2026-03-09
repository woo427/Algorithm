function solution(participant, completion) {
    hash = {}
    
    for (let p of participant) {
        if (hash[p])
            hash[p] += 1
        else
            hash[p] = 1
    }
    
    for (let c of completion) {
        if (hash[c])
            hash[c] -= 1
    }
    
    for (let name of Object.keys(hash)) {
        if (hash[name] === 1)
            return name
    }
}