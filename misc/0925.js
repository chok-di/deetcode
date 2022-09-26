const findRoute = (area) => {
  let rows = area.length;
  let cols = area[0].length;
  let dp = new Array(rows).fill(0).map(x => new Array(cols).fill(0))
  const findShortest = (x,y) => {
    if (dp[x][y] !== 0) {return dp[x][y];}
   
    if (x == 0 && y == 0) {console.log("start"); dp[x][y] = 1;} 
    if (x >= rows || y >= cols || Math.min(x,y) < 0) { console.log('out of range!'); return;}
    if (area[x][y] == 0) {console.log(area[x][y]); console.log("can't pass"); dp[x][y] = -1;} 
   
    let result = [findShortest[(x+1,y)],findShortest[(x-1,y)],findShortest[(x,y+1)],findShortest[(x,y-1)]];
  
    // .filter(num => {num > 0}).sort();
    dp[x][y] = result.length == 0? -1 : result[0] + 1;
    
 
  }

  console.log(findShortest(1,0));
  // for (let row = 0; row < rows; row++) {
  //   for (let col = 0; col < cols; col++) {
  //     if (area[row][col] == 9) {
  //       findShortest(row,col);
  //     }
  //   }
  // }
}



findRoute([[1,0,0],
  [1,0,0],
  [1,9,1]
 ]);
