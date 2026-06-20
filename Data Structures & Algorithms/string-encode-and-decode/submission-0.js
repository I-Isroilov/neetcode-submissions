class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        return strs.map(str => `${str.length}#${str}`).join('');
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        const result = []
        let i = 0;

        while(i < str.length){
            let delimeter = str.indexOf('#', i)
            if (delimeter === -1) break;
            let length = parseInt(str.slice(i, delimeter))

            let start = delimeter + 1
            result.push(str.slice(start, start + length))
            i = start + length
        }
        return result
    }
}
