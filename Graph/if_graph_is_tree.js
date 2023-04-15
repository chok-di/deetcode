function isTree(g) {
  console.log(g);
  let visited = {};
  
  ///dfs traverse through a node
  // false: when cycle detected or when end is reached and not all nodes are visited
  function findCycle(node,prev){
    visited[node] = prev;
    let adjacent = g.list[node].getHead();
    while(adjacent){
      if (adjacent.data.toString() in visited && adjacent.data != prev){
        return true;
      }
      if (!(adjacent.data.toString() in visited)){
        if(findCycle(adjacent.data,node)){
          return true;
        };
      }
      adjacent = adjacent.nextElement;
    }
    return false;
  }
  
  if(findCycle(0,-1)){
    return false;
  }
  if(Object.keys(visited).length != g.vertices){
    return false;
  }
  return true;
  // Write code here
}