fetch("http://localhost:5000/helloworld")
  .then(function (response) {
    return response.json();
  })
  .then(function (text) {
    console.log(text);
  });
