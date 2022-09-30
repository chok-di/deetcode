//https://www.codewars.com/kata/5715508de1bf8174c1001832/train/javascript
function longestComb(arr, command){
  let helper = (command == "< <" || command == "<<") ? 1 : -1
  arr = arr.map(num => num * helper);
  let res = [];
  let bar = 3;
  function backtrack(n,curr) {
    if (n == arr.length){
      if (curr.length > bar) {
        res = [[...curr]];
        bar = curr.length;
        return;
      }
      if (curr.length == bar) {
        res.push([...curr]);
        return;
      } 
      return;
    }
    if (curr.length == 0 || arr[n] > curr[curr.length - 1]) {
      curr.push(arr[n]);
      backtrack(n+1,curr);
      curr.pop();
      backtrack(n+1,curr);
    } else {
      while (n < arr.length && arr[n] <= curr[curr.length - 1]) {
      n += 1
      }
      backtrack(n,curr);
    }
  }
  backtrack(0,[]);
  res = res.map(arr => arr.map(num => num*helper));
  return res.length == 1? res[0] : res;
}