"use strict";

function getUrl(endpoint) {
  return `${window.location.origin}/api/${endpoint}`;
}

function addEventListeners() {
  /*
   * K-means
   */
  [0, 1, 3, 5, 10].forEach(k => {
    document.getElementById(`k-means-${k}`).addEventListener("click", () => {
      loadKMeans(k);
    });
  });

  /*
   * Hierarchical
   */
  document.getElementById("hierarchical").addEventListener("click", () => {
    loadHierarchical();
  });
}

function loadKMeans(iterations) {
  const url = getUrl("k-means-clustering");
  const result = document.getElementById("result");

  removeChildren(result);

  console.log(`retrieving K-means clustering with ${iterations} iterations`);
  fetch(`${url}/${iterations}`)
    .then(res => {
      return res.json();
    })
    .then(json => {
      for (const centroid in json) {
        const ul = document.createElement("ul");
        const b = document.createElement("b");
        b.innerHTML = `centroid ${centroid}`;
        ul.appendChild(b);

        for (const blog of json[centroid]) {
          const li = document.createElement("li");
          const text = document.createTextNode(blog);
          li.appendChild(text);
          ul.appendChild(li);
        }
        result.appendChild(ul);
      }
    })
    .catch(err => {
      console.log(err);
    });
}

function loadHierarchical() {
  const url = getUrl("hierarchical-clustering");
  const result = document.getElementById("result");

  removeChildren(result);

  console.log("retrieving hierarchical clustering");
  fetch(`${url}`)
    .then(res => {
      return res.json();
    })
    .then(json => {
      const pre = document.createElement("pre");
      result.appendChild(pre);
      recursivePrint(json["root"], pre);
      console.log(json)
    })
    .catch(err => {
      console.log(err);
    })
}

function recursivePrint(cluster, elem, indent=8) {
  if (cluster !== undefined) {
    recursivePrint(cluster.left, elem, indent - 4);
    elem.innerHTML += `\n${".".repeat(indent)}${cluster.blog}`;
    recursivePrint(cluster.right, elem, indent + 4);
  }
}

function removeChildren(root) {
  while (root.children.length) {
    root.removeChild(root.children[0]);
  }
}

function main() {
  addEventListeners();
}

window.onload = main;
