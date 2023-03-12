fetch("http://localhost:5000/salary", {
  method: "POST",

  body: JSON.stringify({
    reference_salary: 47000,
  }),

  headers: {
    "Content-type": "application/json; charset=UTF-8",
  },
})
  .then(function (response) {
    return response.json();
  })
  .then(function (text) {
    console.log(text);
  });
