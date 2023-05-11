console.log("Hello Sk")



fetch('https://api.sampleapis.com/beers/ale')
  .then(function(response) {
    return response.json();
  })
  .then(function(data) {
    var tbody = document.querySelector('#taxi-table tbody');
    data.forEach(function(taxi) {
      var row = document.createElement('tr');
      row.innerHTML = `
        <td>${taxi.name}</td>
        <td>${taxi.price}</td>
        <td>${taxi.rating.average}</td>
        <td>${taxi.rating.reviews}</td>
        <td><img src="${taxi.image}" alt="kya hai"></td>
      `;
      tbody.appendChild(row);
    });
  })
  .catch(function(error) {
    console.log('Fetch Error:', error);
  });