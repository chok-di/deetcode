var findPaths = function (area) {
  let rows = area.length;
  let cols = area[0].length;

  function getEmptyBoard() {
    return new Array(rows).fill(0).map(x => new Array(cols).fill(0))
  };



  function getNewDp(old = []) {
    let dp = getEmptyBoard();
    for (let i = 0; i < rows; i++) {
      for (let j = 0; j < cols; j++ {
        let count = old[i][j];
        addCount(i, j + 1, count, dp)


      }
    }
  function addCount(i,j, count, dp) {
    if (out of range or can't go) {
      

    }
  }

  }


  
};

