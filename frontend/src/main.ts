import { getRequestBody, RequestBody } from "./request.js";
import { populateFields, ResponseBody } from "./response.js";

const submitButton = document.getElementById("update-salary") as HTMLButtonElement | null;

submitButton?.addEventListener("click", (e) => {
  let request_body = getRequestBody();
  update_fields(request_body);
});

function update_fields(request_body: RequestBody) {
  fetch("http://localhost:5000/salary", {
    method: "POST",

    body: JSON.stringify(request_body),

    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (response_body: ResponseBody) {
      populateFields(response_body);
    });
}
