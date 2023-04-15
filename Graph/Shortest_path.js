//https://www.educative.io/module/page/xGD3yRS9rp2LK46J6/10370001/6061111024812032/4589820585443328xx
function findMin(g, source, destination){
  let shortest = Infinity;
  function dfs(index,distance){
    if (index == destination){
      shortest = Math.min(shortest, distance);
      return;
    }
    //no need to keep tryiying if distance travelled is greater than current best path
    if (distance >= shortest){
      return;
    }
    let next = g.list[index].getHead();
    while (next){
      dfs(next.data, distance + 1);
      next = next.nextElement;
    }
  }
  dfs(source,0);
  return shortest == Infinity? -1 : shortest;
}