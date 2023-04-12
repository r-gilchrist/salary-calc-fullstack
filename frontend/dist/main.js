var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
import { getRequestBody } from "./request.js";
import { populateFields } from "./response.js";
import { setDefaultDate } from "./date.js";
setDefaultDate();
const submitButton = document.getElementById("update-salary");
submitButton === null || submitButton === void 0 ? void 0 : submitButton.addEventListener("click", (e) => {
    update_fields();
});
function update_fields() {
    return __awaiter(this, void 0, void 0, function* () {
        const request_body = getRequestBody();
        console.log(JSON.stringify(request_body));
        const response_body = yield fetch("http://localhost:5000/salary", {
            method: "POST",
            body: JSON.stringify(request_body),
            headers: { "Content-type": "application/json; charset=UTF-8" },
        });
        const data = yield response_body.json();
        populateFields(data);
    });
}
