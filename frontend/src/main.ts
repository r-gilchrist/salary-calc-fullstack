const grossInput = document.getElementById("gross-input") as HTMLInputElement | null;
const pensionInput = document.getElementById("pension-input") as HTMLInputElement | null;
const submitButton = document.getElementById("update-salary") as HTMLButtonElement | null;

const grossOutput = document.getElementById("gross-output") as HTMLParagraphElement | null;
const incomeTaxOutput = document.getElementById("tax-output") as HTMLParagraphElement | null;
const niOutput = document.getElementById("NI-output") as HTMLParagraphElement | null;
const pensionOutput = document.getElementById("pension-output") as HTMLParagraphElement | null;
const netOutput = document.getElementById("net-output") as HTMLParagraphElement | null;

submitButton?.addEventListener("click", (e) => {
  let request_body = {
    reference_salary: getInputAmount(grossInput),
    pension_contribution: getInputAmount(pensionInput),
  };
  console.log(`Reference salary is ${request_body.reference_salary}`);
  console.log(`Pension % contribution is ${request_body.pension_contribution}`);
});

function getInputAmount(element: HTMLInputElement | null) {
  if (element == null) return 0;
  let amount = Number(element.value);
  if (isNaN(amount)) return 0;
  return amount;
}

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
