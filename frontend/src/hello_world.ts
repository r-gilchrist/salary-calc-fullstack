fetch("http://localhost:80/helloworld")
  .then(function (response) {
    return response.json();
  })
  .then(function (text) {
    console.log(text);
  });
