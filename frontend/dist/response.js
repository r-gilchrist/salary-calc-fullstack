const grossOutput = document.getElementById("gross-output");
const incomeTaxOutput = document.getElementById("tax-output");
const niOutput = document.getElementById("NI-output");
const studentOutput = document.getElementById("student-output");
const pensionOutput = document.getElementById("pension-output");
const netOutput = document.getElementById("net-output");
export function populateFields(response_body) {
    updateOutputField(grossOutput, response_body.reference_salary);
    updateOutputField(incomeTaxOutput, response_body.income_tax);
    updateOutputField(niOutput, response_body.national_insurance);
    updateOutputField(pensionOutput, response_body.pension);
    updateOutputField(studentOutput, response_body.student_loan);
    updateOutputField(netOutput, response_body.net_salary);
}
function updateOutputField(element, amount) {
    if (element == null)
        return;
    element.textContent = `£${(amount / 12).toFixed(2)}`;
}
