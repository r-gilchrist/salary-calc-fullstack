const grossOutput = document.getElementById("gross-output") as HTMLParagraphElement | null;
const incomeTaxOutput = document.getElementById("tax-output") as HTMLParagraphElement | null;
const niOutput = document.getElementById("NI-output") as HTMLParagraphElement | null;
const studentOutput = document.getElementById("student-output") as HTMLParagraphElement | null;
const pensionOutput = document.getElementById("pension-output") as HTMLParagraphElement | null;
const netOutput = document.getElementById("net-output") as HTMLParagraphElement | null;

type ResponseBody = {
  reference_salary: number;
  income_tax: number;
  national_insurance: number;
  pension: number;
  student_loan: number;
  net_salary: number;
};

export function populateFields(response_body: ResponseBody) {
  updateOutputField(grossOutput, response_body.reference_salary);
  updateOutputField(incomeTaxOutput, response_body.income_tax);
  updateOutputField(niOutput, response_body.national_insurance);
  updateOutputField(pensionOutput, response_body.pension);
  updateOutputField(studentOutput, response_body.student_loan);
  updateOutputField(netOutput, response_body.net_salary);
}

function updateOutputField(element: HTMLParagraphElement | null, amount: number) {
  if (element == null) return;
  element.textContent = `£${(amount / 12).toFixed(2)}`;
}
