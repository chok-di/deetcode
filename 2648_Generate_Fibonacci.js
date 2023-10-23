/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
  yield 0;
  yield 1;
  let temp1 = 0;
  let temp2 = 1;
  while(true){
    let newNum = temp1 + temp2;
    temp1 = temp2;
    temp2 = newNum;
    yield newNum;
  }
}

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */