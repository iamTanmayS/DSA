/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    result = init
    for(let i of nums){
        result = fn(result,i)
    }
    return result

    }
