import { RequestBody, ResponseBody } from "./types.js";
import { getDropDownOption, getInputAmount, updateOutputField } from "./helpers.js";

const grossInput = document.getElementById("gross-input") as HTMLInputElement | null;
const pensionInput = document.getElementById("pension-input") as HTMLInputElement | null;
const studentInput = document.getElementById("student-input") as HTMLSelectElement | null;
const submitButton = document.getElementById("update-salary") as HTMLButtonElement | null;

const grossOutput = document.getElementById("gross-output") as HTMLParagraphElement | null;
const incomeTaxOutput = document.getElementById("tax-output") as HTMLParagraphElement | null;
const niOutput = document.getElementById("NI-output") as HTMLParagraphElement | null;
const studentOutput = document.getElementById("student-output") as HTMLParagraphElement | null;
const pensionOutput = document.getElementById("pension-output") as HTMLParagraphElement | null;
const netOutput = document.getElementById("net-output") as HTMLParagraphElement | null;

submitButton?.addEventListener("click", (e) => {
  let request_body = {
    reference_salary: getInputAmount(grossInput),
    pension_contribution: getInputAmount(pensionInput),
    student_loan_type: getDropDownOption(studentInput),
  };
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
      updateOutputField(grossOutput, response_body.reference_salary);
      updateOutputField(incomeTaxOutput, response_body.income_tax);
      updateOutputField(niOutput, response_body.national_insurance);
      updateOutputField(pensionOutput, response_body.pension);
      updateOutputField(studentOutput, response_body.student_loan);
      updateOutputField(netOutput, response_body.net_salary);
    });
}
