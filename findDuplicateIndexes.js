function findDuplicateIndexes(arr) {
  const map = {};
  const ans = [];

  for (let i = 0; i < arr.length; i++) {
    const element = arr[i];
    if (!map[element]) {
      map[element] = i;
    } else {
      ans.push(map[element]);
      ans.push(i);
    }
  }

  return ans;
}

const arr = ['banana', 'apple', 'blueberry', 'apple', 'orange'];

console.log(findDuplicateIndexes(arr));