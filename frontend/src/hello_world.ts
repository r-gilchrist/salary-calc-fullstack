console.log("Hi!");
fetch("http://localhost:5000/salary")
  .then(function (response) {
    return response.json();
  })
  .then(function (text) {
    console.log(text);
  });
