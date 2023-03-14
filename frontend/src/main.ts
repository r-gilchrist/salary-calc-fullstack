import { getRequestBody } from "./request.js";
import { populateFields } from "./response.js";
import { setDefaultDate } from "./date.js";

setDefaultDate()

const submitButton = document.getElementById("update-salary") as HTMLButtonElement | null;

submitButton?.addEventListener("click", (e) => {
  update_fields();
});

async function update_fields() {
  const request_body = getRequestBody();
  console.log(JSON.stringify(request_body));

  const response_body = await fetch("http://localhost:5000/salary", {
    method: "POST",
    body: JSON.stringify(request_body),
    headers: { "Content-type": "application/json; charset=UTF-8" },
  });

  const data = await response_body.json();

  populateFields(data);
}
