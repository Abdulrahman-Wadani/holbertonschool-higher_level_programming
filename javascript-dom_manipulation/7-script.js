const mlist = document.querySelector('#list_movies');

async function addname () {
  const respons = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
  const data = await respons.json();
  for (let i = 0; i < data.results.length; i++) {
    const item = document.createElement('li');
    item.textContent = data.results[i].title;
    mlist.appendChild(item);
  }
}

addname();
