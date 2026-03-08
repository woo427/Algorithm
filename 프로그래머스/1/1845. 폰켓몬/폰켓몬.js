function solution(nums) {
    
    const max = nums.length/2
    const kind = new Set(nums).size
    
    return Math.min(max,kind)
}