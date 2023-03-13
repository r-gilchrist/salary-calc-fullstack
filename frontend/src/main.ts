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

type RequestBody = {
  reference_salary: number;
  pension_contribution: number;
  student_loan_type: string;
};

type ResponseBody = {
  reference_salary: number;
  income_tax: number;
  national_insurance: number;
  pension: number;
  student_loan: number;
  net_salary: number;
};

submitButton?.addEventListener("click", (e) => {
  let loan_type = "";
  if (studentInput != null) {
    loan_type = studentInput.value;
  }
  let request_body = {
    reference_salary: getInputAmount(grossInput),
    pension_contribution: getInputAmount(pensionInput),
    student_loan_type: loan_type,
  };
  update_fields(request_body);
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
      updateOutputField(studentOutput, response_body.student_loan);
      updateOutputField(netOutput, response_body.net_salary);
    });
}

function updateOutputField(element: HTMLParagraphElement | null, amount: number) {
  if (element == null) return;
  element.textContent = `£${(amount / 12).toFixed(2)}`;
}
