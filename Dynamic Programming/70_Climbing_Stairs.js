var climbStairs = function(n) {
  //ways to n+2 = ways to n+1 + ways to n
  if (n == 1) {
      return 1;
  }
  if (n == 2) {
      return 2;
  }
  if (n > 2) {
      let a = 1;
      let b = 2;
      for (let i = 3;i<= n; i++) {
          helper = b;
          b += a;
          a = helper;
      }
      return b;
  }
}

//recursion also solves it, but it's very slow.