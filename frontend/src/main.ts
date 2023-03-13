const grossInput = document.getElementById("gross-input") as HTMLInputElement | null;
const pensionInput = document.getElementById("pension-input") as HTMLInputElement | null;
const submitButton = document.getElementById("update-salary") as HTMLButtonElement | null;

const grossOutput = document.getElementById("gross-output") as HTMLParagraphElement | null;
const incomeTaxOutput = document.getElementById("tax-output") as HTMLParagraphElement | null;
const niOutput = document.getElementById("NI-output") as HTMLParagraphElement | null;
const pensionOutput = document.getElementById("pension-output") as HTMLParagraphElement | null;
const netOutput = document.getElementById("net-output") as HTMLParagraphElement | null;

type RequestBody = {
  reference_salary: number;
  pension_contribution: number;
};

type ResponseBody = {
  reference_salary: number;
  income_tax: number;
  national_insurance: number;
  pension: number;
  net_salary: number;
};

submitButton?.addEventListener("click", (e) => {
  let request_body = {
    reference_salary: getInputAmount(grossInput),
    pension_contribution: getInputAmount(pensionInput),
  };
  update_fields(request_body);
  console.log(`Reference salary is ${request_body.reference_salary}`);
  console.log(`Pension % contribution is ${request_body.pension_contribution}`);
});

function getInputAmount(element: HTMLInputElement | null) {
  if (element == null) return 0;
  let amount = Number(element.value);
  if (isNaN(amount)) return 0;
  return amount;
}

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
      updateOutputField(netOutput, response_body.net_salary);
    });
}

function updateOutputField(element: HTMLParagraphElement | null, amount: number) {
  console.log(amount);
  if (element == null) return;
  element.textContent = `£${(amount / 12).toFixed(2)}`;
}
