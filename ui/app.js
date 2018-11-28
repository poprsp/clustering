"use strict";

function getUrl(endpoint) {
  return `${window.location.origin}/api/${endpoint}`;
}

function addKMeansListener() {
  document.getElementById("k-means").addEventListener("submit", e => {
    const iterations = document.getElementById("k-means-iterations");
    loadKMeans(iterations.value);
  });
}

function loadKMeans(iterations) {
  const url = getUrl("k-means-clustering");
  const result = document.getElementById("result");

  while (result.children.length) {
    result.removeChild(result.children[0]);
  }

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

function main() {
  addKMeansListener();
}

window.onload = main;
