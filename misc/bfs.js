function findShortest(area){
  let rows = area.length;
  let cols = area[0].length;
  let count = new Array(rows).fill("peepeepoopoo").map(x => new Array(cols).fill(Infinity));
  count[0][0] = 0;
  let targetX;
  let targetY;

  function dfs(x,y) {
    if(area[x][y] == 1) {
      for (let directions of [[x+1, y], [x-1,y],[x,y+1],[x,y-1]]) {
        if (Math.min(directions[0],directions[1]) < 0 || directions[0] >= rows || directions[1] >= cols){
          continue
        }
        if (area[[directions[0]][directions[1]]] == 0){console.log("bad route"); continue;}
        if(count[x][y] + 1 < count[directions[0]][directions[1]]) {
          count[directions[0]][directions[1]] = count[x][y] + 1;
          dfs(directions[0], directions[1]);
        } 
      }
    }
  }
  for (let x = 0; x< rows; x++) {
    for (let y = 0; y<cols; y++) {
      dfs(x,y);
      if (area[x][y] == 9){targetX = x; targetY = y;}
    }
  } 

  return count[targetX][targetY] === Infinity? -1 : count[targetX][targetY]; 
}

console.log(findShortest([[1,0,9],
             [1,1,1],
             [1,1,1]]
             ));
   