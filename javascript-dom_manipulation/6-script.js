const Cname = document.querySelector('#character');

async function addname () {
  const respons = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
  const data = await respons.json();
  Cname.textContent = data.name;
}

addname();
