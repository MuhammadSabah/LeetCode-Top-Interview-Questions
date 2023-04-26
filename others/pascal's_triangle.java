class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> resultList = new ArrayList<>();
        if(numRows == 0) return resultList;

        List<Integer> firstRow = new ArrayList<>();
        firstRow.add(1);
        resultList.add(firstRow);

        for(int i = 1; i<numRows; i++){
            List<Integer> prevRow = resultList.get(i-1);
            List<Integer> currRow = new ArrayList<>();
            currRow.add(1);
            for(int j = 1; j<i; j++){
                currRow.add(prevRow.get(j-1) + prevRow.get(j));
            }
            currRow.add(1);
            resultList.add(currRow);
        }
        return resultList;
    }
}